from traits.trait_types import true

import database as db
import numpy as np
import customtkinter
from CTkTable import *


class error_detection:
    noms=[]
    meas=[]
    plus_tols=[]
    minus_tols=[]
    dev=[]
    outtol=[]
    maindata=[]
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
    def deviations(self):
        outside=np.where(self.outtol != 0)
        outside=np.append(outside,outside)
        maindata=[]
        for i in outside:
            maindata.append(db.data.sensory[i])
        maindata=np.array(maindata)
        self.maindata=np.append(self.maindata,maindata)
        self.maindata=np.reshape(self.maindata,maindata.shape)



class MyFrame(customtkinter.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        eroare = error_detection()
        eroare.deviations()
        values = list(eroare.maindata)
        values.insert(0, ['id', 'fisier_id', 'cod', 'nom', '+tol', '-tol', 'meas', 'dev', 'outtol'])
        print(values)


        self.table = CTkTable(master=self, row=len(eroare.maindata), column=len(eroare.maindata[0]), values=values)
        self.table.pack(expand=False, fill="both")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1080×768")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


if __name__=="__main__":

    app=App()
    app.mainloop()