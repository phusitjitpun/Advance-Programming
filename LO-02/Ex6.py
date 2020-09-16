import psycopg2

def deleteStudent(name):
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="nextthunder5971",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="mydb")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from teacher"
        
        cursor.execute(postgreSQL_select_Query,(name,))
        print("Before Delete")
        student_records = cursor.fetchall()
        for row in student_records:
            print(row, '\n')

        postgreSQL_select_Query = "delete from teacher"
        cursor.execute(postgreSQL_select_Query, (name,))
        connection.commit()

        postgreSQL_select_Query = "select * from teacher"
        cursor.execute(postgreSQL_select_Query, (name,))
        print("After Delete")
        student_records = cursor.fetchall()
        for row in student_records:
            print(row, '\n')

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connectiong is closed")

deleteStudent('Anirach')