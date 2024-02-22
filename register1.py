import datetime
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from DatabaseHelper import *

import re

class Register:
    def __init__(self,root):
        self.root=root
        self.f = Frame(self.root, height=1000, width=1000, bg="pink")
        self.f.pack(fill=X)
        self.f.pack_propagate(0)



        self.lbl0 = Label(self.root, text="Registration Form", font=("Calibri", 30, "bold", "italic"), bg="pink")
        self.lbl0.place(x=550, y=30)

        self.lbl1 = Label(self.root, text="Full Name :", font=("Times New Roman", 16), bg="pink")
        self.lbl1.place(x=500, y=150, height=40, width=100)
        self.en1 = Entry(root)
        self.en1.place(x=620, y=150, height=32, width=250)

        self.lbl2 = Label(self.root, text="Age :", font=("Times New Roman", 16), bg="pink")
        self.lbl2.place(x=500, y=210, height=40, width=100)
        self.en2 = Entry(root)
        self.en2.place(x=620, y=210, height=32, width=250)

        self.lbl3 = Label(self.root, text="Gender :", font=("Times New Roman", 16), bg="pink")
        self.lbl3.place(x=500, y=270, height=40, width=100)

        self.en9 = StringVar()
          # Set the default value to "Male"

        self.r1 = Radiobutton(self.root, text="Male", font=("Calibri", 16), bg="pink", variable=self.en9, value="Male")
        self.r1.place(x=620, y=275, height=29)

        self.r2 = Radiobutton(self.root, text="Female", font=("Calibri", 16), bg="pink", variable=self.en9, value="Female")
        self.r2.place(x=730, y=275, height=29)

        self.r3 = Radiobutton(self.root, text="Others", font=("Calibri", 16), bg="pink", variable=self.en9, value="Others")
        self.r3.place(x=860, y=275, height=29)

        self.lbl4 = Label(self.root, text="Contact Number :", font=("Times New Roman", 16), bg="pink")
        self.lbl4.place(x=440, y=330, height=40, width=150)
        self.en3 = Entry(self.root)
        self.en3.place(x=620, y=330, height=32, width=250)

        # lbl5 = Label(root, text="Blood group:", font=("Times New Roman", 16), bg="pink")
        # lbl5.place(x=460, y=390, height=40, width=140)
        # en4 = Entry(root)
        # en4.place(x=620, y=390, height=32, width=250)

        self.lbl6 = Label(self.root, text="Email :", font=("Times New Roman", 16), bg="pink")
        self.lbl6.place(x=500, y=450, height=40, width=100)
        self.en5 = Entry(self.root)
        self.en5.place(x=620, y=450, height=32, width=250)

        self.lbl7 = Label(self.root, text="Password :", font=("Times New Roman", 16), bg="pink")
        self.lbl7.place(x=500, y=510, height=40, width=100)
        self.en6 = Entry(self.root, show="*")
        self.en6.place(x=620, y=510, height=32, width=250)

        self.lbl8 = Label(self.root, text="Weight(in kgs) :", font=("Times New Roman", 16), bg="pink")
        self.lbl8.place(x=450, y=570, height=40, width=150)
        self.en7 = Entry(self.root)
        self.en7.place(x=620, y=570, height=32, width=250)

        self.lbl9 = Label(self.root, text="Disease :", font=("Times New Roman", 16), bg="pink")
        self.lbl9.place(x=470, y=630, height=40, width=150)
        self.en8 = Entry(root)
        self.en8.place(x=620, y=637, height=32, width=250)

        self.options = StringVar()
        self.options.set("blood groups")

        self.en10 = StringVar()
        self.options = ['(A+)', '(A-)', '(B+)', '(O+)', '(O-)', '(AB+)', '(AB-)']
        self.dropdown = OptionMenu(self.root, self.en10, *self.options, command=self.on_select)
        self.dropdown.place(x=620, y=400, width=250)
        # self.selected_option = self.options.get()

        self.b1 = Button(self.f, text="Sign up", font=("Times New Roman", 16), height=1, width=8,command=self.create_user)
        self.b1.place(x=660, y=700)

        # b1 = Button(f, text="Back", font=("Times New Roman", 16), height=1, width=8)
        # b1.place(x=430, y=640)

        self.lb15 = Label(self.root, text="Blood Group:", font=("Times new Roman", 16), height=1, width=8, bg='pink')
        self.lb15.place(x=460, y=390, height=40, width=150)
    # class Register:
    # def _init_(self):
    def goon_mail(self,email):
        self.user=email
        import mailllllling as m
        m.email(self.user)

    def is_valid_email(self,email):
        self.email1=email
        self.pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        print(re.fullmatch(self.pattern, self.email1))
        if re.fullmatch(self.pattern, self.email1):
            print("Valid")
            messagebox.showinfo("message", "valid email")
        else:
            messagebox.showinfo("message", "Enter valid email")
            print("INValid")

    def create_user(self):
        self.user = self.en5.get()
        print(self.user)
        self.name = self.en1.get()
        self.age = self.en2.get()
        self.phone_no = self.en3.get()
        self.weight = self.en7.get()
        self.pwd = self.en6.get()
        self.disease = self.en8.get()
        self.gender = self.en9.get()
        self.bloodgroup = self.en10.get()
        print(self.gender)

        self.today = datetime.datetime.today().date()
        self.expiry_date = self.today + datetime.timedelta(days=2)
        params = (self.name, self.age, self.phone_no, self.user, self.pwd, self.weight, self.disease, self.gender, self.bloodgroup, self.expiry_date)

        query = "Insert into blood_info(FULLNAME,AGE,PHONE,USERNAME,PWD,WEIGHT,DISEASE,GENDER,BLOODGROUP,EXPIRY_DATE) Values(%s,%s,%s,%s,SHA(%s),%s,%s,%s,%s,%s)"
        DatabaseHelper.execute_query(query, params)
        messagebox.showinfo('Success!', f'User with username {self.user} created successfully. Please login again.')

        self.is_valid_email(self.user)
        self.goon_mail(self.user)
        self.root.destroy()

    def on_select(self, value):
        self.en10.set(value)



    def show(self):
        print(self.options.get())

if __name__=="__main__":
    root = Tk()
    root.title("Blood donor system")
    root.iconbitmap(bitmap="bloodlol.icns")
    root.geometry('1000x1000')
    h=Register(root)
    root.mainloop()
