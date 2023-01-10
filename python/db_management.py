'''This is for testing databases'''

import pandas as pd
import pyodbc
from utils import get_config_value, write_config_value, create_config
import os.path

# pylint: disable=c-extension-no-member,anomalous-backslash-in-string,global-statement,expression-not-assigned

CONN: object
CURSOR: object

def main():
    """Main function controlling the order of logic."""

    load_database() if os.path.isfile('config.txt') else create_config()


    #TODO: remove below and implement further
    CURSOR.execute('SELECT Name FROM Models')
    for i in CURSOR:
        print(i[0])
    output = pd.read_sql_query('SELECT * FROM Models', CONN)
    print(output)


def load_database():
    '''Retrieves server connection and loads database into global variables.'''

    #attempt server connection
    server_connected: bool = False
    server_name: str = get_config_value("server_name")
    while server_connected is False:
        try:
            global CONN
            global CURSOR
            CONN = pyodbc.Connection = connect_to_server(server_name)
            CURSOR = CONN.cursor()
            server_connected = True
        except pyodbc.Error as ex:
            print(ex.args[0] + ": Server connection error, is the server name correct?")
            server_name = input("Enter Server Name: ")
            write_config_value("server_name", server_name)

    #attempt database connection
    database_connected: bool = False
    database_name: str = get_config_value("database_name")
    while database_connected is False:
        try:
            CURSOR.execute('USE ' + database_name)
            database_connected = True
        except pyodbc.Error as ex:
            print(ex.args[0] + ": Server connection error, is the database name correct?")
            database_name = input("Enter Database Name: ")
            write_config_value("database_name", database_name)


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
