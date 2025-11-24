import json
class Student:
    def __init__(self,roll, name, marks):
        self.roll=roll
        self.name=name
        self.marks=marks or {}
    def average(self):
        if not self.marks:
            return 0.0
        return sum(self.marks.values())/len(self.marks)
    def __str__(self):
        return f"Roll no:{self.roll}, Name:{self.name}, Marks:{self.marks}, Avg:{self.average():.2f}"
class StudentManagementsystem:
    def __init__(self,filename="Student.txt"):
        self.filename = filename
        self.Students = {}
        self.load_data()
#File Handling
    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                data=json.load(f)
                for roll, info in data.items():
                    self.Students[roll]=Student(roll, info["name"],info["marks"])
        except FileNotFoundError:
            pass
        except Exception as e:
            print("Error loading file:",e)
    def save_data(self):
        try:
            data={}
            for roll, Student in self.Students.items():
                data[roll]={"Name":Student.name,"Marks":Student.marks}
            with open(self.filename, "w") as f:
                json.dump(data,f)
        except Exception as e:
            print("Error saving file:",e)
#CURD Operation
    def add_Student(self, roll, name, marks):
        if roll in self.Students:
            print("Students already exists!")
        else:
            self.Students[roll]=Student(roll, name, marks)
            self.save_data()
            print("Student added Successfully!")
    def view_Students(self):
        if not self.Students:
            print("No Students Found.")
        else:
            for Students in self.Students.values():
                print(Students)
    def search_Student(self,roll):
        return self.Students.get(roll, None)
    def update_Student(self,roll, name=None, marks=None):
        if roll in self.Students:
            if name:
                self.Students[roll].name=name
            if marks:
                self.Students[roll].marks=marks
            self.save_data()
            print("Student Updated Successfully!")
        else:
            print("Student are not found!")
    def delete_Student(self,roll):
        if roll in self.Students:
            del self.Students[roll]
            self.save_data()
            print("Student deleted Successfully!")
        else:
            print("Student not found!")
#Analytics
    def calculate_average(self):
        if not self.Students:
            return 0.0
        return sum(s.average() for s in self.Students.values()) / len(self.Students)
    def find_top_Student(self):
        if not self.Students:
            return None
        return max(self.Students.values(), key=lambda s: s.average())
#Main Program
def main():
    sms=StudentManagementsystem()
    while True:
        print("----Student Management System----")
        print("1.Add Student.")
        print("2.View Students.")
        print("3.Search Student.")
        print("4.Update Student.")
        print("5.Delete Student.")
        print("6.Average of a Class.")
        print("7.Top Student.")
        print("8.Exit.")
        choice=input("Enter a choice(1-8):")
        try:
            if choice=="1":
                roll=input("Enter a Roll no:")
                name=input("Enter a Name:")
                marks={}
                n=int(input("Enter no of subjects:"))
                for i in range(n):
                    sub=input(f"Name of the {i+1} subject:")
                    score=int(input(f"Enter a {sub} mark:"))
                    marks[sub]=score
                sms.add_Student(roll, name, marks)
            elif choice=="2":
                sms.view_Students()
            elif choice=="3":
                roll=input("Enter a Roll no to search:")
                student=sms.search_Student(roll)
                print(student if student else "Student not found")
            elif choice=="4":
                roll=input("Enter a Roll no to update:")
                name=input("Enter a New Name(Leave blank to skip):")
                marks={}
                update_marks=input("Update Marks?(Y/N):")
                if update_marks.upper()=="Y":
                    n=int(input("Enter no of subjects:"))
                    for i in range(n):
                        sub=input(f"Name of the {i+1} subject:")
                        score=int(input(f"Enter a {sub} mark:"))
                        marks[sub]=score
                sms.update_Student(roll, name if name else None, marks if marks else None)
            elif choice=="5":
                roll=input("Enetr a Roll no to delete:")
                delete_marks=input("Delete Marks?(Y/N):")
                sms.delete_Student(roll)
            elif choice=="6":
                print("Average mark of the class:",sms.calculate_average())
            elif choice=="7":
                top=sms.find_top_Student()
                print("Top student:", top if top else "No top Student available")
            elif choice=="8":
                print("Exiting.........")
                break
            else:
                print("Invalid Choice! Re-enter the correct choice.")
        except Exception as e:
            print("Error:",e)
if __name__=="__main__":
    main()
