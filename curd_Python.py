'''
@Author: Tejaswini Shinde
@Date: 2022-05-27  11: 05: 00
@Last Modified by: Tejaswini Shinde
@Last Modified time: 
@Title: Python-Mysql Crud Operations.
'''

import json
import mysql.connector

with open('Credentials.json', 'r') as datafile:
	data = json.load(datafile)
    
mydb = mysql.connector.connect(
  host=data['host'],
  user=data['user'],
  password=data['password'],
  database=data['database']
)
#print(mydb)
curobj=mydb.cursor()
class crud_operations():
    def menu(self):
        """
        Description:
            Takes user input.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns nothing. 
        """
        print("1.Create\n2.Insert\n3.Display\n4.Update\n5.Delete")
        option=int(input("Select the option:"))
        if option==1:
            self.create()
        elif option==2:
            self.insert()
        elif option==3:
            self.display()
        elif option==4:
            self.update()
        elif option==5:
            self.delete()
        else:
            print("Not a valid input...")

    def create(self):
        """
        Description:
            Takes nothing.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns nothing but prints given query output. 
        """
        query="create table employe(employeeid int,firstname varchar(30),lastname varchar(50),department varchar(50),salary double,age int ,experience int);"
        curobj.execute(query)
        print("New table was created successfully")
        self.menu()

    def insert(self):
        """
        Description:
            Takes nothing.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns nothing but prints given query output. 
        """
        query="insert into employees(employeeid,firstname,lastname,department,salary,experience) values(%s,%s,%s,%s,%s,%s)"
        val = [("1","Tejaswini","Shinde","IT","40000","2"),
               ("2","Komal","Gholap","SALES","60000","3"),
                ("3","Swapnil","Shinde","SAP","80000","3")]
        curobj.executemany(query,val)
        mydb.commit()
        print("Data inserted successfully")
        self.menu()

    def display(self):
        """
        Description:
            Takes nothing.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns nothing but prints given query output. 
        """
        query="select *from employees"
        curobj.execute(query)
        myresult=curobj.fetchall()
        for x in myresult:
            print(x)
        print("Displayed data successfully")
        self.menu()
     
    def update(self):
        """
        Description:
            Takes nothing.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns nothing but prints given query output. 
        """
        query="update employees set lastname='Jadhav' where firstname='Tejaswini';"
        curobj.execute(query)
        mydb.commit()
        print("Data updated successfully")
        self.menu()

    def delete(self):
        """
        Description:
            Takes nothing.
        Parameter:
            Not passed any parameters. 
        Return:
            Returns nothing but prints given query output. 
        """
        query="delete from employees where department='IT';"
        curobj.execute(query)
        mydb.commit()
        print("Data deleted successfully")
        self.menu()


if __name__ == "__main__":
    print("Welcome to CRUD Operations")
    crud=crud_operations()
    crud.menu()        