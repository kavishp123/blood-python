from tkinter import *
from DatabaseHelper import *
from tkinter import messagebox
from PIL import Image, ImageTk



class HomePage:
    def __init__(self, root):
        self.root = root  # we need to pass a single root in every file, hence put this here
        self.root.geometry("1500x1000")
        self.frame = Frame(self.root, height=400, width=700, bg="white")
        self.frame.pack(fill=BOTH, expand="yes")
        self.setup_homepage()

    def goon_register(self):
        self.frame.destroy()
        import register1
        register1.Register(self.root)


    def goon_dash(self,username):
        self.s=username
        self.frame.destroy()
        self.body_frame.destroy()
        self.temp_frame.destroy()
        self.temp_root.destroy()
        self.header_frame.destroy()
        self.f.destroy()
        import Dashboard
        Dashboard.Dashboard(root,username)

        print("self",self.s)

    def goon_viewtb(self):
        import Bloodtable as v
    def login(self, login_type):
        self.temp_root = Toplevel()  # creates a new window.. NOT ROOT
        self.temp_root.title(f"{login_type} login")
        self.temp_frame = Frame(self.temp_root, height=300, width=500, bg="white")
        self.temp_frame.pack()
        self.lab = Label(self.temp_frame, width=50, text="Enter below details to login")
        self.lab.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
        self.l1 = Label(self.temp_frame, width=20, text="Enter username: ")
        self.e_username = Entry(self.temp_frame, width=30, fg='black', bg='white')
        self.e_username.focus_set()
        self.e_pwd = Entry(self.temp_frame, width=30, fg='black', bg='white', show='*')
        self.l2 = Label(self.temp_frame, width=20, text="Enter password: ")
        self.l1.grid(row=1, column=1, padx=10, pady=10)
        self.l2.grid(row=2, column=1, padx=10, pady=10)
        self.e_username.grid(row=1, column=2, padx=10, pady=10)
        self.e_pwd.grid(row=2, column=2, padx=10, pady=10)
        self.b1 = Button(self.temp_frame, text="Submit", height=2, width=10,command=self.authenticate)
        self.b1.grid(row=3, column=1, padx=10, sticky='e')
        self.b2 = Button(self.temp_frame, text="Reset", height=2, width=10, command=self.reset)
        self.b2.grid(row=3, column=2, padx=10, sticky='w')
        self.b3=Button(self.temp_frame, text="Register",height=2,width=10,command=self.goon_register)
        self.b3.grid(row=4, column=1, padx=10, sticky='e')
        self.temp_frame.grid_propagate(0)

    def authenticate(self):
        self.user = self.e_username.get()
        pwd = self.e_pwd.get()


        query = "Select Username,Pwd from blood_info where username= %s and pwd=SHA(%s)"
        params = (self.user, pwd)
        result = DatabaseHelper.get_data(query, params)
        if (result is None):
            messagebox.showerror("Login Failed", "Incorrect credentials")
            self.root.destroy()
        else:
            messagebox.showinfo('Login Success', "Login successfuly completed")

            self.goon_dash(self.user)
            print(self.user)
            # self.temp_frame.destroy()
            # self.root.destroy()

    def reset(self):
        self.e_username.delete(0,END)
        self.e_pwd.delete(END)
        self.e_username.focus_set()

    def create_user(self):
        user = self.e_username.get()
        pwd = self.e_pwd.get()
        re_pwd = self.e_re_pwd.get()
        if (pwd != re_pwd):
            messagebox.showerror("Mismatch", "Passwords don't match. Please re-enter")
        else:
            params = (user, pwd)
            query = "Insert into practice_user(Username,Password) Values(%s,SHA(%s))"
            DatabaseHelper.execute_query(query, params)
            messagebox.showinfo('Success!', f'User with username {user} created successfully. Please login again.')
            self.body_frame.destroy()
            self.header_frame.destroy()
            self.setup_homepage()



    def setup_homepage(self):

        self.add_header_section()

        self.body_frame = Frame(self.frame, bg="white", height=250, width=600)
        self.body_frame.pack(side=TOP, fill=X)
        self.body_frame.pack_propagate(0)

        self.lbFrame = LabelFrame(self.body_frame, width=900,  height=1000, font=('Times bold', 18),
                              bg="white", borderwidth=3)
        self.lbFrame.pack(anchor=CENTER, pady=20)
        self.admin_login_b = Button(self.lbFrame, text="view table page", command= self.goon_viewtb, font=('Times New Roman', 25))
        self.admin_login_b.grid(row=0, column=0, padx=90, pady=65)
        self.user_login_b = Button(self.lbFrame, text="User login", command=lambda: self.login("user"), font=('Times New Roman', 25))
        self.user_login_b.grid(row=0, column=1, padx=130, pady=65)

        self.lbFrame.grid_propagate(0)


        self.f = Frame(self.root, height=1000, width=1000)
        # f.pack(fill=X)
        # f.pack(fill=BOTH, expand="yes")
        self.imagee = Image.open("bloodpipe.jpg").resize((1550,300))
        self.imagee_tk = ImageTk.PhotoImage(self.imagee)
        self.lbl = Label(self.frame,image=self.imagee_tk)
        self.lbl.pack(fill=X)
        self.frame.pack_propagate(0)
    def add_header_section(self):

        self.header_frame = Frame(self.frame, height=150, width=600,bg="red")
        self.header_frame.pack(fill=X, side=TOP)
        self.header_frame.grid_propagate(0)

        self.raw_login_image = Image.open("blooddon.jpg")
        self.raw_login_image = self.raw_login_image.resize((100, 100))
        self.login_img = ImageTk.PhotoImage(self.raw_login_image)
        self.login_label = Label(self.header_frame, image=self.login_img)
        # self.login_label.image = self.login_img
        self.login_label.grid(row=0, column=0, padx=20, pady=20)

        self.welcome_label = Label(self.header_frame, text="         Welcome to Blood Donation Application", font=("Times bold", 45),bg="red")
        self.welcome_label.grid(row=0, column=1)

    def user_page(self, username):
        self.lbFrame.destroy()
        self.l_account = Label(self.body_frame, text=f"USER ACCOUNT")
        self.l_account.grid(row=0, column=0, pady=10)
        self.l_name = Label(self.body_frame, text=f"WELCOME, {username}")
        self.l_name.grid(row=1, column=0, pady=10)

    def admin_page(self, username):
        self.lbFrame.destroy()
        self.l_account = Label(self.body_frame, text=f"ADMIN ACCOUNT")
        self.l_account.grid(row=0, column=0, pady=10)
        self.l_name = Label(self.body_frame, text=f"WELCOME, {username}")
        self.l_name.grid(row=0, column=1, pady=10)
        self.lab = Label(self.body_frame, width=50, text="Enter below details to create a new user account")
        self.lab.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        self.l1 = Label(self.body_frame, width=20, text="Enter username: ")
        self.e_username = Entry(self.body_frame, width=30, fg='black', bg='white')
        self.e_username.focus_set()
        self.e_pwd = Entry(self.body_frame, width=30, fg='black', bg='white', show='*')
        self.show_pwd = IntVar()
        self.show_pwd_check = Checkbutton(self.body_frame, text="Show", bg="white", command=self.show_hide_pwd,
                                          variable=self.show_pwd)
        self.l2 = Label(self.body_frame, width=20, text="Enter password: ")
        self.e_re_pwd = Entry(self.body_frame, width=30, fg='black', bg='white', show='*')
        self.l3 = Label(self.body_frame, width=20, text="Re-enter password: ")

        self.l1.grid(row=2, column=1, padx=10, pady=10)
        self.l2.grid(row=3, column=1, padx=10, pady=10)
        self.l3.grid(row=4, column=1, padx=10, pady=10)
        self.e_username.grid(row=2, column=2, padx=10, pady=10)
        self.e_pwd.grid(row=3, column=2, padx=10, pady=10)
        self.show_pwd_check.grid(row=3, column=3, padx=2, pady=10)

        self.e_re_pwd.grid(row=4, column=2, padx=10, pady=10)
        self.b1 = Button(self.body_frame, text="Create user", height=2, width=10, command=lambda: self.create_user())
        self.b1.grid(row=5, column=1, columnspan=2, padx=10)

    def show_hide_pwd(self):
        if self.show_pwd.get() == 1:
            self.e_pwd.config(show="")
        else:
            self.e_pwd.config(show="*")



root = Tk()
root.title("Login")
h = HomePage(root)
# root.geometry('400x400')
root.mainloop()
