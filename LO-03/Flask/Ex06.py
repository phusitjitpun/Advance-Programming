import psycopg2                                             
try:
  connection = psycopg2.connect(user="webadmin",
                        password="RBBehe54965", 
                        host="node1441-phusit.app.ruk-com.cloud",          
                        port="11030",
                        database="postgres")

  connection.autocommit = True

  #Creating a cursor object using the cursor() method 
  cursor = connection.cursor()

  # Preparing query to create a database 
  sql = '''CREATE database Test081'''

  #Creating a database
  cursor.execute(sql)
  print("Database created successfully.........") 
                                                            
except (Exception, psycopg2.Error) as error:
 print("Error while connecting to PostgreSQL", error)
finally:
 # closing database connection.
  if(connection):
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")