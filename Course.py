import matplotlib.pyplot as plt
import os
import pandas as pd
fstudent='student.csv'
fcourse='course.csv'
fbatch='batch.csv'
fdepartment='department.csv'
def course():
    print("Enter 1 to create a new course:")
    print("Enter 2 to view performance of all students in the course:")
    print("Enter 3 to show course statistics:")
    c=int(input("Enter choice:"))
    if(c==1):
        courseID=input("Enter course ID:")
        courseN=input("Enter Course Name:")
        if(os.path.isfile(fcourse)):
            df=pd.read_csv(fcourse)
            newCourse=[courseID,courseN,""]
            df.loc[len(df.index)]=newCourse
        else:
            newCourse={'Course ID':[courseID],'Course Name':[courseN],'Marks Obtained':""}
            df=pd.DataFrame(newCourse)
            
        df.to_csv(fcourse,index=False)
        print("New course created!")    
    elif(c==2):
        df=pd.read_csv(fcourse)
        a=df.to_numpy()
        courseID=input("Enter course ID to view student performance of:")
        for i in range(len(a)):
            if a[i][0]==courseID:
                lc=a[i][2]
        df2=pd.read_csv(fstudent)
        a2=df2.to_numpy()
        l=str.split(lc,"-")
        for i in l:
            c=str.split(i,':')
            for j in range(len(a2)):
                if a2[j][0]==c[0]:
                    name=a2[j][1]
            print("Student ID:",c[0],"\tName:",name,"\tMarks obtained:",c[1])
    elif(c==3):
            df=pd.read_csv(fcourse)
            a=df.to_numpy()
            courseID=input("Enter course ID to view statistics of:")
            marksL=[]
            for i in range(len(a)):
                if a[i][0]==courseID:
                    sml=a[i][2]
                    break
            sml2=sml.split('-')
            for i in sml2:
                sml3=i.split(':')
                marksL.append(int(sml3[1]))
                     
            l=len(marksL)
            gradeinterval=[0,40,50,60,70,80,90,100]
            label=['F','E','D','C','B','A']
            ylist=range(0,l+1)
            plt.title('COURSE STATISTICS')
            plt.hist(marksL,gradeinterval)
            plt.xticks([20,55,65,75,85,95],label)
            plt.yticks(ylist)
            plt.xlabel('GRADES')
            plt.ylabel('NO OF STUDENTS')
            plt.show()
    else:
        print("Sorry! Invalid choice")