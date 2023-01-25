import tkinter as Tk
from tkinter import *
from tkinter import messagebox
import customtkinter
from tkinter import ttk
import dbdef

class Fitness:
    

    def __init__(self, master):
        
        # This is setting the root window 
        self.fitness_window = customtkinter.CTk()

        # This is setting the window name 
        self.fitness_window.title("Fiteness Class Registrationn")

        # This section takes the width and hight of the window and devides by two to be able to center the page
        width = self.fitness_window.winfo_screenwidth()
        height = self.fitness_window.winfo_screenheight()
        x_position = (width/2) - (1220/2)
        y_position = (height/2) - (650/2)
        self.fitness_window.geometry("1220x650+{}+{}".format(int(x_position), int(y_position)))
        
        #This is setting the appearance of the overall gui app 
        customtkinter.set_appearance_mode("light")

        # This is the the variable used to validate if the user has validated the user 
        self.my_val = False

        #=======================================================================================================================================================================================================================================================================================================================================================================================================
        
        # This is a frame that contains all of the widgets and other frames
        self.frame_top = customtkinter.CTkFrame(master=self.fitness_window, width=1300, height=690, fg_color= "#262626", corner_radius=30, bg_color="#262626")
        self.frame_top.pack(fill='both', expand=True)

        # This is a frame that contains all of the widgets and other frames 
        self.frame_top1 = customtkinter.CTkFrame(self.frame_top, width=1220, height=650, fg_color= "#262626", corner_radius=30, bg_color="#262626", border_color="#FFE4C4", border_width=3)
        self.frame_top1.pack()

        # This is the frame that holds the page title 
        self.main_menu_background = customtkinter.CTkFrame(self.frame_top1, width=300, height=30, fg_color= "#383838", corner_radius=30,bg_color="#262626")
        self.main_menu_background.place(x=200, y=60)
        
        # This is the label that displays the page title, this is housed in the self.main_menu_background farme
        self.main_menu_header = customtkinter.CTkLabel(self.main_menu_background, text="Fitness Class Member Validation", font=("italic",15), fg_color="#383838", text_color="#F8F3F3", height=20)
        self.main_menu_header.place(x=35, y=5)

        # This is the label that displays the app name 
        self.app_name1 = customtkinter.CTkLabel(self.frame_top1, text='City Gym App', font=("italic",30), fg_color="#262626", text_color="#F8F3F3", height=40)
        self.app_name1.place(x=250, y=8)

        # This is the farme that contains all of the validation seach widgets 
        self.search_member_for_val = customtkinter.CTkFrame(self.frame_top, width=670, height=170, fg_color= "#383838", corner_radius=30, bg_color="#262626")
        self.search_member_for_val.place(x=40, y=120)

        # This is the frame that holds the treeview that displays the information from the validation check
        self.treeview_frame = customtkinter.CTkFrame(self.frame_top, width=1145, height=260, fg_color= "#383838", corner_radius=30, bg_color="#262626")
        self.treeview_frame.place(x=40, y=325)
        
        #=======================================================================================================================================================================================================================================================================================================================================================================================================
        
        # This is the label that displays the search instructions
        self.app_name1 = customtkinter.CTkLabel(self.search_member_for_val, text='Enter in membership ID to validate membership', font=("italic",16), fg_color="#383838", bg_color="#383838", text_color="#F8F3F3", height=40)
        self.app_name1.place(x=20, y=15)

        # This is the entry widget that is used to check the member id 
        self.member_id_search = customtkinter.CTkEntry(self.search_member_for_val, width=415, fg_color= "#333333", bg_color="#383838", text_color="#FFFAF0", corner_radius=30)
        self.member_id_search.place(x=20, y=55)

        #=======================================================================================================================================================================================================================================================================================================================================================================================================

        # This is the button that resets the inputs to the treeview and self.member_id_search
        self.reset_button = customtkinter.CTkButton(self.search_member_for_val, text="Reset ", font=("italic", 16), fg_color="#383838", text_color="#FFFAF0", corner_radius=30, width=200, height=45 ,border_spacing=0, border_width=3, command= lambda: [(self.my_tree.delete(*self.my_tree.get_children())),self.member_id_search.delete(0, "end")])
        self.reset_button.place(x=450, y=45)

        # This button will withdraw the window back to the main screen and close this window  
        self.validate_button = customtkinter.CTkButton(self.search_member_for_val, text="Validate Member ", font=("italic", 16), fg_color="#383838", text_color="#FFFAF0", corner_radius=30, width=200, height=45 ,border_spacing=0, border_width=3, command= lambda: [dbdef.member_validation(self, self.member_id_search.get())])
        self.validate_button.place(x=20, y=95)

        # This button triggers the clear_booking_screen function and displays to the user the options of what classes they can register for. See the function for more details 
        self.next = customtkinter.CTkButton(self.search_member_for_val, text="Continue", font=("italic", 16), fg_color="#383838", text_color="#FFFAF0", corner_radius=30, width=200, height=45 ,border_spacing=0, border_width=3, command= lambda: self.clear_booking_screen())
        self.next.place(x=235, y=95)
        
        # This button will withdraw the window back to the main screen and close this window, see the function for more details 
        self.exit_button = customtkinter.CTkButton(self.search_member_for_val, text="Exit ", font=("italic", 16), fg_color="#383838", text_color="#FFFAF0", corner_radius=30, width=200, height=45 ,border_spacing=0, border_width=3, command= lambda: self.close_gui())
        self.exit_button.place(x=450, y=95)

        #=======================================================================================================================================================================================================================================================================================================================================================================================================
        
        # This is the frame that the treeview goes into 
        self.tree_frame = Frame(self.treeview_frame, height=300, width=300)
        self.tree_frame.place(x=20, y=25)

        # Create the scrollbar for the trwwview for when there are more entries than the view allows 
        tree_scroll = Scrollbar(self.tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)    

        # Create the treeview
        self.my_tree = ttk.Treeview(self.tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
        self.my_tree.pack()

        # Configure the scrollbar
        tree_scroll.config(command=self.my_tree.yview)

        # Define the columns within the treeview 
        self.my_tree['columns'] = ("Booking ID","Membership ID", "First Name", "Last Name", "Class", "Valid Member" )

        # Format the columns within the treeview
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("Booking ID", anchor=W, width=140)
        self.my_tree.column("Membership ID", anchor=W, width=140)
        self.my_tree.column("First Name", anchor=W, width=140)
        self.my_tree.column("Last Name", anchor=W, width=140)
        self.my_tree.column("Class", anchor=W, width=265)
        self.my_tree.column("Valid Member", anchor=W, width=265)
        
        # Create the headings within the treeview
        self.my_tree.heading("0", text="", anchor=W)
        self.my_tree.heading("Booking ID", text="Booking ID", anchor=W)
        self.my_tree.heading("Membership ID", text="Membership ID", anchor=W)
        self.my_tree.heading("First Name", text="First Name", anchor=W)
        self.my_tree.heading("Last Name", text="Last Name", anchor=W)
        self.my_tree.heading("Class", text="Class", anchor=W)
        self.my_tree.heading("Valid Member", text="Valid Member", anchor=W)

        # Create the striped row tags to displaye the odd and even rows in dirrent colors 
        self.my_tree.tag_configure('oddrow', background="#262626")
        self.my_tree.tag_configure('evenrow', background="#383838")

        #=======================================================================================================================================================================================================================================================================================================================================================================================================
        
        # These entry widgets are to be used for future development 
        self.booking_id_entry = Entry(self.fitness_window, width=30)

        # Entry box for First Name 
        self.fname_entry = Entry(self.fitness_window, width=30)

        # Entry box for Last Name
        self.lname_entry = Entry(self.fitness_window, width=30)

        # Entry box for Last class
        self.class_entry = Entry(self.fitness_window, width=30)

        # Entry box for Last valid member
        self.valid_member_entry = Entry(self.fitness_window, width=30)

        # This entry boxes are used to save information like a variable but are used to populate treeview aswell 
        self.membership_id_entry1 = Entry(self.fitness_window)

        #=======================================================================================================================================================================================================================================================================================================================================================================================================

#=======================================================================================================================================================================================================================================================================================================================================================================================================
    # This function withdraws the gui page and returns the user to the main screen/navigation page
    def close_gui(self):
        self.fitness_window.withdraw()


#=======================================================================================================================================================================================================================================================================================================================================================================================================
    def return_to_member_val(self):
        """
        This function is used when the user clicks exit in the self.class_regitration frame.
        This function destroys self.class_regitration and all elelements in it and returns the user to validate membership screen 
        This function also clears the treeview, clears the self.member_id_search entry and sets the my_val to to false so that the user 
        needs to validate before they can enrol in any more classes
        """
        self.class_regitration.destroy()
        self.my_tree.delete(*self.my_tree.get_children())
        self.member_id_search.delete(0, "end")
        self.my_val = False
        

#=======================================================================================================================================================================================================================================================================================================================================================================================================
    def clear_booking_screen(self):
        """
        This function creates a new frame that hides the validation page elements and inputs class_regitration frame and its label and radio
        button widgets.
        This allows the user to choose a class to enrol in and submit it to the database 
        """

        # This checks if the user has validated the membership and if it hasnt been validated it will pop up a message telling the user to do so 
        if self.my_val == False:
            messagebox.showerror(title="Error!", message="Please enter a valid Member ID")
        
        else:
            
            # This is the farme that all the labels, radio buttons, and buttons are stored in 
            self.class_regitration = customtkinter.CTkFrame(self.frame_top, width=1160, height=470, fg_color= "#383838", corner_radius=30, bg_color="#262626")
            self.class_regitration.place(x=30, y=120)

            # This is a label that instructs the user to choose a radio button 
            self.page_title_fram = customtkinter.CTkLabel(self.class_regitration, text="Register for one of the below classes to push your physical health to the next level", font=("italic",15), fg_color="#383838", text_color="#F8F3F3", height=20)
            self.page_title_fram.place(x=100, y=50)
            
            # This is a frame that the radio button for Cardio, Thursday, 3pm - 5pm is placed in 
            self.cardio_radio_frame = customtkinter.CTkFrame(self.class_regitration, fg_color= "#383838", bg_color="#383838", border_color="#7F7F7F", corner_radius=30, width=700, height=45, border_width=3)
            self.cardio_radio_frame.place(x=60, y=90)

            # This is a frame that the radio button for Cardio, Thursday, 3pm - 5pm in placed in 
            self.main_menu_background = customtkinter.CTkFrame(self.class_regitration, fg_color= "#383838", bg_color="#383838", border_color="#7F7F7F", corner_radius=30, width=700, height=45, border_width=3)
            self.main_menu_background.place(x=60, y=160)

            # This is a frame that the radio button for Pilates, Friday, 9am - 11am is placed in 
            self.main_menu_background = customtkinter.CTkFrame(self.class_regitration, fg_color= "#383838", bg_color="#383838", border_color="#7F7F7F", corner_radius=30, width=700, height=45, border_width=3)
            self.main_menu_background.place(x=60, y=230)

            # This is a frame that the radio button for Spin, Monday, 2pm - 4pm is placed in 
            self.main_menu_background = customtkinter.CTkFrame(self.class_regitration, fg_color= "#383838", bg_color="#383838", border_color="#7F7F7F", corner_radius=30, width=700, height=45, border_width=3)
            self.main_menu_background.place(x=60, y=230)

            # This is a frame for style and has no other use
            left_style_bar = customtkinter.CTkFrame(self.class_regitration, width=45, height=300, fg_color= "#383838", corner_radius=30, border_width=3, border_color="#7F7F7F")
            left_style_bar.place(x=40, y=30)

            #----------------------------

            # This is the variable that the next three radio buttons are stored in if selected 
            self.class_selection = StringVar()

            # This is a radio button that is not placed but rather used as a home for the default set
            self.default_radio_B =customtkinter.CTkRadioButton(self.class_regitration, variable=self.class_selection, value="Default")
            self.class_selection.set("Default")

            # This is a radio button for the Cardio, Thursday, 3pm - 5pm selection
            self.cardio_radio_b = customtkinter.CTkRadioButton(self.class_regitration, variable=self.class_selection, value="1", text="Cardio, Thursday, 3pm - 5pm", font=("italic", 14), text_color_disabled="FFFAF0", bg_color="#383838", text_color="#FFFAF0")
            self.cardio_radio_b.place(x=160, y=100)

            # This is a radio button for the Pilates, Friday, 9am - 11am selection
            self.pilates_radio_b = customtkinter.CTkRadioButton(self.class_regitration, variable=self.class_selection, value="2", text="Pilates, Friday, 9am - 11am", font=("italic", 14), text_color_disabled="FFFAF0", bg_color="#383838", text_color="#FFFAF0")
            self.pilates_radio_b.place(x=160, y=170)

            # This is a radio button for the Spin, Monday, 2pm - 4pm selection
            self.spin_radio_b = customtkinter.CTkRadioButton(self.class_regitration, variable=self.class_selection, value="3", text="Spin, Monday, 2pm - 4pm", font=("italic", 14), text_color_disabled="FFFAF0", bg_color="#383838", text_color="#FFFAF0")
            self.spin_radio_b.place(x=160, y=240)

            # This button thats the radio button selection and queries a database ad enrols the member in the course selected, see the funtion class_registration in the dbdef file, see function for more detail 
            self.register_button = customtkinter.CTkButton(self.class_regitration, text="Register", font=("italic", 16), fg_color="#383838", text_color="#FFFAF0", corner_radius=30, width=200, height=45 ,border_spacing=0, border_width=3, command= lambda: dbdef.class_registration(self, self.member_id_search.get(), self.class_selection.get()))
            self.register_button.place(x=80, y=400)

            # This button sets the radio button functions to the default status and deselects and selected radio buttons 
            self.reset_button = customtkinter.CTkButton(self.class_regitration, text="Reset", font=("italic", 16), fg_color="#383838", text_color="#FFFAF0", corner_radius=30, width=200, height=45 ,border_spacing=0, border_width=3, command= lambda: self.class_selection.set("Default"))
            self.reset_button.place(x=300, y=400)

            # This button destroys the frame and reurns the user to member validation section of the gui 
            self.exit_button = customtkinter.CTkButton(self.class_regitration, text="Exit ", font=("italic", 16), fg_color="#383838", text_color="#FFFAF0", corner_radius=30, width=200, height=45 ,border_spacing=0, border_width=3, command= lambda: self.return_to_member_val())
            self.exit_button.place(x=520, y=400)


#=======================================================================================================================================================================================================================================================================================================================================================================================================






    

        









