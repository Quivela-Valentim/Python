from socket import*

servidor = "127.0.0.1"
porta = 21010

msm = bytes(input("Digite alguma coisa: "), "utf-8")
obj_socket= socket(AF_INET, SOCK_STREAM)
obj_socket.connect((servidor, porta))
obj_socket.send(msm)
resposta = obj_socket.recv(1024)
print("recebemos a mensagem", resposta)
obj_socket.close()