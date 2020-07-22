import psycopg2
from psycopg2 import Error
try:
  connection = psycopg2.connect(user="webadmin",
                        password="RBBehe54965", 
                        host="node1441-phusit.app.ruk-com.cloud",   
                        port="11030",
                        database="test081")

  cursor = connection.cursor()

  create_table_guery = '''CREATE TABLE Comments
      (id        SERIAL PRIMARY KEY,
       name      VARCHAR(50) NOT NULL,
       comment   VARCHAR(1000) NOT NULL ); '''

  cursor. execute(create_table_guery) 
  connection.commit()
  print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.DatabaseError) as error: 
  print("Error while creating PostgreSCIL table", error)
finally:
  # closing database connection.
  if(connection):
    cursor.close()
    connection. close()
    print("PostgreSOL connection is closed")