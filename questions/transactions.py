def print_logs(clients):
    print('ID             Transactions')
    print('-------        ------------')
    for client_id in clients.keys():
        print(f'{client_id}             {clients[client_id]}')

def processLogs(logs, threshold): 
    # I did not understand what n means in terms of constraint of the threshold so I just miss it.
    assert len(logs) >= 1 and len(logs) <= 100000 and threshold >= 1 
    clients = {}
    for transaction in logs:
        sender_id, receiver_id, amount = transaction.split(' ')
        if int(amount) > int(threshold):
            if not (sender_id in clients.keys()):
                clients[sender_id] = 1
            else:
                clients[sender_id] += 1
            if not (receiver_id in clients.keys()) and (receiver_id != sender_id):
                clients[receiver_id] = 1
            elif (receiver_id != sender_id):
                clients[receiver_id] += 1
    print_logs(clients)

processLogs(['88 99 200', '88 99 300', '99 32 100', '12 12 15'], 2)