import tkinter as Tk
from tkinter import *
from tkinter import  ttk
from tkinter import END
import customtkinter
from tkinter import ttk
import dbdef


class Search:
    

    def __init__(self, master):
        
        # This is setting the root window 
        search_window = customtkinter.CTk()

        # This is setting the window name 
        search_window.title("City Gym Search Screen")

        # This is setting the screen size
        search_window.geometry("1425x670")

        # This section takes the width and hight of the window and devides by two to be able to center the page
        width = search_window.winfo_screenwidth()
        height = search_window.winfo_screenheight()
        x_position = (width/2) - (1425/2)
        y_position = (height/2) - (670/2)
        search_window.geometry("1425x670+{}+{}".format(int(x_position), int(y_position)))

        #This is setting the appearance of the overall gui app 
        customtkinter.set_appearance_mode("light")


        # Page Layout for labels, entry widgets and option menu=============================================================================================================================================================================================================================================================================

        # Frame that makes up the background
        self.frame_top = customtkinter.CTkFrame(master=search_window, width=985, height=690, fg_color= "#262626", corner_radius=30, bg_color="#262626")
        self.frame_top.pack(fill='both', expand=True)

        # Frame that makes up the background
        self.frame_top1 = customtkinter.CTkFrame(self.frame_top, width=1425, height=670, fg_color= "#262626", corner_radius=30, bg_color="#262626", border_color="#FFE4C4", border_width=3)
        self.frame_top1.pack()

        # Fram and backround for the search page header
        self.search_fields_frame = customtkinter.CTkFrame(self.frame_top1, width=540, height=190, fg_color= "#383838", corner_radius=30,bg_color="#262626", border_color="#7F7F7F")
        self.search_fields_frame.place(x=10, y=110)

        # Fram and backround for the search page header
        self.treeview_frame = customtkinter.CTkFrame(self.frame_top1, width=1405, height=325, fg_color= "#383838", corner_radius=30,bg_color="#262626", border_color="#7F7F7F")
        self.treeview_frame.place(x=10, y=315)

        # Fram and backround for the search page header
        self.edit_record_frame = customtkinter.CTkFrame(self.frame_top1, width=800, height=190, fg_color= "#383838", corner_radius=30,bg_color="#262626", border_color="#7F7F7F")
        self.edit_record_frame.place(x=580, y=110)

        # Fram and backround for the search page header
        self.main_menu_background = customtkinter.CTkFrame(self.frame_top1, width=300, height=30, fg_color= "#383838", corner_radius=30,bg_color="#262626")
        self.main_menu_background.place(x=120, y=50)

        # Label Search Screen for screen header
        self.main_menu_header = customtkinter.CTkLabel(self.main_menu_background, text="Search Screen", font=("italic",15), fg_color="#383838", text_color="#F8F3F3", height=20)
        self.main_menu_header.place(x=90, y=3)

        # Label for header City Gym App
        self.app_name1 = customtkinter.CTkLabel(self.frame_top1, text='City Gym App', font=("italic",30), fg_color="#262626", text_color="#F8F3F3", height=40)
        self.app_name1.place(x=180, y=8)

        # Label for Search field (Last Name)
        self.last_name_search = customtkinter.CTkLabel(self.search_fields_frame, text='Last Name', font=("italic",14), fg_color="#383838", bg_color="#383838", text_color="#F8F3F3", height=10)
        self.last_name_search.place(x=15, y=12)

        # Entry for search box (Last Name)
        self.search_lastn = customtkinter.CTkEntry(self.search_fields_frame, width=500, fg_color= "#333333", bg_color="#383838", text_color="#FFFAF0", corner_radius=30)
        self.search_lastn.place(x=10, y=32)

        # Label for search field (Member ID)
        self.member_id_search = customtkinter.CTkLabel(self.search_fields_frame, text='Membership ID', font=("italic",14), fg_color="#383838", bg_color="#383838", text_color="#F8F3F3", height=10)
        self.member_id_search.place(x=15, y=67)

        # Entry for search box (Member ID)
        self.search_memberid = customtkinter.CTkEntry(self.search_fields_frame, width=500, fg_color= "#333333", bg_color="#383838", text_color="#F8F3F3", corner_radius=30,)
        self.search_memberid.place(x=10, y=87)

        # Label for search field (Membership Type)
        self.membership_type_search = customtkinter.CTkLabel(self.search_fields_frame, text='Membership Type', font=("italic",14), fg_color="#383838", bg_color="#383838", text_color="#F8F3F3", height=10)
        self.membership_type_search.place(x=15, y=122)

        # Option menu for search box (Membership Type)
        self.search_membership_type = customtkinter.CTkOptionMenu(self.search_fields_frame, values=["Basic", "Regular", "Premium" ], width=500, fg_color= "#63666A", bg_color="#383838", text_color="#FFFAF0", )
        self.search_membership_type.place(x=10, y=142)
        self.search_membership_type.set("")
        #=============================================================================================================================================================================================================================================================================


        # This section is creating and building out the treeview layout=============================================================================================================================================================================================================================================================================

        # Create treeview frame
        tree_frame = Frame(self.treeview_frame, height=300, width=300)
        tree_frame.place(x=15, y=20)

        # Create the scrollbar for the trwwview for when there are more entries than the view allows 
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)    

        # Create the treeview
        self.my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
        self.my_tree.pack()

        # Configure the scrollbar
        tree_scroll.config(command=self.my_tree.yview)

        # Define the columns within the treeview 
        self.my_tree['columns'] = ("Membership ID", "First Name", "Last Name", "Address", "Mobile", "Membership Type", "Payment Frequency", "Extras", "Regular Payment", )

        # Format the columns within the treeview
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("Membership ID", anchor=W, width=90)
        self.my_tree.column("First Name", anchor=W, width=120)
        self.my_tree.column("Last Name", anchor=W, width=120)
        self.my_tree.column("Address", anchor=W, width=300)
        self.my_tree.column("Mobile", anchor=W, width=120)
        self.my_tree.column("Membership Type", anchor=W, width=140)
        self.my_tree.column("Payment Frequency", anchor=W, width=120)
        self.my_tree.column("Extras", anchor=W, width=250)
        self.my_tree.column("Regular Payment", anchor=W, width=100)
        
        # Create the headings within the treeview
        self.my_tree.heading("0", text="", anchor=W)
        self.my_tree.heading("Membership ID", text="Membership ID", anchor=W)
        self.my_tree.heading("First Name", text="First Name", anchor=W)
        self.my_tree.heading("Last Name", text="Last Name", anchor=W)
        self.my_tree.heading("Address", text="Address", anchor=W)
        self.my_tree.heading("Mobile", text="Mobile", anchor=W)
        self.my_tree.heading("Membership Type", text="Membership Type", anchor=W)
        self.my_tree.heading("Payment Frequency", text="Payment Frequency", anchor=W)
        self.my_tree.heading("Extras", text="Extras", anchor=W)
        self.my_tree.heading("Regular Payment", text="Regular Payment", anchor=W)
       
        # Create the striped row tags to displaye the odd and even rows in dirrent colors 
        self.my_tree.tag_configure('oddrow', background="#262626")
        self.my_tree.tag_configure('evenrow', background="#383838")
        #END=============================================================================================================================================================================================================================================================================


        #This section is creating the fields that allow the user to edit basic member information=============================================================================================================================================================================================================================================================================
 
        
        # Creating the frame for the edit records fields 
        data_frame = LabelFrame(self.edit_record_frame, text="Edit Record")
        data_frame.place(x=15, y=35)

        # Label for First Name entry box
        fname_label = Label(data_frame, text="First Name")
        fname_label.grid(row=0, column=0, padx=10, pady=10)

        # Entry box for First Name 
        self.fname_entry = Entry(data_frame, width=30)
        self.fname_entry.grid(row=0, column=1, padx=5, pady=10)

        # Label for Last Name entry box
        lname_label = Label(data_frame, text="Last Name")
        lname_label.grid(row=0, column=2, padx=10, pady=10)

        # Entry box for Last Name
        self.lname_entry = Entry(data_frame, width=30)
        self.lname_entry.grid(row=0, column=3, padx=5, pady=10)

        # Label for Address entry box
        address_label = Label(data_frame, text="Address")
        address_label.grid(row=1, column=0, padx=10, pady=10)

        # Entry Box for Address
        self.address_entry = Entry(data_frame, width=30)
        self.address_entry.grid(row=1, column=1, padx=5, pady=10)

        # Label for Mobile Number 
        mobile_label = Label(data_frame, text="Mobile")
        mobile_label.grid(row=1, column=2, padx=10, pady=10)

        # Entry Box for Mobile Number 
        self.mobile_entry = Entry(data_frame, width=30)
        self.mobile_entry.grid(row=1, column=3, padx=5, pady=10)

        # This entry boxes are used to save information like a variable but are used to populate treeview aswell 
        self.Membership_id_entry = Entry(data_frame)
        self.membership_type_entry = Entry(data_frame)
        self.payment_frequency_entry = Entry(data_frame, background="white", foreground="black" )
        self.extras_entry = Entry(data_frame, background="white", foreground="black" )
        self.Regular_Payment_entry = Entry(data_frame, background="white", foreground="black" )

        
        # This variable is created to group all record edit entry widgets to be used when updating records and allows for looping commands 
        edits = (self.fname_entry, self.lname_entry, self.address_entry, self.mobile_entry)
        #END=============================================================================================================================================================================================================================================================================


        #This section is creating the buttons used to action anything=============================================================================================================================================================================================================================================================================

        
        # This button is used to run the search function saved in the dbdef .py file and populates the treeview based on a sql select query using either last name, membership id, membership type or a combination (Note the parameters in the search_member function)
        self.search_button = customtkinter.CTkButton(self.treeview_frame, text="Search ", font=("italic", 16), fg_color="#262626", text_color="#FFFAF0", corner_radius=30, width=200, height=45 ,border_spacing=0, border_width=3, command= lambda: dbdef.search_member(self, self.search_memberid.get(), self.search_lastn.get(), self.search_membership_type.get()))
        self.search_button.place(x=350, y=255)

        # This button is used to run the clear_entries function saved in the dbdef .py file and clears all fields on the screen (Note the parameters in the clear_entries function)
        self.reset_button = customtkinter.CTkButton(self.treeview_frame, text="Reset ", font=("italic", 16), fg_color="#262626", text_color="#FFFAF0", corner_radius=30, width=200, height=45 ,border_spacing=0, border_width=3, command= lambda: dbdef.clear_entries(self))
        self.reset_button.place(x=560, y=255)
        
        # This button is used to run the update_to_database function saved in the dbdef .py file and takes any all information from the edit records entry boxs and validates the content. Once the content is acceptable it will update the database (Note the parameters in the update_to_database function)
        self.update_button = customtkinter.CTkButton(self.treeview_frame, text="Update Record ", font=("italic", 16), fg_color="#262626", text_color="#FFFAF0", corner_radius=30, width=200, height=45 ,border_spacing=0, border_width=3, command= lambda: dbdef.update_to_database(self, edits, self.Membership_id_entry.get()))
        self.update_button.place(x=770, y=255)

        # This button is used to run the delete_record function saved in the dbdef .py file and takes the record selected based on member_id and removed the record from the database (Note the parameters in the delete_record function)
        self.delete_button = customtkinter.CTkButton(self.treeview_frame, text="Delete Record ", font=("italic", 16), fg_color="#262626", text_color="#FFFAF0", corner_radius=30, width=200, height=45 ,border_spacing=0, border_width=3, command= lambda: dbdef.delete_record(self, self.Membership_id_entry.get()))
        self.delete_button.place(x=980, y=255)
        
        # This button is used to run the close_gui funtion saved in the dbdef .py file and closed the gui pages returning the user to the main menu navigation page 
        self.exit_button = customtkinter.CTkButton(self.treeview_frame, text="Exit ", font=("italic", 16), fg_color="#262626", text_color="#FFFAF0", corner_radius=30, width=200, height=45 ,border_spacing=0, border_width=3, command= lambda: dbdef.close_gui(search_window))
        self.exit_button.place(x=1190, y=255)

        # This is binding the treeview to the 'select_record' function, which will be called when the user clicks on a record in the treeview
        self.my_tree.bind("<ButtonRelease>", self.select_record)
        #END#=============================================================================================================================================================================================================================================================================

    
    #This section is the functions used throught this gui page#=============================================================================================================================================================================================================================================================================

    # This function is used to clear the existing boxs, select the treeview and populate the fields with the values saved in the string positions
    def select_record(self,event):
        # Clear entry boxes
        self.Membership_id_entry.delete(0, END)
        self.fname_entry.delete(0, END)
        self.lname_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.mobile_entry.delete(0, END)
   
        # Grab record Number
        selected = self.my_tree.focus()
        # Grab record values
        values = self.my_tree.item(selected, 'values')

        # outpus to entry boxes
        
        self.Membership_id_entry.insert(0, values[0])
        self.fname_entry.insert(0, values[1])
        self.lname_entry.insert(0, values[2])
        self.address_entry.insert(0, values[3])
        self.mobile_entry.insert(0, values[4])
        self.membership_type_entry.insert(0, values[5])
        self.payment_frequency_entry.insert(0, values[6])
        self.extras_entry.insert(0, values[7])
        self.Regular_Payment_entry.insert(0, values[8])
        

#=============================================================================================================================================================================================================================================================================
