import tkinter as Tk
from tkinter import *
import customtkinter
from tkinter import ttk




class Help:
    

    def __init__(self, master):
        
        # This is setting the root window 
        self.helpwindow = customtkinter.CTk()

        # This is setting the window name
        self.helpwindow.title("City Gym Help Screen")

        # This section takes the width and hight of the window and devides by two to be able to center the page
        width = self.helpwindow.winfo_screenwidth()
        height = self.helpwindow.winfo_screenheight()
        x_position = (width/2) - (985/2)
        y_position = (height/2) - (750/2)
        self.helpwindow.geometry("985x750+{}+{}".format(int(x_position), int(y_position)))

        #This is setting the appearance of the overall gui app 
        customtkinter.set_appearance_mode("light")

        #=======================================================================================================================================================================================================================================================================================================================================================================================================
        
        # This is a frame that contains all of the widgets and other frames
        self.frame_top = customtkinter.CTkFrame(master=self.helpwindow, width=985, height=690, fg_color= "#262626", corner_radius=30, bg_color="#262626")
        self.frame_top.pack(fill='both', expand=True)

        # This is a frame that contains all of the widgets and other frames 
        self.frame_top1 = customtkinter.CTkFrame(self.frame_top, width=985, height=740, fg_color= "#262626", corner_radius=30, bg_color="#262626", border_color="#FFE4C4", border_width=3)
        self.frame_top1.pack()

        # This is the frame that holds the page title 
        self.main_menu_background = customtkinter.CTkFrame(self.frame_top1, width=300, height=30, fg_color= "#383838", corner_radius=30,bg_color="#262626", border_width=3, border_color="#7F7F7F")
        self.main_menu_background.place(x=335, y=60)

        #=======================================================================================================================================================================================================================================================================================================================================================================================================

        # This is the label that displays the page title, this is housed in the self.main_menu_background farme
        self.main_menu_header = customtkinter.CTkLabel(self.frame_top1, text="Help Screen", font=("italic",15), fg_color="#383838", text_color="#F8F3F3", height=20)
        self.main_menu_header.place(x=440, y=65)

        # This is the label that displays the app name 
        self.app_name1 = customtkinter.CTkLabel(self.frame_top1, text='City Gym App', font=("italic",40), fg_color="#262626", text_color="#F8F3F3", height=40)
        self.app_name1.place(x=365, y=8)

        #=======================================================================================================================================================================================================================================================================================================================================================================================================

        # This is the frame widget that is the backround to all the help tips 
        self.left_style_bar = customtkinter.CTkFrame(self.frame_top1, width=935, height=550, fg_color= "#383838", corner_radius=30, border_width=3, border_color="#7F7F7F")
        self.left_style_bar.place(x=25, y=120)

        # This is the section header for the navigation tips for the tips to navigate City Gym App 
        self.app_name1 = customtkinter.CTkLabel(self.frame_top1, text="Tips to navigate City Gym App              ", font=("italic",15), fg_color="#383838", text_color="#F8F3F3", height=40)
        self.app_name1.place(x=35, y=135)

        # This label displays a tip for navigating the City Gym app
        self.app_name1 = customtkinter.CTkLabel(self.frame_top1, text="Select the action you want from the Main Screen                                  ", font=("italic",15), fg_color="#383838", text_color="#F8F3F3", height=40)
        self.app_name1.place(x=55, y=165)

        # This frame widget is to highlight the label widget that has a tip on how to navigate the city gym app
        self.left_style_bar_dot1 = customtkinter.CTkFrame(self.frame_top1, width=8, height=8, fg_color= "#F8F3F3", bg_color="#383838", corner_radius=30, border_color="#7F7F7F")
        self.left_style_bar_dot1.place(x=35, y=182)

        # This label displays a tip for navigating the City Gym app
        self.app_name1 = customtkinter.CTkLabel(self.frame_top1, text="Always Submit after a change is made to a members details             ", font=("italic",15), fg_color="#383838", text_color="#F8F3F3", height=40)
        self.app_name1.place(x=55, y=195)

        # This frame widget is to highlight the label widget that has a tip on how to navigate the city gym app
        self.left_style_bar_dot1 = customtkinter.CTkFrame(self.frame_top1, width=8, height=8, fg_color= "#F8F3F3", bg_color="#383838", corner_radius=30, border_color="#7F7F7F")
        self.left_style_bar_dot1.place(x=35, y=212)

        # This label displays a tip for navigating the City Gym app
        self.app_name1 = customtkinter.CTkLabel(self.frame_top1, text="In the Membership Registration window make sure all fields are selected                           ", font=("italic",15), fg_color="#383838", text_color="#F8F3F3", height=40)
        self.app_name1.place(x=55, y=225)

        # This frame widget is to highlight the label widget that has a tip on how to navigate the city gym app
        self.left_style_bar_dot1 = customtkinter.CTkFrame(self.frame_top1, width=8, height=8, fg_color= "#F8F3F3", bg_color="#383838", corner_radius=30, border_color="#7F7F7F")
        self.left_style_bar_dot1.place(x=35, y=242)

        # This label displays a tip for navigating the City Gym app
        self.app_name1 = customtkinter.CTkLabel(self.frame_top1, text="In the Fitness Class Registration window, only Members can register for fitness classes                  ", font=("italic",15), fg_color="#383838", text_color="#F8F3F3", height=40)
        self.app_name1.place(x=55, y=255)

        # This frame widget is to highlight the label widget that has a tip on how to navigate the city gym app    
        self.left_style_bar_dot1 = customtkinter.CTkFrame(self.frame_top1, width=8, height=8, fg_color= "#F8F3F3", bg_color="#383838", corner_radius=30, border_color="#7F7F7F")
        self.left_style_bar_dot1.place(x=35, y=272)

        # This label displays a tip for navigating the City Gym app
        self.app_name1 = customtkinter.CTkLabel(self.frame_top1, text="In the Search Member window, if you cant find a member try a different search criteria                ", font=("italic",15), fg_color="#383838", text_color="#F8F3F3", height=40)
        self.app_name1.place(x=55, y=285)

        # This frame widget is to highlight the label widget that has a tip on how to navigate the city gym app
        self.left_style_bar_dot1 = customtkinter.CTkFrame(self.frame_top1, width=8, height=8, fg_color= "#F8F3F3", bg_color="#383838", corner_radius=30, border_color="#7F7F7F")
        self.left_style_bar_dot1.place(x=35, y=302)

        # This label displays a tip for navigating the City Gym app
        self.app_name1 = customtkinter.CTkLabel(self.frame_top1, text="The exit button in all windows will return you to the main menu and the main menu exit will close the app            ", font=("italic",15), fg_color="#383838", text_color="#F8F3F3", height=40)
        self.app_name1.place(x=55, y=315)

        # This frame widget is to highlight the label widget that has a tip on how to navigate the city gym app
        self.left_style_bar_dot1 = customtkinter.CTkFrame(self.frame_top1, width=8, height=8, fg_color= "#F8F3F3", bg_color="#383838", corner_radius=30, border_color="#7F7F7F")
        self.left_style_bar_dot1.place(x=35, y=332)

        # This label displays a tip for navigating the City Gym app
        self.app_name1 = customtkinter.CTkLabel(self.frame_top1, text="If any errors occur, follow the onscreen prompt                ", font=("italic",15), fg_color="#383838", text_color="#F8F3F3", height=10)
        self.app_name1.place(x=55, y=355)

        # This frame widget is to highlight the label widget that has a tip on how to navigate the city gym app
        self.left_style_bar_dot1 = customtkinter.CTkFrame(self.frame_top1, width=8, height=8, fg_color= "#F8F3F3", bg_color="#383838", corner_radius=30, border_color="#7F7F7F")
        self.left_style_bar_dot1.place(x=35, y=362)

        # This label displays a tip for navigating the City Gym app
        self.app_name1 = customtkinter.CTkLabel(self.frame_top1, text="In the Member Search Window you can alter the members basic details,             ", font=("italic",15), fg_color="#383838", text_color="#F8F3F3", height=10)
        self.app_name1.place(x=55, y=385)

        # This frame widget is to highlight the label widget that has a tip on how to navigate the city gym app
        self.left_style_bar_dot1 = customtkinter.CTkFrame(self.frame_top1, width=8, height=8, fg_color= "#F8F3F3", bg_color="#383838", corner_radius=30, border_color="#7F7F7F")
        self.left_style_bar_dot1.place(x=35, y=392)

        # This label displays a tip for navigating the City Gym app
        self.app_name1 = customtkinter.CTkLabel(self.frame_top1, text="In all windows, use the reset button to clear all fields easily                 ", font=("italic",15), fg_color="#383838", text_color="#F8F3F3", height=10)
        self.app_name1.place(x=55, y=415)

        # This frame widget is to highlight the label widget that has a tip on how to navigate the city gym app
        self.left_style_bar_dot1 = customtkinter.CTkFrame(self.frame_top1, width=8, height=8, fg_color= "#F8F3F3", bg_color="#383838", corner_radius=30, border_color="#7F7F7F")
        self.left_style_bar_dot1.place(x=35, y=422)

        # This label displays a tip for navigating the City Gym app
        self.app_name1 = customtkinter.CTkLabel(self.frame_top1, text="If there is a issue with the software please call 027 527 2728                 ", font=("italic",15), fg_color="#383838", text_color="#F8F3F3", height=40)
        self.app_name1.place(x=55, y=625)

        # This frame widget is to highlight the label widget that has a tip on how to navigate the city gym app
        self.left_style_bar_dot1 = customtkinter.CTkFrame(self.frame_top1, width=8, height=8, fg_color= "#F8F3F3", bg_color="#383838", corner_radius=30, border_color="#7F7F7F")
        self.left_style_bar_dot1.place(x=35, y=642)

        #=======================================================================================================================================================================================================================================================================================================================================================================================================

        # Exit Button calls the close_gui function and withdraws the page and returns the user to the main screen navigation page  
        self.exit_button = customtkinter.CTkButton(master=self.frame_top1, text="Exit ", font=("italic", 16), fg_color="#383838", text_color="#FFFAF0", corner_radius=30, width=200, height=45 ,border_spacing=0, border_width=3, command= lambda: self.close_gui())
        self.exit_button.place(x=755, y=681)

        #=======================================================================================================================================================================================================================================================================================================================================================================================================

#=======================================================================================================================================================================================================================================================================================================================================================================================================
    # Exit Funtion
    def close_gui(self):
        self.helpwindow.withdraw()


#=======================================================================================================================================================================================================================================================================================================================================================================================================




        



