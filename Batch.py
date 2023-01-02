import os
import pandas as pd
import matplotlib.pyplot as plt
fcourse='course.csv'
fstudent='student.csv'
fbatch='batch.csv'
fdepartment='department.csv'

def pie_chart(name,marks):
        plt.pie(x=marks,labels=name,autopct='%.2f%%')
        plt.show()
def batch():
        print("Enter 1 to create a new batch:")
        print("Enter 2 to view list of all students in a batch:")
        print("Enter 3 to view list of all courses taught in the batch ")
        print("Enter 4 to view complete performance of all students in a batch")
        c=int(input("Enter choice:"))
        if (c==1):
                print("Enter details of the Batch:")
                batchID=input("Batch ID:")
                batchN=input("Batch Name:")
                dept=input("Department Name:")
                courses=input("Courses seperated by colon:")
                newBatch={"Batch ID":[batchID],"Batch Name":[batchN],"Department Name":dept,"List of Courses":courses,"List of students":""}
                newBatch2=[batchID,batchN,dept,courses,""]
                if(os.path.isfile(fbatch)):
                                df=pd.read_csv(fbatch)
                                df.loc[len(df.index)] = newBatch2
                                df.to_csv(fbatch,index=False)
                else:
                                df=pd.DataFrame(newBatch)
                                df.to_csv(fbatch,index=False)
                print("New Batch created succesfully!")
                df=pd.read_csv(fdepartment, encoding = "ISO-8859-1")
                s2=df.to_numpy()
                for i in range(len(s2)):
                        if s2[i][0]==dept:
                                t=':'+batchID
                                s2[i][2]=str(s2[i][2])+(t)
                df=pd.DataFrame(s2)
                df.to_csv(fdepartment)
        elif(c==2):
                bID=input("Enter Batch ID:")
                df=pd.read_csv(fbatch)
                a=df.to_numpy()
                t=0
                for i in range(len(a)):
                                if a[i][0]==bID:
                                        a1=a[i][4]
                                        t=1
                if(t==1):
                        a2=a1.split(":")
                        print("Students")
                        print("Student ID:","Name:")
                        for i in a2:
                                        df2=pd.read_csv(fstudent)
                                        s=df2.to_numpy()
                                        for j in range(len(s)):
                                                if s[j][0]==i:
                                                        name=s[j][1]
                                        print(i,"   ",name)
                elif(t==0):
                                print("Btach ID doesn't exist:")
        elif(c==3):
                bID=input("Enter Batch ID:")
                df=pd.read_csv(fbatch)
                a=df.to_numpy()
                t=0
                for i in range(len(a)):
                                if a[i][0]==bID:
                                        a1=a[i][3]
                                        t=1        
                if(t==1):
                        a2=a1.split(":")
                        print("COURSES")
                        print("Course ID:","Course Name:")
                        for i in a2:
                                        df2=pd.read_csv(fcourse)
                                        s=df2.to_numpy()
                                        for j in range(len(s)):
                                                if s[j][0]==i:
                                                        name=s[j][1]
                                        print(i,"  ",name)
                elif(t==0):
                                print("Btach ID doesn't exist:")
        elif(c==4):
                batchID=input("Enter Batch ID to view performance of all students in it:")
                df=pd.read_csv(fbatch)
                a=df.to_numpy() 
                df1=pd.read_csv(fcourse)
                a1=df1.to_numpy()
                df2=pd.read_csv(fstudent)
                a2=df2.to_numpy()
                studentc=""
                namelist=[]
                markslist=[]
                for i in range(len(a)):
                        if (a[i][0]==batchID):
                                studentc=a[i][4]
                studentL=studentc.split(':')
                print("Class Roll\tStudent Name\tPercentage Obtained")
                for s in studentL:
                        tot=0
                        n=0
                        name=""
                        roll=0
                        for i in range(len(a1)):
                                coursest=str(a1[i][2])
                                coursestL=coursest.split('-')
                                for j in coursestL:
                                        jl=j.split(':')
                                        if jl[0]==s:
                                                tot=tot+int(jl[1])
                                                n+=1
                        avg=tot/n                
                        for i in range(len(a2)):
                                if (a2[i][0]==s):
                                        name=str(a2[i][1])
                                        rollno=int(str(a2[i][2]))
                        print(rollno,'\t\t',name,'\t\t',avg)
                        namelist.append(name)
                        markslist.append(avg)
                ch=int(input(("Enter 1 if you wish to see the performance in pie chart, enter any other number to continue")))
                if ch==1:
                        pie_chart(namelist,markslist)
        else:
                print("Sorry! Invalid choice")

                      
