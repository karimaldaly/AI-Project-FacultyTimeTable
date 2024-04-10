
import sqlite3


Instructors = [["I1", "DR/ AMR S. GHONIEM"], ["I2", "DR/ Mohamed El said"],
               ["I3", "DR/ Salwa "], ["I4", "DR/ MANAL ABD EL KADER"]]
ROOMS = [["H1", 400], ["H2", 350], ["H3", 200], ["H4", 150]]
MEETING_TIMES = [["LEC1", "From 9:00 AM  to   11:00 AM"], ["LEC2", "From 11:00 AM  to  1:30 PM"], [
    "LEC3", "From 2:00 PM  to  4:00 PM"], ["LEC4", "From 4:00 PM  to  6:00 PM"]]

db = sqlite3.connect("app.db")
db.execute("create table if not exists instructors(id text,name text)")
db.execute("create table if not exists rooms(number text,NumOfStudent integer)")
db.execute("create table if not exists meetingtime(number text,meetingtime text)")
cr = db.cursor()


class DataBase:

    def call_data(self):
        self.instructors_data()
        self.rooms_data()
        self.meetingTime_data()
        print("> Data inserted successfully... ")

    def instructors_data(self):
        for x in range(0, len(Instructors)):
            cr.execute(
                "insert into rooms(number) values('{instrutors[x][0]}')")
        for x in range(0, len(Instructors)):
            cr.execute(
                "insert into rooms(NumOfStudent) values('{instrutors[0][x]}')")
        db.commit()

    def rooms_data(self):
        for x in range(0, len(Instructors)):
            cr.execute(
                "insert into rooms(number) values('{instrutors[x][0]}')")
        for x in range(0, len(Instructors)):
            cr.execute(
                "insert into rooms(NumOfStudent) values('{instrutors[0][x]}')")
        db.commit()

    def meetingTime_data(self):
        for x in range(0, len(MEETING_TIMES)):
            cr.execute(
                "insert into rooms(number) values('{instrutors[x][0]}')")
        for x in range(0, len(MEETING_TIMES)):
            cr.execute(
                "insert into rooms(NumOfStudent) values('{instrutors[0][x]}')")
        db.commit()


dataBase = DataBase()
dataBase.call_data()
db.close()
