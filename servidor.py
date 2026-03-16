from socket import*

servidor = "127.0.0.1"
porta = 21010

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((servidor,porta))
obj_socket.listen(2)

print("aguardando por um cliente...")

while True:
    con, cliente = obj_socket.accept()
    print("Conectado com", cliente)
    while True:
        msm_recebida = str(con.recv(1024))
        print("Recebemos ", msm_recebida)
        msm_enviada = "Olá, caro cliente!"
        con.send(msm_enviada)
        break
    con.close()    
