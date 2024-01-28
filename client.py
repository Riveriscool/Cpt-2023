import socket
import time
from customtkinter import *
HOST = '127.0.0.1'  
PORT = 8081
msg1 = None
set_appearance_mode("dark")
set_default_color_theme("dark-blue")
app = CTk()
global Logintries 
Logintries = 3
switch_var = StringVar(value="on")
def settingswithdraw():
    settingspage.withdraw()
def switch_event():
    if switch_var.get() == 'on':
        set_appearance_mode("dark")
    else:
        set_appearance_mode("light")
def deleteusr():
    with open("clientsidedata.txt", "r") as f:
        token = f.read()
    with open("usercorrelations.txt", "r") as f:
        usr = f.read()
    msg = "d " + usr + " " + token
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    client_socket.sendall(msg.encode())
    print("Sent")
    message = client_socket.recv(1024).decode()
    print(f'Received: {message}')
    if message == "S":
        print("Done")
    Loginpage.withdraw()
    Homepage.withdraw()
    app.destroy()
def settingsubmit():
    global settingspage
    global lightdarktoggle
    global deleteuser
    global exitbutton
    
    settingspage = CTk()
    settingspage.geometry("1100x700")
    lightdarktoggle = CTkSwitch(master=settingspage, command=switch_event, variable=switch_var, onvalue='on', offvalue='off')
    lightdarktoggle.grid(row=4,column=3)
    deleteuser = CTkButton(master=settingspage, text="CAUTION--DONT PRESS", width=140,height=20,fg_color=("red","red"),command=deleteusr)
    deleteuser.grid(row=20,column=10)
    exitbutton = CTkButton(master=settingspage, text="Exit",command=settingswithdraw)
    exitbutton.grid(row=3,column=3)
    settingspage.mainloop()
def SendMsg():
    
    print("Sending message start")
    with open("usercorrelations.txt", "r") as f:
        username = f.read()
    with open("clientsidedata.txt", "r") as f:
        token = f.read()
    msg1 = MessageEntry.get("1.0",'end-1c')
    
        
    msg = msg1.replace(" ", "_")
    if msg == "#NewsLetter":
        msg = "𝜶"
    else:
        msg = username + ":" + msg
    realfinalmsg = "m " + token + " " +  msg + "-" + username
    print(realfinalmsg)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    client_socket.sendall(realfinalmsg.encode())
    print("Sent")
    message = client_socket.recv(1024).decode()
    print(f'Received: {message}')
    Messageboard.delete("0.0", "end")
    Messageboard.insert("0.0", message)
    
    
def clickSignupSubmit():
    global msg1
    username = SignupUserField.get("1.0",'end-1c')
    with open("usercorrelations.txt", "w") as f:
        f.write(username)
    password = SignupPasswordField.get("1.0",'end-1c')
    msg1 = 's ' + username + " " + password
    commence()
    
def wasntsure():
    areyousurepage.withdraw()
def areyousure():
    global areyousurepage
    global areyousurelabel
    global imsurebutton
    global imnotsurebutton
    areyousurepage = CTk()
    areyousurepage.geometry('400x300')

    areyousurelabel = CTkLabel(areyousurepage, text='This is a very serious decision, are you sure').pack()

    imsurebutton = CTkButton(areyousurepage, text='Yes! im sure.', command=Logout)
    imsurebutton.pack()
    imnotsurebutton = CTkButton(areyousurepage, text="Eh :( im having second thoughts", command=wasntsure)
    imnotsurebutton.pack()
    areyousurepage.mainloop()
def clickLogin():
    global Loginpage
    global Loginlabel
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    global LoginUserField
    global LoginPasswordField
    global LoginSubmit
    
    Loginpage = CTk()
    Loginpage.geometry('400x300')
    Loginlabel = CTkLabel(Loginpage, text="Login Here!").pack()
    LoginUserField = CTkTextbox(master=Loginpage, width=200, height=70)
    LoginUserField.pack(pady=10, padx=10)
    LoginPasswordField = CTkTextbox(master= Loginpage, width=200, height=70)
    LoginPasswordField.pack(pady=10, padx=10)
    LoginSubmit = CTkButton(master=Loginpage, text="Submit", command=submitLogin)
    LoginSubmit.pack()
    app.withdraw()
    
def Logout():
        with open("clientsidedata.txt", "r") as f:
            token = f.read()
        with open("usercorrelations.txt", "r") as f:
            usr = f.read()
            
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        msg2 = "o " + usr + " " + token
        client_socket.sendall(msg2.encode())
        try:
            Loginpage.withdraw()
        except:
            SignupPage.withdraw()
        Homepage.withdraw()
        areyousurepage.withdraw()
        app.deiconify()
def Get_newsletter():
    with open("clientsidedata.txt", "r") as f:
        token = f.read()
    with open("usercorrelations.txt", "r") as f:
        usr = f.read()
        
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    msg2 = "o " + usr + " " + token
    client_socket.sendall(msg2.encode())
        
    





def homepage():
    global Homepage
    global LogoutBtn
    global Get_newsletter
    global Messageboard
    global MessageEntry
    global SendMessage
    global SettingsButton
    Homepage = CTk()
    Homepage.geometry("1200x700")
    LogoutBtn = CTkButton(master=Homepage, text="Logout",width=50, height=50, corner_radius=50,border_color='red',command=areyousure)
    LogoutBtn.grid(row=0,column=0, padx=100)

  
    Messageboard = CTkTextbox(master=Homepage, width=500)
    Messageboard.grid(row=1,column=3)
    MessageEntry = CTkTextbox(master=Homepage, width=500,height=40, corner_radius=20,border_width=10, border_color="Royal Blue")
    MessageEntry.insert("0.0", "Your message here!")
    MessageEntry.grid(row=7,column=3)
    SendMessage = CTkButton(master=Homepage, text="Send!",height=50,width=40, corner_radius=30,command=SendMsg)
    SendMessage.grid(row=7, column=4)
    SettingsButton = CTkButton(master=Homepage, text="S",width=50,height=50,corner_radius=50,border_color='red',command=settingsubmit)
    SettingsButton.grid(row=1,column=8)
    
    
   
    
    

    
    
    
    Homepage.mainloop()
    
def commence():
    Logintries = 2
    print("beggining commence")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(msg1)
    # connect to the server
    client_socket.connect((HOST, PORT))


    if msg1 != None:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        client_socket.sendall(msg1.encode())
        
        print("sent")

        data = client_socket.recv(1024).decode()
        print(data)
        with open("clientsidedata.txt", "w") as f:
            f.write(data)
 
        if data == "0" or data == 0:

            Logintries -= 1
            msg = "Incorrect Password/Username, you have " + str(Logintries) + " more tries"
            if Logintries > 0:
                print(msg)
            else:
                
                Loginpage.withdraw()
        else:
            homepage()
            try:
                Loginpage.withdraw()
            except:
                SignupPage.withdraw()


        
            
            
        

        client_socket.close()

def startpage():
    print("startpage again")
def submitLogin():
    global msg1
    
    print(LoginUserField.get("1.0",'end-1c'))
    with open("usercorrelations.txt", "w") as f:
        f.write(LoginUserField.get("1.0",'end-1c'))
    print(LoginPasswordField.get("1.0",'end-1c'))
    msg1 = "l " + LoginUserField.get("1.0",'end-1c') + " " + LoginPasswordField.get("1.0",'end-1c')
    commence()
    



def clickSignup():
    global SignupPage
    global SignupUserField
    global SignupPasswordField
    global SignupSubmit
    SignupPage = CTk()
    SignupPage.geometry("400x300")
    SignupPage.title("Signup!")
    SignupUserField = CTkTextbox(master=SignupPage, width=200, height=70)
    SignupUserField.pack(padx=10, pady=10)
    SignupPasswordField = CTkTextbox(master=SignupPage, width=200, height=70)
    SignupPasswordField.pack(padx=10,pady=10)
    SignupSubmit = CTkButton(master=SignupPage, text="Sign Up!", command=clickSignupSubmit)
    SignupSubmit.pack()
    SignupPage.mainloop()

app.geometry("400x300")

WelcomeScreen = CTkLabel(app, text="Welcome to RiverNet")
WelcomeScreen.pack()


LoginBtn = CTkButton(master=app, text="Login", command=clickLogin)

LoginBtn.pack()
SignupBtn = CTkButton(master=app, text="Signup", command=clickSignup)
SignupBtn.pack()

app.mainloop()


# define host and port
HOST = '127.0.0.1'  
PORT = 8081