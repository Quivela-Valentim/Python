import socket
resposta = "S"
while resposta == "S":
    url = input("digite a url: ")
    ip = socket.gethostbyname(url)
    print("O número de endereço ip será:", ip)
    resposta= input("digite S para continuar:").upper()