import socket
import elliptic

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

ec = elliptic.EC(1, 18, 19)
pub_key = elliptic.Coord
pub_key, priv_key = elliptic.ecdsa_generate_keys(ec)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(pub_key)
    s.sendall(bytes(pub_key[0]))
    print(pub_key[0])
    s.sendall(bytes(pub_key[1]))
    server_public_key_bytes = s.recv(1024)
    print("server pubkey: " + server_public_key_bytes.decode("utf-8"))

#print('Received', repr(data))

