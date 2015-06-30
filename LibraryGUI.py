__author__ = 'Ahmad Al-Sajid'
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from DataBase import *
from Query import *


class LIbraryGUI:
    def __init__(self, root):
        self.root = root
        self.style = ttk.Style()
        self.style.configure('Tmenu', background='#e1d8b9')
        self.style.configure('TFrame', background='#e1d8b9')
        self.style.configure('TButton', background='#e1d8b9')
        self.style.configure('TLabel', background='#e1d8b9', font=('Arial', 11))
        self.style.configure('Header.TLabel', font=('Arial', 28, 'bold'))
        self.db = LibDB()
        self.db.default_user_password()
        self.query = Query()


        self.login_screen()


    def create_frames(self):
        self.frame_header = ttk.Frame(self.root)
        self.frame_header.pack()

        self.separator = ttk.Frame(self.root,height=50)
        self.separator.pack()

        self.frame_content = ttk.Frame(self.root)
        self.frame_content.pack()

    # disable previous frames to allocate new options
    def disable_frame(self):
        self.frame_header.destroy()
        self.separator.destroy()
        self.frame_content.destroy()

    def login_screen(self):
        self.create_frames()

        # create and use logo
        self.logo = PhotoImage(file='UAp_logo.gif').subsample(3, 3)
        ttk.Label(self.frame_header, image=self.logo).grid(row=0, column=0)
        ttk.Label(self.frame_header, text='Library Management System', style='Header.TLabel').grid(row=0, column=1)

        # prompt username
        ttk.Label(self.frame_content, text='Username :').grid(row=0, column=0, padx=5, sticky='s')
        ttk.Label(self.frame_content).grid(row=1, column=0, padx=5, sticky='s')  # create distance
        self.entry_name = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.entry_name.grid(row=0, column=1, columnspan=2, padx=5, sticky='s')
        self.entry_name.bind("<Return>",self.submit)

        # prompt password
        ttk.Label(self.frame_content, text='Password :').grid(row=2, column=0, padx=5, sticky='s')
        ttk.Label(self.frame_content).grid(row=3, column=0, padx=5, sticky='s')  # create distance
        self.entry_password = ttk.Entry(self.frame_content, show='*', width=30, font=('Arial', 11))
        self.entry_password.grid(row=2, column=1, columnspan=2, padx=5, sticky='e')
        self.entry_password.bind("<Return>",self.submit)

        ttk.Button(self.frame_content, text='Submit',
                   command= self.submit).grid(row=4, column=1, padx=5, pady=5, sticky='e')
        ttk.Button(self.frame_content, text='Clear',
                   command=self.clear).grid(row=4, column=2, padx=5, pady=5, sticky='w')

    # submit button calls this function to enter main window
    def submit(self,event = NONE):
        self.username = self.db.retrieve_info(self.query.username_db)
        self.password = self.db.retrieve_info(self.query.password_db)

        if self.entry_name.get() != self.username[0][0] or self.entry_password.get() != self.password[0][0]:
            messagebox.showinfo('Access Denied', 'You have entered wrong username or password\nPlease try again')
            self.clear()
        else:
            self.success_login()

    # cancel button calls this function to clear the username and password field
    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_password.delete(0, 'end')

    # after login, menu bar will appear
    def success_login(self):
        self.menus()  # add menu to window
        self.disable_frame()
        self.create_frames()
        ttk.Label(self.frame_header, text='Welcome to Library of CSE, UAP', style='Header.TLabel').grid(row=0,
                                                                                                             column=1)

    # menu buttons
    def menus(self):
        # creating menu
        self.menubar = Menu(self.root)

        # create a pulldown menu for student details, and add it to the menu bar
        student = Menu(self.menubar, tearoff=0)
        student.add_command(label="Add Student Information", command= self.add_student_information)
        student.add_command(label="Edit Student Information", command= self.edit_student_information)
        #student.add_separator()
        student.add_command(label="Student Details", command= self.student_details)
        self.menubar.add_cascade(label="Student Info", menu=student)

        # create a pulldown menu for books details, and add it to the menu bar
        book_info = Menu(self.menubar, tearoff=0)
        book_info.add_command(label="Add New Book", command=  self.add_new_book)
        book_info.add_command(label="Edit Book Information", command=  self.edit_book_information)
        book_info.add_command(label="Book List", command=  self.book_list)
        self.menubar.add_cascade(label="Book Info", menu=book_info)

        # create a pulldown menu for searching information, and add it to the menu bar
        search_book = Menu(self.menubar, tearoff=0)
        search_book.add_command(label="Search Book", command=  self.search_book)
        search_book.add_command(label="Search Student", command=  self.single_student_details)
        # search_book.add_command(label="Book Information", command=  self.book_information(root))
        #search_book.add_command(label="Borrower Information", command=  self.borrower_information)
        #search_book.add_separator()
        self.menubar.add_cascade(label="Search", menu=search_book)

        # create a pulldown menu for borrow details, and add it to the menu bar
        borrow_info = Menu(self.menubar, tearoff=0)
        borrow_info.add_command(label="Borrow Book", command=  self.borrow_book)
        borrow_info.add_command(label="Return Book", command=  self.return_book)
        #borrow_info.add_separator()
        borrow_info.add_command(label="Borrower List", command=  self.borrower_list)
        self.menubar.add_cascade(label="Borrow", menu=borrow_info)

        # create a pulldown menu for Updating username/Password, and add it to the menu bar
        setting = Menu(self.menubar, tearoff=0)
        setting.add_command(label="Change Username", command=  self.change_username)
        setting.add_command(label="Change Password", command=  self.change_password)
        self.menubar.add_cascade(label="Setting", menu=setting)
        self.root.config(menu=self.menubar)

        # create a pulldown menu for Updating help menu, and add it to the menu bar
        help_ = Menu(self.menubar, tearoff=0)
        help_.add_command(label="About", command=  self.about)
        help_.add_command(label="Guide", command=  self.guide)
        self.menubar.add_cascade(label="Help", menu=help_)
        self.root.config(menu=self.menubar)

    def add_student_information(self):
        self.disable_frame()
        self.create_frames()
        ttk.Label(self.frame_header, text='Add student details to database', style='Header.TLabel').grid(row=0,
                                                                                                         column=1)
        #input name
        ttk.Label(self.frame_content, text='Student Name :').grid(row=0, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=1, column=0, padx=5, sticky='s')  # create distance
        self.entry_name = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.entry_name.grid(row=0, column=1, columnspan=2, padx=5, sticky='s')
        self.entry_name.bind("<Return>",self.submit_add_student_information)

        #input registration
        ttk.Label(self.frame_content, text='Registration NO. :').grid(row=2, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=3, column=0, padx=5, sticky='s')  # create distance
        self.entry_registration = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.entry_registration.grid(row=2, column=1, columnspan=2, padx=5, sticky='s')
        self.entry_registration.bind("<Return>",self.submit_add_student_information)

        #input year
        ttk.Label(self.frame_content, text='Year :').grid(row=4, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=5, column=0, padx=5, sticky='s')  # create distance
        year = IntVar()  # declared to input variable of year
        self.spinbox_year = Spinbox(self.frame_content, from_=1990, to=2090, textvariable=year, width=28,
                                    font=('Arial', 11))
        self.spinbox_year.grid(row=4, column=1, columnspan=2, padx=5, sticky='s')
        self.spinbox_year.bind("<Return>",self.submit_add_student_information)

        #input semester
        ttk.Label(self.frame_content, text='Semester :').grid(row=6, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=7, column=0, padx=5, sticky='s')  # create distance
        month = StringVar()  # declared to input variable of semester
        self.dropdown_semester = ttk.Combobox(self.frame_content, textvariable=month, width=28, font=('Arial', 11))
        self.dropdown_semester.config(values=('SPRING', 'FALL'))
        self.dropdown_semester.state(['readonly'])
        self.dropdown_semester.grid(row=6, column=1, columnspan=2, padx=5, sticky='s')
        self.dropdown_semester.bind("<Return>",self.submit_add_student_information)

        #input contact name
        ttk.Label(self.frame_content, text='Contact NO :').grid(row=8, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=9, column=0, padx=5, sticky='s')  # create distance
        self.entry_contact = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.entry_contact.grid(row=8, column=1, columnspan=2, padx=5, sticky='s')
        self.entry_contact.bind("<Return>",self.submit_add_student_information)

        #submit info
        ttk.Button(self.frame_content, text='Submit',
                   command=  self.submit_add_student_information).grid(row=10, column=1, padx=5, pady=5,
                                                                                   sticky='w')
        #cancel info
        ttk.Button(self.frame_content, text='Clear',
                   command=self.clear_add_edit_student_information).grid(row=10, column=1, padx=5, pady=5, sticky='e')

    def edit_student_information(self):
        self.disable_frame()
        self.create_frames()

        ttk.Label(self.frame_header, text='Edit Student Information', style='Header.TLabel').grid(row=0, column=1)

        #input registration
        ttk.Label(self.frame_content, text='Registration NO. :').grid(row=0, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=3, column=0, padx=5, sticky='s')  # create distance
        self.entry_registration = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.entry_registration.grid(row=0, column=1, columnspan=2, padx=5, sticky='s')
        self.entry_registration.bind("<Return>",self.fetch_data_to_edit_student_information)

        #input name
        ttk.Label(self.frame_content, text='Student Name :').grid(row=2, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=1, column=0, padx=5, sticky='s')  # create distance
        self.entry_name = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.entry_name.grid(row=2, column=1, columnspan=2, padx=5, sticky='s')
        self.entry_name.bind("<Return>",self.submit_edit_student_information)

        #input year
        ttk.Label(self.frame_content, text='Year :').grid(row=4, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=5, column=0, padx=5, sticky='s')  # create distance
        year = StringVar()  # declared to input variable of year
        self.spinbox_year = Spinbox(self.frame_content, from_=1990, to=2090, textvariable=year, width=28,
                                    font=('Arial', 11))
        self.spinbox_year.grid(row=4, column=1, columnspan=2, padx=5, sticky='s')
        self.spinbox_year.bind("<Return>",self.submit_edit_student_information)

        #input semester
        ttk.Label(self.frame_content, text='Semester :').grid(row=6, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=7, column=0, padx=5, sticky='s')  # create distance
        month = StringVar()  # declared to input variable of semester
        self.dropdown_semester = ttk.Combobox(self.frame_content, textvariable=month, width=28, font=('Arial', 11))
        self.dropdown_semester.config(values=('SPRING', 'FALL'))
        self.dropdown_semester.grid(row=6, column=1, columnspan=2, padx=5, sticky='s')
        self.dropdown_semester.bind("<Return>",self.submit_edit_student_information)

        #input contact name
        ttk.Label(self.frame_content, text='Contact NO :').grid(row=8, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=9, column=0, padx=5, sticky='s')  # create distance
        self.entry_contact = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.entry_contact.grid(row=8, column=1, columnspan=2, padx=5, sticky='s')
        self.entry_contact.bind("<Return>",self.submit_edit_student_information)

        #submit info
        ttk.Button(self.frame_content, text='Submit',
                   command=  self.submit_edit_student_information).grid(row=10, column=1, padx=5, pady=5,
                                                                                   sticky='w')
        #cancel info
        ttk.Button(self.frame_content, text='Clear',
                   command=self.clear_add_edit_student_information).grid(row=10, column=1, padx=5, pady=5, sticky='e')

    #done
    def student_details(self):
        self.disable_frame()
        self.create_frames()
        ttk.Label(self.frame_header, text='Students details', style='Header.TLabel').grid(row=0, column=1)

        self.treeview_student_details = ttk.Treeview(self.frame_content)
        self.treeview_student_details.grid(row=0, column=0, rowspan=10, columnspan=6) #, padx=5, pady=5
        self.column_name = ( 'Registration', 'year', 'Semester', 'Contact No')
        self.treeview_student_details.config(columns=( 'Registration', 'year', 'Semester', 'Contact No'))
        self.treeview_student_details.config(height=15)
        self.yscroll = ttk.Scrollbar(self.frame_content,orient = VERTICAL, command = self.treeview_student_details.yview)
        self.treeview_student_details.config(yscrollcommand = self.yscroll.set)
        self.yscroll.grid(row = 0, column = 11, rowspan = 10, sticky = 'ns')

        for col_name in self.column_name:
            self.treeview_student_details.column(col_name, width=190, anchor='center')

        self.treeview_student_details.heading('#0', text='Name')

        for col_name in self.column_name:
            self.treeview_student_details.heading(col_name, text=col_name)

        # ADD DATA TO TABLE
        self.student_info = self.db.retrieve_info(self.query.student_details)
        for i, row in enumerate(self.student_info):
            self.treeview_student_details.insert('',i,text = row[1],values =(row[0],row[2], row[3], row[4]))

    #done
    def add_new_book(self):
        self.disable_frame()
        self.create_frames()

        ttk.Label(self.frame_header, text='Add Book details to database', style='Header.TLabel').grid(row=0, column=1)

        #input book title
        ttk.Label(self.frame_content, text='Book Title :').grid(row=0, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=1, column=0, padx=5, sticky='s')  # create distance
        self.book_title = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.book_title.grid(row=0, column=1, columnspan=2, padx=5, sticky='s')
        self.book_title.bind("<Return>",self.submit_add_new_book)

        #input book author
        ttk.Label(self.frame_content, text='Author Name :').grid(row=2, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=3, column=0, padx=5, sticky='s')  # create distance
        self.book_author = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.book_author.grid(row=2, column=1, columnspan=2, padx=5, sticky='s')
        self.book_author.bind("<Return>",self.submit_add_new_book)

        #input book edition
        ttk.Label(self.frame_content, text='Book Edition :').grid(row=4, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=5, column=0, padx=5, sticky='s')  # create distance
        self.book_edition = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.book_edition.grid(row=4, column=1, columnspan=2, padx=5, sticky='s')
        self.book_edition.bind("<Return>",self.submit_add_new_book)

        #input book ISBN
        ttk.Label(self.frame_content, text='ISBN No. :').grid(row=6, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=7, column=0, padx=5, sticky='s')  # create distance
        self.book_ISBN = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.book_ISBN.grid(row=6, column=1, columnspan=2, padx=5, sticky='s')
        self.book_ISBN.bind("<Return>",self.submit_add_new_book)

        #input book Category
        ttk.Label(self.frame_content, text='Category :').grid(row=8, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=9, column=0, padx=5, sticky='s')  # create distance
        self.book_Category = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.book_Category.grid(row=8, column=1, columnspan=2, padx=5, sticky='s')
        self.book_Category.bind("<Return>",self.submit_add_new_book)

        ttk.Label(self.frame_content).grid(row=9, column=0, padx=50, sticky='s')  # create distance

        #submit book info
        ttk.Button(self.frame_content, text='Submit',
                   command=  self.submit_add_new_book).grid(row=10, column=1, padx=5, pady=5,
                                                                                   sticky='w')
        #cancel book info
        ttk.Button(self.frame_content, text='Clear',
                   command=self.clear_add_new_book).grid(row=10, column=1, padx=5, pady=5, sticky='e')

    def edit_book_information(self):
        self.disable_frame()
        self.create_frames()
        ttk.Label(self.frame_header, text='Edit Book Information', style='Header.TLabel').grid(row=0, column=1)

        #select book id
        ttk.Label(self.frame_content, text='Book ID :').grid(row=0, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=1, column=0, padx=5, sticky='s')  # create distance
        self.book_id = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.book_id.grid(row=0, column=1, columnspan=2, padx=5, sticky='s')
        self.book_id.bind("<Return>",self.fetch_data_to_edit_book_information)

        #input book title
        ttk.Label(self.frame_content, text='Book Title :').grid(row=2, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=3, column=0, padx=5, sticky='s')  # create distance
        self.book_title = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.book_title.grid(row=2, column=1, columnspan=2, padx=5, sticky='s')
        self.book_title.bind("<Return>",self.submit_edit_book_information)

        #input book author
        ttk.Label(self.frame_content, text='Author Name :').grid(row=4, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=5, column=0, padx=5, sticky='s')  # create distance
        self.book_author = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.book_author.grid(row=4, column=1, columnspan=2, padx=5, sticky='s')
        self.book_author.bind("<Return>",self.submit_edit_book_information)

        #input book edition
        ttk.Label(self.frame_content, text='Book Edition :').grid(row=6, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=7, column=0, padx=5, sticky='s')  # create distance
        self.book_edition = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.book_edition.grid(row=6, column=1, columnspan=2, padx=5, sticky='s')
        self.book_edition.bind("<Return>",self.submit_edit_book_information)

        #input book ISBN
        ttk.Label(self.frame_content, text='ISBN No. :').grid(row=8, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=9, column=0, padx=5, sticky='s')  # create distance
        self.book_ISBN = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.book_ISBN.grid(row=8, column=1, columnspan=2, padx=5, sticky='s')
        self.book_ISBN.bind("<Return>",self.submit_edit_book_information)

        #input book Category
        ttk.Label(self.frame_content, text='Category :').grid(row=10, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=11, column=0, padx=5, sticky='s')  # create distance
        self.book_Category = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.book_Category.grid(row=10, column=1, columnspan=2, padx=5, sticky='s')
        self.book_Category.bind("<Return>",self.submit_edit_book_information)

        #submit book info
        ttk.Button(self.frame_content, text='Submit',
                   command=  self.submit_edit_book_information).grid(row=12, column=1,padx=5, pady=5,
                                                                                   sticky='w')
        #cancel book info
        ttk.Button(self.frame_content, text='Clear',
                   command=self.clear_edit_book_information).grid(row=12, column=1, padx=5, pady=5, sticky='e')

    #done
    def book_list(self):
        self.disable_frame()
        self.create_frames()
        ttk.Label(self.frame_header, text='Detailed Book List', style='Header.TLabel').grid(row=0, column=1)
        self.treeview_book_list = ttk.Treeview(self.frame_content)
        self.treeview_book_list.grid(row=0, column=0, rowspan=10, columnspan=6)
        self.column_name = ('Book ID', 'Author', 'Edition','ISBN', 'Category','Availability')
        self.treeview_book_list.config(columns=('Book ID', 'Author', 'Edition','ISBN', 'Category','Availability'))
        self.treeview_book_list.config(height=15)
        self.yscroll = ttk.Scrollbar(self.frame_content,orient = VERTICAL, command = self.treeview_book_list.yview)
        self.treeview_book_list.config(yscrollcommand = self.yscroll.set)
        self.yscroll.grid(row = 0, column = 11, rowspan = 10, sticky = 'ns')

        for col_name in self.column_name:
            self.treeview_book_list.column(col_name, width=125, anchor='center')

        self.treeview_book_list.heading('#0', text='Title')

        for col_name in self.column_name:
            self.treeview_book_list.heading(col_name, text=col_name)

        self.book_info = self.db.retrieve_info(self.query.book_details)
        for i, row in enumerate(self.book_info):
            self.treeview_book_list.insert('',i,text = row[1],values =(str(row[0]).zfill(6),row[2], row[3], row[4],row[5],row[6]))


    def search_book(self):
        self.disable_frame()
        self.create_frames()
        ttk.Label(self.frame_header, text='Book Information', style='Header.TLabel').grid(row=0, column=1)

        ttk.Label(self.separator, text='Search book by :').grid(row=0, column=0, padx=5, sticky='e')
        #ttk.Label(self.separator).grid(row=1, column=0, padx=5, sticky='s')  # create distance
        month = StringVar()
        self.dropdown_search_key = ttk.Combobox(self.separator, textvariable=month, width=28, font=('Arial', 11))
        self.dropdown_search_key.config(values=('BOOK ID', 'BOOK TITLE','AUTHOR','ISBN','CATEGORY'))
        self.dropdown_search_key.state(['readonly'])
        self.dropdown_search_key.grid(row=0, column=1, padx=5, sticky='s')

        self.search_keyword = ttk.Entry(self.separator, width=30, font=('Arial', 11))
        self.search_keyword.grid(row=0, column=2, columnspan=2, padx=5, sticky='s')
        self.search_keyword.bind("<Return>",self.submit_search_book_information)

        #submit info
        ttk.Button(self.separator, text='Search',
                   command=  self.submit_search_book_information).grid(row=1, column=2, padx=5, pady=5,
                                                                                   sticky='w')
        #cancel info
        ttk.Button(self.separator, text='Clear',
                   command=  self.clear_search_book_information).grid(row=1, column=2, padx=5, pady=5,
                                                                                   sticky='e')
        #  show searched book info
        self.treeview_book_list = ttk.Treeview(self.frame_content)
        self.treeview_book_list.grid(row=0, column=0, rowspan=10, columnspan=6)
        self.column_name = ('Book ID', 'Author', 'Edition','ISBN', 'Category','Availability')
        self.treeview_book_list.config(columns=('Book ID', 'Author', 'Edition','ISBN', 'Category','Availability'))
        self.treeview_book_list.config(height=15)
        self.yscroll = ttk.Scrollbar(self.frame_content,orient = VERTICAL, command = self.treeview_book_list.yview)
        self.treeview_book_list.config(yscrollcommand = self.yscroll.set)
        self.yscroll.grid(row = 0, column = 11, rowspan = 10, sticky = 'ns')

        for col_name in self.column_name:
            self.treeview_book_list.column(col_name, width=125, anchor='center')

        self.treeview_book_list.heading('#0', text='Title')

        for col_name in self.column_name:
            self.treeview_book_list.heading(col_name, text=col_name)



    def single_student_details(self):
        self.disable_frame()
        self.create_frames()
        ttk.Label(self.frame_header, text='Student Information', style='Header.TLabel').grid(row=0, column=1)
        #input registration
        ttk.Label(self.separator, text='Student Registration :').grid(row=0, column=0, padx=5, sticky='e')
        ttk.Label(self.separator).grid(row=1, column=0, padx=5, sticky='s')  # create distance
        self.entry_registration = ttk.Entry(self.separator, width=30, font=('Arial', 11))
        self.entry_registration.grid(row=0, column=1, columnspan=2, padx=5, sticky='s')
        self.entry_registration.bind("<Return>", self.submit_search_single_student_information)
        #submit info
        ttk.Button(self.separator, text='Search',
                   command=  self.submit_search_single_student_information).grid(row=1, column=1, padx=5, pady=5,
                                                                                   sticky='e')
        #cancel info
        ttk.Button(self.separator, text='Clear',
                   command=  self.clear_single_student_information).grid(row=1, column=2, padx=5, pady=5,
                                                                                   sticky='w')
        ###############################  this is to show students information  ######################################
        #                                                                                                           #
        #                                                                                                           #
        self.treeview_single_student_details = ttk.Treeview(self.frame_content)
        self.treeview_single_student_details.grid(row=0, column=0, rowspan=2, columnspan=10, pady=20)
        self.column_name = ( 'Registration', 'year', 'Semester', 'Contact No')
        self.treeview_single_student_details.config(columns=( 'Registration', 'year', 'Semester', 'Contact No'))
        self.treeview_single_student_details.config(height=1)

        for col_name in self.column_name:
            self.treeview_single_student_details.column(col_name, width=190, anchor='center')

        self.treeview_single_student_details.heading('#0', text='Name')

        for col_name in self.column_name:
            self.treeview_single_student_details.heading(col_name, text=col_name)
        #                                                                                                           #
        #                                                                                                           #
        ###############################  this is to show students information  ######################################

        ###############################  this is to show borrow information  ######################################
        #                                                                                                         #
        #                                                                                                         #
        self.treeview_single_student_borrow_details = ttk.Treeview(self.frame_content)
        self.treeview_single_student_borrow_details.grid(row=4, column=0, rowspan=2, columnspan=10)
        self.column_name = ( 'Book ID','Borrow number','Borrow Date','Return Date')
        self.treeview_single_student_borrow_details.config(columns=( 'Book ID','Borrow number','Borrow Date','Return Date'))
        self.treeview_single_student_borrow_details.config(height=12)
        ################################ scroll bar ###########################################################
        self.yscroll = ttk.Scrollbar(self.frame_content,orient = VERTICAL, command = self.treeview_single_student_borrow_details.yview)
        self.treeview_single_student_borrow_details.config(yscrollcommand = self.yscroll.set)
        self.yscroll.grid(row = 4, column = 11, rowspan = 10, sticky = 'ns')

        for col_name in self.column_name:
            self.treeview_single_student_borrow_details.column(col_name, width=190, anchor='center')

        self.treeview_single_student_borrow_details.heading('#0', text='Book Title')

        for col_name in self.column_name:
            self.treeview_single_student_borrow_details.heading(col_name, text=col_name)
        #                                                                                                         #
        #                                                                                                         #
        ###############################  this is to show borrow information  ######################################

    # done
    def borrow_book(self):
        self.disable_frame()
        self.create_frames()

        ttk.Label(self.frame_header, text='Borrow Book', style='Header.TLabel').grid(row=0, column=1)

        #input registration
        ttk.Label(self.frame_content, text='Student Registration :').grid(row=0, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=1, column=0, padx=5, sticky='s')  # create distance
        self.registration = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.registration.grid(row=0, column=1, columnspan=2, padx=5, sticky='s')
        self.registration.bind("<Return>",self.submit_borrow_book)

        #input book id
        ttk.Label(self.frame_content, text='Book ID:').grid(row=2, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=3, column=0, padx=5, sticky='s')  # create distance
        self.book_id = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.book_id.grid(row=2, column=1, columnspan=2, padx=5, sticky='s')
        self.book_id.bind("<Return>",self.submit_borrow_book)

        #submit info
        ttk.Button(self.frame_content, text='Submit',
                   command=  self.submit_borrow_book).grid(row=10, column=1, padx=5, pady=5,
                                                                                   sticky='w')
        #cancel info
        ttk.Button(self.frame_content, text='Clear',
                   command=self.clear_borrow_return_book).grid(row=10, column=1, padx=5, pady=5, sticky='e')

    #done
    def return_book(self):
        self.disable_frame()
        self.create_frames()

        ttk.Label(self.frame_header, text='Return Book', style='Header.TLabel').grid(row=0, column=1)

        #input registration
        ttk.Label(self.frame_content, text='Student Registration :').grid(row=0, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=1, column=0, padx=5, sticky='s')  # create distance
        self.registration = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.registration.grid(row=0, column=1, columnspan=2, padx=5, sticky='s')
        self.registration.bind("<Return>",self.submit_return_book)

        #input book id
        ttk.Label(self.frame_content, text='Book ID:').grid(row=2, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=3, column=0, padx=5, sticky='s')  # create distance
        self.book_id = ttk.Entry(self.frame_content, width=30, font=('Arial', 11))
        self.book_id.grid(row=2, column=1, columnspan=2, padx=5, sticky='s')
        self.book_id.bind("<Return>",self.submit_return_book)

        #submit info
        ttk.Button(self.frame_content, text='Submit',
                   command=  self.submit_return_book).grid(row=10, column=1, padx=5, pady=5,
                                                                                   sticky='w')
        #cancel info
        ttk.Button(self.frame_content, text='Clear',
                   command=self.clear_borrow_return_book).grid(row=10, column=1, padx=5, pady=5, sticky='e')

    #done
    def borrower_list(self):
        self.disable_frame()
        self.create_frames()

        ttk.Label(self.frame_header, text='Borrower List', style='Header.TLabel').grid(row=0, column=1)

        self.treeview_borrower_list = ttk.Treeview(self.frame_content)
        self.treeview_borrower_list.grid(row=0, column=0, rowspan=10, columnspan=6)
        self.column_name = ('Registration','Borrow ID','Book ID','Book Name','Borrow Date','Return Date')
        self.treeview_borrower_list.config(columns=('Registration','Borrow ID','Book ID','Book Name','Borrow Date','Return Date'))
        self.treeview_borrower_list.config(height=15)
        ################ scroll bar   ########################################################################
        self.yscroll = ttk.Scrollbar(self.frame_content,orient = VERTICAL, command = self.treeview_borrower_list.yview)
        self.treeview_borrower_list.config(yscrollcommand = self.yscroll.set)
        self.yscroll.grid(row = 0, column = 11, rowspan = 10, sticky = 'ns')

        for col_name in self.column_name:
            self.treeview_borrower_list.column(col_name, width=125, anchor='center')

        self.treeview_borrower_list.heading('#0', text='Name')

        for col_name in self.column_name:
            self.treeview_borrower_list.heading(col_name, text=col_name)

        self.borrower_list_details = self.db.retrieve_info(self.query.borrower_list_details)
        #[name, reg, borrow_number, book id, title, borrow date, return date]
        for i, row in enumerate(self.borrower_list_details):
            self.treeview_borrower_list.insert('',i, text = row[0], values = (row[1],str(row[2]).zfill(10),str(row[3]).zfill(6),row[4],row[5],row[6]))


    #done
    def change_username(self):
        self.disable_frame()
        self.create_frames()
        ttk.Label(self.frame_header, text='Change Username', style='Header.TLabel').grid(row=0, column=1)

        #input CURRENT USERNAME
        ttk.Label(self.frame_content, text='Current Username :').grid(row=0, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=1, column=0, padx=5, sticky='s')  # create distance
        self.current_username_password = ttk.Entry(self.frame_content,show='*', width=30, font=('Arial', 11))
        self.current_username_password.grid(row=0, column=1, columnspan=2, padx=5, sticky='s')
        self.current_username_password.bind("<Return>", self.submit_change_username)

        #input NEW USERNAME
        ttk.Label(self.frame_content, text='New Username :').grid(row=2, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=3, column=0, padx=5, sticky='s')  # create distance
        self.new_username_password = ttk.Entry(self.frame_content,show='*', width=30, font=('Arial', 11))
        self.new_username_password.grid(row=2, column=1, columnspan=2, padx=5, sticky='s')
        self.new_username_password.bind("<Return>", self.submit_change_username)

        #input CONFIRM NEW USERNAME
        ttk.Label(self.frame_content, text='Confirm New Username :').grid(row=4, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=5, column=0, padx=5, sticky='s')  # create distance
        self.confirm_new_username_password = ttk.Entry(self.frame_content,show='*', width=30, font=('Arial', 11))
        self.confirm_new_username_password.grid(row=4, column=1, columnspan=2, padx=5, sticky='s')
        self.confirm_new_username_password.bind("<Return>", self.submit_change_username)

        #submit info
        ttk.Button(self.frame_content, text='Submit',
                   command=  self.submit_change_username).grid(row=6, column=1, padx=5, pady=5,
                                                                                   sticky='w')
        #cancel info
        ttk.Button(self.frame_content, text='Clear',
                   command=self.clear_change_username_password).grid(row=6, column=1, padx=5, pady=5, sticky='e')


    #done
    def change_password(self):
        self.disable_frame()
        self.create_frames()
        ttk.Label(self.frame_header, text='Change Password', style='Header.TLabel').grid(row=0, column=1)

        #input CURRENT password
        ttk.Label(self.frame_content, text='Current Password :').grid(row=0, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=1, column=0, padx=5, sticky='s')  # create distance
        self.current_username_password = ttk.Entry(self.frame_content,show='*', width=30, font=('Arial', 11))
        self.current_username_password.grid(row=0, column=1, columnspan=2, padx=5, sticky='s')
        self.current_username_password.bind("<Return>", self.submit_change_password)

        #input NEW password
        ttk.Label(self.frame_content, text='New Password :').grid(row=2, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=3, column=0, padx=5, sticky='s')  # create distance
        self.new_username_password = ttk.Entry(self.frame_content,show='*', width=30, font=('Arial', 11))
        self.new_username_password.grid(row=2, column=1, columnspan=2, padx=5, sticky='s')
        self.new_username_password.bind("<Return>", self.submit_change_password)

        #input CONFIRM NEW password
        ttk.Label(self.frame_content, text='Confirm New Password :').grid(row=4, column=0, padx=5, sticky='e')
        ttk.Label(self.frame_content).grid(row=5, column=0, padx=5, sticky='s')  # create distance
        self.confirm_new_username_password = ttk.Entry(self.frame_content,show='*', width=30, font=('Arial', 11))
        self.confirm_new_username_password.grid(row=4, column=1, columnspan=2, padx=5, sticky='s')
        self.confirm_new_username_password.bind("<Return>", self.submit_change_password)

        #submit info
        ttk.Button(self.frame_content, text='Submit',
                   command=  self.submit_change_password).grid(row=6, column=1, padx=5, pady=5,
                                                                                   sticky='w')
        #cancel info
        ttk.Button(self.frame_content, text='Clear',
                   command=self.clear_change_username_password).grid(row=6, column=1, padx=5, pady=5, sticky='e')


    def about(self):
        self.disable_frame()
        self.create_frames()
        ttk.Label(self.frame_header, text='Library Management System v1.0.0', style='Header.TLabel').grid(row=0,
                                                                                                          column=1)
        ttk.Label(self.frame_content, text='Created By:\n\n\n').grid(row=0, column=0,rowspan =3, padx=5, sticky='w')
        ttk.Label(self.frame_content).grid(row=1, column=0, padx=5, sticky='s')  # create distance

        ttk.Label(self.frame_content, text='Syeda Tasmiah Islam\nRegistration : 12201020\nDept. of CSE\nUniversity of Asia Pacific\n\n\n').grid(row=3, column=0,rowspan=4, padx=5, sticky='e')

        ttk.Label(self.frame_content, text='Ahmad Al-Sajid\nRegistration : 12201028\nDept. of CSE\nUniversity of Asia Pacific\n\n\n').grid(row=9, column=0,rowspan=4, padx=5, sticky='e')


    def guide(self):
        self.disable_frame()
        self.create_frames()
        ttk.Label(self.frame_header, text='Guide to use this software', style='Header.TLabel').grid(row=0, column=1)

        ttk.Label(self.frame_content, text='\nPlease read the "READ ME.TXT" file to learn more about this software').grid(row=0, column=0,rowspan =3, padx=5, sticky='w')


    
#########################################  submit button methods  #################################################
    #done
    def submit_add_student_information(self,event = NONE):
        self.name = self.entry_name.get()
        self.reg =  self.entry_registration.get()
        self.year = self.spinbox_year.get()
        self.sem = self.dropdown_semester.get()
        self.con = self.entry_contact.get()
        if self.con==NONE:
            self.con='NULL'
        if self.name=='' or self.reg=='' or self.sem=='':
            messagebox.showinfo('Warning','You can\'t leave fields empty')
        else:
            self.data = (int(self.reg),self.name,self.year,self.sem,self.con)
            self.db.add_info(self.query.add_student_info,self.data)
            self.clear_add_edit_student_information()
            messagebox.showinfo('Success','Successfully added student\'s details')

    def fetch_data_to_edit_student_information(self,event):
        self.temp_reg = int(self.entry_registration.get())
        self.valid_reg = self.db.retrieve_info(self.query.valid_student)
        self.tup_temp_reg = (self.temp_reg,)
        if self.tup_temp_reg not in self.valid_reg:
            messagebox.showinfo('Warning','Wrong registration number')
        else:
            self.student_details_info = self.db.retrieve_info(self.query.single_student_details,self.tup_temp_reg)
            #[reg, name, years, semester, contact, borrow number]
            self.entry_name.delete(0,'end')
            self.entry_name.insert(0,self.student_details_info[0][1])

            self.spinbox_year.destroy()
            self.year = StringVar()  # declared to input variable of year
            self.year.set(self.student_details_info[0][2])
            self.spinbox_year = Spinbox(self.frame_content, from_=1990, to=2090, textvariable=self.year, width=28,
                                        font=('Arial', 11))
            self.spinbox_year.grid(row=4, column=1, columnspan=2, padx=5, sticky='s')


            self.dropdown_semester.set(self.student_details_info[0][3])
            self.dropdown_semester.state(["readonly"])

            self.entry_contact.delete(0,'end')
            self.entry_contact.insert(0,self.student_details_info[0][4])


    def submit_edit_student_information(self,event = NONE):
        self.name = self.entry_name.get()
        self.reg =  self.entry_registration.get()
        self.year = int(self.spinbox_year.get())
        self.sem = self.dropdown_semester.get()
        self.con = self.entry_contact.get()
        if self.con==NONE:
            self.con='NULL'
        if self.name=='' or self.reg=='' or self.sem=='':
            messagebox.showinfo('Warning','You can\'t leave fields empty')
        else:
            self.data = (self.name,self.year,self.sem,self.con,int(self.reg))
            self.db.add_info(self.query.edit_student_info,self.data)
            self.clear_add_edit_student_information()
            messagebox.showinfo('Success','Successfully edited student\'s details')

      
    def submit_add_new_book(self,event = NONE):
        self.name = self.book_title.get()
        self.author = self.book_author.get()
        self.edition = self.book_edition.get()
        self.isbn = self.book_ISBN.get()
        self.category = self.book_Category.get()

        if self.name=='' or self.author=='' or self.edition=='' or self.isbn=='' or self.category=='':
            messagebox.showinfo('Warning','You can\'t leave fields empty')
        else:
            self.book_data = (self.name, self.author, self.edition, self.isbn, self.category)
            self.db.add_info(self.query.add_book_info,self.book_data)
            self.clear_add_new_book()
            messagebox.showinfo('Success','Successfully added book\'s details')


    def fetch_data_to_edit_book_information(self,event= NONE):
        self.temp_book = int(self.book_id.get())
        self.valid_book = self.db.retrieve_info(self.query.valid_book)
        self.tup_temp_book = (self.temp_book,)
        if self.tup_temp_book not in self.valid_book:
            messagebox.showinfo('Warning','Wrong book ID number')
        else:
            self.book_details_info = self.db.retrieve_info(self.query.single_book_details,self.tup_temp_book)
            #[book id, title, author, edition, isbn, category]
            self.book_title.delete(0,'end')
            self.book_title.insert(0,self.book_details_info[0][1])
            self.book_author.delete(0,'end')
            self.book_author.insert(0,self.book_details_info[0][2])
            self.book_edition.delete(0,'end')
            self.book_edition.insert(0,self.book_details_info[0][3])
            self.book_ISBN.delete(0,'end')
            self.book_ISBN.insert(0,self.book_details_info[0][4])
            self.book_Category.delete(0,'end')
            self.book_Category.insert(0,self.book_details_info[0][5])


    def submit_edit_book_information(self,event = NONE):
        #[book id, title, author, edition, isbn, category]
        self.title = self.book_title.get()
        self.author = self.book_author.get()
        self.editions = self.book_edition.get()
        self.isbn_num = self.book_ISBN.get()
        self.category = self.book_Category.get()
        self.id = self.book_id.get()
        if self.title=='' or self.author=='' or self.editions=='' or self.isbn_num=='' or self.category=='' or self.id=='':
            messagebox.showinfo('Warning','You can\'t leave fields empty')
        else:
            self.data = (self.title, self.author, self.editions, self.isbn_num, self.category, int(self.id))
            self.db.add_info(self.query.edit_book_info,self.data)
            self.clear_edit_book_information()
            messagebox.showinfo('Success','Successfully edited book details')

      
    def submit_borrow_book(self,event = NONE):
        self.registration_input =self.registration.get()
        self.book_id_input = self.book_id.get()

        if self.registration_input =='' or self.book_id_input =='':
            messagebox.showinfo('Warning','You can\'t leave fields empty')
        else:
            self.valid_reg = self.db.retrieve_info(self.query.valid_student)
            self.valid_book = self.db.retrieve_info(self.query.valid_book)
            self.temp_reg = (int(self.registration_input),)
            self.temp_book = (int(self.book_id_input),)

            if self.temp_reg not in self.valid_reg or self.temp_book not in self.valid_book:
                messagebox.showinfo('Warning','Wrong Registration or Book ID')
            else:
                self.already_borrowed_a_book = self.db.retrieve_info(self.query.already_borrowed_a_book, self.temp_reg)

                self.already_borrowed_by_student = self.db.retrieve_info(self.query.already_borrowed_by_student, self.temp_book)

                if self.already_borrowed_a_book[0][0] != 0:
                    messagebox.showinfo('Warning','This student already borrowed a book')
                elif self.already_borrowed_by_student[0][0]=="NOT AVAILABLE":
                    messagebox.showinfo('Warning','This book is already borrowed')
                else:
                    self.today = datetime.now().date()
                    self.data = (int(self.book_id_input),int(self.registration_input),self.today)
                    self.db.add_info(self.query.borrow_book,self.data)
                    self.clear_borrow_return_book()
                    messagebox.showinfo('Successful','The book is successfully borrowed')


    def submit_return_book(self,event = NONE):
        self.registration_input =self.registration.get()
        self.book_id_input = self.book_id.get()

        if self.registration_input =='' or self.book_id_input =='':
            messagebox.showinfo('Warning','You can\'t leave fields empty')
        else:
            self.valid_reg = self.db.retrieve_info(self.query.valid_student)
            self.valid_book = self.db.retrieve_info(self.query.valid_book)
            self.temp_reg = (int(self.registration_input),)
            self.temp_book = (int(self.book_id_input),)


            if self.temp_reg not in self.valid_reg or self.temp_book not in self.valid_book:
                messagebox.showinfo('Warning','Wrong Registration or Book ID')
            else:
                self.already_borrowed_a_book = self.db.retrieve_info(self.query.already_borrowed_a_book, self.temp_reg)
                self.already_borrowed_by_student = self.db.retrieve_info(self.query.already_borrowed_by_student, self.temp_book)

                if self.already_borrowed_a_book[0][0] == 0:
                    messagebox.showinfo('Warning','Student did not borrowed a book')
                elif self.already_borrowed_by_student[0][0]!="NOT AVAILABLE":
                    messagebox.showinfo('Warning','This book is not borrowed')
                else:
                    self.today = datetime.now().date()
                    self.data = (int(self.book_id_input),int(self.registration_input),self.today)
                    self.db.update_return_book_info(self.data)
                    self.clear_borrow_return_book()
                    messagebox.showinfo('Successful','The book is successfully returned')

     
    def submit_change_username(self,event = NONE):
        self.current_username = self.current_username_password.get()
        self.new_username = self.new_username_password.get()
        self.confirm_new_username = self.confirm_new_username_password.get()
        if self.current_username=='' or self.new_username=='' or self.confirm_new_username=='':
            messagebox.showinfo('Warning','You can\'t leave fields empty')
        elif self.new_username != self.confirm_new_username:
            messagebox.showinfo('Warning','New username does not match')
        else:
            self.current_username_on_db = self.db.retrieve_info(self.query.username_db)
            if self.current_username != self.current_username_on_db[0][0]:
                messagebox.showinfo('Warning','Wrong current username')
            else:
                self.db.add_info("UPDATE ADMIN SET USERNAME =%s",(self.new_username,))
                self.clear_change_username_password()
                messagebox.showinfo('Success','Successfully changed username')

     
    def submit_change_password(self,event = NONE):
        self.current_password = self.current_username_password.get()
        self.new_password = self.new_username_password.get()
        self.confirm_new_password = self.confirm_new_username_password.get()
        if self.current_password=='' or self.new_password=='' or self.confirm_new_password=='':
            messagebox.showinfo('Warning','You can\'t leave fields empty')
        elif self.new_password != self.confirm_new_password:
            messagebox.showinfo('Warning','New password does not match')
        else:
            self.current_password_on_db = self.db.retrieve_info(self.query.password_db)
            if self.current_password != self.current_password_on_db[0][0]:
                messagebox.showinfo('Warning','Wrong current password')
            else:
                self.db.add_info("UPDATE ADMIN SET PASSWORD =%s",(self.new_password,))
                self.clear_change_username_password()
                messagebox.showinfo('Success','Successfully changed password')

     
    def submit_search_single_student_information(self,event=NONE):
        self.registration = self.entry_registration.get()
        self.treeview_single_student_details.delete(*self.treeview_single_student_details.get_children())  # first clear the field
        self.treeview_single_student_borrow_details.delete(*self.treeview_single_student_borrow_details.get_children())
        if self.registration=='':
            messagebox.showinfo('Warning','You can\'t leave fields empty')
        else:
            self.valid_student = self.db.retrieve_info(self.query.valid_student)
            self.temp_reg = (int(self.registration),)
            if self.temp_reg not in self.valid_student:
                messagebox.showinfo('Warning','Wrong registration number')
            else:
                self.row = self.db.retrieve_info(self.query.single_student_details,self.temp_reg) #student_details_info
                self.treeview_single_student_details.delete(*self.treeview_single_student_details.get_children())  # first clear the field
                self.treeview_single_student_details.insert('',0,text = self.row[0][1],values=(self.row[0][0],self.row[0][2],self.row[0][3],self.row[0][4]))

                self.treeview_single_student_borrow_details.delete(*self.treeview_single_student_borrow_details.get_children())
                self.brwdtl= self.db.retrieve_info(self.query.single_student_borrowed_book,self.temp_reg)  # brwdtl = borrowed details
                #[book title, book id,borrow number, borrow date, return date]
                for i, row in enumerate(self.brwdtl):
                    self.treeview_single_student_borrow_details.insert('',i,text = row[0],values=(str(row[1]).zfill(6),str(row[2]).zfill(10),row[3],row[4]))


    def submit_search_book_information(self, event=NONE):
        self.keyword = self.dropdown_search_key.get()
        self.search_book_info = self.search_keyword.get()
        self.treeview_book_list.delete(*self.treeview_book_list.get_children())
        if self.keyword == '' or self.search_book_info =='':
            messagebox.showinfo('Warning','You can\'t leave fields empty')
        else:
            #('BOOK ID', 'BOOK TITLE','AUTHOR','edition','ISBN','CATEGORY','availability')
            if self.keyword=='BOOK ID':
                self.book_search_info = self.db.retrieve_info(self.query.search_book_by_book_id,(int(self.search_book_info),))
            elif self.keyword=='BOOK TITLE':
                self.book_search_info = self.db.retrieve_info(self.query.search_book_by_book_title,('%'+self.search_book_info+'%',))
            elif self.keyword=='AUTHOR':
                self.book_search_info = self.db.retrieve_info(self.query.search_book_by_author,('%'+self.search_book_info+'%',))
            elif self.keyword=='ISBN':
                self.book_search_info = self.db.retrieve_info(self.query.search_book_by_isbn,('%'+self.search_book_info+'%',))
            elif self.keyword=='CATEGORY':
                self.book_search_info = self.db.retrieve_info(self.query.search_book_by_category,('%'+self.search_book_info+'%',))

            if not self.book_search_info:
                messagebox.showinfo('Warning','No data found')
            else:

                for i, row in enumerate(self.book_search_info):
                    self.treeview_book_list.insert('',i,text = row[1],values = (str(row[0]).zfill(6),row[2],row[3],row[4],row[5],row[6]))


    #########################################  submit button methods end ###############################################

    ##################################### #clear button methods #######################################################
     
    def clear_add_edit_student_information(self):
        self.entry_name.delete(0,'end')
        self.entry_registration.delete(0,'end')
        self.spinbox_year.destroy()
        year = IntVar()  # declared to input variable of year
        self.spinbox_year = Spinbox(self.frame_content, from_=1990, to=2090, textvariable=year, width=28,
                                    font=('Arial', 11))
        self.spinbox_year.grid(row=4, column=1, columnspan=2, padx=5, sticky='s')
        self.dropdown_semester.state(["!readonly"])
        self.dropdown_semester.delete(0,'end')
        self.dropdown_semester.state(["readonly"])
        self.entry_contact.delete(0,'end')

     
    def clear_add_new_book(self):
        self.book_title.delete(0,'end')
        self.book_author.delete(0,'end')
        self.book_edition.delete(0,'end')
        self.book_ISBN.delete(0,'end')
        self.book_Category.delete(0,'end')

     
    def clear_edit_book_information(self):
        self.book_id.delete(0,'end')
        self.clear_add_new_book() # it clears other fields

     
    def clear_borrow_return_book(self):
        self.registration.delete(0,'end')
        self.book_id.delete(0,'end')

     
    def clear_single_student_information(self):
        self.entry_registration.delete(0,'end')
        self.treeview_single_student_details.delete(*self.treeview_single_student_details.get_children())  # first clear the field
        self.treeview_single_student_borrow_details.delete(*self.treeview_single_student_borrow_details.get_children())

     
    def clear_change_username_password(self):
        self.current_username_password.delete(0,'end')
        self.new_username_password.delete(0,'end')
        self.confirm_new_username_password.delete(0,'end')
            

    def clear_search_book_information(self):
        self.dropdown_search_key.state(["!readonly"])
        self.dropdown_search_key.delete(0,'end')
        self.dropdown_search_key.state(["readonly"])
        self.search_keyword.delete(0,'end')
        self.treeview_book_list.delete(*self.treeview_book_list.get_children())

##################################### #clear button methods ends #######################################################

def main():
    root = Tk()
    root.title('Library Management System')
    root.minsize(width=1000, height=500)
    root.maxsize(width=1000, height=500)
    root.iconbitmap('UAP_icon.ico')
    root.configure(background='#e1d8b9')
    lms = LIbraryGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()