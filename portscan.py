import socket

portas = [21, 23, 80, 443, 8080]
alvo_scan = input("Digite uma URL ou IP do alvo: ")

for porta in portas:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    alvo = s.connect_ex((alvo_scan, porta))
    if alvo == 0:
        print(porta, "OPEN")
    else:
        print(porta, "CLOSE")
