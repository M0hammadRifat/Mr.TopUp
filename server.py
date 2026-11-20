#!/usr/bin/env python3
"""
Custom Development Server for Free Fire Topup Platform
Includes built-in zero-CORS proxy for OrionLike API integration.
"""
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os
import sys
import urllib.parse
import urllib.request
import urllib.error

PORT = 8000
BIND_ADDR = "0.0.0.0"

class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS for all local requests
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/orion-status":
            self.handle_orion_status(parsed.query)
            return

        if path == "/api/orion-dispatch":
            self.handle_orion_dispatch(parsed.query)
            return

        if path == "/api/check-player":
            self.handle_check_player(parsed.query)
            return

        super().do_GET()

    def handle_check_player(self, query_str):
        params = urllib.parse.parse_qs(query_str)
        uid = params.get("uid", [""])[0].strip() or params.get("id", [""])[0].strip()
        server = params.get("server", ["bd"])[0].strip().upper()
        if not uid:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"success": False, "message": "UID is required"}).encode())
            return

        target_url = f"https://apis.rrrtopup.com/api/v1/player-nickname?id={urllib.parse.quote(uid)}&product_id=21"
        try:
            req = urllib.request.Request(target_url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                "Origin": "https://rrrtopup.com",
                "Referer": "https://rrrtopup.com/"
            })
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read()
                self.send_response(resp.status)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(data)
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"success": False, "message": str(e)}).encode())

    def handle_orion_status(self, query_str):
        params = urllib.parse.parse_qs(query_str)
        key = params.get("key", [""])[0].strip() or "CUS-132ED22C01C03EDD2D39C5760A13"
        url = f"https://orionlike.com/api/status?key={urllib.parse.quote(key)}"

        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read()
                self.send_response(resp.status)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(data)
        except urllib.error.HTTPError as he:
            err_data = he.read()
            self.send_response(he.code)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(err_data if err_data else json.dumps({"status": "failed", "message": str(he)}).encode())
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "failed", "message": str(e)}).encode())

    def handle_orion_dispatch(self, query_str):
        params = urllib.parse.parse_qs(query_str)
        key = params.get("key", [""])[0].strip() or "CUS-132ED22C01C03EDD2D39C5760A13"
        server_name = params.get("server_name", ["bd"])[0].strip().lower() or "bd"
        uid = params.get("uid", [""])[0].strip()
        type_param = params.get("type", ["like100"])[0].strip().lower() or "like100"

        if not uid:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "failed", "message": "UID is required"}).encode())
            return

        def query_orion(t):
            target_url = (
                f"https://orionlike.com/api?key={urllib.parse.quote(key)}"
                f"&server_name={urllib.parse.quote(server_name)}"
                f"&uid={urllib.parse.quote(uid)}"
                f"&type={urllib.parse.quote(t)}"
            )
            try:
                req = urllib.request.Request(target_url, headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                    "Accept": "application/json"
                })
                with urllib.request.urlopen(req, timeout=25) as resp:
                    raw = resp.read()
                    return resp.status, json.loads(raw.decode("utf-8", errors="ignore"))
            except urllib.error.HTTPError as he:
                try:
                    err_json = json.loads(he.read().decode("utf-8", errors="ignore"))
                    return he.code, err_json
                except Exception:
                    return he.code, {"status": "failed", "code": he.code, "message": str(he)}
            except Exception as e:
                return 500, {"status": "failed", "message": str(e)}

        status_code, result = query_orion(type_param)

        # Automatic fallback: if like200 failed with code 2005 (insufficient points for 200 likes), auto-retry with like100
        if status_code == 403 and result.get("code") == 2005 and type_param == "like200":
            status_code, result = query_orion("like100")

        # Mark claimed status and provide human-friendly messages
        if result.get("status") == "Claimed":
            result["claimed"] = True
            result["success"] = True
            result["human_message"] = "Player UID has already claimed daily maximum likes today (Garena 24h limit). Next batch will deliver on tomorrow's reset."
        elif result.get("status") == "success":
            result["success"] = True
            result["claimed"] = False
            result["human_message"] = f"Successfully delivered {result.get('LikesGivenByAPI', 0)} likes to {result.get('PlayerNickname', uid)}."

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(result).encode())

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = HTTPServer((BIND_ADDR, PORT), CustomHandler)
    print(f"Server started at http://{BIND_ADDR}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
