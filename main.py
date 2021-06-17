from CRUD import CRUD
from logger_config import logger
log = logger.get_logger()

def crud_operation():
    '''
    Description:
    Performs CRUD Operation on MySql
    Parameter:
    None
    Return:
    None
    '''
    try:
        log.info("Start")
        user_input = ""
        connect = CRUD('localhost','root','','testdb')
        while user_input != 'q':
            print("1 - Create Table")
            print("2 - Drop Table")
            print("3 - Insert record to employee_table")
            print("4 - Update record from employee_table")
            print("5 - Delete record from employee_table")
            print("q - Quit")
            user_input = input("Select Option: ")

            if (user_input == "1"):
                log.info("Choosen to create a new table")
                connect.create_table()

            elif (user_input == "2"):
                log.info("Choosen to drop table")
                connect.drop_table()

            elif (user_input == "3"):
                table_name = input('Enter the table name: ')
                log.info("Choosen to insert record")
                connect.insert(table_name)

            elif (user_input == "4"):
                table_name = input('Enter the table name: ')
                log.info("Choosen to update record")
                connect.update(table_name)

            elif (user_input == "5"):
                log.info("Choosen to delete record")
                connect.delete()

            elif user_input == "q":
                log.info("Choosen to quit")
                break

            else:
                print("Please Select Proper Option")

    except:
        raise Exception("Program Stopped")

if __name__ == '__main__':
    crud_operation()
