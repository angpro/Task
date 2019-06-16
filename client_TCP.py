import socket, threading, time

port_server = 8685

shutdown = False

def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                if str(data.decode("utf-8")) != '':
                    print(data.decode("utf-8"))
                time.sleep(0.2)
        except:
            pass

print("Client has been activated")
IP = socket.gethostbyname(socket.gethostname())
port = 0

server = (IP, port_server)

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((IP, port_server))
soc.setblocking(0)

rT = threading.Thread(target = receving, args = ("RecvThread",soc))
rT.start()

while shutdown == False:
    try:
        message = input()
        if message != "":
            soc.send(bytes(str(message), encoding='UTF-8'))
        time.sleep(0.2)
    except:
        shutdown = True

rT.join()
soc.close()


