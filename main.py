import database as db
import numpy as np


class error_detection:
    noms=[]
    meas=[]
    plus_tols=[]
    minus_tols=[]
    dev=[]
    def __init__(self):
        for i in range(len(db.data.sensory)):
            self.noms.append(db.data.sensory[i][3])
            self.plus_tols.append(db.data.sensory[i][4])
            self.minus_tols.append(db.data.sensory[i][5])
            self.meas.append(db.data.sensory[i][6])
            self.dev.append(db.data.sensory[i][7])
        self.noms=np.array(self.noms)
        self.plus_tols = np.array(self.plus_tols)
        self.minus_tols = np.array(self.minus_tols)
        self.meas = np.array(self.meas)
        self.dev = np.array(self.dev)
    def deviations(self):
        negative_idx =np.where(self.dev<0)
        positive_idx = np.where(self.dev > 0)
        outside = np.append(np.where(np.abs(self.dev[negative_idx]) >= self.minus_tols[negative_idx]),
                            np.where(self.dev[positive_idx] >= self.plus_tols[positive_idx]))
        print(outside)
        for i in outside:
            print(db.data.sensory[i])


test=error_detection()
test.deviations()