# -*- coding: utf-8 -*-
"""HTTP Range destekleyen basit test sunucusu.

Python'un kendi http.server'ı Range istemlerini yok sayıyor; tarayıcı da
o videoyu "aranamaz" sayıp currentTime atamalarını görmezden geliyor.
Kaydırmaya bağlı video bu yüzden yerel testte donuk kalıyor."""
import os, re, sys, http.server, socketserver

class Islek(http.server.SimpleHTTPRequestHandler):
    def send_head(self):
        yol = self.translate_path(self.path)
        if os.path.isdir(yol) or not os.path.exists(yol):
            return super().send_head()
        aralik = self.headers.get('Range')
        if not aralik:
            self.send_response(200)
            self.send_header('Accept-Ranges', 'bytes')
            self.send_header('Content-Type', self.guess_type(yol))
            self.send_header('Content-Length', str(os.path.getsize(yol)))
            self.end_headers()
            return open(yol, 'rb')
        m = re.match(r'bytes=(\d*)-(\d*)', aralik)
        boyut = os.path.getsize(yol)
        bas = int(m.group(1)) if m.group(1) else 0
        son = int(m.group(2)) if m.group(2) else boyut - 1
        son = min(son, boyut - 1)
        f = open(yol, 'rb'); f.seek(bas)
        self.send_response(206)
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Content-Type', self.guess_type(yol))
        self.send_header('Content-Range', 'bytes %d-%d/%d' % (bas, son, boyut))
        self.send_header('Content-Length', str(son - bas + 1))
        self.end_headers()
        return _Kesit(f, son - bas + 1)

class _Kesit:
    def __init__(self, f, n): self.f, self.kalan = f, n
    def read(self, k=-1):
        if self.kalan <= 0: return b''
        if k < 0 or k > self.kalan: k = self.kalan
        d = self.f.read(k); self.kalan -= len(d); return d
    def close(self): self.f.close()

if __name__ == '__main__':
    port = int(sys.argv[1]); os.chdir(sys.argv[2])
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(('', port), Islek) as s:
        s.serve_forever()
