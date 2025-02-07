#!/usr/bin/python3
import tkinter as tk
from tkinter import filedialog
import admin_camera_app as aCA
import register_personnel as rP
import register_student as rS
import register_visitor as rV
import os
import sys


class AddSelectorApp:
    def __init__(self, vid_source, admin_hom, condition, refresh):

        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        # Color ------------
        self.sub_complimentary_color = "#808080" #gray
        self.main_color = "#0072bc" #Blue
        self.sub_color = "#FFF875" #light Yellow
        self.complimentary_color_1 = "#E7E7E7" #light  gray
        self.complimentary_color_2 = "#F7FAE9" #Cream Color
        self.hover_color = "#FFF200" #pure Yellow
        # Color ------------
        self.video_source = vid_source
        self.admin_home_window = admin_hom
        self.window_will_open = condition
        self.refresh_func = refresh
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        # build ui
        self.add_select_app = tk.Toplevel()
        self.add_select_app.configure(background=self.main_color, height=200, width=200)
        self.add_select_app.geometry("500x400")
        self.add_select_app.resizable(False, False)
        self.add_select_app.title("SeekU - Camera")
        self.add_select_app.iconbitmap(".\SeekU\SeekU.ico")

        self.add_select_frame2 = tk.Frame(self.add_select_app)
        self.add_select_frame2.configure(background=self.main_color, height=200, width=200)
        self.capture_n_save_button = tk.Button(self.add_select_frame2)
        self.capture_n_save_button.configure(
            background=self.complimentary_color_2,
            default="active",
            font="{arial Black} 20 {}",
            foreground=self.main_color,
            justify="center",
            relief="ridge",
            text="Capture and Save",
            width=10,
        )
        self.capture_n_save_button.place(
            anchor="center", relheight=0.175, relwidth=0.55, relx=0.5, rely=0.45
        )
        self.capture_n_save_button.bind(
            "<ButtonPress>", self.capture_and_save_press, add=""
        )
        self.save_button = tk.Button(self.add_select_frame2)
        self.save_button.configure(
            background=self.complimentary_color_2,
            default="active",
            font="{arial Black} 24 {}",
            foreground=self.main_color,
            justify="center",
            relief="ridge",
            text="Save",
            width=10,
        )
        self.save_button.place(
            anchor="center", relheight=0.175, relwidth=0.55, relx=0.5, rely=0.7
        )
        self.save_button.bind("<ButtonPress>", self.save_press, add="")
        self.reminder_label = tk.Label(self.add_select_frame2)
        self.reminder_label.configure(
            background=self.main_color,
            font="{lucida} 10 {}",
            foreground=self.complimentary_color_2,
            text="client should already have a photo on the data set.",
        )
        self.reminder_label.place(anchor="center", relx=0.5, rely=0.825)
        self.add_select_frame2.place(
            anchor="center", relheight=1.0, relwidth=1.0, relx=0.5, rely=0.5
        )
        self.add_select_frame = tk.Frame(self.add_select_app)
        self.add_select_frame.configure(background=self.complimentary_color_2, height=200, width=200)
        self.seeku_logo = tk.Label(self.add_select_frame)
        self.img_SeekUsmall = tk.PhotoImage(file=".\SeekU\SeekU small.png")
        self.seeku_logo.configure(
            background=self.complimentary_color_2, image=self.img_SeekUsmall, text="label1"
        )
        self.seeku_logo.place(anchor="center", relx=0.3, rely=0.5)
        self.app_name_label = tk.Label(self.add_select_frame)
        self.img_SeekULogotypemicro = tk.PhotoImage(
            file=".\SeekU\SeekU Logotype micro.png"
        )
        self.app_name_label.configure(
            background=self.complimentary_color_2,
            font="{arial black} 40 {}",
            foreground=self.main_color,
            image=self.img_SeekULogotypemicro,
            relief="flat",
            text="SEEK",
        )
        self.app_name_label.place(anchor="center", relx=0.65, rely=0.5)
        self.add_select_frame.place(
            anchor="center", relheight=0.25, relwidth=1, relx=0.5, rely=0.125
        )
        self.add_select_frame3 = tk.Frame(self.add_select_app)
        self.add_select_frame3.configure(background=self.complimentary_color_2, height=200, width=200)
        self.return_label = tk.Label(self.add_select_frame3)
        self.return_label.config(
            background=self.complimentary_color_2,
            font="{arial} 12 {}",
            foreground=self.main_color,
            relief="flat",
            text="Return",
        )
        self.return_label.place(anchor="center", relx=0.1, rely=0.5)
        self.return_label.bind("<1>", self.return_press, add="")
        self.return_label.bind("<Enter>", self.return_hover, add="")
        self.return_label.bind("<Leave>", self.return_hover_out, add="")

        self.add_select_frame3.place(
            anchor="center", relheight=0.1, relwidth=1, relx=0.5, rely=0.95
        )

        self.disable_save_only()
        # Main widget
        self.mainwindow = self.add_select_app
        self.center(self.mainwindow)
        self.mainwindow.protocol("WM_DELETE_WINDOW", self.exit_window)
        self.mainwindow.attributes("-topmost", True)
        self.mainwindow.grab_set()

    # this function will destroy the window and closes the system/program.
    def exit_window(self):
        self.show_home_window()

    # this function will hide the window after logging in.
    def hide_this_window(self):
        self.add_select_app.withdraw()
        self.admin_home_window.withdraw()
    # this function will return to the login window
    def show_home_window(self):
        self.add_select_app.grab_release()
        self.admin_home_window.deiconify()
        self.add_select_app.destroy()

    def disable_save_only(self):
        if self.window_will_open == "Manage Visitors":
            self.save_button.configure(state="disabled")

    def capture_save_clients_logic(self):
        saveonly = False
        folder = self.select_folder()
        if folder:
            aCA.CameraApp(
                self.video_source,
                self.add_select_app,
                self.admin_home_window,
                folder,
                self.window_will_open,
                self.refresh_func,
                saveonly,
            )
            self.add_select_app.grab_release()
            self.hide_this_window()

    def save_clients_logic(self):
        saveonly = True
        folder = self.select_folder()
        if folder:
            if self.window_will_open == "Manage Students":
                rS.RegisterStudentApp(self.add_select_app,self.admin_home_window, folder,saveonly,self.refresh_func, self.window_will_open)
            elif self.window_will_open == "Manage Personnels":
                rP.RegisterPersonnelApp(self.add_select_app,self.admin_home_window, folder,saveonly,self.refresh_func, self.window_will_open)    
            self.add_select_app.grab_release()
            self.hide_this_window()
            

    def select_folder(self):
        self.mainwindow.attributes("-topmost", False)
        dialog_parent = tk.Toplevel(self.mainwindow)
        dialog_parent.withdraw()
        dialog_parent.grab_set()
        folder_select = filedialog.askdirectory(title="Select Folder")
        if folder_select == "":
            folder_select = False
            dialog_parent.grab_release()
            dialog_parent.destroy()
            self.mainwindow.grab_set()
            return folder_select
        else:
            dialog_parent.grab_release()
            dialog_parent.destroy()
            return folder_select

    # this function will center the window
    def center(self, win):
        win.update()
        w_req, h_req = win.winfo_width(), win.winfo_height()
        w_form = win.winfo_rootx() - win.winfo_x()
        w = w_req + w_form * 2
        h = h_req + (win.winfo_rooty() - win.winfo_y()) + w_form
        x = (win.winfo_screenwidth() // 2) - (w // 2)
        y = (win.winfo_screenheight() // 2) - (h // 2)
        win.geometry("{0}x{1}+{2}+{3}".format(w_req, h_req, x, y))

    def capture_and_save_press(self, event=None):
        self.capture_save_clients_logic()

    def save_press(self, event=None):
        if self.window_will_open == "Manage Visitors":
            pass
        else:
            self.save_clients_logic()

    def return_press(self, event=None):
        self.show_home_window()

    def return_hover(self, event=None):
        self.return_label.configure(font="{arial} 12 {bold}")

    def return_hover_out(self, event=None):
        self.return_label.configure(font="{arial} 12 {}")
