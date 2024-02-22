import datetime
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from DatabaseHelper import *



import re

# class Register:
    # def __init__(self):
def goon_mail(user):
    import mailllllling as m
    m.email(user)
def is_valid_email(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    print(re.fullmatch(pattern, email))
    if re.fullmatch(pattern, email):
        print("Valid")
        messagebox.showinfo("message","valid email")
    else:
        messagebox.showinfo("message","Enter valid email")
        print("INValid")




def create_user(en1,en2,en3,en5,en6,en7,en8,en9,en10):
    user = en5.get()
    print(user)
    name=en1.get()
    age=en2.get()
    phone_no=en3.get()
    weight=en7.get()
    pwd = en6.get()
    disease=en8.get()
    gender = en9.get()
    bloodgroup=en10.get()
    print(gender)

    today = datetime.datetime.today().date()
    expiry_date = today + datetime.timedelta(days=2)
    params = (name,age,phone_no,user, pwd,weight,disease,gender,bloodgroup, expiry_date)

    query = "Insert into blood_info(FULLNAME,AGE,PHONE,USERNAME,PWD,WEIGHT,DISEASE,GENDER,BLOODGROUP,EXPIRY_DATE) Values(%s,%s,%s,%s,SHA(%s),%s,%s,%s,%s,%s)"
    DatabaseHelper.execute_query(query, params)
    messagebox.showinfo('Success!', f'User with username {user} created successfully. Please login again.')

    is_valid_email(user)
    goon_mail(user)
    root.destroy()

root = Tk()
root.title("Blood donor system")
root.geometry('1000x1000')

f = Frame(root, height=1000, width=1000, bg="pink")
f.pack(fill=X)

lbl0 = Label(root, text="Registration Form", font=("Calibri", 30, "bold", "italic"), bg="pink")
lbl0.place(x=550, y=30)

lbl1 = Label(root, text="Full Name :", font=("Times New Roman", 16), bg="pink")
lbl1.place(x=500, y=150, height=40, width=100)
en1 = Entry(root)
en1.place(x=620, y=150, height=32, width=250)

lbl2 = Label(root, text="Age :", font=("Times New Roman", 16), bg="pink")
lbl2.place(x=500, y=210, height=40, width=100)
en2 = Entry(root)
en2.place(x=620, y=210, height=32, width=250)

lbl3 = Label(root, text="Gender :", font=("Times New Roman", 16), bg="pink")
lbl3.place(x=500, y=270, height=40, width=100)

en9 = StringVar()
en9.set("Male") # Set the default value to "Male"

r1 = Radiobutton(root, text="Male", font=("Calibri", 16), bg="pink", variable=en9, value="Male")
r1.place(x=620, y=275, height=29)

r2 = Radiobutton(root, text="Female", font=("Calibri", 16), bg="pink", variable=en9, value="Female")
r2.place(x=730, y=275, height=29)

r3 = Radiobutton(root, text="Others", font=("Calibri", 16), bg="pink", variable=en9, value="Others")
r3.place(x=860, y=275, height=29)



lbl4 = Label(root, text="Contact Number :", font=("Times New Roman", 16), bg="pink")
lbl4.place(x=440, y=330, height=40, width=150)
en3 = Entry(root)
en3.place(x=620, y=330, height=32, width=250)

# lbl5 = Label(root, text="Blood group:", font=("Times New Roman", 16), bg="pink")
# lbl5.place(x=460, y=390, height=40, width=140)
# en4 = Entry(root)
# en4.place(x=620, y=390, height=32, width=250)


lbl6 = Label(root, text="Email :", font=("Times New Roman", 16), bg="pink")
lbl6.place(x=500, y=450, height=40, width=100)
en5 = Entry(root)
en5.place(x=620, y=450, height=32, width=250)

lbl7 = Label(root, text="Password :", font=("Times New Roman", 16), bg="pink")
lbl7.place(x=500, y=510, height=40, width=100)
en6 = Entry(root, show="*")
en6.place(x=620, y=510, height=32, width=250)

lbl8 = Label(root, text="Weight(in kgs) :", font=("Times New Roman", 16), bg="pink")
lbl8.place(x=450, y=570, height=40, width=150)
en7 = Entry(root)
en7.place(x=620, y=570, height=32, width=250)

lbl9 = Label(root, text="Disease :", font=("Times New Roman", 16), bg="pink")
lbl9.place(x=470, y=630, height=40, width=150)
en8 = Entry(root)
en8.place(x=620, y=637, height=32, width=250)

options = StringVar()
options.set("blood groups")

en10 = StringVar()

def on_select(value):
    en10.set(value)

dropdown = OptionMenu(root, options, '(A+)', '(A-)', '(B+)', '(O+)', '(O-)', '(AB+)', '(AB-)', command=on_select)
dropdown.place(x=620, y=400, width=250)
selected_option = options.get()



b1 = Button(f, text="Sign up", font=("Times New Roman", 16), height=1, width=8,command=lambda: create_user(en1,en2,en3,en5,en6,en7,en8,en9,en10))
b1.place(x=660, y=700)

# b1 = Button(f, text="Back", font=("Times New Roman", 16), height=1, width=8)
# b1.place(x=430, y=640)

lb15 = Label(root, text="Blood Group:", font=("Times new Roman", 16), height=1, width=8, bg='pink')
lb15.place(x=460, y=390, height=40, width=150)







def show():
    print(options.get())


f.pack_propagate(0)
root.mainloop()