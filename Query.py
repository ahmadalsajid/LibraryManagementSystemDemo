__author__ = 'Ahmad Al-Sajid'

class Query:
    def __init__(self):
        #SELECT STATEMENTS
        self.username_db = ("SELECT USERNAME FROM ADMIN")
        self.password_db = ("SELECT PASSWORD FROM ADMIN")
        self.student_details = ("SELECT * FROM STUDENT")
        self.single_student_details = ("SELECT * FROM STUDENT WHERE REGISTRATION = %s")
        self.single_book_details = ("SELECT * FROM BOOK WHERE BOOK_ID = %s")
        self.book_details = ("SELECT * FROM BOOK ORDER BY CATEGORY, BOOK_TITLE ASC")
        self.valid_student = ("SELECT REGISTRATION FROM STUDENT")
        self.valid_book = ("SELECT BOOK_ID FROM BOOK")
        self.already_borrowed_a_book = ("SELECT BORROW_NUMBER FROM STUDENT WHERE REGISTRATION = %s")

        self.search_book_by_book_id = ("SELECT * FROM BOOK WHERE BOOK_ID = %s")
        self.search_book_by_book_title = ("SELECT * FROM BOOK WHERE BOOK_TITLE LIKE %s")
        self.search_book_by_author = ("SELECT * FROM BOOK WHERE AUTHOR LIKE %s")
        self.search_book_by_isbn = ("SELECT * FROM BOOK WHERE ISBN LIKE %s")
        self.search_book_by_category = ("SELECT * FROM BOOK WHERE CATEGORY LIKE %s")


        self.already_borrowed_by_student = ("SELECT AVAILABILITY FROM BOOK WHERE BOOK_ID = %s")

        self.single_student_borrowed_book = ("""SELECT BOOK.BOOK_TITLE, BORROWER_LIST.BOOK_ID, BORROWER_LIST.BORROW_NUMBER,
                                                BORROWER_LIST.BORROW_DATE, BORROWER_LIST.RETURN_DATE FROM BORROWER_LIST
                                                JOIN BOOK ON BORROWER_LIST.BOOK_ID= BOOK.BOOK_ID WHERE BORROWER_LIST.REGISTRATION = %s
                                                ORDER BY BORROWER_LIST.BORROW_NUMBER ASC""")

        self.borrower_list_details = ("""SELECT STUDENT.STUDENT_NAME, STUDENT.REGISTRATION, BORROWER_LIST.BORROW_NUMBER,
                                  BORROWER_LIST.BOOK_ID, BOOK.BOOK_TITLE, BORROWER_LIST.BORROW_DATE,
                                  BORROWER_LIST.RETURN_DATE FROM STUDENT JOIN BORROWER_LIST ON
                                  STUDENT.REGISTRATION = BORROWER_LIST.REGISTRATION
                                  JOIN BOOK ON BORROWER_LIST.BOOK_ID = BOOK.BOOK_ID ORDER BY BORROWER_LIST.BORROW_NUMBER ASC""")



        #INSERT STATEMENTS
        self.add_student_info = ("INSERT INTO STUDENT(REGISTRATION, STUDENT_NAME ,YEARS, SEMESTER,CONTACT) VALUES (%s,%s,%s,%s,%s)")
        self.add_book_info = ("INSERT INTO BOOK(BOOK_ID, BOOK_TITLE,AUTHOR,EDITION,ISBN,CATEGORY) VALUES(NULL,%s,%s,%s,%s,%s)")
        self.borrow_book = ("INSERT INTO BORROWER_LIST(BORROW_NUMBER, BOOK_ID, REGISTRATION,BORROW_DATE) VALUES (NULL ,%s,%s,%s)")


        #UPDATE STATEMENTS
        self.update_student_borrow_book = ("UPDATE STUDENT SET BORROW_NUMBER = %s WHERE REGISTRATION = '%s'")
        self.update_borrowed_book_not_available = ("UPDATE BOOK SET AVAILABILITY = 'NOT AVAILABLE' WHERE BOOK_ID = '%s'")
        self.return_book = ("UPDATE BORROWER_LIST SET RETURN_DATE = %s BORROW_NUMBER WHERE  = '%s'")
        self.edit_student_info = ("UPDATE STUDENT SET STUDENT_NAME = %s, YEARS = %s,SEMESTER = %s,CONTACT = %s WHERE REGISTRATION = %s")
        self.edit_book_info = ("UPDATE BOOK SET BOOK_TITLE = %s,AUTHOR = %s,EDITION = %s,ISBN = %s,CATEGORY = %s WHERE BOOK_ID = %s")