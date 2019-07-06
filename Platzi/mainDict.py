
clients = [
    {
        'name': 'David',
        'company': 'Google',
        'email': 'david.atehortua@google.com',
        'position': 'Software engineer',
    },
    {
        'name': 'Gohan',
        'company': 'Facebook',
        'email': 'Gohan@facebook.com',
        'position': 'Data engineer',
    },
    {
        'name': 'Damaris',
        'company': 'ONU',
        'email': 'Damaris@ONU.com',
        'position': 'Teacher',
    }
]

def create_client(client):
    # global clients
    if client not in clients:
        clients.append(client)
    else:
        print('Client already in the client\'s list')

def update_client(current_name , new_name):
    if current_name in clients:
        clients[clients.index(current_name)] = new_name
    else:
        print('Client is not in clients list')


def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name =  client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']))

def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50) # pinta el asterisco el número de veces por la que se esta multiplicando
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')

def _get_client_name():
    return input('What is the client name? ')

def _get_client_field(field_name):
    field = None

    while not field:
        field = input('what is the client {}?'.format(field_name))

    return field

if __name__ == '__main__':
    _print_welcome()

    command = input() #detiene la ejecución del software, hasta que el usuario ingrese un valor
    command = command.upper()

    list_clients()

    if command == 'C':
        client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'), 
        }
        create_client(client)
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

