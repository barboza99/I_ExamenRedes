from multiprocessing.dummy import current_process
import mysql.connector

args = {'host': 'localhost', 
        'user': 'root', 
        'password': '1234una', 
        'dbname': 'examen', 
        'tableName': 'usuarios'}

query1 = "SELECT * FROM usuarios;"

def connecion():
    try:
        connection = mysql.connector.connect(host = args['host'],
                                            database = args['dbname'],
                                            user = args['user'],
                                            password = args['password'])
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected: ", db_info)
            cursor = connection.cursor()
            cursor.execute(query1)
            records = cursor.fetchall()
            
            # print("\nFilas: ")
            # for row in records:
            #     print("Id = ", row[0])
            #     print("firstName = ", row[1])
            #     print("lastName = ", row[2])
            #     print("address = ", row[3])
            return records
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally: 
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")