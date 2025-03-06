import sqlite3
class Exam():
    def __init__(self,adress):
        self.con = sqlite3.connect(adress)
        self.cur = self.con.cursor()
    def create_table(self):
        self.cur.execute("create table if not exists student (id integer primary key,fname text,lname text,dname text,pas text)")
        self.con.commit()
    def update_all(self):
        lst = []
        self.cur.execute("select * from student")
        resualt = self.cur.fetchall()
        for i in resualt:
            lst.append(f"{i[0]}-{i[1]} {i[2]}-Dar dore {i[3]} Sabt Shode")
        return lst
    def insert(self,fname,lname,pas,dname):
        self.cur.execute("insert into student values (NULL,?,?,?,?)",(fname,lname,dname,pas))
        self.con.commit()
    def login(self,pas):
        self.cur.execute("select pas from student")
        s = self.cur.fetchall()
        for password in s:
            if pas == password[0]:
                return True
        return False
    def delete(self,id):
        self.cur.execute("delete from student where id = ?",(id,))
        self.con.commit()
