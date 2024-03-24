import socket
import random
import argparse

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
        return self
    
    def easy_mode_response(self, data):
        if data < self.number:
            message = "The number is greater than " + str(data)
        elif data > self.number:
            message = "The number is less than " + str(data)
        else:
            message = "Congratulations! You guessed the number!"
        return message 

    def hard_mode_response(self, data, seed):
        lie = random.randint(1, 100)
        if data < self.number:
            if lie > seed:
                message = "The number is greater than " + str(data)
            else:
                message = "The number is less than " + str(data)
        elif data > self.number:
            if lie > seed:
                message = "The number is less than " + str(data)
            else:
                message = "The number is greater than " + str(data)
        else:
            message = "Congratulations! You guessed the number!"
        return message 
    
    def run(self, difficulty, seed):
        print("Waiting for client to connect...")
        conn, address = self.serversocket.accept()  # accept new connection
        print("Connection from: ", address)
        # determine the answer
        self.number = random.randint(1, 100)
        print("The answer is:", self.number)

        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            if not data:
                # if data is not received break
                break
            data = int(data)
            print("Received: ", data)
            if difficulty == 'easy':
                message = self.easy_mode_response(data)
            else:
                message = self.hard_mode_response(data, seed)
            conn.send(message.encode())  # send data to the client
            print("Sent: ", message)
            if message == "Congratulations! You guessed the number!":
                break

        conn.close()  # close the connection
    
    def close(self):
        self.serversocket.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='游戏参数设置')
    parser.add_argument('--difficulty', choices=['easy', 'hard'], default='easy', help='设置游戏的难度模式')
    parser.add_argument('--seed', type=int, default=50, help='设置撒谎概率')
    args = parser.parse_args()
    serversocket = ServerSocket().start()
    while True:
        serversocket.run(args.difficulty, args.seed)