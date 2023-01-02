import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
fdepartment='department.csv'
fbatch='batch.csv'
fcourse='course.csv'

def line_graph(bl,ml,d):
        plt.plot(bl,ml, linestyle = 'dashed')
        plt.title("{} STATISTICS".format(d))
        plt.yticks([0,10,20,30,40,50,60,70,80,90,100])
        plt.xlabel("Batch Name")
        plt.ylabel("Average Percentage")
        plt.show()

def department():
        print("Enter 1 to Create a new department")
        print("Enter 2 to view all batches in a department")
        print("Enter 3 to view average performance of all batches in the department with line plot:")
        c=int(input("Enter your choice:"))
        if (c==1):
                print("Enter details of department")
                deptID=input("Department ID:")
                deptN=input("Department Name:")
                
                if(os.path.isfile(fdepartment)):
                        df=pd.read_csv(fdepartment)
                        newDept2=[deptID,deptN,""]                     
                        df.loc[len(df.index)] = newDept2
                        df.to_csv(fdepartment,index=False)
                else:
                        newDept={"Department ID":deptID,"Department Name":deptN,"List of Batches":""}
                        df=pd.DataFrame(newDept)
                        df.to_csv(fdepartment,index=False)
                print("New Department created succesfully!")
        elif(c==2):
                deptID=input("Enter department ID:")
                df=pd.read_csv(fdepartment)
                s=df.to_numpy()
                for i in range(len(s)):
                        if s[i][0]==deptID:
                                lob=s[i][2]
                print("List of Batches:",lob)
        elif(c==3):
                deptID=input("Enter department ID:")
                df=pd.read_csv(fdepartment)
                df2=pd.read_csv(fbatch)
                df3=pd.read_csv(fcourse)
                s=df.to_numpy()
                s2=df2.to_numpy()
                s3=df3.to_numpy()
                for i in range(len(s)):
                        if s[i][0]==deptID:
                                batch=str(s[i][2])
                                batchlist=batch.split(':')
                                markslist=[]
                                studentL=[]
                                for j in batchlist:
                                        tot=0
                                        n=0
                                        for i in range(len(s2)):
                                                if (s2[i][0]==j):
                                                        studentc=s2[i][4]
                                        studentL=studentc.split(':')
                                       
                                        for st in studentL:
                                                
                                                for i in range(len(s3)):
                                                        coursest=str(s3[i][2])
                                                        coursestL=coursest.split('-')
                                                        for j in coursestL:
                                                                jl=j.split(':')
                                                                if jl[0]==st:
                                                                        tot=tot+int(jl[1])
                                                                        n+=1
                                                                        break
                                        avg=tot/n
                                        #print(avg)                
                                        markslist.append(avg)
                                for j in range(len(batchlist)):
                                        print("BATCH:",batchlist[j],"\tMARKS:",markslist[j])       
                                break
                ch=int(input("Enter 1 if you wish to print line  otherwise enter any other number to continue")) 
                if ch==1:
                        line_graph(batchlist,markslist,deptID)
        else:
                print("Wrong Choice entered, Sorry!")

                                   
                
                                                        

                                       

                        