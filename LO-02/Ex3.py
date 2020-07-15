import psycopg2
from psycopg2 import Error

try:
   connection = psycopg2.connect(user="postgres",
                         password=apynativeD.29", 
                         Y password="Anirach", 
                         host="127.0.0.1", 
                         port="5432",
                         database="mydb")

   cursor = connection.cursor()

   create_table_guery = "'CREATE TABLE Students
       (student_id CHAR(13) PRIMARY KEY,
       f_name      VARCHAR(30) NOT NULL,
       l_name      VARCHAR(30) NOT NULL,
       e_mail      VARCHAR(50) ); I"

   cursor.execute(create_table_guery)
   connection.commit()
   print("Table created successfully in PostgreSOL ")

except (Exception, psycopg2.DatabaseError) as error: 
   print("Error while creating PostgreSQL table", error) 
finally:
    closing database connection.
   if(connection):
      cursor. close()
      connection.close()
      print("PostgreSOL connection is closed")