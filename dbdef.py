import sqlite3
import json
from tkinter import *
from tkinter import messagebox
import tkinter as Tk
from tkinter import *
from tkinter import messagebox
from tkinter import END
import sqlite3
import re




#=============================================================================================================================================================================================================================================================================
def data_format_registration(self, entry_widgets):
    """
    This function formats the data from registration entries.
    It takes in an array of entry_widgets from the registration page and formats the data.
    It strips trailing whitespaces and capitalizes the first letter of the data.
    """
    for self.entry_widget in self.entry_widgets:
        text = self.entry_widget.get()
        text = text.rstrip()
        self.entry_widget.delete(0, 'end')
        self.entry_widget.insert(0, text)

    for self.entry_widget in self.entry_widgets:
        text = self.entry_widget.get()
        text = text.capitalize()
        self.entry_widget.delete(0, 'end')
        self.entry_widget.insert(0, text) 

#=============================================================================================================================================================================================================================================================================
def close_gui(window):
    """
    This funtion is created to close the gui and return the user to the previous page
    (Note this does not close the full app but instead used the withdraw method() to only close this page)
    """
    window.withdraw()


#=============================================================================================================================================================================================================================================================================
def data_format_search_edit(edits):
    """
    This function formats the data from search and edit entries.
    It takes in an array of edits from the search and edit page and formats the data.
    It strips trailing whitespaces and capitalizes the first letter of the data.
    """
    for edit in edits:
        text = edit.get()
        text = text.rstrip()
        edit.delete(0, 'end')
        edit.insert(0, text)

    for edit in edits:
        text = edit.get()
        text = text.capitalize()
        edit.delete(0, 'end')
        edit.insert(0, text) 


#=============================================================================================================================================================================================================================================================================
def clear_entries(self):
        """
        This function clears the entry boxes on the registration page.
        It deletes the content of all the entry boxes and deletes all the treeview children
        """
        #Clear entry boxes
        self.Membership_id_entry.delete(0, END)
        self.fname_entry.delete(0, END)
        self.lname_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.mobile_entry.delete(0, END)
        self.membership_type_entry.delete(0, END)
        self.payment_frequency_entry.delete(0, END)
        self.extras_entry.delete(0, END)
        self.Regular_Payment_entry.delete(0, END)
        self.search_lastn.delete(0, END)
        self.search_memberid.delete(0, END)
        self.search_membership_type.set("")
        self.my_tree.delete(*self.my_tree.get_children())


#=============================================================================================================================================================================================================================================================================
def registration_to_database(self):
    """
    This function is used to store user registration information to the database.
    It takes the user entered data from the entry widgets, formats it into the 
    correct data types and then uses a SQL query to add the data to the relevant
    database table.
    """

    message1 = "Please review Step 1 & Step 2, the following errors have occured: \n"
    first_name_fail = False
    last_name_fail = False
    mobile_num_fail = False
    full_address_fail = False
    membership_details_blank_fail = False
    global proceed_to_calculate 
    proceed_to_calculate = False


    if not re.match(r'^[a-zA-Z ]+$', self.fname_textb.get()) or self.fname_textb.get() == "":
        message1 += "\n First name can't be blank and should contain character letters only \n"
        first_name_fail = True

    if not re.match(r'^[a-zA-Z ]+$', self.sname_textb.get()) or self.fname_textb.get() == "":
        last_name_fail = True
        message1 += "\n Last name can't be blank and should contain character letters only \n"
        

    if not re.match(r'^[0-9 ]+$', self.mnumber_textb.get()) or self.mnumber_textb.get() == "":
        mobile_num_fail = True
        message1 += "\n Invalid mobile number entered\n"

    if self.address_textb.get() == "":
        message1 += "\n Full address can't be black and should contain a valid address \n"
        full_address_fail = True

    if self.membership_type_choice.get() == "Default" or self.membership_duration_choice.get() =="Default" or self.debit_payment_choice.get() == "Default" or self.payment_frequency_choice.get() == "Default":
        message1 += "\n Unselected items in Step 2 "
        membership_details_blank_fail = True


    if first_name_fail or last_name_fail or mobile_num_fail or full_address_fail or membership_details_blank_fail:
        messagebox.showerror(title="error", message=message1, ) 
        first_name_fail = False
        last_name_fail = False
        mobile_num_fail = False
        full_address_fail = False
        membership_details_blank_fail = False
        message1 = "\nPlease review Step 1 & Step 2, the following errors have occured: "
        
    else:
        proceed_to_calculate = True
        pass

        # See function comments for detail on this function 
        data_format_registration(self, self.entry_widgets)

        # Try/except for creating a connection and creating a cursor. This is wraped in error message if connection cannot be made and will alert user via a popup message 
        try:
            conn = sqlite3.connect('my_city_gym.db')
        
        except Exception:
            messagebox.showerror(title="Error!", message="Unable to make connection", )

        c = conn.cursor()

        # Try/except for inputting registration data into the Members table of the SQL database. This is wrapped in an error message if data is able/not able to be added via a popup message
        try:
            # Querying the Membership Table to get the membership_type_id                     
            c.execute("SELECT membership_type_id FROM Membership WHERE membership_type=?", (self.membership_type_choice.get(),))
            membership_type_id = c.fetchone()[0]

            # Converting my extras list into a JSON string so I can upload it to SQL database
            extras_string = json.dumps(self.extras)

            # Select query to insert entry widget input into the correct columns in the Members table (I have previously queried the membership_type_id table to match the membership type that is selected)
            c.execute("INSERT INTO Members (first_name, last_name, address, mobile_number, payment_frequency, extras, regular_payment, membership_type_id) VALUES (:first_name, :last_name, :address, :mobile_number, :payment_frequency, :extras, :regular_payment, :membership_type_id)", 
                    {
                        'first_name': self.fname_textb.get(),
                        'last_name': self.sname_textb.get(),
                        'address': self.address_textb.get(),
                        'mobile_number': self.mnumber_textb.get(),
                        'payment_frequency': self.payment_frequency_choice.get(),
                        'extras': json.dumps(extras_string),
                        'regular_payment': self.reg_membership_cost,
                        'membership_type_id': membership_type_id,
                    })
            # Message to display on the screen when a user successfully added information to the SQL database
            messagebox.showinfo(title="Success!", message="You have successfully registered your information", ) 
        
        # If the user is not able to successfully input registration data this message will alert them to this 
        except Exception:
            messagebox.showerror(title="Error!", message="You have not successfully registered your information", )

        # commit changes to database
        conn.commit()

        # close connection
        conn.close()


#=============================================================================================================================================================================================================================================================================
def search_member(self, member_id, last_name, lookup_record):
    """
    This function takes in three parameters, self, member_id, last_name, and lookup_record.  
    The self parameter refers to the instance of the class the code is running in, while the other two parameters are strings that are used to search the database. 
    The function starts by deleting any existing items in the tree view to make room for the search results.
    """
    self.my_tree.delete(*self.my_tree.get_children())

    # Try/except for creating a connection and creating a cursor. This is wraped in error message if connection cannot be made and will alert user via a popup message 
    try:
        conn = sqlite3.connect('my_city_gym.db')
        
    except Exception:
        messagebox.showerror(title="Error!", message="Unable to make connection", )
     
    c = conn.cursor()

        #The if statement checks to see if the lookup_record parameter is set to true, if it is then an additional condition is added to the query
    if lookup_record:
        c.execute("SELECT membership_type_id FROM Membership WHERE membership_type LIKE ?", (lookup_record,))
        membership_type_id = c.fetchone()[0]

        # This select query will take all entry widget inputs and look for a match on the Members table.
        #  This uses a or function to allow multiple variations of search and also uses the LIKE function to allow for different types of inputs that are similar to match
        query = f"""SELECT * FROM members 
        WHERE member_id LIKE '{member_id}' OR last_name LIKE '{last_name}' OR membership_type_id LIKE '{membership_type_id}'"""

        # The query is then executed and any results are stored in the data variable
        data = c.execute(query)

    else:
        query = f"""SELECT * FROM members 
        WHERE member_id LIKE '{member_id}' OR last_name LIKE '{last_name}'"""

        # The query is then executed and any results are stored in the data variable
        data = c.execute(query)

    # All information from query saved in data is returned and saved in datas 
    datas = data.fetchall()

    # This check is to catch if there are no entries returned form the search query and displays an error message "No members match your search"
    if len(datas) == 0:
        messagebox.showerror(title="Error!", message="No members match your search, please double check search input", ) 

        #The clear_entries() function is then called to clear the entries.
        clear_entries(self)    

    else:
        # Try/except block that populates the triewview and if that is not possible for some reason it will display error 
        try:
            # Populate the tree view with the data
            for row in datas:
                node_id = row[0]
                node_label = row[1]
                node_information = row[2]
                node_address = row[3]
                node_mobile = row[4]
                node_membership_type = row[5]
                node_payment_frequency = row[6]
                node_extras = row[7]
                node_regular_payment = row[8]

                # Add the node to the tree view
                self.my_tree.insert("", "end", node_id, values=(node_id, node_label, node_information, node_address, node_mobile, node_membership_type, node_payment_frequency, node_extras, node_regular_payment))

                # Alternating row tags
                if node_id % 2 == 0:
                        self.my_tree.item(node_id, tags=('evenrow'))
                else:
                        self.my_tree.item(node_id, tags=('oddrow'))

        # If this section is not able to input data into the treeview it will display an error that advsises this 
        except IndexError:
            messagebox.showerror(title="Error!", message="Unable to display your information", )

    
    #Close the connection
    conn.close()

#=============================================================================================================================================================================================================================================================================
def update_to_database(self, edits, lookup_record2):
    """
    This function is used to update the information of members in the database.
    The function takes two parameters, edits and lookup_record2.
    The edits parameter is a dictionary object containing the data that needs to be updated in the database.
    The lookup_record2 parameter is the Member Id of the member whose information needs to be updated
    """

    message1 = ""
    first_name_fail = False
    last_name_fail = False
    mobile_num_fail = False
    full_address_fail = False
    global proceed_to_calculate 
    proceed_to_calculate = False


    if not re.match(r'^[a-zA-Z ]+$', self.fname_entry.get()) or self.fname_entry.get() == "":
        message1 += "\n First name can't be blank and should contain character letters only \n"
        first_name_fail = True

    if not re.match(r'^[a-zA-Z ]+$', self.lname_entry.get()) or self.lname_entry.get() == "":
        last_name_fail = True
        message1 += "\n Last name can't be blank and should contain character letters only \n"
        
    if not re.match(r'^[0-9 ]+$', self.mobile_entry.get()) or self.mobile_entry.get() == "":
        mobile_num_fail = True
        message1 += "\n Invalid mobile number entered\n"

    if self.address_entry.get() == "":
        message1 += "\n Full address can't be black and should contain a valid address \n"
        full_address_fail = True

    if first_name_fail or last_name_fail or mobile_num_fail or full_address_fail:
        messagebox.showerror(title="error", message=message1, ) 
        first_name_fail = False
        last_name_fail = False
        mobile_num_fail = False
        full_address_fail = False
        message1 = ""
    else:

        # First, the edits dictionary is passed through the data_format_search_edit function, which checks the data for formatting and validates it.
        data_format_search_edit(edits)
    
        # Try/except for creating a connection and creating a cursor. This is wraped in error message if connection cannot be made and will alert user via a popup message 
        try:
            conn = sqlite3.connect('my_city_gym.db')
            
        except Exception:
            messagebox.showerror(title="Error!", message="Unable to make connection", )

        # Create a cursor object
        c = conn.cursor()

        """
        The execute() method accepts the query and the edits dictionary as parameters. 
        The query contains the columns to be updated, and the edits dictionary contains the new values for the columns.
        The member_id is also passed in the query as a parameter to select the record to be updated.    
        This is all done through a try/except block with related error message 
        """
        try:
        
            # Update the record with the new data 
            c.execute("UPDATE Members SET first_name = :first_name, last_name = :last_name, address = :address, mobile_number = :mobile_number WHERE member_id = :member_id", 
                    {   
                        'member_id': lookup_record2,
                        'first_name': self.fname_entry.get(),
                        'last_name': self.lname_entry.get(),
                        'address': self.address_entry.get(),
                        'mobile_number': self.mobile_entry.get(),

                    })
                # Message to display on screen when user successfully added information to database
            messagebox.showinfo(title="Success!", message=f"You have successfully updated Member ID {lookup_record2}", ) 

        except Exception:
            messagebox.showerror(title="Error!", message=f"There has been a issue updateding Member ID {lookup_record2}, please check your inputs", )

        # commit changes to database
        conn.commit()

        #close connection
        conn.close()

        #The clear_entries() function is then called to clear the entries.
        clear_entries(self)


#=============================================================================================================================================================================================================================================================================
def delete_record(self, lookup_record):
    """
    This function deletes a record from the Members table in the my_city_gym database. 
    It takes the user's input of the Member ID they wish to delete as a parameter.
    """
    # This delete method removes any input currently on the treeview 
    self.my_tree.delete(*self.my_tree.get_children())

    # Try/except for creating a connection and creating a cursor. This is wraped in error message if connection cannot be made and will alert user via a popup message 
    try:
        conn = sqlite3.connect('my_city_gym.db')
        
    except Exception:
        messagebox.showerror(title="Error!", message="Unable to make connection", )

    # Create a cursor object
    c = conn.cursor()

    # Within a try/except block a select query is run to find all data associated with the member_id held within a variable and delete all associated data
    try:
        c.execute('DELETE FROM Members WHERE member_id = ?', (lookup_record,))
        messagebox.showinfo(title=f"Success! Deleted Member ID {lookup_record}", message=f"You have successfully deleted Member ID {lookup_record}")
    
    # Error message if no record matches member_id 
    except Exception:
        messagebox.showerror(title="Error!", message="Unable to delete record", )

    # commit changes to database
    conn.commit()

    # close connection
    conn.close()

    #The clear_entries() function is then called to clear the entries.
    clear_entries(self)


#=============================================================================================================================================================================================================================================================================
def member_validation(self, member_id,):
    """ 
    This function is used to validate a member ID entered by a user. 
    It will check if the ID is valid by searching for the member in the Members table in the database.
    If the ID is found, the user will be able to view the member's information in a tree view. 
    """

    # This is deleting any existing entries in the tree view.
    self.my_tree.delete(*self.my_tree.get_children())

    # This checks if the member ID entered is valid. If it is empty, an error message is displayed. 
    if member_id == "":
        messagebox.showerror(title="Error!", message="Please enter a valid Member ID", )
    else:


        # Try/except for creating a connection and creating a cursor. This is wraped in error message if connection cannot be made and will alert user via a popup message 
        try:
            conn = sqlite3.connect('my_city_gym.db')
            
        except Exception:
            messagebox.showerror(title="Error!", message="Unable to make connection", )

        # Create a cursor object
        c = conn.cursor()
        
        # A query is executed to search the Booking table in the database.
        query = f"""SELECT * FROM Booking WHERE member_id LIKE '{member_id}'"""

        # The vairable data is the executed query
        data = c.execute(query)

        # Query output is stored in datas
        datas = data.fetchall()


        if len(datas) == 0:
            # Query the Member table to find the information that matches the member_id 
            query = f"""SELECT first_name, last_name FROM Members WHERE member_id LIKE '{member_id}'"""
            data = c.execute(query)
            data1 = data.fetchmany() 

            # Transfers the information into manageable format 
            for row in data1:
                fname = row[0]
                lname = row[1]

                # Datas1 is now a list with data from data1
                datas1 = [fname, lname]
                
                # This is setting the treeview section to "Yes" to visually see the member is valid 
                valid_member = "Yes"

                # This is used as a filler vairable for the treeview 
                booking_blank = "None"

                # This is used as a filler vairable for the treeview 
                class_none = "None"

                # This is inserting the vairable into the treeview 
                self.my_tree.insert("", "end", values=(booking_blank, member_id, datas1[0], datas1[1], class_none, valid_member))

                # This is setting the my_val bool vairable to True to allow the user to contine to the class registration section of the page  
                self.my_val = True
        
        # If the query returns results from the Booking table, the member's information is displayed along with their booking information. 
        else:
            try:
        #       # Transfers the information into manageable format 
                for row in datas:
                    node_booking_id = row[0]
                    node_id = row[1]
                    node_label = row[2]
                    node_information = row[3]
                    node_cadio = row[4]

                    # This is setting the treeview section to "Yes" to visually see the member is valid 
                    valid_member = "Yes"

                    # This is inserting the vairable into the treeview 
                    self.my_tree.insert("", "end", node_booking_id, values=(node_booking_id, node_id, node_label, node_information, node_cadio, valid_member))
                    
                    # This is setting the my_val bool vairable to True to allow the user to contine to the class registration section of the page  
                    self.my_val = True

                    # Alternating row tags
                    if node_id % 2 == 0:
                            self.my_tree.item(node_booking_id, tags=('evenrow'))
                    else:
                            self.my_tree.item(node_booking_id, tags=('oddrow'))     

            # If this section is not able to input data into the treeview it will display an error that advsises this 
            except IndexError:
                messagebox.showerror(title="Error!", message="Unable to display your information", )


#=============================================================================================================================================================================================================================================================================
def class_registration(self, member_id, button_value):
    """
    This function takes in a member_id and a button_value as parameters. 
    It is used to register a member for a fitness class in the database.
    """

    # Try/except for creating a connection and creating a cursor. This is wraped in error message if connection cannot be made and will alert user via a popup message 
    try:
        conn = sqlite3.connect('my_city_gym.db')
        
    except Exception:
        messagebox.showerror(title="Error!", message="Unable to make connection", )

    # Create a cursor object
    c = conn.cursor()

    # This error is displayed if the user does not make a selection from the raidio buttons 
    if button_value == "Default":
        messagebox.showerror(title="Error!", message="Please make a section before registering for a class", )
    else:
        
        """
        It first attempts to create a connection to the 'my_city_gym.db' database.
        If it is unsuccessful, it will alert the user with a pop-up message.
        """ 
        # Query the Fitness table to find the class_id that matches the radio button value 
        c.execute("SELECT fitness_class_type FROM Fitness WHERE class_id = ?", (button_value,))

        # The vairable class_type is the executed query
        class_type = c.fetchone()

        # Query the Booking table to find if the member_id has already taken the selected class 
        c.execute("SELECT member_id FROM Booking WHERE member_id = ? AND fitness_class_type = ?", (member_id, class_type[0]))

        # Store the query result 
        booking_data = c.fetchone() 

        print(booking_data)

        # If the data exists, then an error should be displayed to re-select 
        if booking_data:
            messagebox.showerror(title="Error!", message="You have already registered for this class, please select diffrent class", )
            self.class_selection.set("Default")

        
        # If the data does not exist, the function queries the Member table to find the information that matches the member_id.
        # It then queries the Fitness table to find the class_id that matches the radio button value.
        # A new row is then created in the Booking table with the appropriate data.
        # A success pop-up message is then displayed and the class_selection is set to the default value.
        else:
            # Query the Member table to find the information that matches the member_id 
            c.execute("SELECT first_name, last_name FROM Members WHERE member_id = ?", (member_id,))

            # Store the query result 
            member_data = c.fetchmany() 

            # Query the Fitness table to find the class_id that matches the radio button value 
            c.execute("SELECT fitness_class_type FROM Fitness WHERE class_id = ?", (button_value,))

            # The vairable fitness_data is the executed query
            fitness_data = c.fetchone() 
            
            # Transfers the information into manageable format 
            for row in member_data:
                fname = row[0]
                lname = row[1]

            # Datas1 is now a list with data from member_data
            member_data = [fname, lname]
        
            # This is inserting the data into the Booking table by setting the destination and then providing the data that is going into those fields
            c.execute("INSERT INTO Booking (member_id, first_name, last_name, fitness_class_type) VALUES (?, ?, ?, ?)", (member_id, member_data[0], member_data[1], fitness_data[0]))
            
            # This is the message the user gets when the data is successfully into into the database 
            messagebox.showinfo(title="Success!", message=f"You have successfully registered for {fitness_data}", )
            
            # This is setting the radio buttons to the default status 
            self.class_selection.set("Default")

        # Commit changes to the database 
        conn.commit() 
    
        # Close connection to the database 
        conn.close()


#=============================================================================================================================================================================================================================================================================







    


    


    

    





