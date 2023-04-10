import socket
import json
import secrets
def write_to_file(message):
    with open('messageboard.txt', 'a+') as file:
        file.seek(0)
        content = file.read()
        if len(content) > 0 and content[-1] != '\n':
            file.write('\n')
        file.write(message)
def updateMessageBoard(token, username, message):
        shouldDelete = False
        with open('userdata.json', "r") as f:
            data = json.load(f)
   
        print(f'username: {username}')
        with open('messageboard.txt', "r") as f:
            messages = f.read()
        if data[username][1] == token:
            msg = message.replace("_"," ")
            if msg == "𝜶":
                get_newsletter(username, token)
                return messages
                
            write_to_file(msg)

        with open('messageboard.txt') as f:
            count = sum(1 for _ in f)
            if count > 8:
                shouldDelete=True
        if shouldDelete:
            file_to_delete = open("messageboard.txt",'w')
            file_to_delete.close()
                
        
    
        return messages


def get_newsletter(username, token):
    with open('userdata.json', "r") as f:
        data = json.load(f)
    if token == data[username][1]:
        data[username][2] = True
        with open('userdata.json', 'w') as f:
            json.dump(data, f)

        


def add_usr(username, password):
    with open('userdata.json', 'r') as f:
    # Load the JSON data from the file
        data = json.load(f)

    # Add a new argument to the data
    data[username] = [password, 0, False]

# Open the JSON file for writing
    with open('userdata.json', 'w') as f:
    # Write the modified JSON data to the file
        json.dump(data, f, indent=4)
    
    return login(username, password)
    


def createtoken():
    random_number = secrets.randbits(15*4)
    return random_number

def login(username, password):
    print("Starting login process...")
    with open("userdata.json", "r") as f:
        data = json.load(f)
    token = 0
    print('validating...')
    if username in data:
        realpassword = data[username][0]
        if realpassword == password:
            print("creatingtoken")
            token = createtoken()
            data[username][1] = str(token)
            with open('userdata.json', 'w') as f:
                json.dump(data, f)
                print(token)
            
        return token
    return 0
    

def logout(username, token):

    with open('userdata.json', "r") as f:
        data = json.load(f)
   
   
    print(f'Token: {token}, realtoken: {data[username][1]}')
    print(data[username][1])
    print(token)
    if data[username][1] == token:
        print("it equals")
        data[username][1] = '0'
        with open('userdata.json', 'w') as file:
            print(data)
            

            json.dump(data, file)
            print("Token updated successfully.")






HOST = "127.0.0.1"
PORT = 8081

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()


"L usr password"
while True:
   
    clientConnected, clientAddress = s.accept()

    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]))
    rawdata = clientConnected.recv(1024)
    data = rawdata.decode()
    print(data)
    choice = data.split(" ")
    print(choice)
    if choice[0] == "l":
        print("l")
        token = (str(login(choice[1], choice[2])))
        print("about to send...")
        print(f'Token: {token}')
        clientConnected.send(token.encode())
        print("sent!")
        
    elif choice[0] == 's':
        token = add_usr(choice[1],choice[2])
        clientConnected.send(str(token).encode())
    elif choice[0] == "o":
        logout(choice[1],choice[2])
        clientConnected.send("s".encode())
    elif choice[0] == "n":
        get_newsletter(choice[1],choice[2])
        clientConnected.send("s".encode())
        
    elif choice[0] == "m":
        #realfinalmsg = "m " + token + " " + username + ":" +  msg + "-" + username
        
        
        usermsg = choice[2]
        usermsglist = usermsg.split("-")
        msg = usermsglist[0]
        user = usermsglist[1]
        tkn = choice[1]
        
        print(f'msg:{msg}, tkn:{tkn}')
        newmsg = updateMessageBoard(tkn,user,msg)
        clientConnected.send(newmsg.encode())
        




    print(data)

 

    # Send some data back to the client

  