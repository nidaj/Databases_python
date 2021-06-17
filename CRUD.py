
from mysql.connector.cursor import MySQLCursor
from logger_config import logger
import mysql.connector
log = logger.get_logger()
class CRUD:
    def __init__(self,host,user,passwd,database) :
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.connection()
        
    def connection(self):
        '''
        Description: 
        Parameter:
        Return:
        '''
        try:
            mydb = mysql.connector.connect(
                host = self.host,
                user = self.user,
                passwd = self.passwd,
                database = self.database
            )
           
            if(mydb):
                log.info("Connection Successfull")
            self.db = mydb
            # else:
            # log.error('Connection error')
        except:
            log.error("Connection error")

        
    def show_tables(self):
        '''
        Description: 
        Parameter:
        Return:
        '''
        try:
            mycursor = self.db.cursor()
            mycursor.execute('SHOW TABLES')
            tables = mycursor.fetchall()
            log.info(f'The tables in database {self.database} are:')
            for tb in tables:
                log.info(f'{tb[0]}')
        except:
            log.error('Show tables Unsuccessful')
        
    def create_table(self):
        '''
        Description: 
        Parameter:
        Return:
        '''
        try:
            self.show_tables()
            mycursor = self.db.cursor()
            table_name = input("Enter the table name: ")
            mycursor.execute("CREATE TABLE "+table_name+" (Roll_no INTEGER(10) unsigned NOT NULL ,Name VARCHAR(50),PRIMARY KEY(Roll_no),percentage float(10))")
            self.db.commit()
            log.info(f'{table_name} successfully Table created')
        except:
            log.error('create table unsuccesful')
    def insert(self,table_name):
        '''
        Description: 
        Parameter:
        Return:
        '''
        try:
            s_name = input('Enter name :')
            roll_no = int(input('Enter roll no: '))
            percent = float(input('Enter the percentage marks: '))
            mycursor = self.db.cursor()
            mycursor.execute('INSERT INTO {self.table_name} values ({s_name},{roll_no},{percent})')
            self.db.commit()
            log.info(f'Entry added to {table_name}')
        except:
            log.error(f'Could not add entries to {table_name}')

        
    def update(self,table_name):
        '''
        Description: 
        Parameter:
        Return:
        '''
        try:
            roll_no = int(input("Update by Roll no: "))
            name = input("Enter name: ")
            percent = float(input("Enter Percentage: "))

            
            cursor = self.db.cursor()

            cursor.execute(f"UPDATE {table_name} SET Name={name}, percentage = {percent}WHERE Roll_no = {roll_no}")

            self.db.commit()
            log.info(f"Entered: {roll_no}, {name}, {percent}")
            log.info(f"{cursor.rowcount()}record updated")
        except:
            log.error("Update aborted")        

    def delete(self):
        '''
        Description: 
        Parameter:
        Return:
        '''
        try:
            mycursor = self.db.cursor()
            table_name = input("Enter the table name: ")
            roll_no = input('Enter the roll number to be deleted')
            mycursor.execute(f'DELETE FROM {table_name}WHERE Roll_no = '+roll_no+'')
            self.db.commit()
            log.info(f'Entry deleted from {table_name}')
        except:
            log.error(f'Entry couldnot be deleted')

    def drop_table(self):
        '''
        Description: 
        Parameter:
        Return:
        '''
        try:
            mycursor = self.db.cursor()
            table_name = input('Enter the table to be dropped: ')
            mycursor.execute(f'DROP TABLE {table_name}')
            self.db.commit()
            log.info(f'{table_name} DROPPED')
        except:
            log.error('DROP table unsuccesful')
        
    
        

