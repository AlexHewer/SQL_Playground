'''This is for testing databases'''

import pandas as pd
import pyodbc
from utils import get_config_value

# pylint: disable=c-extension-no-member,anomalous-backslash-in-string

#TODO: write to config file
#TODO: implement better solution for when config file value is invalid

def main():
    """Main function controlling the order of logic."""
    db_data: tuple = load_database()
    conn = db_data[0]
    cursor = db_data[1]


    #TODO: remove below and implement further
    cursor.execute('SELECT Name FROM Models')
    for i in cursor:
        print(i[0])
    d_f = pd.read_sql_query('SELECT * FROM Models', conn)
    print(d_f)


def load_database() -> tuple:
    '''Retrieves server connection and loads database.
            Returns:
                    tuple: arg 0 = connection. arg 1 = cursor'''
    server_connected: bool = False
    server_name: str = get_config_value("server_name")
    while server_connected is False:
        try:
            conn: pyodbc.Connection = connect_to_server(server_name)
            cursor: pyodbc.Cursor = conn.cursor()
            server_connected = True
        except pyodbc.Error as ex:
            print(ex.args[0] + ": Server connection error, is the server name correct?")
            server_name = input("Enter Server Name: ")

    database_connected: bool = False
    database_name: str = get_config_value("database_name")
    while database_connected is False:
        try:
            cursor.execute('USE ' + database_name)
            database_connected = True
        except pyodbc.Error as ex:
            print(ex.args[0] + ": Server connection error, is the database name correct?")
            database_name = input("Enter Database Name: ")

    return conn, cursor


def connect_to_server(server) -> pyodbc.Connection:
    '''Returns the server connection.
            Parameters:
                    server (string): The server in which the database is stored on
            Returns:
                    connection (pyodbc.Connection): Server connection'''

    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=' + server + ';'
                      'Trusted_Connection=yes;')
    return conn


if __name__ == "__main__":
    main()
