import smtplib as smt 
import urllib.request
from time import sleep

# check for internet conncetion
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

# check for document made
def egmail(file = "Registered_Emails"):
    try:
        f = open(file,"r")
        return True
    except:
        return False


# Add email and register email
while True:
    Made = egmail()

    if Made == True:
        print("Hello Welocme to the email bot")
        print("Do you want to send email or add email in your registerd emails")
        a = input()
        if a == "Send email":
             break
        if a == "Add email":
            print("Senders Email:- ")   
            email = input()
            print("Senders Password:- ")
            password = input()
            with open("Registered_Emails","a") as f :
             f.write(f"{email} \n ")
             f.write(f"{password} \n")
             quit()
   
    if Made == False:
        print("Senders Email:- ")   
        email = input()
        print("Senders Password:- ")
        password = input()
        with open("Registered_Emails","a") as f :
            f.write(f"{email} \n ")
            f.write(f"{password} \n")
            
        print(f"sucessfully regestired {email}")
        continue
    break          
# Variable defined take user input


Internet = connect()
print("Write the Gmail On which u want to send message")
Reciver = input()
print("Now write down the messsage which u want to send")
Message = input()

while True:
        Internet = connect()
        if Internet == True:
            print("sucessfully connected to internet")
            print("from which email do you want to send message")
            file = open('Registered_Emails', "r+")
            details = file.read()
            file.close()

            print(details)    
            print("Type the email line number which u want")
            number = int(input())
            
            Number1 = number - 1
            Number2 = number
            file = open("Registered_Emails", "r+")
            content = file.readlines()
            emailnum = content[Number1]
            passnum = content[Number2]
            

           
            print("sending email")
            server = smt.SMTP('SMTP.gmail.com',587)
            server.starttls()
            server.login(emailnum,passnum)
            server.sendmail(emailnum,Reciver,Message)
            break
        
    
    
        elif Internet == False:
        
            print("You are not conected to internet")
            print("Type 'continue' to continue or 'cancel' to cancel")
            go_on = input()

            if go_on == 'cancel':
                print("SENDING EMAIL CANCELED")
                break
            elif go_on == 'continue':
                print("Your email will be sent when you are connceted to internet")
                while Internet == True:
                    Internet = connect()
                    sleep(1)



# Code return by intelligent2007 and Gamingfever8250

             
             
            








