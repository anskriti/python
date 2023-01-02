print("STUDENT EXAMINATION PORTAL")
print("Enter 1 to run Student Module")
print("Enter 2 to run Course Module")
print("Enter 3 to run Batch Module")
print("Enter 4 to run Department Module")
print("Enter 5 to run Examination Module")
c=int(input("Enter Choice:"))
if c==1:
    print("\n"+"STUDENT MODULE")
    import Student
    Student.student()
elif c==2:
    print("\n"+"COURSE MODULE")
    import Course
    Course.course()
elif c==3:
    print("\n"+"BATCH MODULE")
    import Batch
    Batch.batch()
elif c==4:
    print("\n"+"DEPARTMENT MODULE")
    import Department
    Department.department()
elif c==5:
    print("\n"+"EXAMINATION MODULE")
    import Examination
    Examination.examination()
else:
    print("\n"+"SORRY WRONG CHOICE!")

