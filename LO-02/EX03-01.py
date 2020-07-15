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

   create_table_guery = '''CREATE TABLE Registration
       (student_id CHAR(13) NOT NULL,
       subject_id      VARCHAR(30) NOT NULL,
       year     CHAR(4) NOT NULL,
       semester      CHAR(1) NOT NULL,
       grade    CHAR(2) ); '''

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