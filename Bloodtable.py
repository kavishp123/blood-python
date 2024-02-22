from DatabaseHelper import *
from tkinter import *
from Components.table import *

root=Tk()
class Bloodtable:
    def __init__(self,root):
        self.frame=Frame(root,width=2000,height=1000,bg="lightpink")
        self.frame.pack(expand=1, fill=BOTH)

        lbl = Label(self.frame, text="List of Donors", bg="red", font=("Calibri", 30, "bold", "italic"))
        lbl.pack(side=TOP,fill=BOTH)
        self.frame.pack_propagate(0)
        self.printtable()

    def printtable(self):
        query = "select DONOR_ID,FULLNAME,AGE,GENDER,PHONE,BLOODGROUP,WEIGHT,DISEASE,EXPIRY_DATE from blood_info"
        result = DatabaseHelper.get_all_data(query)

        self.viewpr_table = SimpleTable(self.frame, rows=len(result), columns=len(result[0]), width=2000,height=1200)
        self.viewpr_table.place(x=0, y=60)
        for r in range(len(result)):
            for c in range(len(result[0])):
                self.viewpr_table.set(row=r, column=c, value=result[r][c])


m=Bloodtable(root)
root.mainloop()
