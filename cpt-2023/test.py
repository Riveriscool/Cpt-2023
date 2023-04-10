import json
import random
import secrets
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

def createtoken():
    random_number = secrets.randbits(15*4)
    return random_number

def login(username, password):
    with open("userdata.json", "r") as f:
        data = json.load(f)
    token = 0
    realpassword = data[username][0]
    if realpassword == password:
        print("creatingtoken")
        token = createtoken()
        data[username][1] = token
        with open('file.json', 'w') as f:
            json.dump(data, f)
            print(token)
            


        

    return token



def logout(username, token):
    with open('userdata.json', "r") as f:
        data = json.load(f)
   
   

    print(data[username][1])
    print(token)
    if data[username][1] == token:
        print("it equals")
        data[username][1] = '0'
        with open('userdata.json', 'w') as file:
            print(data)
            

            json.dump(data, file)
            print("Token updated successfully.")

def add_usr(username, password):
    with open('userdata.json', 'r') as f:
    # Load the JSON data from the file
        data = json.load(f)

    # Add a new argument to the data
    data[username] = [password, '0', False]

# Open the JSON file for writing
    with open('userdata.json', 'w') as f:
    # Write the modified JSON data to the file
        json.dump(data, f, indent=4)

def login(username, password):
    print("Starting login process...")
    with open("userdata.json", "r") as f:
        data = json.load(f)
    token = 0
    print('validating...')
    realpassword = data[username][0]
    if realpassword == password:
        print("creatingtoken")
        token = createtoken()
        data[username][1] = str(token)
        with open('userdata.json', 'w') as f:
            json.dump(data, f)
            print(token)
            
    return token


def write_to_file(message):
    with open('hi.txt', 'a+') as file:
        file.seek(0)
        content = file.read()
        if len(content) > 0 and content[-1] != '\n':
            file.write('\n')
        file.write(message)

"""with open('messageboard.txt', "r") as f:
    messages = f.read()
    x = len(f.readlines())
    #print("x is: " + str(x))
    if x > 10:
        shouldDelete=True
with open('messageboard.txt') as f:
   count = sum(1 for _ in f)
print(count)"""
def get_newsletter(username, token):
    with open('userdata.json', "r") as f:
        data = json.load(f)
    if token == data[username][1]:
        data[username][2] = True
        with open('userdata.json', 'w') as f:
            json.dump(data, f)

get_newsletter("River", "757033354417556531")
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


