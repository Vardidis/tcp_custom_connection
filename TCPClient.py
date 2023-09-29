from socket import *
import sys

hostname = sys.argv[1]
port = sys.argv[2]

serverName = hostname
serverPort = int(port)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = bytes(input('Input text:'), 'utf-8')
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print('From Server:', bytes.decode(modifiedSentence))
clientSocket.close()