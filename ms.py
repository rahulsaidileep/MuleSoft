# import sqlite to perform DBMS
import sqlite3
import os.path
#function to create sqlite connection
def sqlConnnection():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "SQLite_Mulesoft.db")
    global sqliteConnection,cursor
    sqliteConnection=sqlite3.connect(db_path)  
    #"SQLite_Mulesoft.db" is name of the Database to which the connection is established 
    # if database id not present it will create a database in that name (here : SQLite_Mulesoft.db)
    cursor=sqliteConnection.cursor()   
    #cursor are used to execute queries

#function to create table in database
def sqlCreateTable():
    query="create table IF NOT EXISTS Movies_Data(movie_name varchar(45),actor varchar(50),actress varchar(50),director varchar(50),release_year Integer);"
    cursor.execute(query)

#function to insert values in created table 
#method 1: INDIVIDUALLY
def sqlInsertValues1():
    query1="Insert into Movies_Data values('RRR','Ram Charan,NTR','Alia Bhatt','S. S. Rajamouli','2022');"
    query2="Insert into Movies_Data values('Radhe Shyam','Prabhas','Pooja Hegde','Radha Krishna Kumar','2022');"
    query3="Insert into Movies_Data values('Bheemla Nayak','Pawan Kalyan','Nithya Menon','	Saagar K Chandra','2022');"
    query4="Insert into Movies_Data values('Baahubali 2','Prabhas','Anushka Shetty','S. S. Rajamouli','2017');"
    query5="Insert into Movies_Data values('Darling','Prabhas','Kajal Aggarwal','	A. Karunakaran','2010');"
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    cursor.execute(query4)
    cursor.execute(query5)
    sqliteConnection.commit() #tp save changes

#method 1: using loops
def sqlInsertValues2():
    total =["Insert into Movies_Data values('RRR','Ram Charan,NTR','Alia Bhatt','S. S. Rajamouli','2022');",
   "Insert into Movies_Data values('Radhe Shyam','Prabhas','Pooja Hegde','Radha Krishna Kumar','2022');",
    "Insert into Movies_Data values('Bheemla Nayak','Pawan Kalyan','Nithya Menon','	Saagar K Chandra','2022');",
    "Insert into Movies_Data values('Baahubali 2','Prabhas','Anushka Shetty','S. S. Rajamouli','2017');",
    "Insert into Movies_Data values('Mirchi','Prabhas','Anushka Shetty','Koratala Siva','2013');"]
    for i in total:
        cursor.execute(i)
    sqliteConnection.commit()
 

#function to perform queries
def sqlQueries():
    sqliteConnection=sqlite3.connect("SQLite_Mulesoft.db")
    cur=sqliteConnection.cursor()
    query1="Select * from 'Movies_Data'"
    query2="Select * from Movies_Data where actor='Prabhas';"
    cur.execute(query1)
    result1=cur.fetchall()   
    cur.execute(query2)
    result2=cur.fetchall()   
    print('Result1 : ',result1)
    print()
    print('Result2 : ',result2)

if __name__== "__main__":
    sqlConnnection()

    sqlCreateTable()

    sqlInsertValues1()

    #sqlInsertValues2()

    sqlQueries()