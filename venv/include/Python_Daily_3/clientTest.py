import socket


if __name__ == 'main':
    # Create socket object
    s = socket.socket()
    # Get localhost
    host = socket.gethostname() # 获取本地主机名
    # Set port
    port = 12345

    s.connect((host, port))
    print(s.recv(1024))
    s.close()
