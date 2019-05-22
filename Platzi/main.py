
clients = ['David','Gohan','Damaris']

def create_client(client_name):
    # global clients
    if client_name not in clients:
        clients.append(client_name)
    else:
        print('Client already in the client\'s list')

def update_client(current_name , new_name):
    if current_name in clients:
        clients[clients.index(current_name)] = new_name
    else:
        print('Client is not in clients list')


def list_clients():
    print(clients)

def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50) # pinta el asterisco el número de veces por la que se esta multiplicando
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')

def _get_client_name():
    return input('What is the client name? ')

if __name__ == '__main__':
    _print_welcome()

    command = input() #detiene la ejecución del software, hasta que el usuario ingrese un valor
    command = command.upper()

    print(clients)

    if command == 'C':
        create_client(_get_client_name())
    elif command == 'D':
        pass
    elif command == 'U':
        current_name = _get_client_name()
        new_name = input('What is the updated client name? ')
        update_client(current_name, new_name)
        pass
    else:
        print('Invalid command')
    
    list_clients()

