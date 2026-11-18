"""Servidor local de Metalens sin caché: Chrome siempre carga la última versión de cada archivo.
Uso: python3 serve.py 5520"""
import http.server, os, sys

class NoCache(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        super().end_headers()

os.chdir(os.path.dirname(os.path.abspath(__file__)))
port = int(sys.argv[1]) if len(sys.argv) > 1 else 5520
http.server.ThreadingHTTPServer(('', port), NoCache).serve_forever()
