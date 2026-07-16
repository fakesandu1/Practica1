import mysql.connector
import log_in as log
import pandas as pd
import glob

cnx=mysql.connector.connect(user=log.user,password=log.password,
                            host="127.0.0.1",database="Practica")
cursor=cnx.cursor()

class database:
    piese=[]
    sensory=[]
    PartName=[]
    fisier=[]
    cod=[]
    nominal=[]
    plustol=[]
    minustol=[]
    meas=[]
    dev=[]
    outtol=[]
    def __init__(self):
        self.piese=[]
        self.instrument=[]
        self.sensory=[]
        self.fisier = []
        self.PartName=[]
        self.cod=[]
        self.nominal=[]
        self.plustol = []
        self.minustol = []
        self.meas = []
        self.dev = []
        self.outtol = []
    def input_p(self):
        query= "select id_fisier,nume_fisier,PartName from piesa"
        cursor.execute(query)
        for(id_fisier,nume_fisier,PartName) in cursor:
            self.piese.append([id_fisier,nume_fisier,PartName])
    def input_s(self):
        query="select id,nume_fisier,cod,nom,plus_tol,minus_tol,meas,dev,outtol from sensory join piesa on sensory.id_fisier=piesa.id_fisier;"
        cursor.execute(query)
        for( id,nume_fisier,cod,nom,plus_tol,minus_tol,meas,dev,outtol) in cursor:
            self.sensory.append([id,nume_fisier,cod,nom,plus_tol,minus_tol,meas,dev,outtol])
    def reading(self):
        path="CSV/"
        all_files=glob.glob(path+"*.csv")
        sensory=[]
        for filename in all_files:
            df=pd.read_csv(filename,index_col=None,header=0)
            sensory.append(df)
        df=pd.concat(sensory,axis=0,ignore_index=True)
        df=df.values.tolist()

        for i in range(0,len(df)):
            self.PartName.append(df[i][0])
            self.fisier.append(df[i][1])
            self.cod.append(df[i][3])
            self.nominal.append(df[i][5])
            self.plustol.append(df[i][6])
            self.minustol.append(df[i][7])
            self.meas.append(df[i][8])
            self.dev.append(df[i][9])
            self.outtol.append(df[i][10])
        for i in range(0,len(self.cod)):
            if pd.isna(self.cod[i]):
                self.cod[i]='nimic'
            if pd.isna(self.PartName[i]):
                self.PartName[i]='nimic'
    def db_insert(self):
        query = "insert into piesa(nume_fisier,PartName) value(%s,%s)"
        set_fisiere = set(self.fisier)
        fisiere = list(set_fisiere)
        for i in range(1,len(fisiere)-1):
            cursor.execute(query,(fisiere[i],self.PartName[i]))
            cnx.commit()
        query="insert into sensory(id_fisier,cod,nom,plus_tol,minus_tol,meas,dev,outtol) values (%s,%s,%s,%s,%s,%s,%s,%s)"

        id=0
        for i in range(1,len(self.meas)):
            query1="select distinct id_fisier from piesa where nume_fisier=%s"
            cursor.execute(query1,(self.fisier[i],))
            for(id_fisier) in cursor:
                id=id_fisier
                id=id[0]
            print(f"Values being inserted: id={id}, cod={self.cod[i]}, nominal={self.nominal[i]}, plustol={self.plustol[i]}, minustol={self.minustol[i]}, meas={self.meas[i]}, dev={self.dev[i]}, outtol={self.outtol[i]}")
            print(f"Types: {type(self.nominal[i])}")
            cursor.execute(query,(id,self.cod[i],self.nominal[i],self.plustol[i],self.minustol[i],self.meas[i],self.dev[i],self.outtol[i]))
        cnx.commit()


data=database() # scoate datele din baza de date

logdata=database() # va citi si stoca fisierul csv
logdata.reading()
#logdata.db_insert() #inserarea in baza de date

data.input_s()
data.input_p()

cursor.close()
cnx.close()