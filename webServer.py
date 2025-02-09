# import socket module
from socket import *
# In order to terminate the program

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen(1)
  #Fill in end

  while True:
    #Establish the connection
    
    #print('Ready to serve...')
    # Fill in start -are you accepting connections?
    connectionSocket, addr = serverSocket.accept()
    # Fill in end
    
    try:
      # Fill in start -a client is sending you a message
      message = connectionSocket.recv(1024).decode()
      # Fill in end

      filename = message.split()[1]

      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      #fill in start #fill in end
      f = open(filename[1:], "rb")
      #fill in end

      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    

      #Fill in start
      outputdata = b"HTTP/1.1 200 OK\r\n"
      #Content-Type is an example on how to send a header as bytes. There are more!
      outputdata = outputdata + b"Date: Sunday, 9 Feb 2025 16:31:00 GMT\r\n"
      outputdata = outputdata + b"Server: Socket Server (Windows)\r\n"
      outputdata = outputdata + b"Connection: close\r\n"
      #outputdata = outputdata + b"Content-Length: \r\n"
      outputdata = outputdata + b"Content-Type: text/html; charset=UTF-8\r\n"
      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
      #Fill in end
      htmlcontent = b""
      for i in f: #for line in file
      # Fill in start - append your html file contents
        htmlcontent = htmlcontent + f.readline()
      # Fill in end
      #Send the content of the requested file to the client (don't forget the headers you created)!
      #Send everything as one send command, do not send one line/item at a time!
      outputdata = outputdata + b"Content-Length: " + str(len(htmlcontent)).encode() + b"\r\n"
      # Fill in start
      outputdata = outputdata + b"\r\n" + htmlcontent
      connectionSocket.sendall(outputdata)
      # Fill in end

      connectionSocket.close() #closing the connection socket

    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      outputdata = b"HTTP/1.1 404 Not Found\r\n"
      connectionSocket.sendall(outputdata)
      #Fill in end

      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

  # Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop. 
  # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
  # serverSocket.close()
  # sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
