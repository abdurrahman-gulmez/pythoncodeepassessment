import pandas as pd


class Student:
    def __init__(self,name,surname,stdNo,courses):
        self.name = name
        self.surname = surname
        self.stdNo = stdNo
        self.courses = courses

class Course():
    def __init__(self,courseName, courseCode, students):
        self.courseName = courseName
        self.courseCode = courseCode
        self.students = students

class University(Course, Student):
    def __init__(self ,controlList, name,surname,stdNo,courses,courseName, courseCode, students):
        Course.__init__(self,courseName, courseCode, students)
        Student.__init__(self,name,surname,stdNo,courses)
        self.registerList = []
        self.controlList = controlList
        self.instruction()
    
    def instruction(self):
        print("Please choose a choice: ")
        while(True):
            print("1- Add student to a course")
            print("2- Remove student from a course")
            print("3- Show the file of students")
            print("4- Show the file of courses")
            print("5- Show the file of students and courses")
            print("6- Exit")
            choice = input("Enter a number between 1-6: ")
            if choice == "1":
                self.addStudents()
            elif choice == "2":
                self.deleteStudents()
            elif choice == "3":
                self.showStudentFile()
            elif choice == "4":
                self.showCoursefile()
            elif choice == "5":
                self.showAllFile()
            elif choice == "6":
                break
            else:
                print("Wrong choice. Enter a number between 1-6 !!!")
            

    def addStudents(self):
        inputName = input("Enter the name of the student you want to add to a course: ")
        inputSurname = input("Enter the surname of the student you want to add to a course:")
        inputCourse = input("Enter the name of the course you want to add to the student: ")
        a, b, c = 0, 0, 0
        while((a < len(self.name)) and (b < len(self.surname)) and (c < len(self.courseName))):
            if inputName in self.name[a]:
                if inputSurname in self.surname[b]:
                    if inputCourse in self.courseName[c]:
                        if(self.controlList[c][1] < self.courses[c][2]):
                            self.controlList[c][1] += 1
                            registerDict = {"Name": self.students[a][0], 
                                            "Surname": self.students[b][1], 
                                            "Student Number": self.students[a][2], 
                                            "Course Name": self.courses[c][0],
                                            "Course Code": self.courses[c][1],
                                            "Course Limit": self.courses[c][2],
                                            "Registration Number": self.controlList[c][1]
                            }
                            self.registerList.append(registerDict)
                            break
                        print("Course is full. You cannot do any addition.")
                        break
                    c += 1
                    continue
                b += 1
                continue
            a += 1
        
        if (a == len(self.students)) or (b == len(self.students)) or (c == len(self.courses)):
            print("There is not such a student or course")

    def deleteStudents(self):
        inputName = input("Enter the name of the student you want to delete to a course: ")
        inputSurname = input("Enter the surname of the student you want to delete to a course:")
        inputCourse = input("Enter the name of the course you want to delete to the student: ")
        a, b, c = 0, 0, 0
        while((a < len(self.registerList)) and (b < len(self.registerList)) and (c < len(self.registerList))):
            if inputName in self.registerList[a]["Name"]:
                if inputSurname in self.registerList[b]["Surname"]:
                    if inputCourse in self.registerList[c]["Course Name"]:
                        self.registerList.remove(self.registerList[a])
                        self.controlList[c][1] -= 1
                        break
                    c += 1
                    continue
                b += 1
                continue
            a += 1
        
        if (a == len(self.registerList)) or (b == len(self.registerList)) or (c == len(self.registerList)):
            print("There is not such a register")

    def showStudentFile(self):
        studentDataFrame = pd.DataFrame(data=self.students, columns=["Name","Surname","Student Number"])
        studentDataFrame.to_excel("studentFile.xlsx")
    
    def showCoursefile(self):
        courseDataFrame = pd.DataFrame(data=self.courses, columns= ["Course Name","Course Code","Course Limit"])
        courseRegistraions = []
        for register in range(len(self.controlList)):
            courseRegistraions.append(self.controlList[register][1])
        courseDataFrame["Course Registration"] = courseRegistraions
        courseDataFrame.to_excel("courseFile.xlsx")
    
    def showAllFile(self):
        allDataFrame = pd.DataFrame(data=self.registerList)
        allDataFrame.to_excel("allFile.xlsx")

courses_ = []
courseNames = []
courseCodes = []
courseLimits = []

index = 0
while(True):
    selection = input("Please press 1 to register a course to the university\nPress another key except 1 to exit from register\nYour selection: ")
    if selection == "1": 
        courseName = input("Enter the course name to register to university: ")
        courseCode = int(input("Enter the course code of that course: "))
        courseLimit = int(input("Enter the course student limit of that course: "))
        courseNames.append(courseName)
        courseCodes.append(courseCode)
        courseLimits.append(courseLimit)
    else:
        break

# courses information
x = 0
while(x < len(courseNames)):
    courses_.append([courseNames[x],courseCodes[x],courseLimits[x]])
    x += 1
    
students_ = []
studentNames = []
studentSurnames = []
studentNumbers = []

while(True):
    selection = input("Please press 1 to register a student to the university\nPress another key except 1 to exit from register\nYour selection: ")
    if selection == "1": 
        studentName = input("Enter the name of the student to register to university: ")
        studentSurname = input("Enter the surname of that student: ")
        studentNumber = int(input("Enter the number of that student: "))
        studentNames.append(studentName)
        studentSurnames.append(studentSurname)
        studentNumbers.append(studentNumber)
    else:
        break
# students information
y = 0
while(y < len(studentNames)):
    students_.append([studentNames[y],studentSurnames[y],studentNumbers[y]])
    y += 1

courseRegisterNumbers = []
for a in range(len(courseNames)):
    courseRegisterNumbers.append(0)
registerControlList = []

z = 0
while(z < len(courseNames)):
    registerControlList.append([courseNames[z],courseRegisterNumbers[z]])
    z += 1

print(registerControlList)

university = University(registerControlList,studentNames,studentSurnames,studentNumbers,courses_, courseNames,courseCodes,students_)

