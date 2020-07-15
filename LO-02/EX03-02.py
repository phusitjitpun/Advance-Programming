import psycopg2
from psycopg2 import Error

try:
   connection = psycopg2.connect(user="postgres",
                         password="nextthunder5971", 
                         #password="Anirach", 
                         host="127.0.0.1", 
                         port="5432",
                         database="mydb")

   cursor = connection.cursor()

   create_table_guery = '''CREATE TABLE Subjects
       (student_id VARCHAR(15) PRIMARY KEY,
       subject_name      VARCHAR(50) NOT NULL,
       credit     INTEGER NOT NULL,
       teacher_id    CHAR(3) ); '''

   cursor.execute(create_table_guery)
   connection.commit()
   print("Table created successfully in PostgreSOL ")

except (Exception, psycopg2.DatabaseError) as error: 
   print("Error while creating PostgreSQL table", error) 
finally:
    #closing database connection.
    if(connection):
        cursor. close()
        connection.close()
        print("PostgreSOL connection is closed")