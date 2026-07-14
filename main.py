from pandas.core.interchange import column

import database as db
import numpy as np
import customtkinter


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
        print(outside)
        for i in outside:
            #print(db.data.sensory[i])
            maindata.append(db.data.sensory[i])
        maindata=np.array(maindata)
        self.maindata=np.append(self.maindata,maindata)
        print(self.maindata)



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1080×768")


        self.textbox = customtkinter.CTkTextbox(master=self,width=1080,height=768,corner_radius=0)
        self.textbox.grid(row=0,column=0,sticky="nsew")
        self.textbox.insert("0.0","test")

        self.button=customtkinter.CTkButton(self,text="test",command=self.button_callback)
        self.button.grid(row=0,column=0,padx=5,pady=5)

    def button_callback(self):
        eroare = error_detection()
        eroare.deviations()

        for i in range(0,len(eroare.maindata)):
            self.textbox.insert("0.0","%s\n"%eroare.maindata)

if __name__=="__main__":

    app=App()
    app.mainloop()