import tkinter as tk
import socket
import threading
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="bcProject"
)

nickname = input("Choose your nickname before joining server: ")

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#this is the ip of the server that we want to connect to
client.connect(("127.0.0.1", 55555))

def receive():

    while True:
        try:
            #receiving from the server
            message = client.recv(1024).decode('ascii')
            if (message == 'NICK'):
                client.send(nickname.encode('ascii'))

            else:
                print(message)

        except:
            (print("An error Occured!"))
            client.close()
            break


def write():
    while True:
        messageOnly = f'{input("")}'
        message = f'{nickname}: {messageOnly}'
        client.send(message.encode('ascii'))
        if "nimu" in messageOnly or "sami" in messageOnly:
            window = tk.Tk()
            window.title("Welcome to LikeGeeks app")
            lbl = tk.Label(window, text="কি ভাতিজা......  কি লিখো এইসব? ভালো হয়ে যাও", foreground="red", background="black", font=("Arial Bold", 36))
            lbl.grid(column=0, row=0)
            window.mainloop()
            return
        elif "word" not in messageOnly:
            print("Text verified")

        mycursor = mydb.cursor()
        sql = "INSERT INTO usercomment (name, message) VALUES (%s, %s)"
        val = (nickname, messageOnly)
        mycursor.execute(sql, val)
        mydb.commit()
#we are running 2 threads receive thread and the write thread


#the thread for receiving
receive_thread = threading.Thread(target = receive)
receive_thread.start()


#the thread for writing
write_thread = threading.Thread(target = write)
write_thread.start()




