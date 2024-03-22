# TCP_Socket_Programming

## Instructions


## Problems
### Problem 1: Permission denied
Q: Running`serversocket.bind(('localhost', 80))`returns`PermissionError: [Errno 13] Permission denied`  
A: Choose a higher port number (e.g. 8080, or any unprivileged port above 1024) that doesn't require special permissions.
### Problem 2: Address already in use
Q: When trying to start a new game, in `serversocket.bind(('localhost', 8080))`, I get the error `OSError: [Errno 98] Address already in use`.  
A: This is because the former server socket is still running and hasn't been closed properly. GPT told me to use SO_REUSEADDR to reuse the address. And it worked.

## References
-  [Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html)