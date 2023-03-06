#!/usr/bin/python3
import tkinter as tk


class EditUserApp:
    def __init__(self, master=None):
        # build ui
    #PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------

        self.edit_bool = True
    #PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
    
        self.edit_user_app = tk.Tk()
        self.edit_user_app.configure(
            background="#F7FAE9", height=200, width=200)
        self.edit_user_app.geometry("600x700")
        self.edit_user_app.resizable(False, False)
        self.edit_user_app.title("SeekU - Edit User")
        self.edit_user_app.iconbitmap(".\SeekU\SeekU.ico")
    #Contains-the-edit-label-and-entry-widgets--------------------------------------------------------------------------------------------------------- 
        self.edit_user_frame2 = tk.Frame(self.edit_user_app)
        self.edit_user_frame2.configure(
            background="#F7FAE9", height=200, width=200)
        self.edit_user_label = tk.Label(self.edit_user_frame2)
        self.edit_user_label.configure(
            background="#F7FAE9",
            font="{arial} 24 {bold}",
            text='Edit User')
        self.edit_user_label.place(
            anchor="center", relx=0.5, rely=0.05, x=0, y=0)
        self.username_label = tk.Label(self.edit_user_frame2)
        self.username_label.configure(
            background="#F7FAE9",
            font="{arial} 16 {bold}",
            text='Username')
        self.username_label.place(
            anchor="center", relx=0.385, rely=0.14, x=0, y=0)
        self.username_entry = tk.Entry(self.edit_user_frame2)
        self.username_entry.configure(font="{arial} 14 {}")
        self.username_entry.place(
            anchor="center",
            relwidth=0.4,
            relx=0.5,
            rely=0.19,
            x=0,
            y=0)
        self.password_label = tk.Label(self.edit_user_frame2)
        self.password_label.configure(
            background="#F7FAE9",
            font="{arial} 16 {bold}",
            text='Password')
        self.password_label.place(
            anchor="center", relx=0.385, rely=0.26, x=0, y=0)
        self.password_entry = tk.Entry(self.edit_user_frame2)
        self.password_entry.configure(font="{arial} 14 {}")
        self.password_entry.place(
            anchor="center",
            relwidth=0.4,
            relx=0.5,
            rely=0.31,
            x=0,
            y=0)
        self.first_name_label = tk.Label(self.edit_user_frame2)
        self.first_name_label.configure(
            background="#F7FAE9",
            font="{arial} 16 {bold}",
            text='First Name')
        self.first_name_label.place(
            anchor="center", relx=0.39, rely=0.39, x=0, y=0)
        self.first_name_entry = tk.Entry(self.edit_user_frame2)
        self.first_name_entry.configure(font="{arial} 14 {}")
        self.first_name_entry.place(
            anchor="center",
            relwidth=0.4,
            relx=0.5,
            rely=0.44,
            x=0,
            y=0)
        self.last_name_label = tk.Label(self.edit_user_frame2)
        self.last_name_label.configure(
            background="#F7FAE9",
            font="{arial} 16 {bold}",
            text='Last Name')
        self.last_name_label.place(
            anchor="center", relx=0.39, rely=0.52, x=0, y=0)
        self.last_name_entry = tk.Entry(self.edit_user_frame2)
        self.last_name_entry.configure(font="{arial} 14 {}")
        self.last_name_entry.place(
            anchor="center",
            relwidth=0.4,
            relx=0.5,
            rely=0.58,
            x=0,
            y=0)
        self.user_role_var = tk.StringVar(value='Choose User Type')
        __values = ['Security Guard', 'High Admin', 'Low Admin']
        self.user_role_optionmenu = tk.OptionMenu(
            self.edit_user_frame2, self.user_role_var, *__values, command=None)
        self.user_role_optionmenu.place(
            anchor="center",relwidth=0.4, relx=.5, rely=0.7, x=0, y=0)
        self.user_role_optionmenu.configure(font="{arial} 16",justify="left")
        self.user_role_options = self.edit_user_app.nametowidget(self.user_role_optionmenu.menuname)
        self.user_role_options.config(font="{arial} 16")
        self.user_role_label = tk.Label(self.edit_user_frame2)
        self.user_role_label.configure(
            background="#F7FAE9",
            font="{arial} 16 {bold}",
            text='User Role')
        self.user_role_label.place(
            anchor="center", relx=0.38, rely=0.64, x=0, y=0)
        self.user_status_label = tk.Label(self.edit_user_frame2)
        self.user_status_label.configure(
            background="#F7FAE9",
            font="{arial} 16 {bold}",
            text='User Status')
        self.user_status_label.place(anchor="center", relx=0.395, rely=0.76, x=0, y=0)

         # variable for the radiobuttons, to connect them
        self.stat_var = tk.StringVar()
        self.stat_var.set('Active')
        self.active_radiobutton = tk.Radiobutton(self.edit_user_frame2)
        self.active_radiobutton.configure(
            background="#F7FAE9",
            font="{arial} 14 {}",
            text='Active',
            variable = self.stat_var,
            value = 'Active')
        self.active_radiobutton.place(
            anchor="center", relx=0.4, rely=0.82, x=0, y=0)
        self.inactive_radiobutton = tk.Radiobutton(self.edit_user_frame2)
        self.inactive_radiobutton.configure(
            background="#F7FAE9",
            font="{arial} 14 {}",
            text='Inactive',
            variable = self.stat_var,
            value = 'Inactive')
        self.inactive_radiobutton.place(
            anchor="center", relx=0.6, rely=0.82, x=0, y=0)
        
        self.edit_user_button = tk.Button(self.edit_user_frame2)
        self.edit_user_button.configure(
            background="#0072bc",
            font="{arial black} 20 {}",
            foreground="#F7FAE9",
            text='Edit')
        self.edit_user_button.place(
            anchor="center",
            relheight=0.08,
            relwidth=0.27,
            relx=.3,
            rely=0.9)
        self.edit_user_button.bind(
            "<ButtonPress>", self.edit_user, add="")
        

        self.save_user_button = tk.Button(self.edit_user_frame2)
        self.save_user_button.configure(
            background="#0072bc",
            font="{arial black} 20 {}",
            foreground="#F7FAE9",
            text='Save')
        self.save_user_button.place(
            anchor="center",
            relheight=0.08,
            relwidth=0.27,
            relx=.7,
            rely=0.9)
        self.save_user_button.bind(
            "<ButtonPress>", self.edit_user, add="")
        self.edit_user_frame2.place(
            anchor="center",
            relheight=0.82,
            relwidth=1.0,
            relx=0.5,
            rely=0.59)
        self.edit_user_frame2.place(
            anchor="center",
            relheight=0.82,
            relwidth=1.0,
            relx=0.5,
            rely=0.59)
        
    #Contains-the-edit-label-and-entry-widgets--------------------------------------------------------------------------------------------------------- 
    #Contains-the-logo-and-logotype--------------------------------------------------------------------------------------------------------- 

        self.edit_user_frame1 = tk.Frame(self.edit_user_app)
        self.edit_user_frame1.configure(
            background="#fff000", height=200, width=200)
        self.school_logo_label = tk.Label(self.edit_user_frame1)
        self.img_STICollegeBalagtasLogomedium = tk.PhotoImage(
            file=".\SeekU\STI College Balagtas Logo medium.png")
        self.school_logo_label.configure(
            background="#fff000",
            image=self.img_STICollegeBalagtasLogomedium,
            text='label1')
        self.school_logo_label.place(anchor="center", relx=.25, rely=0.5)
        self.edit_user_frame1.place(
            anchor="center",
            relheight=0.17,
            relwidth=1.0,
            relx=0.5,
            rely=0.09)
    #Contains-the-logo-and-logotype--------------------------------------------------------------------------------------------------------- 

        self.disable_entry()
        # Main widget
        self.mainwindow = self.edit_user_app

    def run(self):
        self.mainwindow.mainloop()
    # disables entry widgets
    def disable_entry(self):  
        self.username_entry.configure(state='disabled') 
        self.password_entry.configure(state='disabled')    
        self.last_name_entry.configure(state='disabled')
        self.first_name_entry.configure(state='disabled')
        self.user_role_optionmenu.configure(state='disabled')
        self.active_radiobutton.configure(state='disabled')
        self.inactive_radiobutton.configure(state='disabled')
    # enables entry widgets
    def enable_entry(self):  
        self.password_entry.configure(state='normal')    
        self.last_name_entry.configure(state='normal')
        self.first_name_entry.configure(state='normal')
        self.user_role_optionmenu.configure(state='normal')
        self.active_radiobutton.configure(state='normal')
        self.inactive_radiobutton.configure(state='normal')

    # enables and disables entry
    def edit_user(self, event=None):
        if self.edit_bool == True:
            self.enable_entry()
            self.edit_bool = False
        elif self.edit_bool == False:
            self.disable_entry()
            self.edit_bool = True

    def save_user(self, event=None):
        pass


if __name__ == "__main__":
    app = EditUserApp()
    app.run()