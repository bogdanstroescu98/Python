import mysql.connector as mysql
from tkinter import *
import tkinter.messagebox as MessageBox

def insert():
    id = e_id.get()
    titlu = e_titlu.get()
    nota = e_nota.get("1.0","end-1c")

    if(id == "" or titlu == "" or nota == ""):
        MessageBox.showinfo("Insert Status","Toate campurile trebuie completate")
    else:
        try:
            db = mysql.connect(
                host='localhost',
                user='bogdan',
                password='mypassword',
                database='proiect',
                auth_plugin='mysql_native_password'
            )
            cursor = db.cursor()
            cursor.execute("INSERT INTO note VALUES('"+id+"','"+titlu+"','"+nota+"')")
            cursor.execute("commit")

            e_id.delete(0, "end")
            e_titlu.delete(0, "end")
            e_nota.delete("1.0","end-1c")
            show()
            MessageBox.showinfo("Insert Status","Nota adaugata cu succes")
            db.close()
        except:
            MessageBox.showinfo("Insert Status","ID-ul exista deja in baza de date")

def delete():
    if(e_id.get() == ""):
        MessageBox.showinfo("Delete Status","ID-ul introdus nu exista in baza de date")
    else:
        db = mysql.connect(
            host='localhost',
            user='bogdan',
            password='mypassword',
            database='proiect',
            auth_plugin='mysql_native_password'
        )
        cursor = db.cursor()
        cursor.execute("DELETE FROM note WHERE ID='"+e_id.get()+"'")
        cursor.execute("commit")
        e_id.delete(0, "end")
        e_titlu.delete(0, "end")
        e_nota.delete("1.0", "end-1c")
        show()
        MessageBox.showinfo("Delete Status", "Nota a fost stearsa cu succes")
        db.close()

def update():
    id = e_id.get()
    titlu = e_titlu.get()
    nota = e_nota.get("1.0", "end-1c")
    if (id == "" or titlu == "" or nota == ""):
        MessageBox.showinfo("Update Status","Trebuie completate toate campurile")
    else:
        db = mysql.connect(
            host='localhost',
            user='bogdan',
            password='mypassword',
            database='proiect',
            auth_plugin='mysql_native_password'
        )
        cursor = db.cursor()
        cursor.execute("UPDATE note SET TITLU='"+titlu+"',NOTA='"+nota+"' WHERE ID='"+id+"'")
        cursor.execute("commit")
        e_id.delete(0, "end")
        e_titlu.delete(0, "end")
        e_nota.delete("1.0", "end-1c")
        show()
        MessageBox.showinfo("Update Status", "Nota a fost modificata cu succes")
        db.close()

def get():
    if (e_id.get() == ""):
        MessageBox.showinfo("Get Status", "ID-ul introdus nu exista in baza de date")
    else:
        db = mysql.connect(
            host='localhost',
            user='bogdan',
            password='mypassword',
            database='proiect',
            auth_plugin='mysql_native_password'
        )
        cursor = db.cursor()
        e_titlu.delete(0, "end")
        e_nota.delete("1.0", "end-1c")
        cursor.execute("SELECT * FROM note WHERE ID='" + e_id.get() + "'")
        rows = cursor.fetchall()
        for row in rows:
            e_titlu.insert(0, row[1])
            e_nota.insert('1.0',row[2])
        show()
        db.close()

def show():
    db = mysql.connect(
        host='localhost',
        user='bogdan',
        password='mypassword',
        database='proiect',
        auth_plugin='mysql_native_password'
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM note")
    rows = cursor.fetchall()
    list.delete(0, list.size())

    for row in rows:
        inserData = str(row[0])+'    '+row[1]+'     '+row[2]
        list.insert(list.size()+1, inserData)
    db.close()

root = Tk()
root.geometry("1000x1000")
root.title("NotesApp")

id = Label(root, text='Introduceti un ID:', font=('bold',10))
id.place(x=20,y=30)

titlu = Label(root, text='Introduceti un titlu:', font=('bold',10))
titlu.place(x=20,y=60)

nota = Label(root, text='Introduceti nota:', font=('bold',10))
nota.place(x=20,y=90)

e_id = Entry()
e_id.place(x=150, y=30)

e_titlu = Entry()
e_titlu.place(x=150, y=60)

e_nota = Text(root,height=20,width=20)
e_nota.pack()
e_nota.place(x=150, y=90)

insert = Button(root, text="Adaugati", font=("bold",15), bg="yellow", command=insert)
insert.place(x=20, y=550)

delete = Button(root, text="Stergeti", font=("bold",15), bg="yellow", command=delete)
delete.place(x=125, y=550)

update = Button(root, text = "Modificati", font=("bold",15),bg = "yellow", command =update)
update.place(x=220, y=550)

get = Button(root, text = "Afisati", font=("bold",15),bg = "yellow", command =get )
get.place(x=330, y=550)

list = Listbox(root, width=70,height=30)
list.place(x=500,y=50)
show()

root.mainloop()