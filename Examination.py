import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
fcourse='course.csv'
fstudent='student.csv'
fbatch='batch.csv'
dfb=pd.read_csv(fbatch)
dfc=pd.read_csv(fcourse)
dfs=pd.read_csv(fstudent)
def examination():
    print("Enter 1 for new Examination")
    print("Enter 2 for scatter plot")
    c=int(input("Enter choice:"))
    if c==1:
        print("Enter details of an Examination:")
        c=True
        lp1=[]
        n=int(input("No. of courses:"))
        for i in range(n):
            courseID=input("Enter Course ID:")
            n=int(input("Enter number of students:"))
            s=''
            print ("Enter details of student 1:")
            id=input("Student ID:")
            m=input("Marks:")
            s=id+":"+m
            lp=[[id,m],]
            for i in range(2,n+1):
                print ("Enter details of student",i,":")
                id=input("Student ID:")
                m=input("Marks:")
                a=id+":"+m
                s=s+"-"+a
                lp.append([id,m])
            df=dfc
            a=df.to_numpy()
            for i in range(len(a)):
                if a[i][0]==courseID:
                    a[i][2]=s
            
            lp1.append(lp)
            df=pd.DataFrame(a)
            df.to_csv(fcourse,index=False)
        
        print("Performance of all Students in the Exam:")
        sno=1
        for j in lp1:
            for i in j:
                print(sno,"Student ID:",i[0],"Marks:",i[1])
                sno+=1
       
    elif c==2:
        scatter_plot()
    else:
        print("Sorry Wrong choice!")

#time to print scatter plot

def scatter_plot():
    ac=dfc.to_numpy()
    ab=dfb.to_numpy()
    for i in range(len(ac)):
        x=[]
        y=[]
        course=ac[i][0] #courseID
        students=ac[i][2]
        studentL=students.split('-')
        for j in  range(len(ab)): 
            
            batchID=ab[j][0]
            batchcourses=ab[j][3]
            batchcoursesL=batchcourses.split(":")
            if course in batchcoursesL:
                tot=0
                n=0
                batchstudent=ab[j][4]
                batchstudentL=batchstudent.split(':')
                for k in studentL:
                    studentL2=k.split(':')
                    if studentL2[0] in batchstudentL:
                        tot=tot+int(studentL2[1]) 
                        n=n+1 
                avg=tot/n
                x.append(avg)
                y.append(batchID)
        plt.scatter(x,y)
    plt.xlabel("MARKS")
    plt.ylabel("BATCH")
    plt.show()





