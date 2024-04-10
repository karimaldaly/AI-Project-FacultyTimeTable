import sqlite3 as sql

conn = sql.connect('schedule.db')
c = conn.cursor()

c.execute("""create table room (number text , capacity integer)""")
c.execute("insert into room values ('H1', 400),"
                                    "('H2', 350),"
                                    "('H3', 200),"
                                    "('H4', 150) ")
                                    
c.execute("""create table meeting_time (id text , time text)""")
c.execute("insert into meeting_time values ('LEC1', 'From 9:00 AM  to   11:00 AM'),"
                                    " ('LEC2', 'From 12:00 PM  to   1:30 PM'),"
                                    " ('LEC3', 'From 2:00 PM  to   4:00 PM'),"
                                    " ('LEC4', 'From 4:00 PM  to   6:00 PM'),")

c.execute("""create table insrtuctor (number text , name text)""")
c.execute("insert into insrtuctor values ('I1', 'DR/ AMR S. GHONIEM'),"
                                    "('I2', 'DR/ Mohamed Elsaid'),"
                                    "('I3', 'DR/ Salwa moustafa'),"
                                    "('I4', 'DR/ MANAL ABD EL KADER'),")

c.execute("""create table course (number text , name text)""")
c.execute("insert into course values ('C1', 'ST-121'),"
                                    "('C2', 'CS-214'),"
                                    "('C3', 'CS-314'),"
                                    "('C4', 'IS-241'),"
                                    "('C5', 'IT-222'),"
                                    "('C6', 'IS-211'),"
                                    "('C7', 'IS-444'),")

c.execute("""create table department (name text)""")
c.execute("insert into department values ('MI'),"
                                    "('CS'),"
                                    "('IS'),")
                              
#/////////////////////////////////////////////////////////////////

class DataDB:
    

    def __init__(self):
        self._conn = sql.connect('schedule.db')
        self._c = self._conn.cursor()
        self._rooms = self._select_rooms()
        self._meetingTime = self._select_meetingTime()
        self._instructor = self._select_instructor()
        self._department = self._select_department()
        self._course = self._select_course()


    def select_Room(self):
        self._c.excute("select * from room")
        rooms = self._c.fetchall()
        returnRooms = []
        for i in range(0, len(rooms)):
            returnRooms.append(Room(rooms[i][0],rooms[i][1]))
        returnRooms = []

    def select_Instructor(self):
        self._c.excute("select * from instructor")
        instructors = self._c.fetchall()
        returnInstructors = []
        for i in range(0, len(instructors)):
            returnInstructors.append(Instructor(instructors[i][0],instructors[i][1]))
        returnInstructors = []

    def select_meeting_time(self):
        self._c.excute("select * from meeting_time")
        meetings = self._c.fetchall()
        returnMeetings = []
        for i in range(0, len(meetings)):
            returnMeetings.append(MeetingTime(meetings[i][0],meetings[i][1]))
        returnMeetings = []

    def select_department(self):
        self._c.excute("select * from department")
        departments = self._c.fetchall()
        returnDepartments = []
        for i in range(0, len(departments)):
            returnDepartments.append(Department(departments[i][0],departments[i][1]))
        returnDepartments = []

    def select_course(self):
        self._c.excute("select * from course")
        courses = self._c.fetchall()
        returnCourses = []
        for i in range(0, len(courses)):
            returnCourses.append(Course(courses[i][0],courses[i][1]))
        returnCourses = []


#////////////////////////////////////////////////////////


class Course:
    def __init__(self, number, name, instructors, maxNumbOfStudents):
        self._number = number
        self._name = name
        self._maxNumbOfStudents = maxNumbOfStudents
        self._instructors = instructors

    def get_number(self): return self._number
    def get_name(self): return self._name
    def get_instructors(self): return self._instructors
    def get_maxNumbOfStudents(self): return self._maxNumbOfStudents
    def __str__(self): return self._name


class Instructor:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def get_id(self): return self._id
    def get_name(self): return self._name
    def __str__(self): return self._name

class Room:
    def __init__(self, number, seatingCapacity):
        self._number = number
        self._seatingCapacity = seatingCapacity

    def get_number(self): return self._number
    def get_seatingCapacity(self): return self._seatingCapacity

class MeetingTime:
    def __init__(self, id, time):
        self._id = id
        self._time = time

    def get_id(self): return self._id
    def get_time(self): return self._time


class Department:
    def __init__(self, name, courses):
        self._name = name
        self._courses = courses

    def get_name(self): return self._name
    def get_courses(self): return self._courses

class Class:
    def __init__(self, id, dept, course):
        self._id = id
        self._dept = dept
        self._course = course
        self._instructor = None
        self._meetingTime = None
        self._room = None

    def get_id(self): return self._id
    def get_dept(self): return self._dept
    def get_course(self): return self._course
    def get_instructor(self): return self._instructor
    def get_meetingTime(self): return self._meetingTime
    def get_room(self): return self._room
    def set_instructor(self, instructor): self._instructor = instructor
    def set_meetingTime(self, meetingTime): self._meetingTime = meetingTime
    def set_room(self, room): self._room = room

    def __str__(self):
        return str(self._dept.get_name()) + "," + str(self._course.get_number()) + "," + \
            str(self._room.get_number()) + "," + str(self._instructor.get_id()) + "," + str(self._meetingTime.get_id())













