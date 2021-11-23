import socket
import elliptic

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

ec = elliptic.EC(1, 18, 19)
pub_key, priv_key = elliptic.ecdsa_generate_keys(ec)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        #while True:
        cpk0 = int.from_bytes(conn.recv(1024), "little")
        print(cpk0)
        cpk1 = int.from_bytes(conn.recv(1024), "little")
        print("s2")
        client_public_key = elliptic.Coord(cpk0, cpk1)
        print(client_public_key)
            #if not data:
                #break
        conn.sendall(bytes(pub_key))