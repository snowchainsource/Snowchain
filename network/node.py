"""
Network Layer: Peer-to-Peer Nodes
"""
import socket
import threading

class Node:
    def __init__(self, host='127.0.0.1', port=5000):
        self.host = host
        self.port = port
        self.peers = set()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        threading.Thread(target=self.listen_for_peers, daemon=True).start()

    def listen_for_peers(self):
        while True:
            conn, addr = self.server.accept()
            self.peers.add(addr)
            threading.Thread(target=self.handle_peer, args=(conn, addr), daemon=True).start()

    def handle_peer(self, conn, addr):
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # Handle incoming data (transactions/blocks)
        conn.close()
