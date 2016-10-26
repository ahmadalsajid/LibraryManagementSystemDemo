#                                     LIBRARY MANAGEMENT SYSTEM
						                                    v.1.0.0


For running this software, you first need to install XAMPP and mysql.connector to connect data base to python.

Before running the sowtware for the first time, a user and database is needed to be created in phpmyadmin() or
in localhost with database name "libmansysdata" and collasion as "utf_general_ci"

It is also needed to create a user "library" with password "123456" with all user privileges.

Unfortunately, before running this software, XMAPP server is needed to be started and Apache and MySQL is 
needed to be started.

Extract the folder "Library management system demo.rar" and run "LibraryGUI.exe" inside it.
Default username and password are "admin" & "123456", use it to login to the library management system.

Features:
    - Student info
	- Add student information : Fill the entry fields and hit enter or click submit button.
		
	- Edit student information: Enter a valid student registration number in registration field and hit
 				    enter to retrieve the informations of the desired students information to
				    specific fields. Then edit the necessary information and click submit to 
				    edit student's information.

	- Student details         : This feature will display all the students detailed information serially.


    - Book info
	- Add new book		  : Fill the entry fields and hit enter or click submit button.
	- Edit book information   : Enter a valid book serial number in Book ID field and hit
                  		    enter to retrieve the informations of the desired book information to 
				    specific fields. Then edit the necessary informations and click submit to
    			    	    edit book's information.

	- Book list		  : This feature will display all the books detailed informations serially.


    - Search
	- Search book		  : select search category and input desired information to search and hit
 				    enter.

	- Search student	  : Enter valid student registration and the detailed information of student
			    	    will appear on the screen.


    -Borrow
	- Borrow book		  : Enter valid student registration number and valid book ID to borrow the
 				    book.

	- Return book		  : Enter valid student registration number and valid book ID to borrow the
			    	    book.

	- Borrower list		  : This list will show all the borrowing history.


    - setting
	- Change username	  : User can change default username here.

	- Change password	  : User can change default password here.


    - Help
	- About			  : Information about this software.
	- Guide			  : Useful information to use this software.

