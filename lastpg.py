from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Blood donor system")
root.geometry('1000x1000')

f = Frame(root, height=1000, width=1000, bg="pink")
f.pack(fill=X)

lbl0 = Label(root, text="Donor Details",width=75,height=2 ,bg="red" , borderwidth=3 , font=("Calibri", 30, "bold", "italic"))
lbl0.place(x=0, y=0)

lbl1 = Label(root, text="Full Name :", font=("Times New Roman", 16), bg="pink")
lbl1.place(x=75, y=150, height=40, width=100)
en1 = Entry(root)
en1.place(x=200, y=150, height=32, width=250)

lbl2 = Label(root, text="Age :", font=("Times New Roman", 16), bg="pink")
lbl2.place(x=98, y=210, height=40, width=100)
en2 = Entry(root)
en2.place(x=200, y=210, height=32, width=250)

lbl3 = Label(root, text="Gender :", font=("Times New Roman", 16), bg="pink")
lbl3.place(x=80, y=270, height=40, width=100)
# r1 = Radiobutton(root, text="Male", font=("Calibri", 16), bg="pink", variable=vars, value=1)
# r1.place(x=620, y=275, height=29)
# r2 = Radiobutton(root, text="Female", font=("Calibri", 16), bg="pink", variable=vars, value=2)
# r2.place(x=730, y=275, height=29)
# r3 = Radiobutton(root, text="Others", font=("Calibri", 16), bg="pink", variable=vars, value=3)
# r3.place(x=860, y=275, height=29)
en96 = Entry(root)
en96.place(x=200, y=275, height=32, width=250)

lbl4 = Label(root, text="Contact Number :", font=("Times New Roman", 16), bg="pink")
lbl4.place(x=20, y=330, height=40, width=150)
en3 = Entry(root)
en3.place(x=200, y=330, height=32, width=250)

# lbl5 = Label(root, text="Blood group:", font=("Times New Roman", 16), bg="pink")
# lbl5.place(x=460, y=390, height=40, width=140)
# en4 = Entry(root)
# en4.place(x=620, y=390, height=32, width=250)


lbl6 = Label(root, text="Username :", font=("Times New Roman", 16), bg="pink")
lbl6.place(x=70, y=450, height=40, width=100)
en5 = Entry(root)
en5.place(x=200, y=450, height=32, width=250)

lbl7 = Label(root, text="Password :", font=("Times New Roman", 16), bg="pink")
lbl7.place(x=70, y=510, height=40, width=100)
en6 = Entry(root, show="*")
en6.place(x=200, y=510, height=32, width=250)

lbl8 = Label(root, text="Weight(in kgs) :", font=("Times New Roman", 16), bg="pink")
lbl8.place(x=20, y=570, height=40, width=150)
en7 = Entry(root)
en7.place(x=200, y=570, height=32, width=250)

lbl9 = Label(root, text="Disease :", font=("Times New Roman", 16), bg="pink")
lbl9.place(x=50, y=630, height=40, width=150)
en8 = Entry(root)
en8.place(x=200, y=637, height=32, width=250)

# b1 = Button(f, text="Sign up", font=("Times New Roman", 16), height=1, width=8)
# b1.place(x=660, y=700)

# b1 = Button(f, text="Back", font=("Times New Roman", 16), height=1, width=8)
# b1.place(x=430, y=640)

lb15 = Label(root, text="Blood Group:", font=("Times new Roman", 16), height=1, width=8, bg='pink')
lb15.place(x=36, y=390, height=40, width=150)

options = StringVar()
options.set("blood groups")
dropdown = OptionMenu(root, options, '(A+)', '(A-)', '(B+)', '(O+)', '(O-)', '(AB+)', '(AB-)').place_configure(
    width=250, x=200, y=400)


lbl_image = Label(root)
raw_login_image = Image.open("blood_view.jpg")
raw_login_image = raw_login_image.resize((800, 600))
login_img = ImageTk.PhotoImage(raw_login_image)
login_label = Label(root, image=login_img)
        # self.login_label.image = self.login_img
login_label.place(x=600, y=150, height=600, width=800)



def show():
    print(options.get())


f.pack_propagate(0)

root.iconbitmap("bloodlol.icns")
root.mainloop()