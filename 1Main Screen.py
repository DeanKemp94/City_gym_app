import tkinter as Tk
from tkinter import *
import customtkinter
import Registration
import Help
import Fitness
import Search
from tkinter import ttk

# This is setting the root window 
root = customtkinter.CTk()

# This is setting the window name 
root.title("City Gym App")

# This section takes the width and hight of the window and devides by two to be able to center the page 
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
x_position = (width/2) - (985/2)
y_position = (height/2) - (750/2)
root.geometry("985x750+{}+{}".format(int(x_position), int(y_position)))

#This is setting the appearance of the overall gui app 
customtkinter.set_appearance_mode("light")

#Class name 
class Main_Screen:
    
    # This will initiate the gui and get called when app is run 
    def __init__(self, master):
        # Frames that make up the background, foreground, that all of the widgets are contained in=======================================================================================================================================================================================================================================================================================================================================================================================================
        backround_frame = customtkinter.CTkFrame(master = root, width=985, height=690, fg_color= "#262626", corner_radius=30, bg_color="#262626")
        backround_frame.pack(fill='both', expand=True)

        frame_top = customtkinter.CTkFrame(backround_frame, width=985, height=740, fg_color= "#262626", corner_radius=30, bg_color="#262626", border_color="#FFE4C4", border_width=3)
        frame_top.pack()

        main_menu_background = customtkinter.CTkFrame(frame_top, width=300, height=30, fg_color= "#383838", corner_radius=30,bg_color="#262626", border_width=3, border_color="#7F7F7F")
        main_menu_background.place(x=335, y=60)

        # This is the frame that contained the "main screen" label
        main_menu_header = customtkinter.CTkLabel(frame_top, text="Main Screen", font=("italic",15), fg_color="#383838", text_color="#F8F3F3", height=20)
        main_menu_header.place(x=440, y=65)

        # This is the main heading 
        app_name1 = customtkinter.CTkLabel(frame_top, text='City Gym App', font=("italic",40), fg_color="#262626", text_color="#F8F3F3", height=40)
        app_name1.place(x=365, y=8)
        #==========End of Section=======================================================================================================================================================================================================================================================================================================================================================================================================


        # This section is made up of all the navigation buttons=======================================================================================================================================================================================================================================================================================================================================================================================================
        # This opens the Registration gui page by calling the file then the class
        membership_registration_button = customtkinter.CTkButton(master=frame_top, text="Membership Registration", font=("italic", 16), fg_color="#383838", text_color="#FFFAF0", corner_radius=30, width=700, height=45 ,border_spacing=0, border_width=3, command=lambda: Registration.Registration(master))
        membership_registration_button.place(x=140, y=180)

        # This opens the Search gui page by calling the file then the class
        search_form_button = customtkinter.CTkButton(master=frame_top, text="Search Member", font=("italic", 16), fg_color="#383838", text_color="#FFFAF0", corner_radius=30, width=700, height=45 ,border_spacing=0, border_width=3, command= lambda: Search.Search(master))
        search_form_button.place(x=140, y=260)

        # This opens the Fitness gui page by calling the file then the class
        fitness_form_button = customtkinter.CTkButton(master=frame_top, text="Fitness Class Registration", font=("italic", 16), fg_color="#383838", text_color="#FFFAF0", corner_radius=30, width=700, height=45 ,border_spacing=0, border_width=3, command= lambda: Fitness.Fitness(master))
        fitness_form_button.place(x=140, y=340)

        # This opens the Help gui page by calling the file then the class
        help_screen_button = customtkinter.CTkButton(master=frame_top, text="Help Screen", font=("italic", 16), fg_color="#383838", text_color="#FFFAF0", corner_radius=30, width=700, height=45 ,border_spacing=0, border_width=3, command= lambda: Help.Help(master))
        help_screen_button.place(x=140, y=420)

        # This closes the application gui
        exit_button = customtkinter.CTkButton(master=frame_top, text="Exit Application", font=("italic", 16), fg_color="#383838", text_color="#FFFAF0", corner_radius=30, width=700, height=45 ,border_spacing=0, border_width=3, command=root.quit)
        exit_button.place(x=140, y=500)
        #==========End of Section=======================================================================================================================================================================================================================================================================================================================================================================================================


        # Bar to the left and dots in it (Styling)=======================================================================================================================================================================================================================================================================================================================================================================================================

        left_style_bar = customtkinter.CTkFrame(frame_top, width=60, height=440, fg_color= "#383838", corner_radius=30, border_width=3, border_color="#7F7F7F")
        left_style_bar.place(x=115, y=140)

        left_style_bar_dot1 = customtkinter.CTkFrame(frame_top, width=30, height=30, fg_color= "#F8F3F3", bg_color="#383838", corner_radius=30, border_width=3, border_color="#7F7F7F")
        left_style_bar_dot1.place(x=130, y=185)

        left_style_bar_dot2 = customtkinter.CTkFrame(frame_top, width=30, height=30, fg_color= "#F8F3F3", bg_color="#383838", corner_radius=30, border_width=3, border_color="#7F7F7F")
        left_style_bar_dot2.place(x=130, y=265)

        left_style_bar_dot3 = customtkinter.CTkFrame(frame_top, width=30, height=30, fg_color= "#F8F3F3", bg_color="#383838", corner_radius=30, border_width=3, border_color="#7F7F7F")
        left_style_bar_dot3.place(x=130, y=345)

        left_style_bar_dot4 = customtkinter.CTkFrame(frame_top, width=30, height=30, fg_color= "#F8F3F3", bg_color="#383838", corner_radius=30, border_width=3, border_color="#7F7F7F")
        left_style_bar_dot4.place(x=130, y=425)

        left_style_bar_dot5 = customtkinter.CTkFrame(frame_top, width=30, height=30, fg_color= "#F8F3F3", bg_color="#383838", corner_radius=30, border_width=3, border_color="#7F7F7F")
        left_style_bar_dot5.place(x=130, y=505)
        #==========End of Section=======================================================================================================================================================================================================================================================================================================================================================================================================


# Loop that the gui app runs in 
main_screen = Main_Screen(root)
root.mainloop()

