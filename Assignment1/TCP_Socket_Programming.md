# TCP_Socket_Programming

## Instructions
- To start the game: Open two terminals, one run`python server.py` and the other run `python main.py`. Then the game will start.  
  -  at the end of the command lines, you can add `--difficulty easy` to turn on the easy mode or `--difficulty hard` to turn on the hard mode.`python main.py` automatically starts the game in the easy mode.
  - you can set the probability of telling lies in the hard mode by adding `--seed xx` to the command line arguments, where `xx` is a number between 0 and 100. The higher the number, the higher the probability of telling lies.
- What happens in **server.py**:
  1. **parse** the command line arguments to determine the difficulty level
      - easy mode: the server tells the truth, always
      - hard mode: the server has a 50% chance of telling a lie
  2. create a **server socket** and bind it to the specified port (8080)
  3. listen for incoming connections
  4. accept the connection from the client
  5. **start a game** according to the difficulty level
  - server.py **won't turn off automatically**, so you need to press `Ctrl+C` to stop it.
- What happens in **main.py**:
  1. welcome the user to the game
  2. start a new game by creating a new **client socket** and connecting to the server
      - client socket runs, instructing user to **input their guess**
      - client socket sends the guess to the server and waits for the response
      - client socket receives the response and **prints it to the user**
  3. ask the user whether they want to **play a new game or quit**
  4. quit or go back to step 2 accordingly

## Flowchart
<img src = Assignment1_flowchart.jpg >

## Optional Work
- **Difficulty Levels**: The game can be played in two difficulty levels: easy and hard. In easy mode, the server always tells the truth, while in hard mode, the server has a 50% chance of telling a lie. The user can choose the difficulty level by adding `--difficulty easy` or `--difficulty hard` to the command line arguments.
- **Seed**: In hard mode, the server has a 50% chance of telling a lie. The user can set the probability of telling lies by adding `--seed xx` to the command line arguments, where `xx` is a number between 0 and 100. The higher the number, the higher the probability of telling lies.
- **Player**: In easy mode,  players use 5.2 times to get to the correct answer on average. But it's hard to tell n hard mode.

## Problems Ecountered
### Problem 1: Permission denied
Q: Running`serversocket.bind(('localhost', 80))`returns`PermissionError: [Errno 13] Permission denied`  
A: Choose a higher port number (e.g. 8080, or any unprivileged port above 1024) that doesn't require special permissions.
### Problem 2: Address already in use
Q: When trying to start a new game, in `serversocket.bind(('localhost', 8080))`, I get the error `OSError: [Errno 98] Address already in use`.  
A: This is because the former server socket is still running and hasn't been closed properly. GPT told me to use SO_REUSEADDR to reuse the address. And it worked.
### Problem 3: Stuck progress
Q: At first, I messed client and server up. In the attempt to reconstruct my code, it stuck at running the server.  
TA: Seperate your code into two files, one for server and one for client. Run them separately.

## References
-  [Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html)