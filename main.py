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
        retlist = []
        res = self.__cur.execute("SELECT * From kurs")
        ret = res.fetchall()
        for i in ret:
            k = Kurs()
            k.settid(i[0])
            k.setname(i[1])
            k.setraum(i[2])
            retlist.append(k)
        return retlist

    def printfunktion(self):
        res = self.__cur.execute("SELECT * From kurs")
        ret = res.fetchall()

        for i in ret:
            print("die id ist:", i[0])
            print("das fach ist:", i[1])
            print("der raum ist:", i[2])

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
db.addKurs(kurs1)
db.addKurs(kurs2)
ret = db.getKurse()
ret1 = db.printfunktion()

print(ret[0].getname())
