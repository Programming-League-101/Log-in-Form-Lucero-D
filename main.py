import tkinter
from getpass import getpass




height = 600 #height
width = 500 #width
def main_page():
    main_page = tkinter.Toplevel()
    main_page.title("Menu")
    f = open("sample.txt", "r")
    g = open("sample1.txt", "r")
    read = f.read()
    read1 = g.read()
    canvas = tkinter.Canvas(main_page, bg='gray', height=720, width=1280)
    canvas.pack()

    photo = tkinter.PhotoImage(file='7shi to kroni.png')
    photo_label = tkinter.Label(main_page, image=photo)
    photo_label.place(relwidth=1, relheight=1)

    main_page.mainloop()





def Login_GUI():
    main = tkinter.Tk()
    main.title('Log in Form')

    def Button1():
        createacc()

    def Button(Enter, Enter1):
        f = open("sample.txt", "r")
        g = open("sample1.txt", "r")
        read = f.read()
        read1 = g.read()
        if len(Enter) < 8 or len(Enter1) < 4:
            label3['text'] = "This Account does not Exist!"
        else:
            if Enter not in read and Enter1 not in read1:
                label3['text'] = "This Account does not Exist!"
            else:
                label3['text'] = "Welcome!" + '\n' + Enter
                main_page()



    canvas = tkinter.Canvas(main, bg='gray', height=height, width=width)
    canvas.pack()

    photo = tkinter.PhotoImage(file='7shi to kroni.png')
    photo_label = tkinter.Label(main, image=photo)
    photo_label.place(relwidth=1, relheight=1)

    framework = tkinter.Frame(main, bg='#80c1ff', bd=5)
    framework.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.05, anchor='n')

    label1 = tkinter.Label(framework, text="Username:")
    label1.place(relwidth=0.2, relheight=1)

    Enter = tkinter.Entry(framework, font=30, bg='gray')
    Enter.place(relwidth=0.8, relheight=1, relx=0.2)

    Second_framework = tkinter.Frame(main, bg='#80c1ff', bd=5)
    Second_framework.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.05, anchor='n')

    label2 = tkinter.Label(Second_framework, text="Password:")
    label2.place(relwidth=0.2, relheight=1)

    Enter1 = tkinter.Entry(Second_framework, font=30, bg='gray',  show="*")
    Enter1.place(relwidth=0.8, relheight=1, relx=0.2)

    third_framework = tkinter.Frame(main, bg='#80c1ff', bd=3)
    third_framework.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.05, anchor='n')

    button = tkinter.Button(third_framework, text="Log In", anchor='n', command=lambda: Button(Enter.get(), Enter1.get()))
    button.place(relwidth=0.3, relheight=1, relx=0.15)

    button1 = tkinter.Button(third_framework, text="Create Account!", anchor='n', command=lambda: Button1())
    button1.place(relwidth=0.3, relheight=1, relx=0.55)

    fourth_framework = tkinter.Frame(main, bg='#80c1ff', bd=5)
    fourth_framework.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.65, anchor='n')

    label3 = tkinter.Label(fourth_framework, bg='gray', font='40',)
    label3.place(relwidth=1, relheight=1)


    main.mainloop()







def createacc():
    main1 = tkinter.Toplevel()
    main1.title('Registration Form')




    def create_button(entry, entry1, entry2, entry3):
        if entry == entry1:
            f = open("sample.txt", "r")
            read = f.read()
            if len(entry) < 8:
                flabel['text'] = ("Username shoul be 8 or more characters long!")
            else:
                if entry not in read:
                    f = open("sample.txt", "a")
                    f.write("\n")
                    f.write(entry)
                    f.close()
                    if entry2 == entry3:
                        g = open("sample1.txt", "r")
                        read1 = g.read()
                        if len(entry2) < 4:
                            flabel['text'] = ("Password should be 4 or more characters long")
                        else:
                            if entry2 not in read1:
                                g = open("sample1.txt", "a")
                                g.write("\n")
                                g.write(entry2)
                                g.close()
                                flabel['text'] = "Account Successfully Created"

                            else:
                                g = open("sample1.txt", "r")
                                g.read()
                                g.close()
                                flabel['text'] = "Account Successfully Created"

                    else:
                        flabel['text'] = "Password is not Identical!"
                else:
                    flabel['text'] = "Account Already Exist!"
        else:
            flabel['text'] = "Username is not Identical!"

    canvas1 = tkinter.Canvas(main1, bg='gray', height=height, width=width)
    canvas1.pack()

    photo1 = tkinter.PhotoImage(file='pyimage2.png')
    photo_label1 = tkinter.Label(main1, image=photo1)
    photo_label1.place(relwidth=1, relheight=1)

    framework = tkinter.Frame(main1, bg='#80c1ff', bd=10)
    framework.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')

    labelcreate = tkinter.Label(main1, text="Create Your Account!")
    labelcreate.place(rely=0.1, relx=0.39)

    framework1 = tkinter.Frame(main1, bg='#80c1ff', bd=1)
    framework1.place(relx=0.5, rely=0.15, relwidth=1, relheight=0.1, anchor='n')

    ulabel = tkinter.Label(framework1, bg='white', text="Enter Your Username")
    ulabel.place(relx=0.25, rely=0, relwidth=0.5, relheight=0.5)

    entry = tkinter.Entry(framework1, bg='gray')
    entry.place(relx=0.25, rely=0.5, relwidth=0.5, relheight=0.5)

    framework2 = tkinter.Frame(main1, bg='#80c1ff', bd=1)
    framework2.place(relx=0.5, rely=0.25, relwidth=1, relheight=0.1, anchor='n')

    ulabel1 = tkinter.Label(framework2, bg='white', text="Confirm Your Username")
    ulabel1.place(relx=0.25, rely=0, relwidth=0.5, relheight=0.5)

    entry1 = tkinter.Entry(framework2, bg='gray')
    entry1.place(relx=0.25, rely=0.5, relwidth=0.5, relheight=0.5)

    framework3 = tkinter.Frame(main1, bg='#80c1ff', bd=1)
    framework3.place(relx=0.5, rely=0.35, relwidth=1, relheight=0.1, anchor='n')

    ulabel2 = tkinter.Label(framework3, bg='white', text="Enter Your Password")
    ulabel2.place(relx=0.25, rely=0, relwidth=0.5, relheight=0.5)

    entry2 = tkinter.Entry(framework3, bg='gray', show="*")
    entry2.place(relx=0.25, rely=0.5, relwidth=0.5, relheight=0.5)

    framework4 = tkinter.Frame(main1, bg='#80c1ff', bd=1)
    framework4.place(relx=0.5, rely=0.45, relwidth=1, relheight=0.1, anchor='n')

    ulabel3 = tkinter.Label(framework4, bg='white', text="Confirm Your Password")
    ulabel3.place(relx=0.25, rely=0, relwidth=0.5, relheight=0.5)

    entry3 = tkinter.Entry(framework4, bg='gray', show="*")
    entry3.place(relx=0.25, rely=0.5, relwidth=0.5, relheight=0.5)

    button = tkinter.Button(main1, text="Create Account", command=lambda: create_button(entry.get(), entry1.get(), entry2.get(), entry3.get()))
    button.place(rely=0.55, relx=0.41)

    pbutton = tkinter.Button(main1, text="Proceed to Log In", command=main1.destroy)
    pbutton.place(rely=0.6, relx=0.4)

    flabel = tkinter.Label(framework, bg='gray', bd=2)
    flabel.place(relx=0.25, rely=0.65, relwidth=0.5, relheight=0.3)

    main1.mainloop()

Login_GUI()











