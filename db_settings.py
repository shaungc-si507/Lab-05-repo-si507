import sqlite3 # https://docs.python.org/2/library/sqlite3.html
import pathlib
import os

DATABASE_FILE_NAME = 'chocolate_sources.sqlite'

def get_database():
    return sqlite3.connect(DATABASE_FILE_NAME)


class Database:
    def __init__(self, database_file_name=DATABASE_FILE_NAME):
        self.up(database_file_name)
    
    def run_sql_commands(self, commands=[]):
        for sql_command, *arg_tuple in commands:
            self.cursor.execute(sql_command, *arg_tuple)
        return self.connection.commit()
    
    def run_sql_command_many_data(self, sql_command, data_list=[]):
        print('hey ======')
        print(sql_command)
        self.cursor.executemany(sql_command, data_list)
        return self.connection.commit()
    
    def down(self):
        self.connection.close()
    
    def up(self, filename):
        file_path = pathlib.Path(filename)
        if file_path.exists():
            os.remove(file_path.absolute())
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()