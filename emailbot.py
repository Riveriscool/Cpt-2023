#IGNORE THIS FOR NOW!
"""
    pswd = "oprrjxtawaymxyxd"




    message = "hi"


    simple_email_context = ssl.create_default_context()


    try:
        # Connect to the server
        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls(context=simple_email_context)
        TIE_server.login(email_from, pswd)
        print("Connected to server ")
        
        # Send the actual email
        print()
        print(f"Sending email to - {email_to}")
        TIE_server.sendmail(email_from, email_to, message)
        print(f"Email successfully sent to - {email_to}")

    # If there's an error, print it out
    except Exception as e:
        print(e)

    # Close the port
    finally:
        TIE_server.quit()



with open("userdata.json") as f:
    data = json.load(f)

for username, (password, token, nl) in data.items():

    if nl:
        send_msg(username)


"""