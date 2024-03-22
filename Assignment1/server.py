import socket
import random

class ServerSocket:
    def __init__(self):
        self.number = -1
        self.serversocket = None

    def start(self):
        # create an INET, STREAMing socket #see Socet programming HOWTO
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) ## GPT suggested using SO_REUSEADDR
        print("Serversocket created successfully", self.serversocket)
        # bind the socket to a public host, and a well-known port
        self.serversocket.bind(('localhost', 8080))
        print("Server is listening on port 8080")
        # become a server socket
        self.serversocket.listen(1)
        # determine the answer
        self.number = random.randint(1, 100)
        print("The answer is:", self.number)
        return self
    
    async def run(self):
        conn, address = self.serversocket.accept()  # accept new connection
        print("Connection from: ", address)

        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            if not data:
                # if data is not received break
                break
            data = int(data)
            print("Received: ", data)
            if data < self.number:
                message = "The number is greater than " + str(data)
            elif data > self.number:
                message = "The number is less than " + str(data)
            else:
                message = "Congratulations! You guessed the number!"
            conn.send(message.encode())  # send data to the client
            print("Sent: ", message)
            if message == "Congratulations! You guessed the number!":
                break

        conn.close()  # close the connection
    
    def close(self):
        self.serversocket.close()