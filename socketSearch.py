import socket

resp="S"

while resp == "S":
    url = str(input("Digite uma URL: "))
    ip = socket.gethostbyname(url)
    print("O ip referente a URL {} é: {}".format(url, ip))
    with open("url.txt", "a") as url_arq:
        url_arq.write(url + "\n")
    resp = input('Digite S para continuar:').upper()