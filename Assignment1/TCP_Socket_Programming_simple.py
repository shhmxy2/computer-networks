# Assignment Goals
# 1. Enhance understanding of the TCP protocol through socket programming;
# 2. Gain first hand experience with setting up a TCP connection, and using it to support simple network applications.

import socket
import random
import asyncio

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

async def start_a_new_game():
    serversocket = ServerSocket().start()
    clientsocket = ClientSocket().start()
    print("The game has started!")
    await asyncio.gather(serversocket.run(), clientsocket.run())
    
    clientsocket.close()  # close the client socket
    serversocket.close()  # close the server socket

def main():
    while True:
        print("Welcome to the number guessing game!")
        asyncio.run(start_a_new_game())
        again = input("Do you want to play again? (y/n): ")
        new_game = True
        while True:
            if again.lower() == 'n' or again.lower() == 'no':
                new_game = False
                print("Thank you for playing!")
                break
            elif again.lower() == 'y' or again.lower() == 'yes':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
                again = input("Do you want to play again? (y/n): ")
        if new_game:
            continue
        else:
            break

if __name__ == '__main__':
    main()