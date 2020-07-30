from tkinter import *
import os
from PIL import ImageTk,Image
import random
import json

def delete3():
    screen4.destroy()


def delete4():
    screen5.destroy()


with open('./data.json', encoding="utf8") as f:
    data = json.load(f)

# convert the dictionary in lists of questions and answers_choice
questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]

answers = [1, 2, 1, 1, 3, 1, 0, 1, 3, 3]

user_answer = []
def Res():
    print("Score List")
    uid_info=uid.get()
    score_info=score.get()
    file = open(uid_info, "w")
    file.write(uid_info+" "+score_info+"\n")
    file.close()

indexes = []

def gen():
    global indexes
    while (len(indexes) < 5):
        x = random.randint(0, 9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        screen6,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        screen6,
        font=("Consolas", 20),
        background="#ffffff",
    )
    labelresulttext.pack()
    print("Score is : ",str(score))
    if score >= 20:
        labelresulttext.configure(text="You Are Excellent !!",bg=None,fg="red",font=('arial', 20, 'bold'))
    elif (score >= 10 and score < 20):
        labelresulttext.configure(text="You Can Be Better !!",bg=None,fg="red",font=('arial', 20, 'bold'))
    else:
        labelresulttext.configure(text="You Should Work Hard !!",bg=None,fg="red",font=('arial', 20, 'bold'))


def calc():
    global indexes, user_answer, answers,score
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)


ques = 1


def selected():
    global radiovar, user_answer
    global lblQuestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text=questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        calc()


def startquiz():
    global screen6
    screen6 = Toplevel(screen)
    screen6.config(bg="snow")
    global lblQuestion, r1, r2, r3, r4
    lblQuestion = Label(
        screen6,
        text=questions[indexes[0]],
        font=("Consolas", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblQuestion.pack(pady=(100, 30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        screen6,
        text=answers_choice[indexes[0]][0],
        font=("Times", 12),
        value=0,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        screen6,
        text=answers_choice[indexes[0]][1],
        font=("Times", 12),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        screen6,
        text=answers_choice[indexes[0]][2],
        font=("Times", 12),
        value=2,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        screen6,
        text=answers_choice[indexes[0]][3],
        font=("Times", 12),
        value=3,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r4.pack(pady=5)


def startIspressed():
    gen()
    startquiz()


def login_sucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Quiz Start")
    screen3.geometry("1200x800")



    lblInstruction = Label(
        screen3,
        text="Read The Rules And\nClick Start Once You Are ready",
        background="#ffffff",
        font=("Consolas", 14),
        justify="center",
    )
    lblInstruction.pack(pady=(10, 100))
    btnStart = Button(screen3, text="Start Quiz", width=24, height=1, bg="gray", borderwidth=15, relief=SUNKEN,
                      fg="#FACA2F", padx=5, pady=5, font=('arial', 10, 'bold'), command=startIspressed)
    btnStart.place(x=500,y=400)
    Label(screen3,text="Are you ready for Quiz",bg=None,fg="#FACA2F",font=('arial', 20, 'bold')).place(x=460,y=350)
    lblRules = Label(
        screen3,
        text="This quiz contains 10 questions\nYou will get 20 seconds to solve a question\nOnce you select a radio button that will be a final choice\nhence think before you select",
        width=155,
        font=("Times", 14),
        background="#000000",
        foreground="#FACA2F",
    )
    lblRules.pack(side=BOTTOM)


def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error").pack()
    Button(screen4, text="OK", command=delete3).pack()

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()


def register_user():
    print("working")

    email_info = email.get()
    password_info = password.get()
    name_info=name.get()
    uid_info=uid.get()
    file = open(email_info, "w")
    file.write(email_info + "\n")
    file.write(password_info+"\n")
    file.write(name_info+"\n")
    file.write(uid_info+"\n")
    file.close()

    email_entry.delete(0, END)
    password_entry.delete(0, END)
    name_entry.delete(0,END)
    uid_entry.delete(0,END)


    Label(screen1, text="Registration Sucess", fg="green", font=("calibri", 11)).pack()


def login_verify():
    email1 = email_verify.get()
    password1 = password_verify.get()
    email_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if email1 in list_of_files:
        file1 = open(email1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognised()

    else:
        user_not_found()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("1200x800")
    screen1.iconbitmap("img.ico")
    def button_hover(e):
        my_button1["bg"] = "orange"
    def button_hover_leave(e):
        my_button1["bg"] = "black"
    global email
    global password
    global name
    global uid
    global name_entry
    global uid_entry
    global email_entry
    global password_entry
    email = StringVar()
    password = StringVar()
    name=StringVar()
    uid=StringVar()

    Label(screen1, text="Please enter details below",fg="red",bg=None,relief=SUNKEN,font=('arial', 20, 'bold')).place(x=600,y=155)
    Label(screen1, text="").pack()
    Label(screen1,text="Name : ",borderwidth=15,width=10,relief=SUNKEN,font=('arial', 20, 'bold')).place(x=500,y=200)
    name_entry=Entry(screen1,textvariable=name, width=50, bd=5, insertwidth=4,borderwidth=15,relief=SUNKEN, bg="snow",justify="center")
    name_entry.place(x=720,y=202)
    Label(screen1,text="Uid : ",borderwidth=15,width=10,relief=SUNKEN,font=('arial', 20, 'bold')).place(x=500,y=300)
    uid_entry=Entry(screen1,textvariable=uid, width=50, bd=5, insertwidth=4,borderwidth=15,relief=SUNKEN, bg="snow",justify="center")
    uid_entry.place(x=720,y=302)
    Label(screen1, text="Email : ",borderwidth=15,width=10,relief=SUNKEN,font=('arial', 20, 'bold')).place(x=500,y=400)
    email_entry = Entry(screen1,textvariable=email, width=50, bd=5, insertwidth=4,borderwidth=15,relief=SUNKEN, bg="snow",justify="center")
    email_entry.place(x=720,y=402)
    Label(screen1, text="Password : ",borderwidth=15,width=10,relief=SUNKEN,font=('arial', 20, 'bold')).place(x=500,y=500)
    password_entry = Entry(screen1,textvariable=password, width=50, bd=5, insertwidth=4,borderwidth=15,relief=SUNKEN, bg="snow",justify="center",show="*")
    password_entry.place(x=720,y=502)
    my_button1=Button(screen1, text="Register", width=24, height=1, bg="gray",borderwidth=15,relief=SUNKEN, fg="white", padx=5, pady=5, font=('arial', 10, 'bold'), command=register_user)
    my_button1.place(x=700,y=602)
    my_button1.bind("<Enter>",button_hover)
    my_button1.bind("<Leave>",button_hover_leave)

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("1200x800")
    screen2.iconbitmap("img.ico")
    Label(screen2, text="Please enter details below to login",fg="red",bg=None,font=('arial', 15, 'bold')).place(x=650,y=160)
    screen2.config(bg="white")
    global  email_verify
    global password_verify

    email_verify = StringVar()
    password_verify = StringVar()

    global email_entry1
    global password_entry1
    def button_hover(e):
        my_button1["bg"] = "orange"
    def button_hover_leave(e):
        my_button1["bg"] = "black"
    Label(screen2, text="Email : ",borderwidth=15,width=9,relief=SUNKEN,font=('arial', 20, 'bold')).place(x=500,y=200)
    email_entry1 = Entry(screen2, width=50, bd=5, insertwidth=4, bg="snow",borderwidth=15,relief=SUNKEN,justify="center", textvariable=email_verify)
    email_entry1.place(x=700,y=205)
    Label(screen2, text="Password : ",borderwidth=15,relief=SUNKEN,font=('arial', 20, 'bold')).place(x=500,y=300)
    password_entry1 = Entry(screen2, width=50, bd=5, insertwidth=4,show="*",bg="snow",borderwidth=15,relief=SUNKEN,justify="center", textvariable=password_verify)
    password_entry1.place(x=700,y=305)
    my_button1=Button(screen2, text="Login",  width=24, height=1, bg="gray",borderwidth=15,relief=SUNKEN, fg="white", padx=5, pady=5, font=('arial', 10, 'bold'),command=login_verify)
    my_button1.place(x=700,y=400)
    my_button1.bind("<Enter>",button_hover)
    my_button1.bind("<Leave>",button_hover_leave)


def main_screen():
    global screen

    def button_hover(e):
        my_button1["bg"] = "orange"
    def button_hover_leave(e):
        my_button1["bg"] = "white"

    def button_hover_1(e):
        my_button2["bg"] = "orange"

    def button_hover_leave_1(e):
        my_button2["bg"] = "white"

    screen = Tk()
    screen.geometry("1200x800")
    screen.config(bg="snow")
    screen.title("Quiz")

    screen.iconbitmap("img.ico")
    img=ImageTk.PhotoImage(Image.open("img3.jpg"))
    lab = Label(image=img,bg=None)
    lab.place(x=650,y=50)
    my_button1=Button(text="Login", height="2", width="25", bg="white",borderwidth=15,relief=SUNKEN, fg="black", padx=5, pady=5, font=('arial', 15, 'bold'), command=login)
    my_button1.place(x=595,y=300)
    my_button2=Button(text="Register", height="2", width="25", bg="white",borderwidth=15,relief=SUNKEN, fg="black", padx=5, pady=5, font=('arial', 15, 'bold'), command=register)
    my_button2.place(x=595,y=450)
    my_button1.bind("<Enter>",button_hover)
    my_button1.bind("<Leave>",button_hover_leave)
    my_button2.bind("<Enter>",button_hover_1)
    my_button2.bind("<Leave>",button_hover_leave_1)
    Label(text="Click on register button if not registered else press login",bg=None,fg="red").place(x=600,y=600)

    screen.mainloop()


main_screen()