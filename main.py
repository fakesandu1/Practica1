from PIL.ImageOps import expand

import database as db
import numpy as np
import customtkinter
from CTkTable import *
customtkinter.set_appearance_mode("dark")

class error_detection:
    noms=[]
    meas=[]
    plus_tols=[]
    minus_tols=[]
    dev=[]
    outtol=[]
    maindata=[]
    outside=[]
    def __init__(self):
        for i in range(len(db.data.sensory)):
            self.noms.append(db.data.sensory[i][3])
            self.plus_tols.append(db.data.sensory[i][4])
            self.minus_tols.append(db.data.sensory[i][5])
            self.meas.append(db.data.sensory[i][6])
            self.dev.append(db.data.sensory[i][7])
            self.outtol.append(db.data.sensory[i][8])
        self.noms=np.array(self.noms)
        self.plus_tols = np.array(self.plus_tols)
        self.minus_tols = np.array(self.minus_tols)
        self.meas = np.array(self.meas)
        self.dev = np.array(self.dev)
        self.outtol=np.array(self.outtol)
        self.maindata=np.array(self.maindata)
        self.outside=np.array([])
    def deviations(self):
        if len(self.outside)==0:
            self.outside=np.where(self.outtol != 0)
            maindata=[]
            for i in self.outside[0]:
                maindata.append(db.data.sensory[i])
            maindata=np.array(maindata)
            self.maindata=np.append(self.maindata,maindata)
            self.maindata=np.reshape(self.maindata,maindata.shape)


class Table_Frame(customtkinter.CTkScrollableFrame):
    def __init__(self,master,values,**kwargs):
        super().__init__(master,**kwargs)

        self.values = list(values)
        self.values.insert(0, ['id', 'fisier_id', 'cod', 'nom', '+tol', '-tol', 'meas', 'dev', 'outtol'])

        self.table = CTkTable(master=self, row=len(values), column=len(values[0]), values=self.values)
        self.table.pack(expand=True, fill="both")
    def Clear_table(self):
        value_index=[]
        for i in range(0,len(self.values[0])):
            value_index.append(i)
        print(value_index)
        self.table.delete_columns(value_index)
        self.table.add_row(['id', 'fisier_id', 'cod', 'nom', '+tol', '-tol', 'meas', 'dev', 'outtol'],0)





class EntryBox(customtkinter.CTkFrame):
    def __init__(self,values,master,**kwargs):
        super().__init__(master,**kwargs)
        self.values=values

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Search")
        self.entry.pack(expand=True, fill="both")

        self.button = customtkinter.CTkButton(self, text="Search", command=self.button_press)
        self.button.pack(expand=True,fill="both")

        self.label=customtkinter.CTkLabel(self, text="Search Result", fg_color="transparent")
        self.label.pack(expand=True,fill="both")

        self.search = ''

    def button_press(self):
        self.search = self.entry.get()
        print("the search is=", self.search)
        search = np.where(self.values == self.search)
        print(search)
        search_result=''
        if len(search[0]) == 0:
            self.label.configure(text="no search result")
            print("no results")
        else:
            for i in search[0]:
                search_result+="   ".join(self.values[i])+'\n'
                print(self.values[i])
            print(search_result)
            self.label.configure(text=search_result)


class App(customtkinter.CTk):
    def __init__(self,values):
        super().__init__()
        self.values=values

        self.grid_rowconfigure(0,weight=0)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.entry_frame= EntryBox(master=self,values=values)
        self.entry_frame.grid(row=0, column=0, padx=10, pady=30, sticky="ew")

        self.table_frame = Table_Frame(master=self,values=values,height=750)
        self.table_frame.grid(row=2, column=0, padx=10, pady=30, sticky="nsew")






if __name__=="__main__":
    erroare=error_detection()
    erroare.deviations()
    values=erroare.maindata


    app=App(values)
    app.mainloop()