import psycopg2
try:
    connection = psycopg2.connect(user="webadmin",
                                password="FFGqce84823",
                                host="node8579-advweb-12.app.ruk-com.cloud",
                                port="11102",
                                database="CloudDB")

    cursor = connection.cursor()
    #print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(),"\n")

    #print postgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")