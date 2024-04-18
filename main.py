import sqlite3

class Kurs:
    __id = 1
    __name = "hans"
    __raum = "EG-102"


    def getname(self):
        return self.__name


    def setname(self, value):
        self.__name = value


    def getid(self):
        return self.__id


    def settid(self, value):
        self.__id = value


    def getraum(self):
        return self.__raum


    def setraum(self, value):
        self.__raum = value

class Db:
    kurs = Kurs()
    def init(self):
        self.__con = sqlite3.connect("test.db")
        self.__cur = self.__con.cursor()

    def create(self):
        self.__cur.execute("CREATE TABLE kurs(pk, name, raum)")

    def addKurs(self, kurs):
        self.__cur.execute("INSERT INTO kurs VALUES (?, ?, ?)", [kurs.getid(), kurs.getname(), kurs.getraum()])

    def getKurse(self):
        res = self.__cur.execute("SELECT * From kurs")
        ret = res.fetchall()
        k = Kurs()
        k.settid(ret[0][0])
        k.setname(ret[0][1])
        k.setraum(ret[0][2])
        return k


kurs1 = Kurs()
kurs1.settid(1)
kurs1.setname("DB")
kurs1.setraum("EG-102")

kurs2 = Kurs()
kurs2.settid(2)
kurs2.setname("PG")
kurs2.setraum("EG-103")

db = Db()

db.init()
#db.create()
db.addKurs(kurs)
ret = db.getKurse()
print(ret)
