import database as db
import numpy as np


class error_detection:
    noms=[]
    meas=[]
    plus_tols=[]
    minus_tols=[]
    dev=[]
    outtol=[]
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
    def deviations(self):
        outside=np.where(self.outtol != 0)
        outside=np.append(outside,outside)
        print(outside)
        for i in outside:
            print(db.data.sensory[i])





eroare=error_detection()
eroare.deviations()