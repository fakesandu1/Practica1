Rolul principal al apicatiei este de a citi un set de CSV-uri si de a:
1. Le introduce pe acestea intr-o baza de date,
2. care mai apoi sunt extrase si puse intr-un GUI unde se poate face un search pe detalile dorite

pt mai mute detali/modificari vizitati:https://github.com/fakesandu1/Practica1

Introducerea ori citirea din baza de Date:
Baza de date este una de Mysql sub forma

create table if not exists piesa(
    id_fisier int primary key auto_increment,
    nume_fisier varchar(1000)
    PartName varchar(1000)
);


create table if not exists sensory(
    id int primary key auto_increment,
    id_fisier int,
    cod varchar(50),
    nom float,
    plus_tol float,
    minus_tol float,
    meas float,
    dev float,
    outtol float,
    foreign key (id_fisier) references piesa(id_fisier)
);


Citirea si introducere sunt realizate de database.py in particular de clasa database.
Citirea datelor care trebuiesc introduse in baza de datelor sunt realizate de functia reading() care citeste CSV-uri sub forma:
PartName/Fisier/Caracteristica/Cod/Axa/NOMINAL/+TOL/-TOL/MEAS/DEV/OUTTOL

Functia pt introducere in baza de date este db_insert() iar cele de input_s() si input_p() scot datele din baza.

Partea GUI (facuta cu ajutorul librarie customtkinter) cat si filtrarea datelor care sunt in afara outtol este realizata de main.py.
De mentionat ca functia de search poate filtra rezultatele numai de pe o singura coloana.
