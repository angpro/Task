import socket, datetime

clients = []

try:
    IP = socket.gethostbyname(socket.gethostname())
    port = 9090
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.bind((IP,port))
except socket.error as msg:
    print("Error in socket: " + str(msg))
    pass


ext = False

print ("Server has started ")

while not ext:
    try:
        data, addr = soc.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

        date_time = datetime.datetime.today()

        msg = "[ " + addr[0]+ " ]+[ " + str(addr[1]) + " ]+[ " + date_time.strftime("%Y-%m-%d-%H.%M.%S") + " ]/" + data.decode("utf-8")
        print(msg)
        log_file = open('log.txt', '+a')
        print(msg, file=log_file)
        log_file.close()

        # What should be sent to client may be written here

    except:
        print("\nServer stopped ")
        ext = True

soc.close()
log_file.close()

