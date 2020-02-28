import socket

sock = socket.socket()
sock.bind(("127.0.0.1", 8800))
sock.listen(5)

while 1:
    print('Server Waiting...')
    conn, addr = sock.accept()
    data = conn.recv(1024)

    with open('index.html') as f:
        send_content = f.read()
    conn.send("HTTP/1.1 200 OK\r\n\r\n{0}".format(send_content).encode("utf-8"))
    conn.close()
