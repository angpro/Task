import socket, threading, time

#IP = '172.20.10.2' local ip

shutdown = False

def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode("utf-8"))
                time.sleep(0.2)
        except:
            pass

print("Client has been activated")
IP = socket.gethostbyname(socket.gethostname())
port = 0

server = ("172.20.10.2", 9090)

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind((IP, port))
soc.setblocking(0)

rT = threading.Thread(target = receving, args = ("RecvThread",soc))
rT.start()

while shutdown == False:
    try:
        message = input()
        if message != "":
            soc.sendto(message.encode("utf-8"),server)
        time.sleep(0.2)
    except:
        shutdown = True

rT.join()
soc.close()


