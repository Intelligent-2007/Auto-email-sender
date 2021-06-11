import smtplib as smt 
import urllib.request
from time import sleep
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

Internet = connect()
print("Senders Email:- ")
email = input()
print("Senders Password:- ")
password = input()
print("Write the Gmail On which u want to send message")
Reciver = input()
print("Now write down the messsage which u want to send")
Message = input()


while True:
    Internet = connect()
    if Internet == True:
        print("sucessfully connected to internet")
        print("sending email")
        server = smt.SMTP('SMTP.gmail.com',587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email,Reciver,Message)
        break
        
    
    
    elif Internet == False:
        
        print("You are not conected to internet")
        print("Type 'continue' to continue or 'cancel' to cancel")
        a = input()
        if a == 'cancel':
            print("SENDING EMAIL CANCELED")
            break
        elif a == 'continue':
            print("Your email will be sent when you are connceted to internet")
            while Internet == True:
                Internet = connect()
                sleep(1)
        

        
        


    

        
