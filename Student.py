import os
import pandas as pd

fstudent='student.csv'
fbatch='batch.csv'
fcourse='course.csv'

def grade(m):
        if (m>=90):
                grade='A'
        elif (m>=80):
                grade='B'
        elif (m>=70):
                grade='C'
        elif (m>=60):
                grade='D'
        elif(m>=40):
                grade='E'
        elif(m<40):
                grade='F'
        return grade

def student():
        print("Enter 1 to create a new student:")
        print("Enter 2 to update student details:")
        print("Enter 3 to remove a student from database:")
        print("Enter 4 to generate a report card:")
        c=int(input("Enter your Choice:"))
        if (c==1):        
                print("Enter details of Students below:")
                sID=input("Student ID:")
                NameF=input("First Name:")
                NameM=input("Middle Name:")
                NameL=input("Last Name:")
                Name="{} {} {}".format(NameF,NameM,NameL)
                Rollno=int(input("Roll number:"))
                BatchID=input("Batch Name:")
                newSt={'Student ID':[sID],'Name':[Name],'Class Roll Number':[Rollno],'Batch ID':[BatchID]}
                newSt2=[sID,Name,Rollno,BatchID]
                if(os.path.isfile(fstudent)):
                        df=pd.read_csv(fstudent)
                        df.loc[len(df.index)] = newSt2
                else:    
                        df=pd.DataFrame(newSt)
                        df.set_index("Student ID",inplace=True)
                df.to_csv(fstudent,index=False)
                df1=pd.read_csv(fbatch)
                a1=df1.to_numpy()
                for i in range(len(a1)):
                        if (a1[i][0]==batchID):
                                a1[i][4]==a1[i][4]+':'+sID
                                break
                df1=pd.DataFrame(a1)
                df1.to_csv(fbatch)
                print("New Student created succesfully!")

        elif (c==2):   
                df=pd.read_csv(fstudent)
                sID=input("Enter ID of the student to update details of:")
                print("Enter 1 if you want to change Name of Student")
                print("Enter 2 if you want to change Classs Roll No of Student")
                print("Enter 3 if you want to change Batch ID of Student")
                ch=int(input("Enter choice:"))
                s=df.to_numpy()
                L=len(s)
                if ch==1:
                        newName=input("Enter new name of student:")
                        for i in range(L):
                                if s[i][0]==sID:
                                        s[i][1]=newName
                                        break
                        df=pd.DataFrame(s)
                        df.set_index("Student ID",inplace=True)
                        df.to_csv(fstudent,index=False)                
                elif ch==2:
                        newroll=int(input("Enter new class roll number:"))
                        for i in range(L):
                                if s[i][0]==sID:
                                        s[i][2]=newroll
                                        break
                        df=pd.DataFrame(s)
                        
                        df.to_csv(fstudent,index=False)
                elif ch==3:
                        newbatch=input("Enter new Batch ID:")
                        for i in range(L):
                                if s[i][0]==sID:
                                        s[i][3]=newbatch
                                        break
                        df=pd.DataFrame(s)
                        df.to_csv(fstudent,index=False)

        elif (c==3):
                sID=input("Enter ID of the student to delete details of:")
                df=pd.read_csv(fstudent)
                df.set_index("Student ID",inplace=True)
                df=df.drop(sID)
                df.to_csv(fstudent)
                print("Done!")
        elif (c==4):
                sID=input("Enter ID of student to generate Report Card of:")
                coursenlist=[]
                gradelist=[]
                percentlist=[]
                statuslist=[]
                df=pd.read_csv(fstudent)
                a=df.to_numpy()
                for i in range(len(a)):
                        if (a[i][0]==sID):
                                name=a[i][1]
                                roll=a[i][2]
                                batchID=a[i][3]
                                break

                df2=pd.read_csv(fbatch)          
                a2=df2.to_numpy()
                for i in range(len(a2)):
                        if(a2[i][0]==batchID):
                                cl=a2[i][3]
                                courses=str.split(cl,":")
                                break

                df3=pd.read_csv(fcourse)
                a3=df3.to_numpy()
                
                for course in courses:
                        for i in range(len(a3)):
                            if(a3[i][0]==course):
                                ml=a3[i][2]
                                
                                ml2=str(ml).split("-")
                                
                                for j in range (len(ml2)):
                                        
                                        ml3=str(ml2[j]).split(":")
                                        
                                        if ml3[0]==sID:
                                               
                                                marks=int(ml3[1])
                                                g=grade(marks)
                                                gradelist.append(g)
                                                percentlist.append(marks)
                                                if (g=='F'):
                                                        statuslist.append('FAIL')        
                                                else:
                                                        statuslist.append('PASS')
                                                coursenlist.append(a3[i][1])
                                                break
                                        
                f=open("Result.txt",'w')
                f.write("Name: {}\n".format(name))
                f.write("Student ID: {}\n".format(sID))
                f.write("Batch ID: {}\n".format(batchID))
                f.write("Roll Number: {}\n".format(roll))
                
                for i in range(len(courses)):
                        content="Course ID: "+str(courses[i])+'\tCourse Name: '+str(coursenlist[i])+'\tPercentage: '+str(percentlist[i])+'\tGrade: '+str(gradelist[i])+'\tStatus: '+str(statuslist[i])+'\n'
                        f.write(content)
                print("Report generated!")
                f.close()
        else:
                print("Sorry, invalid choice entered!")