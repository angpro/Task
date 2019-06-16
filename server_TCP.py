import socket, datetime

clients = []
buffersize = 1024

try:
    IP = socket.gethostbyname(socket.gethostname())
    port = 8685
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind((IP,port))
    soc.listen(1)
except socket.error as msg:
    print("Error in socket: " + str(msg))
    pass

print(IP)

shutdown = False

print ("Server has started ")

log_file = open('log.txt', '+a')


while not shutdown:
    try:
        data, addr = soc.accept()
        if addr not in clients:
            clients.append(addr)

        while True:
            connection = data.recv(buffersize)
            if not connection: break
            date_time = datetime.datetime.today()
            msg = "[ " + addr[0]+ " ]+[ " + str(addr[1]) + " ]+[ " + date_time.strftime("%Y-%m-%d-%H.%M.%S") + " ]/" + connection.decode("utf-8")
            print(msg)
            log_file = open('log.txt', '+a')
            print(msg, file=log_file)
            log_file.close()

        # What should be send to client may be written here

    except:
        print("\nServer stopped ")
        shutdown = True

soc.close()
log_file.close()

