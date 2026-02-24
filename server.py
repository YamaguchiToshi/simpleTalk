#!/usr/bin/env python3
"""
簡易Webサーバ
使い方: python3 server.py
ブラウザで http://localhost:8000 にアクセス
"""

import http.server
import socketserver
import os

PORT = 8001

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # CORS対応（必要に応じて）
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

# カレントディレクトリをサーバのルートに設定
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"サーバ起動: http://localhost:{PORT}")
    print("終了するには Ctrl+C を押してください")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nサーバを停止しました")
