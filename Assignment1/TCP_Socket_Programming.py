# Assignment Goals
# 1. Enhance understanding of the TCP protocol through socket programming;
# 2. Gain first hand experience with setting up a TCP connection, and using it to support simple network applications.

import socket
import random

def start_a_new_game():
    # create an INET, STREAMing socket  #see Socet programming HOWTO
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) ## GPT suggested using SO_REUSEADDR
    print("Serversocket created successfully", serversocket)
    # bind the socket to a public host, and a well-known port
    serversocket.bind(('localhost', 8080))
    print("Server is listening on port 8080")
    # become a server socket
    serversocket.listen(1)
    # determine the answer
    number = random.randint(1, 100)
    print("The answer is:", number)

    # create an INET, STREAMing socket
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Clientsocket created successfully", clientsocket)
    # now connect to the web server on port 8080
    clientsocket.connect(('localhost', 8080))
    print("Connected to server")

    conn, address = serversocket.accept()  # accept new connection
    print("Connection from: ", address)
    while True:
        to_send = input("Try another number: ")
        clientsocket.send(to_send.encode())
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        data = int(data)
        print("Received: ", data)
        if data < number:
            message = "The number is greater than " + str(data)
        elif data > number:
            message = "The number is less than " + str(data)
        else:
            message = "Congratulations! You guessed the number!"
            print("Sent: ", message)
            break
        conn.send(message.encode())  # send data to the client
        print("Sent: ", message)

    conn.close()  # close the connection
    clientsocket.close()  # close the client socket
    serversocket.close()  # close the server socket

def main():
    while True:
        print("Welcome to the number guessing game!")
        start_a_new_game()
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