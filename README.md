<h1 align=center><b>Quiz_With_Registration_And_Login</b></h1>

<h2><i><b> Source Code</b></i></h2>

```
from tkinter import *
import os
from PIL import ImageTk,Image
import random
import json
import time
from tkinter import messagebox
import re

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def closeAll():
    screen.destroy()
    screen6.destroy()



with open('./data.json', encoding="utf8") as f:
    data = json.load(f)

questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]

answers = [0, 1, 1, 1, 3, 1, 0, 1, 3, 3]

user_answer = []

indexes = []

def DataStore():
    num_info=num.get()
    comment_info=comment.get()
    var1_info=var1.get()
    var2_info=var2.get()
    var3_info=var3.get()

    with open("records.txt","a") as file:
        if num_info:
            file.write("PC No. : "+num_info+"\n")
            file.write("Scores get : "+str(score)+"\n")
            file.write("Comments : "+comment_info+"\n")
            file.write("Rate us : "+str(var1_info)+" "+str(var2_info)+" "+str(var3_info)+"\n\n")
            file.close()
    closeAll()

def gen():
    global indexes
    while (len(indexes) < 5):
        x = random.randint(0, 9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    global num
    global comment
    global var1,var2,var3
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
    Label(screen6,bg="gold",width=250,height=5).place(x=0,y=0)
    Label(screen6,bg="snow",width=10,height=250).pack(side=LEFT)
    Label(screen6,bg="snow",width=10,height=250).pack(side=RIGHT)
    Label(screen6,bg="gold",width=250,height=5).pack(side=BOTTOM)
    labelresulttext.pack()
    num=StringVar()
    comment=StringVar()
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    if score >= 20:
        labelresulttext.configure(text="You Are Excellent !!",bg="snow",fg="red",font=('arial', 30, 'bold'))
        Label(screen6,text=("Your score : "+str(score)),fg="red",bg="snow",font=('arial', 40, 'bold')).pack()
        Label(screen6, text="\nPC no.", fg="red",bg="snow", font=('arial', 20, 'bold'),justify=CENTER).pack()
        Entry(screen6, textvariable=num, width=20, bd=5, insertwidth=4, borderwidth=15, relief=SUNKEN,
              bg="snow", justify="center").pack()
        lab7 = Label(screen6, text="\nRate us  ", width=24,bg="snow", font=('arial', 20, 'bold'),justify=CENTER).pack()
        Checkbutton(screen6, text=" Excellence ", variable=var1,font=('arial', 10, 'bold'), bg="snow",justify=CENTER).pack()
        Checkbutton(screen6, text=" Good  ", variable=var2,font=('arial', 10, 'bold'), bg="snow",justify=CENTER).pack()
        Checkbutton(screen6, text=" Average ", variable=var3,font=('arial', 10, 'bold'), bg="snow",justify=CENTER).pack()
        Label(screen6, text="\nComments:", fg="red", bg="snow", font=('arial', 20, 'bold'),justify=CENTER).pack()
        Entry(screen6, textvariable=comment, width=50, bd=5,relief=SUNKEN,
              bg="snow", justify="center",font=('arial', 15, 'bold')).pack(ipady=40)
        Button(screen6, text="Submit", height="2", width="25", bg="white",borderwidth=15,relief=SUNKEN, fg="black", padx=5, pady=5, font=('arial', 15, 'bold'), command=DataStore).pack(side=BOTTOM)
    elif (score >= 10 and score < 20):
        labelresulttext.configure(text="You Can Be Better !!",bg="snow",fg="red",font=('arial', 30, 'bold'))
        Label(screen6, text=("Your score : " + str(score)), fg="red", bg="snow", font=('arial', 40, 'bold')).pack()
        Label(screen6, text="\nPC no.", fg="red", bg="snow", font=('arial', 20, 'bold'), justify=CENTER).pack()
        Entry(screen6, textvariable=num, width=20, bd=5, insertwidth=4, borderwidth=15, relief=SUNKEN,
              bg="snow", justify="center").pack()
        lab7 = Label(screen6, text="\nRate us  ", width=24, bg="snow", font=('arial', 20, 'bold'),
                     justify=CENTER).pack()
        Checkbutton(screen6, text=" Excellence ", variable=var1, font=('arial', 10, 'bold'), bg="snow",
                    justify=CENTER).pack()
        Checkbutton(screen6, text=" Good  ", variable=var2, font=('arial', 10, 'bold'), bg="snow",
                    justify=CENTER).pack()
        Checkbutton(screen6, text=" Average ", variable=var3, font=('arial', 10, 'bold'), bg="snow",
                    justify=CENTER).pack()
        Label(screen6, text="\nComments:", fg="red", bg="snow", font=('arial', 20, 'bold'), justify=CENTER).pack()
        Entry(screen6, textvariable=comment, width=50, bd=5, relief=SUNKEN,
              bg="snow", justify="center", font=('arial', 15, 'bold')).pack(ipady=40)
        Button(screen6, text="Submit", height="2", width="25", bg="white", borderwidth=15, relief=SUNKEN, fg="black",
               padx=5, pady=5, font=('arial', 15, 'bold'), command=DataStore).pack(side=BOTTOM)
    else:
        labelresulttext.configure(text="You Should Work Hard !!",bg="snow",fg="red",font=('arial', 30, 'bold'))
        Label(screen6,text=("Your score : "+str(score)),fg="red",bg="snow",font=('arial', 40, 'bold')).pack()
        Label(screen6, text="\nPC no.", fg="red",bg="snow", font=('arial', 20, 'bold'),justify=CENTER).pack()
        Entry(screen6, textvariable=num, width=20, bd=5, insertwidth=4, borderwidth=15, relief=SUNKEN,
              bg="snow", justify="center").pack()
        lab7 = Label(screen6, text="\nRate us  ", width=24,bg="snow", font=('arial', 20, 'bold'),justify=CENTER).pack()
        Checkbutton(screen6, text=" Excellence ", variable=var1,font=('arial', 10, 'bold'), bg="snow",justify=CENTER).pack()
        Checkbutton(screen6, text=" Good  ", variable=var2,font=('arial', 10, 'bold'), bg="snow",justify=CENTER).pack()
        Checkbutton(screen6, text=" Average ", variable=var3,font=('arial', 10, 'bold'), bg="snow",justify=CENTER).pack()
        Label(screen6, text="\nComments:", fg="red", bg="snow", font=('arial', 20, 'bold'),justify=CENTER).pack()
        Entry(screen6, textvariable=comment, width=50, bd=5,relief=SUNKEN,
              bg="snow", justify="center",font=('arial', 15, 'bold')).pack(ipady=40)
        Button(screen6, text="Submit", height="2", width="25", bg="white",borderwidth=15,relief=SUNKEN, fg="black", padx=5, pady=5, font=('arial', 15, 'bold'), command=DataStore).pack(side=BOTTOM)

def calc():
    global indexes, user_answer, answers,score
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    else:
        x -= 1
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
    screen6.geometry("1200x800")
    global lblQuestion, r1, r2, r3, r4
    screen6.iconbitmap("img.ico")
    screen6.overrideredirect(True)
    screen6.overrideredirect(False)
    screen6.attributes('-fullscreen', True)
    lblQuestion = Label(
        screen6,
        text=questions[indexes[0]],
        font=("Consolas", 25,'bold'),
        width=500,
        justify="center",
        wraplength=400,
        background="snow",
    )
    lblQuestion.pack(pady=(100, 30))
    global radiovar
    radiovar = IntVar()
    def button_hover1(e):
        r1["bg"] = "snow2"

    def button_hover_leave1(e):
        r1["bg"] = "snow"

    def button_hover2(e):
        r2["bg"] = "snow2"

    def button_hover_leave2(e):
        r2["bg"] = "snow"

    def button_hover3(e):
        r3["bg"] = "snow2"

    def button_hover_leave3(e):
        r3["bg"] = "snow"
    def button_hover4(e):
        r4["bg"] = "snow2"

    def button_hover_leave4(e):
        r4["bg"] = "snow"
    radiovar.set(-1)
    r1 = Radiobutton(
        screen6,
        text=answers_choice[indexes[0]][0],
        font=('arial', 25, 'bold'),
        value=0,
        variable=radiovar,
        command=selected,
        background="snow",
    )
    r1.pack(pady=5)
    r1.bind("<Enter>",button_hover1)
    r1.bind("<Leave>",button_hover_leave1)
    r2 = Radiobutton(
        screen6,
        text=answers_choice[indexes[0]][1],
        font=('arial', 25, 'bold'),
        value=1,
        variable=radiovar,
        command=selected,
        background="snow",
    )
    r2.pack(pady=5)
    r2.bind("<Enter>",button_hover2)
    r2.bind("<Leave>",button_hover_leave2)
    r3 = Radiobutton(
        screen6,
        text=answers_choice[indexes[0]][2],
        font=('arial', 25, 'bold'),
        value=2,
        variable=radiovar,
        command=selected,
        background="snow",
    )
    r3.pack(pady=5)
    r3.bind("<Enter>",button_hover3)
    r3.bind("<Leave>",button_hover_leave3)
    r4 = Radiobutton(
        screen6,
        text=answers_choice[indexes[0]][3],
        font=('arial', 25, 'bold'),
        value=3,
        variable=radiovar,
        command=selected,
        background="snow",
    )
    r4.pack(pady=5)
    r4.bind("<Enter>",button_hover4)
    r4.bind("<Leave>",button_hover_leave4)

def startIspressed():
    gen()
    startquiz()


def login_sucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Quiz Start")
    screen3.geometry("1200x800")
    screen3.iconbitmap("img.ico")
    def button_hover(e):
        btnStart["bg"] = "orange"
    def button_hover_leave(e):
        btnStart["bg"] ="snow"
    lblInstruction = Label(
        screen3,
        text="Read The Rules And\nClick Start Once You Are ready",
        background="white",
        fg="black",
        font=("Consolas", 18),
        justify="center",
    )
    lblInstruction.pack(pady=(10, 100))
    btnStart = Button(screen3, text="Start Quiz", width=24, height=1, bg="snow", borderwidth=15, relief=SUNKEN,
                      fg="black", padx=5, pady=5, font=('arial', 10, 'bold'), command=startIspressed)
    btnStart.pack(side=BOTTOM)
    btnStart.bind("<Enter>",button_hover)
    btnStart.bind("<Leave>",button_hover_leave)
    Label(screen3,text="Quiz Time",bg=None,fg="gold",font=('Courier', 80, 'bold'),justify="center").pack(pady=(10,30))
    Label(screen3,text="Click if ready",bg=None,fg="gold",font=('arial', 20, 'bold')).pack(side=BOTTOM)
    Label(screen3,text="1.  All Questions are compulsary.\n\n2.  Each question contain 5 points.\n\n3.  No negative marking.\n\n4.  In case if you find merge in any other activity than strict action will be taken against you.\n\n5.  One attempt for each question.\n\n6. Once u move to next question previous answer can not be canged only one attempt for each question.\n\n7. In last you need to enter your system number to save your marks else no marks is being uploaded.\n\n",width=155,font=("Times", 16,"bold"),background="white",foreground="black").pack(side=LEFT)


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
    Label(screen5, text="Entry Left").pack()
    Button(screen5, text="OK", command=delete4).pack()

def delete9():
    screen10.destroy()
def new():
    global screen10
    screen10 = Toplevel(screen1)
    screen10.title("Warning")
    screen10.geometry("200x100")
    Label(screen10, text="Enter Name").pack()
    Button(screen10, text="OK", command=delete9).pack()

def delete10():
    screen11.destroy()
def new1():
    global screen11
    screen11 = Toplevel(screen1)
    screen11.title("Warning")
    screen11.geometry("200x100")
    Label(screen11, text="Enter Correct \n Email").pack()
    Button(screen11, text="OK", command=delete10).pack()

def delete11():
    screen12.destroy()
def new2():
    global screen12
    screen12 = Toplevel(screen1)
    screen12.title("Warning")
    screen12.geometry("200x100")
    Label(screen12, text="Enter Uid").pack()
    Button(screen12, text="OK", command=delete11).pack()

def delete12():
    screen13.destroy()
def new3():
    global screen13
    screen13 = Toplevel(screen1)
    screen13.title("Warning")
    screen13.geometry("300x150")
    Label(screen13, text="Enter in this\n Format \n uppercase letters: A-Z \n lowercase letters: a-z \n numbers: 0-9 \n any of the special characters: @#$%^&+=").pack()
    Button(screen13, text="OK", command=delete12).pack()


def register_user():
    global name_info
    global uid_info
    global email_info
    email_info = email.get()
    password_info = password.get()
    name_info=name.get()
    uid_info=uid.get()
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$.%^&+=]).*$"
    if name_info:
        if (re.search(regex,email.get())):
            if uid_info:
                if (re.findall(pattern,password.get())):
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
                    Label(screen1, text="Registration Sucess", fg="green", font=("calibri", 11)).place(x=755,y=670)
                else:
                    new3()
            else:
                new2()
        else:
            new1()
    else:
        new()


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
def sucess():
    pass

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("1200x800")
    screen1.iconbitmap("img.ico")
    screen1.config(bg="peach puff")
    def button_hover(e):
        my_button1["bg"] = "orange"
    def button_hover_leave(e):
        my_button1["bg"] = "white"
    def userText(event):
        email_entry.delete(0, END)
        usercheck = True
    def nameText(event):
        name_entry.delete(0, END)
        namecheck = True

    def uidtext(event):
        uid_entry.delete(0, END)
        uidcheck = True

    usercheck = False
    namecheck=False
    uidcheck=False
    global email
    global password
    global name
    global uid
    global name_entry
    global uid_entry
    global email_entry
    global password_entry
    global font1
    def caps(event):
        name.set(name.get().upper())
    def caps1(event):
        uid.set(uid.get().upper())
    font1=('open sans',10,'bold')
    email = StringVar()
    password = StringVar()
    name=StringVar()
    uid=StringVar()
    Label(screen1,bg="black",width=250,height=5).place(x=0,y=0)
    Label(screen1,bg="light blue",width=10,height=250).pack(side=LEFT)
    Label(screen1,bg="light blue",width=10,height=250).pack(side=RIGHT)
    Label(screen1,bg="black",text="Register only once",fg="gold",font=('arial',20,'bold'),width=250,height=3).pack(side=BOTTOM)
    Label(screen1, text="Please enter details below",fg="red",bg=None,relief=SUNKEN,font=('arial', 20, 'bold')).place(x=600,y=155)

    mandatory_entry = Entry(screen1)
    Label(screen1,text="Name : ",borderwidth=15,width=10,relief=SUNKEN,font=('arial', 20, 'bold')).place(x=500,y=200)
    name_entry=Entry(screen1,textvariable=name, width=50, bd=5,font=font1, insertwidth=4,borderwidth=15,relief=SUNKEN, bg="snow",justify="center")
    name_entry.insert(0,"Name")
    name_entry.bind("<Button>",nameText)
    name_entry.bind("<KeyRelease>",caps)
    name_entry.place(x=720,y=202)
    Label(screen1,text="Uid : ",borderwidth=15,width=10,relief=SUNKEN,font=('arial', 20, 'bold')).place(x=500,y=300)
    uid_entry=Entry(screen1,textvariable=uid, width=50, bd=5,font=font1, insertwidth=4,borderwidth=15,relief=SUNKEN, bg="snow",justify="center")
    uid_entry.insert(0,"UID")
    uid_entry.bind("<Button>",uidtext)
    uid_entry.bind("<KeyRelease>",caps1)
    uid_entry.place(x=720,y=302)
    Label(screen1, text="Email : ",borderwidth=15,width=10,relief=SUNKEN,font=('arial', 20, 'bold')).place(x=500,y=400)
    email_entry = Entry(screen1,textvariable=email,width=50, bd=5,font=font1, insertwidth=4,borderwidth=15,relief=SUNKEN, bg="snow",justify="center")
    email_entry.insert(0, "abc.123@gmail.com")
    email_entry.bind("<Button>", userText)
    email_entry.place(x=720,y=402)
    Label(screen1, text="Password : ",borderwidth=15,width=10,relief=SUNKEN,font=('arial', 20, 'bold')).place(x=500,y=500)
    password_entry = Entry(screen1,textvariable=password, width=50, bd=5,font=font1, insertwidth=4,borderwidth=15,relief=SUNKEN, bg="snow",justify="center",show="*")
    password_entry.place(x=720,y=502)
    my_button1=Button(screen1, text="Register", height=1, width=20, bg="white",borderwidth=15,relief=SUNKEN, fg="black", padx=5, pady=4, font=('arial', 15, 'bold'), command=register_user)
    my_button1.place(x=700,y=580)
    screen1.bind("<Return>", lambda event=None: my_button1.invoke())
    my_button1.bind("<Enter>",button_hover)
    my_button1.bind("<Leave>",button_hover_leave)

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("1200x800")
    screen2.iconbitmap("img.ico")

    def userText(event):
        email_entry1.delete(0, END)
        usercheck = True
    usercheck = False
    Label(screen2, text="Please enter details below to login",fg="red",bg=None,font=('arial', 15, 'bold')).place(x=650,y=160)
    screen2.config(bg="light cyan")
    global  email_verify
    global password_verify

    email_verify = StringVar()
    password_verify = StringVar()
    global email_entry1
    global password_entry1
    def button_hover(e):
        my_button1["bg"] = "orange"
    def button_hover_leave(e):
        my_button1["bg"] = "white"
    font2=('open sans',10,'bold')
    Label(screen2,bg="black",width=250,height=5).place(x=0,y=0)
    Label(screen2,bg="snow",width=10,height=250).pack(side=LEFT)
    Label(screen2,bg="snow",width=10,height=250).pack(side=RIGHT)
    Label(screen2,bg="black",width=250,height=5).pack(side=BOTTOM)
    Label(screen2, text="Email : ",borderwidth=15,width=9,relief=SUNKEN,font=('arial', 20, 'bold')).place(x=500,y=200)
    email_entry1 = Entry(screen2, width=50, bd=5, insertwidth=4,font=font2, bg="snow",borderwidth=15,relief=SUNKEN,justify="center", textvariable=email_verify)
    email_entry1.insert(0,"abc.123@gmail.com")
    email_entry1.bind("<Button>",userText)
    email_entry1.place(x=700,y=205)
    Label(screen2, text="Password : ",borderwidth=15,relief=SUNKEN,font=('arial', 20, 'bold')).place(x=500,y=300)
    password_entry1 = Entry(screen2, width=50, bd=5, insertwidth=4,font=font2,show="*",bg="snow",borderwidth=15,relief=SUNKEN,justify="center", textvariable=password_verify)
    password_entry1.place(x=700,y=305)
    my_button1=Button(screen2, text="Login", height=1, width=22, bg="white",borderwidth=15,relief=SUNKEN, fg="black", padx=5, pady=5, font=('arial', 15, 'bold'),command=login_verify)
    my_button1.place(x=700,y=400)
    screen2.bind("<Return>", lambda event=None: my_button1.invoke())
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

    def button_hover3(e):
        Low["bg"] = "red"

    def button_hover_leave3(e):
        Low["bg"] = "black"

    screen = Tk()
    screen.geometry("1200x800")
    screen.config(bg="green4")
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
    Label(bg="gold4",width=250,height=2).pack(side=TOP)
    Label(bg="snow",width=10,height=60).pack(side=LEFT)
    Label(bg="snow",width=10,height=60).pack(side=RIGHT)
    Low=Label(text="Click on register button if not registered else press login",bg="black",width=100,height=4,fg="white", font=('arial', 25, 'bold'))
    Low.pack(side=BOTTOM)
    Low.bind("<Enter>",button_hover3)
    Low.bind("<Leave>",button_hover_leave3)
    screen.mainloop()


main_screen()
```

<p><b> There are some major changes which i have not shown here but you can download it from Project.zip file.</b></p>


![](https://github.com/Psingh12354/Quiz_With_Registration_And_Login/blob/master/img1.PNG)
![](https://github.com/Psingh12354/Quiz_With_Registration_And_Login/blob/master/img2.PNG)
![](https://github.com/Psingh12354/Quiz_With_Registration_And_Login/blob/master/img3.PNG)
![](https://github.com/Psingh12354/Quiz_With_Registration_And_Login/blob/master/img4.PNG)
![](https://github.com/Psingh12354/Quiz_With_Registration_And_Login/blob/master/img10.PNG)
![](https://github.com/Psingh12354/Quiz_With_Registration_And_Login/blob/master/img11.PNG)

[![](github.com/Psingh12354/Quiz_With_Registration_And_Login/blob/master/img1.PNG)](https://youtu.be/ylM1KvbX420)
