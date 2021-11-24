import socket
import elliptic

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

ec = elliptic.EC(1, 18, 19)
#pub_key = elliptic.Coord
pub_key, priv_key = elliptic.ecdsa_generate_keys(ec)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello')
    data = s.recv(1024)

print('Received: ', repr(data))

