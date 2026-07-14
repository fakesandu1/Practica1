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



class App(customtkinter.CTk):
    def __init__(self):
        eroare = error_detection()
        eroare.deviations()
        values=list(eroare.maindata)
        values.insert(0,['id','fisier_id','cod','nom','+tol','-tol','meas','dev','outtol'])
        print(values)

        super().__init__()
        self.geometry("1080×768")

        self.table=CTkTable(master=self,row=len(eroare.maindata),column=len(eroare.maindata[0]),values=values)
        self.table.pack(expand=False, fill="both")



if __name__=="__main__":

    app=App()
    app.mainloop()