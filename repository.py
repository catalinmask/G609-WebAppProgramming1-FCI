import sqlite3
from sqlite3.dbapi2 import Cursor
import datetime
database="BazaProiect.db"
# in query salvez instructiunile

def connect(dbfile):# Conectez baza de date
    conn=sqlite3.connect(dbfile) 
    return conn

def create_cursor(conn): # creez cursor pentru baza de date // cursorul se plimba prin baza de date
    cursor=conn.cursor()
    return cursor

def get_users(conn):
    query="select * from users" # *-inseamna "tot" || selecteaza-mi tot din tabelul users
    cursor=conn.cursor()
    data=list(cursor.execute(query)) # cursorul o sa se duca in query, ia tot si baga intr-o lista
    return data # o lista cu toti userii (cu toate datele din tabel)

def get_user_by_username(conn, username):
    query=f"select username, password from DateUtilizatori where username = '{username}' "
    cursor=conn.cursor()
    results=list(cursor.execute(query))
    return results[0] 

def create_user(conn, body):
    query="""insert into DateUtilizatori (email, username, password, marca_masina, km_masina, km_schimb) values (?,?,?,?,?,?)"""
    userData=[
        body.get("email"),
        body.get("username"),
        body.get("Password"),
        body.get("marca_masina"),
        body.get("km_masina"),
        body.get("km_schimb")
    ]
    cursor=conn.cursor()
    cursor.execute(query,userData) #cursorul executa query ul de pe linia 28 cu datele de pe linia 29, inlocurieste ????
    conn.commit() # commit salveaza modificarile

 
def delete_user(conn, username):
    query=f"delete from users where username = '{username}'"
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()

def get_user_password(conn, email):
    query = f"select password from users where email='{email}'"
    cursor = conn.cursor()
    password = list(cursor.execute(query)) # baga in lista toate parolele din db care se potrivesc cu email uk
    if password:
        return password[0][0] #returneaza indicele cu primul rezultat din query
    else:
        return None

def edit_user(conn, username, details):
    set_statement=""
    for key, value in details.items():
        if type(value) == str:
            set_statement += f"{key}='{value}'," # Key este partea pana in ":" si value valoarea de dupa ":"
        else:
            set_statement += f"{key}={value},"
    if len(set_statement) > 1:
        set_statement=set_statement[:-1]
    query=f"update users set {set_statement} where username='{username}'"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

def main():
    database=r"/Users/catalinflorea/Desktop/Programare web 1/PYTHON/Edit DB/users.db"
    conn=connect(database)
    timpCurent=datetime.datetime.now()
    uname="eu"
    modificari={
        "email":"catalinmask@yahoo.com",
        "last_updated_at":str(timpCurent)
    }
    with conn:
        edit_user(conn, "catalinmask", modificari)

if __name__ == '__main__':
    main()