import mysql.connector
import log_in as log
import csv


cnx=mysql.connector.connect(user=log.user,password=log.password,
                            host="127.0.0.1",database="Practica")
cursor=cnx.cursor()

class database:
    piese=[]
    sensory=[]
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
        self.cod=[]
        self.nominal=[]
        self.plustol = []
        self.minustol = []
        self.meas = []
        self.dev = []
        self.outtol = []
    def input_p(self):
        query= "select id_fisier,nume_fisier from piesa"
        cursor.execute(query)
        for(id_fisier,nume_fisier) in cursor:
            self.piese.append([id_fisier,nume_fisier])
    def input_s(self):
        query="select id,id_fisier,cod,nom,plus_tol,minus_tol,meas,dev,outtol from sensory"
        cursor.execute(query)
        for( id,id_fisier,cod,nom,plus_tol,minus_tol,meas,dev,outtol) in cursor:
            self.sensory.append([id,id_fisier,cod,nom,plus_tol,minus_tol,meas,dev,outtol])
    def reading(self):
        with open("rezultate_metrologie_sigur.csv", "r") as f:
            data = csv.reader(f)
            for row in data:
                self.fisier.append(row[0])
                self.cod.append(row[2])
                self.nominal.append(row[4])
                self.plustol.append(row[5])
                self.minustol.append(row[6])
                self.meas.append(row[7])
                self.dev.append(row[8])
                self.outtol.append(row[9])
    def db_insert(self):
        query = "insert into piesa(nume_fisier) value(%s)"
        set_fisiere = set(self.fisier)
        set_fisiere.remove("﻿Fisier")
        fisiere = list(set_fisiere)
        for i in range(1,len(fisiere)-1):
            cursor.execute(query,(fisiere[i],))
            cnx.commit()
        query="insert into sensory(id_fisier,cod,nom,plus_tol,minus_tol,meas,dev,outtol) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        id=0
        for i in range(1,len(self.meas)-1):
            query1="select distinct id_fisier from piesa where nume_fisier=%s"
            cursor.execute(query1,(self.fisier[i],))
            for(id_fisier) in cursor:
                id=id_fisier
                id=id[0]
            print(f"Values being inserted: id={id}, cod={self.cod[i]}, nominal={self.nominal[i]}, plustol={self.plustol[i]}, minustol={self.minustol[i]}, meas={self.meas[i]}, dev={self.dev[i]}, outtol={self.outtol[i]}")
            print(f"Types: {type(self.minustol[i])}")
            cursor.execute(query,(id,self.cod[i],self.nominal[i],self.plustol[i],self.minustol[i],self.meas[i],self.dev[i],self.outtol[i]))
        cnx.commit()


data=database() # scoate datele din baza de date

logdata=database() # va citi si stoca fisierul csv
logdata.reading()


data.input_s()
data.input_p()

cursor.close()
cnx.close()