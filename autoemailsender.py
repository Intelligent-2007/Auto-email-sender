import smtplib as smt               # <----- Email sending
import urllib.request                 # <------ Internt checks

from tkinter import *          

root = Tk()
root.title("Auto Email Bot")

root.geometry("300x250")
root.maxsize(300,250)
root.minsize(300,250)
# root.configure(bg = "red")


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


def Made_true():
    


    
    def internet_true():
        welc1.place_forget()
        Send_email.place_forget()
        Add_email.place_forget()
        So1 = Label(root, text = "ENTER THE RECIVERS EMAIL AND MESSAGE")
        So1.place(relx = 1, x = -150, y = 45, anchor = N)

        Reciver_email = Entry(root, width = 30)
        Reciver_email.place(relx = 1, x = -150, y = 85, anchor = CENTER)
        Reciver_email.insert(0,"ENTER RECIVER EMAIL")

        Message1 = Entry(root , width = 30)
        Message1.place(relx = 1, x = -150,y = 125, anchor = CENTER)
        Message1.insert(0,"MESSAGE")


        def check_for_internet():

            internet = connect()
            if internet == True:
                emailsendstart()
            else:
                internet_false()

        def internet_false():

            Reciver_email.place_forget()
            Message1.place_forget()
            done.place_forget()
            So1.place_forget()
            
            Itnot = Label(root, text = "You are not connected to internet ").place(relx = 1, x = -150, y = 85, anchor = CENTER)

            def cont2():
                exit()

           
            Con2 = Button(root, text = "Cancel", command = cont2).pack(relx = 1, x = -150,y = 125, anchor = CENTER)

    
        def emailsendstart():
            done.place_forget()
            Reciver_email.place_forget()
            Message1.place_forget()
            So1.place_forget()

            mail = str(Reciver_email.get())
            mess = str(Message1.get())


            file = open('Registered_Emails', "r+")
            details = file.read()
            file.close()

            info = Label(root, text = details) 
            info.pack()
            Num = Label(root, text = "Type The email number which you want to use")
            Num.pack()
            Email_num = Entry(root, width = 50)
            Email_num.pack()
            

            def Completep():
                
                number = int(Email_num.get())
                

                Number1 = number - 2
                Number2 = Number1 + number
                Number3 = Number2 + 1
                file = open("Registered_Emails", "r+")
                content = file.readlines()
                emailnum = content[Number2]
                passnum = content[Number3]
            

           
            
                server = smt.SMTP('SMTP.gmail.com',587)
                server.starttls()
                server.login(emailnum,passnum)
                server.sendmail(emailnum,mail,mess)
                info.pack_forget()
                Email_num.pack_forget()
                Num.pack_forget()
                Ok.pack_forget()

                Sent = Label(root, text = "Sucessfully Sent Email!")
                Sent.place(relx = 1, x = -150,y = 125, anchor = CENTER)

            Ok = Button(root, text = "Submit", command = Completep)
            Ok.pack()

        done = Button(root, text = "Submit", command = check_for_internet)
        done.place(relx = 1, x = -165,y = 150)

    def addemail1():
        welc1.place_forget()
        Send_email.place_forget()
        Add_email.place_forget()
        Senders_email = Entry(root, width = 40) 
        Senders_email.place(relx = 1, x = -150, y = 85, anchor = CENTER)
        Senders_email.insert(0, "Type your email")

        Senders_password = Entry(root, width = 40)
        Senders_password.place(relx = 1, x = -150,y = 125, anchor = CENTER)
        Senders_password.insert(0,"Type your password")
    
        def submit_email():
            email = Senders_email.get()
            password = Senders_password.get()
            with open("Registered_Emails","a") as f :                        
                f.write(f"{email} \n ")
                f.write(f"{password} \n")
            Submit.place_forget()
            Senders_email.place_forget()
            Senders_password.place_forget()
            Made_true()

        Submit = Button(root, width = 20, text = "submit",command = submit_email )
        Submit.place(relx = 1, x = -165,y = 150)
        
    
    
    welc1 = Label(root,text = "Welcome To Email Bot")
    welc1.place(relx = 1, x = -150, y = 45, anchor = N)
    Send_email = Button(root, text = "Send email", command = internet_true, )
    Send_email.place(relx = 1, x = -150, y = 85, anchor = CENTER)                                                                              
    Add_email = Button(root,text = "Add email", command = addemail1)
    Add_email.place(relx = 1, x = -150,y = 125, anchor = CENTER)
    



def addemail():


    Senders_email = Entry(root, width = 40) 
    Senders_email.place(relx = 1, x = -150, y = 85, anchor = CENTER)
    Senders_email.insert(0, "Type your email")

    Senders_password = Entry(root, width = 40)
    Senders_password.place(relx = 1, x = -150,y = 125, anchor = CENTER)
    Senders_password.insert(0,"Type your password")
    
    def submit_email():
        email = Senders_email.get()
        password = Senders_password.get()
        with open("Registered_Emails","a") as f :                        
            f.write(f"{email} \n ")
            f.write(f"{password} \n")
        Submit.place_forget()
        Welcome.place_forget
        Senders_email.place_forget()
        Senders_password.place_forget()
        Welcome.place_forget()
        Made_true()
        

    Submit = Button(root, width = 20, text = "submit",command = submit_email )
    Submit.place(relx = 1, x = -165,y = 150)
    



Made = egmail()

if Made == True: 
    Made_true()

if Made == False:
    Welcome = Label(root, text = "WELCOME TO EMAIL BOT \n REGISTER YOUR EMAIL ")
    Welcome.place(relx = 1, x = -150, y = 45, anchor = N)
    addemail()
    


root.mainloop()





    










             
             
            








