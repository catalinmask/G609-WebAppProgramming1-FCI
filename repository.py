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
    query="select * from DateUtilizatori" # *-inseamna "tot" || selecteaza-mi tot din tabelul users
    cursor=conn.cursor()
    data=list(cursor.execute(query)) # cursorul o sa se duca in query, ia tot si baga intr-o lista
    return data # o lista cu toti userii (cu toate datele din tabel)

def get_user_by_username(conn, username):
    query=f"select username, password from DateUtilizatori where username = '{username}' "
    cursor=conn.cursor()
    results=list(cursor.execute(query))
    return results[0] 

def get_user_data_by_username(conn, username):
    query=f"select email, username, marca_masina, km_masina, km_schimb from DateUtilizatori where username='{username}' "
    cursor=conn.cursor()
    dateUtilizatori=list(cursor.execute(query))
    if len(dateUtilizatori)==0:
        return {}

    dateUtilizatori=dateUtilizatori[0]
    date={
        "email": dateUtilizatori[0],
        "username": dateUtilizatori[1],
        "marca_masina": dateUtilizatori[2],
        "km_masina": dateUtilizatori[3],
        "km_schimb": dateUtilizatori[4]
    }
    return date
    

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
    if userData[0]=='' or userData[1]=='' or userData[2]=='' or userData[3]=='' or userData[4]=='' or userData[5]=='':
        raise Exception("Missing user information")
        
    cursor=conn.cursor()
    cursor.execute(query,userData) #cursorul executa query ul de pe linia 28 cu datele de pe linia 29, inlocurieste ????
    conn.commit() # commit salveaza modificarile

 
def delete_user(conn, username):
    query=f"delete from DateUtilizatori where username = '{username}'"
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()

def get_user_password(conn, username):
    query = f"select password from DateUtilizatori where username='{username}'"
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
    query=f"update DateUtilizatori  set {set_statement} where username='{username}'"
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