__author__ = 'Ahmad Al-Sajid'
from tkinter import messagebox
import mysql.connector as sqlcon
from mysql.connector import errorcode
from Query import *


class LibDB:
    def __init__(self):
        self.qry = Query()
        try:
            self.db = sqlcon.connect(user='library',password = '123456', host = 'localhost', database = 'libmansysdata')
            self.cursor = self.db.cursor()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS ADMIN( USERNAME VARCHAR(50),"
                                "PASSWORD VARCHAR(50)"
                                ")ENGINE=InnoDB")

            self.cursor.execute("CREATE TABLE IF NOT EXISTS STUDENT( REGISTRATION INT PRIMARY KEY NOT NULL,"
                           "STUDENT_NAME VARCHAR(50),"
                           "YEARS VARCHAR(6),"
                           "SEMESTER VARCHAR(10),"
                           "CONTACT VARCHAR (15) DEFAULT '',"
                           "BORROW_NUMBER INT DEFAULT 0)ENGINE=InnoDB")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS BOOK ( BOOK_ID INT(6) ZEROFILL NOT NULL AUTO_INCREMENT,"
                           "BOOK_TITLE VARCHAR(50),"
                           "AUTHOR VARCHAR(50),"
                           "EDITION VARCHAR(50),"
                           "ISBN VARCHAR(50),"
                           "CATEGORY VARCHAR(50),"
                           "AVAILABILITY VARCHAR(20) DEFAULT 'AVAILABLE',"
                           "PRIMARY KEY (BOOK_ID))ENGINE=InnoDB")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS BORROWER_LIST ( BORROW_NUMBER INT(10) ZEROFILL NOT NULL AUTO_INCREMENT,"
                           "BOOK_ID INT,"
                           "REGISTRATION INT,"
                           "BORROW_DATE DATE,"
                           "RETURN_DATE DATE,"
                           "PRIMARY KEY (BORROW_NUMBER))ENGINE=InnoDB")
            self.cursor.close()
            self.db.close()
        except sqlcon.Error as err:
            messagebox.showinfo('Warning','Error in database!!\n'+str(err))


    def add_info(self, sql, values):
        self.sql = sql
        self.values = values
        self.db = sqlcon.connect(user='library',password = '123456', host = 'localhost', database = 'libmansysdata')
        self.cursor = self.db.cursor()
        self.cursor.execute(self.sql, self.values)

        if self.sql == self.qry.borrow_book:  # in case of borrowing books
            self.cursor.execute("SELECT BORROW_NUMBER  FROM BORROWER_LIST ORDER BY `BORROW_NUMBER`  DESC limit 1")
            self.last_borrow_id = self.cursor.fetchone()
            self.cursor.execute(self.qry.update_student_borrow_book, (self.last_borrow_id[0],self.values[1]))
            self.cursor.execute(self.qry.update_borrowed_book_not_available,(self.values[0],))
        self.db.commit()
        self.cursor.close()
        self.db.close()


    def retrieve_info(self, sql, value=()):
        self.sql = sql
        self.db = sqlcon.connect(user='library',password = '123456', host = 'localhost', database = 'libmansysdata')
        self.cursor = self.db.cursor()
        self.cursor.execute(self.sql, value)
        self.rows = self.cursor.fetchall()
        self.cursor.close()
        self.db.close()
        return self.rows


    def update_return_book_info(self, values):
        self.values = values  # [book_id, registration, date]
        self.db = sqlcon.connect(user='library',password = '123456', host = 'localhost', database = 'libmansysdata')
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT BORROW_NUMBER FROM STUDENT WHERE REGISTRATION = %s",(self.values[1],))
        self.temp_brw = self.cursor.fetchall()
        self.cursor.execute("UPDATE BORROWER_LIST SET RETURN_DATE = %s WHERE BORROW_NUMBER  = '%s'",(self.values[2],self.temp_brw[0][0]))
        self.cursor.execute("UPDATE BOOK SET AVAILABILITY = 'AVAILABLE' WHERE BOOK_ID = '%s'",(self.values[0],))
        self.cursor.execute("UPDATE STUDENT SET BORROW_NUMBER = 0 WHERE REGISTRATION = '%s'",(self.values[1],))

        self.db.commit()
        self.cursor.close()
        self.db.close()


    def default_user_password(self):
        self.db = sqlcon.connect(user='library',password = '123456', host = 'localhost', database = 'libmansysdata')
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT * FROM ADMIN LIMIT 1")
        self.check = self.cursor.fetchall()
        if not self.check:
            self.cursor.execute("INSERT INTO ADMIN(USERNAME, PASSWORD) VALUES('admin', '123456')")
        self.db.commit()
        self.cursor.close()
        self.db.close()







