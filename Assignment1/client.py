import socket

class ClientSocket:
    def __init__(self):
        self.clientsocket = None

    def start(self):
        # create an INET, STREAMing socket
        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Clientsocket created successfully", self.clientsocket)
        # now connect to the web server on port 8080
        self.clientsocket.connect(('localhost', 8080))
        print("Connected to server")
        return self

    async def run(self):
        while True:
            to_send = input("Try to guess number: ")
            self.send_message(to_send.encode())
            data = self.receive_message(1024).decode()
            if data is None:
                break
            print("Received: ", data)
            if data == "Congratulations! You guessed the number!":
                break

    def close(self):
        self.clientsocket.close()

    def send_message(self, message):
        self.clientsocket.send(message)
        print("Sent: ", message)

    def receive_message(self, buffer_size):
        data = self.clientsocket.recv(buffer_size)
        return data
