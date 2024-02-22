import datetime
from tkinter import *



from DatabaseHelper import *

class Dashboard():


    def get_data(self):
        query="Select * from blood_info where username=%s"
        parameters=self.username
        result=DatabaseHelper.get_data(query,parameters)
        self.result = result

    def goon_register(self,root):
        import register as r
        root.destroy()




    def update_labels(self, is_expired):
        result = self.result
        self.dash_name_from_db.configure(text=f"{result['FULLNAME']}")
        self.dash_phn_no_label_db.configure(text=f"{result['PHONE']}")
        if not is_expired:
            self.dash_bld_grp_label_db.configure(text=f"{result['BLOODGROUP']}")
            self.dash_gndr_label_db.configure(text=f"{result['GENDER']}")
            self.dash_wgt_label_db.configure(text=f"{result['WEIGHT']}")
            self.dash_age_label_db.configure(text=f"{result['AGE']}")
            self.dash_un_label_db.configure(text=f"{result['USERNAME']}")
            self.dash_dis_label_db.configure(text=f"{result['DISEASE']}")
            self.dash_exp_label_db.configure(text=f"{result['EXPIRY_DATE']}")


    def __init__(self,root,username):
        self.root=root
        self.root.geometry("1500x1000")
        self.root.configure(bg="pink")
        self.frame=Frame(self.root,width=1000,height=1000,bg="pink")
        self.frame.pack(side=TOP)
        self.username = username

        self.dash_name_label = Label(self.root, text="Name", width=15, height=1, font="Poppins 24 bold",bg="pink").place(x=0, y=120)
        self.dash_phn_no_label = Label(self.root, text="Phone no.", width=15, height=1, font="Poppins 24 bold",bg="pink").place(x=0, y=230)
        self.dash_name_from_db=Label(self.root, text = "Harsh",width=15,height=1,font="Courier 24 italic",bg="pink")
        self.dash_name_from_db.place(x = 270,y = 120)
        self.dash_phn_no_label_db=Label( self.root,text = "90222",width=15,height=1,font="Courier 24 italic",bg="pink")
        self.dash_phn_no_label_db.place(x = 270,y = 230)
        self.get_data()

        expiry_date= self.result['EXPIRY_DATE']
        today = datetime.datetime.today().date()

        lbl0 = Label(self.root, text="Dashboard", width=65, height=2, bg="brown", fg="white",
                     font=("Calibri", 35, "bold", "italic"), anchor=CENTER)
        lbl0.place(x=0, y=0)

        self.dash_session_exp = Label(self.root, text="Days left", width=15, height=1, font="Poppins 24 bold",
                                      bg="pink").place(x=940, y=240)


        if expiry_date>today:
            #other details
            self.dash_bld_grp_label = Label(self.root, text="Blood Group", width=15, height=1, font="Poppins 24 bold",
                                            bg="pink").place(x=0, y=170)

            self.dash_gndr_label = Label(self.root, text="Gender", width=15, height=1, font="Poppins 24 bold",
                                         bg="pink").place(x=0, y=290)
            self.dash_wgt_label = Label(self.root, text="Weight", width=15, height=1, font="Poppins 24 bold",
                                        bg="pink").place(x=0, y=350)
            self.dash_age_label = Label(self.root, text="Age", width=15, height=1, font="Poppins 24 bold",
                                        bg="pink").place(x=0, y=410)
            self.dash_un_label = Label(self.root, text="Username", width=15, height=1, font="Poppins 24 bold",
                                       bg="pink").place(x=0, y=470)
            self.dash_dis_label = Label(self.root, text="Disease", width=15, height=1, font="Poppins 24 bold",
                                        bg="pink").place(x=0, y=530)

            # DatabaseHelper.get_data()

            self.dash_bld_grp_label_db = Label(self.root, text="O+", width=15, height=1, font="Courier 24 italic",
                                               bg="pink")
            self.dash_bld_grp_label_db.place(x=270, y=170)
            self.dash_gndr_label_db = Label(self.root, text="Male", width=15, height=1, font="Courier 24 italic",
                                            bg="pink")
            self.dash_gndr_label_db.place(x=270, y=290)
            self.dash_wgt_label_db = Label(self.root, text="50", width=15, height=1, font="Courier 24 italic",
                                           bg="pink")
            self.dash_wgt_label_db.place(x=270, y=350)
            self.dash_age_label_db = Label(self.root, text="19", width=15, height=1, font="Courier 24 italic",
                                           bg="pink")
            self.dash_age_label_db.place(x=270, y=410)
            self.dash_un_label_db = Label(self.root, text="kavish", width=35, height=1, font="Courier 24 italic",
                                          bg="pink")
            self.dash_un_label_db.place(x=270, y=470)
            self.dash_dis_label_db = Label(self.root, text="Low haemoglobin", width=15, height=1,
                                           font="Courier 24 italic", bg="pink")
            self.dash_dis_label_db.place(x=270, y=530)
            self.update_labels(False)

            self.dash_prev_label = Label(self.root, text="Last Blood Donated ", width=20, height=1,
                                         font="Poppins 24 bold", bg="pink").place(x=600, y=240)


        else:
            #register button here
            self.btn = Button(self.root, text='Reregister', bg="orange", command=lambda:  self.goon_register(root)).place(x=950, y=310)
            self.update_labels(True)
            self.lblll=Label(self.root,text="Account Expired please Reregister!!!",bg="pink",fg="red")
            self.lblll.place(x=300,y=300)




        print(f"Username mila:{username}")

        # dash_title = Label( text = "Dashboard",width=20,height=1,font="Courier 30 bold",bg="pink").place(x = 500,y = 2)






        self.frame.pack_propagate(0)



if __name__ == '__main__':
    root = Tk()
    root.title("Dashboard")
    root.geometry("1500x1000")
    root.configure(bg="pink")
    k=Dashboard(root)
    root.iconbitmap("blood2.ico")
    root.mainloop()