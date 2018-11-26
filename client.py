import socket

HOST = '127.0.0.1'
PORT = 8001


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        cmd = input("Please input msg:")
        s.send(cmd.encode())
        data = s.recv(1024)
        print(data.decode())

    s.close()


if __name__ == '__main__':
    main()
