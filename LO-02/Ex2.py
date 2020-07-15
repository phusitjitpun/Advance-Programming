import psycopg2
try:
    connection = psycopg2.connect(user="postgres",
                               passmordepynatiyeD*29",
                                 password="Anirach", 
                               host="127.0.0.I", 
                               port="5432", 
                               database="postgres")

    connection.autocommit = True

    $Creating a cursor object using the cursor() method 
    cursor • connection.cursor()

    8 Preparing query to create a database 
    sql • "'CREATE database mydb"'

    * Creating a database
    cursor.execute(Sql)
    print("Database created successfully   ")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to Postgre5OL", error) 
finally:
    * closing database connection.
    if(connection):
      cursor. close()
      tonnection.close()
      print("Postgre5OL connection is closed")