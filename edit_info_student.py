#!/usr/bin/python3
import tkinter as tk
import Treeview_table_mod as tbl
import tkinter.messagebox as messbx
import query_mod as qry
import PIL.Image, PIL.ImageTk
import admin_camera_app as aCA
import sys
import os
import re


class EditStudentApp:
    def __init__(
        self,
        sn,
        sfn,
        sln,
        sm,
        sp,
        ss,
        scn,
        sa,
        sstat,
        vid_source,
        admin_win,
        img_path,
        select,
        refresh,
        this_is_archive
    ):

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
        self.admin_home_window = admin_win
        self.img_path = img_path
        self.student_number = sn
        self.student_firstname = sfn
        self.student_lastname = sln
        self.student_middlename = sm
        self.student_program = sp
        self.student_section = ss
        self.student_contact_number = scn
        self.student_address = sa
        self.student_status = sstat
        self.first_stat = sstat
        self.treeview = tbl.TreeviewGUI()
        self.sql_query = qry.dbQueries()
        self.edit_bool = True
        self.client = select
        self.refresh_func = refresh
        self.this_is_archived = this_is_archive
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        # build ui
        self.edit_student_app = tk.Toplevel()
        self.edit_student_app.configure(background=self.complimentary_color_2, height=200, width=200)
        width = self.edit_student_app.winfo_screenwidth()
        height = self.edit_student_app.winfo_screenheight()
        self.edit_student_app.geometry("%dx%d" % (width, height))
        self.edit_student_app.resizable(False, False)
        self.edit_student_app.title("SeekU - Admin Edit Student Info")
        self.edit_student_app.iconbitmap(".\SeekU\SeekU.ico")
        # Contains-the-camera-canvas---------------------------------------------------------------------------------------------------------
        self.edit_stud_frame4 = tk.Frame(self.edit_student_app)
        self.edit_stud_frame4.configure(background=self.main_color, height=200, width=200)
        self.camera_canvas = tk.Canvas(self.edit_stud_frame4)
        self.camera_canvas.configure(
            background=self.main_color, highlightbackground=self.main_color
        )
        self.camera_canvas.place(
            anchor="center", relheight=1.0, relwidth=1.0, relx=0.5, rely=0.5, x=0, y=0
        )
        self.camera_canvas.bind("<1>", self.change_pic, add="")
        self.edit_stud_frame4.place(
            anchor="center", relheight=0.50, relwidth=0.50, relx=0.65, rely=0.47
        )
        # Contains-the-camera-canvas---------------------------------------------------------------------------------------------------------
        # Contains-return-button-the-app-name-logotype-and-app-logo---------------------------------------------------------------------------------------------------------
        self.edit_stud_frame3 = tk.Frame(self.edit_student_app)
        self.edit_stud_frame3.configure(background=self.complimentary_color_2, height=200, width=200)
        self.app_name_logo = tk.Label(self.edit_stud_frame3)
        self.img_SeekULogotypesmall = tk.PhotoImage(
            file=".\SeekU\SeekU Logotype small.png"
        )
        self.app_name_logo.configure(
            anchor="w",
            background=self.complimentary_color_2,
            font="{arial black} 100 {}",
            foreground=self.main_color,
            image=self.img_SeekULogotypesmall,
            justify="left",
            text="SEEK",
        )
        self.app_name_logo.place(anchor="center", relx=0.60, rely=0.5)
        self.app_logo_label = tk.Label(self.edit_stud_frame3)
        self.img_SeekUlarge = tk.PhotoImage(file=".\SeekU\SeekU large.png")
        self.app_logo_label.configure(
            background=self.complimentary_color_2, image=self.img_SeekUlarge, text="label1"
        )
        self.app_logo_label.place(anchor="center", relx=0.32, rely=0.5)
        self.return_button = tk.Button(self.edit_stud_frame3)
        self.return_button.configure(
            background=self.main_color,
            font="{arial} 20 {bold}",
            foreground="#ffffff",
            text="Return",
        )
        self.return_button.place(anchor="center", relx=0.935, rely=0.85, x=0, y=0)
        self.return_button.bind("<1>", self.return_func, add="")

        self.revert_button = tk.Button(self.edit_stud_frame3)
        self.revert_button.configure(
            background=self.main_color,
            font="{arial} 20 {bold}",
            foreground="#ffffff",
            text="Revert Pic",
        )
        self.revert_button.place(anchor="center", relx=0.914, rely=0.5)
        self.revert_button.bind("<1>", self.revert_pic_func, add="")

        self.edit_stud_frame3.place(
            anchor="center", relheight=0.25, relwidth=0.61, relx=0.65, rely=0.85
        )
        # Contains-return-button-the-app-name-logotype-and-app-logo---------------------------------------------------------------------------------------------------------
        # Contains-register-button-the-entry-widgets---------------------------------------------------------------------------------------------------------
        self.edit_stud_frame2 = tk.Frame(self.edit_student_app)
        self.edit_stud_frame2.configure(background=self.complimentary_color_2, height=200, width=200)
        self.edit_stud_label = tk.Label(self.edit_stud_frame2)
        self.edit_stud_label.configure(
            background=self.complimentary_color_2, font="{arial} 28 {bold}", text="Edit Student"
        )
        self.edit_stud_label.place(anchor="center", relx=0.5, rely=0.05, x=0, y=0)
        self.student_num_label = tk.Label(self.edit_stud_frame2)
        self.student_num_label.configure(
            background=self.complimentary_color_2,
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Student No.",
        )
        self.student_num_label.place(anchor="center", relx=0.33, rely=0.10, x=0, y=0)
        self.student_num_entry = tk.Entry(self.edit_stud_frame2)
        self.student_num_entry.configure(font="{arial} 20 {}")
        self.student_num_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.14, x=0, y=0
        )
        # rely minus.025
        self.first_name_label = tk.Label(self.edit_stud_frame2)
        self.first_name_label.configure(
            background=self.complimentary_color_2,
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="First Name",
        )
        self.first_name_label.place(anchor="center", relx=0.32, rely=0.19, x=0, y=0)
        self.first_name_entry = tk.Entry(self.edit_stud_frame2)
        self.first_name_entry.configure(font="{arial} 20 {}")
        self.first_name_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.23, x=0, y=0
        )
        self.mid_name_label = tk.Label(self.edit_stud_frame2)
        self.mid_name_label.configure(
            background=self.complimentary_color_2,
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Middle Name",
        )
        self.mid_name_label.place(anchor="center", relx=0.345, rely=0.275, x=0, y=0)
        self.mid_name_entry = tk.Entry(self.edit_stud_frame2)
        self.mid_name_entry.configure(font="{arial} 20 {}")
        self.mid_name_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.315, x=0, y=0
        )
        self.last_name_label = tk.Label(self.edit_stud_frame2)
        self.last_name_label.configure(
            background=self.complimentary_color_2,
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Last Name",
        )
        self.last_name_label.place(anchor="center", relx=0.32, rely=0.36, x=0, y=0)
        self.last_name_entry = tk.Entry(self.edit_stud_frame2)
        self.last_name_entry.configure(font="{arial} 20 {}")
        self.last_name_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.40, x=0, y=0
        )
        self.program_label = tk.Label(self.edit_stud_frame2)
        self.program_label.configure(
            background=self.complimentary_color_2,
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Program",
        )
        self.program_label.place(anchor="center", relx=0.295, rely=0.45, x=0, y=0)
        self.program_entry = tk.Entry(self.edit_stud_frame2)
        self.program_entry.configure(font="{arial} 20 {}")
        self.program_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.49, x=0, y=0
        )
        self.section_label = tk.Label(self.edit_stud_frame2)
        self.section_label.configure(
            background=self.complimentary_color_2,
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Section",
        )
        self.section_label.place(anchor="center", relx=0.28, rely=0.535, x=0, y=0)
        self.section_entry = tk.Entry(self.edit_stud_frame2)
        self.section_entry.configure(font="{arial} 20 {}")
        self.section_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.575, x=0, y=0
        )
        self.contact_num_label = tk.Label(self.edit_stud_frame2)
        self.contact_num_label.configure(
            background=self.complimentary_color_2,
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Contact No.",
        )
        self.contact_num_label.place(anchor="center", relx=0.33, rely=0.62, x=0, y=0)
        self.contact_num_entry = tk.Entry(self.edit_stud_frame2)
        self.contact_num_entry.configure(font="{arial} 20 {}")
        self.contact_num_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.66, x=0, y=0
        )
        self.address_label = tk.Label(self.edit_stud_frame2)
        self.address_label.configure(
            background=self.complimentary_color_2,
            cursor="arrow",
            font="{arial} 20 {bold}",
            text="Address",
        )
        self.address_label.place(anchor="center", relx=0.295, rely=0.705, x=0, y=0)
        self.address_entry = tk.Entry(self.edit_stud_frame2)
        self.address_entry.configure(font="{arial} 20 {}")
        self.address_entry.place(
            anchor="center", relwidth=0.62, relx=0.5, rely=0.745, x=0, y=0
        )
        self.user_status_label = tk.Label(self.edit_stud_frame2)
        self.user_status_label.configure(
            background=self.complimentary_color_2, font="{arial} 20 {bold}", text="Student Status"
        )
        self.user_status_label.place(anchor="center", relx=0.370, rely=0.8, x=0, y=0)
        # variable for the radiobuttons, to connect them
        self.stat_var = tk.StringVar()
        self.stat_var.set(self.student_status)
        self.active_radiobutton = tk.Radiobutton(self.edit_stud_frame2)
        self.active_radiobutton.configure(
            background=self.complimentary_color_2,
            font="{arial} 18 {}",
            text="Active",
            variable=self.stat_var,
            value="IsActive",
        )
        self.active_radiobutton.place(anchor="center", relx=0.4, rely=0.85, x=0, y=0)
        self.inactive_radiobutton = tk.Radiobutton(self.edit_stud_frame2)
        self.inactive_radiobutton.configure(
            background=self.complimentary_color_2,
            font="{arial} 18 {}",
            text="Archive",
            variable=self.stat_var,
            value="IsArchived",
        )
        self.inactive_radiobutton.place(anchor="center", relx=0.6, rely=0.85, x=0, y=0)
        self.save_changes_button = tk.Button(self.edit_stud_frame2)
        self.save_changes_button.configure(
            background=self.main_color,
            font="{arial} 20 {bold}",
            foreground="#ffffff",
            text="Save",
        )
        self.save_changes_button.place(anchor="center", relx=0.70, rely=0.92, x=0, y=0)
        self.save_changes_button.bind("<1>", self.save_student, add="")
        self.edit_changes_button = tk.Button(self.edit_stud_frame2)
        self.edit_changes_button.configure(
            background=self.main_color,
            font="{arial} 20 {bold}",
            foreground="#ffffff",
            text="Edit",
        )
        self.edit_changes_button.place(anchor="center", relx=0.30, rely=0.92, x=0, y=0)
        self.edit_changes_button.bind("<1>", self.edit_student, add="")
        self.edit_stud_frame2.place(
            anchor="center", relheight=0.86, relwidth=0.35, relx=0.18, rely=0.565
        )
        # Contains-register-button-the-entry-widgets---------------------------------------------------------------------------------------------------------
        # Contains-school-logo-------------------------------------------------------------------------------------------------------------------------------------
        self.edit_stud_frame1 = tk.Frame(self.edit_student_app)
        self.edit_stud_frame1.configure(background=self.sub_color, height=200, width=200)
        self.school_logo_label = tk.Label(self.edit_stud_frame1)
        self.img_STICollegeBalagtasLogomedium = tk.PhotoImage(
            file=".\SeekU\STI College Balagtas Logo medium.png"
        )
        self.school_logo_label.configure(
            background=self.sub_color,
            image=self.img_STICollegeBalagtasLogomedium,
            text="label1",
        )
        self.school_logo_label.place(anchor="center", relx=0.25, rely=0.5)
        self.edit_stud_frame1.place(
            anchor="center", relheight=0.13, relwidth=1.0, relx=0.5, rely=0.065
        )
        # Contains-school-logo-------------------------------------------------------------------------------------------------------------------------------------
        self.disp_pic()
        self.put_info()
        self.disable_entry()
        self.hide_revert_button()
        # Main widget
        self.mainwindow = self.edit_student_app
        # will set the window to fullscreen
        self.mainwindow.wm_attributes("-fullscreen", "True")
        # this protocol will do a function after pressing the close button.
        self.mainwindow.protocol("WM_DELETE_WINDOW", self.exit_program)

    # this function will destroy the window and closes the system/program.
    def exit_program(self):
        sys.exit()

    def hide_revert_button(self):
        self.revert_button.place_forget()

    def show_revert_button(self):
        self.revert_button.place(anchor="center", relx=0.914, rely=0.5)

    # this will return to the camera app
    def show_home_win(self):
        self.admin_home_window.deiconify()
        if self.this_is_archived:
            self.refresh_func(self.client, "IsArchived")
        else:
            self.refresh_func(self.client, "IsActive")
        self.edit_student_app.destroy()

    def hide_this_window(self):
        self.edit_student_app.withdraw()

    # this function will destroy the current window and return to camera app
    def show_cam_app_window(self):
        self.hide_this_window()
        aCA.CameraEditApp(
            self.disp_temp_pic, self.video_source, self.edit_student_app, self.img_path
        )

    def put_info(self):
        self.select_student()

    # enables entry widgets
    def disable_entry(self):
        self.address_entry.configure(state="disabled")
        self.mid_name_entry.configure(state="disabled")
        self.last_name_entry.configure(state="disabled")
        self.first_name_entry.configure(state="disabled")
        self.contact_num_entry.configure(state="disabled")
        self.student_num_entry.configure(state="disabled")
        self.program_entry.configure(state="disabled")
        self.section_entry.configure(state="disabled")
        self.active_radiobutton.configure(state="disabled")
        self.inactive_radiobutton.configure(state="disabled")

    # enables entry widgets
    def enable_entry(self):
        self.address_entry.configure(state="normal")
        self.mid_name_entry.configure(state="normal")
        self.last_name_entry.configure(state="normal")
        self.first_name_entry.configure(state="normal")
        self.contact_num_entry.configure(state="normal")
        self.program_entry.configure(state="normal")
        self.section_entry.configure(state="normal")
        self.active_radiobutton.configure(state="normal")
        self.inactive_radiobutton.configure(state="normal")

    def select_student(self):
        self.student_num_entry.insert(0, self.student_number)
        self.first_name_entry.insert(0, self.student_firstname)
        self.last_name_entry.insert(0, self.student_lastname)
        self.mid_name_entry.insert(0, self.student_middlename)
        self.program_entry.insert(0, self.student_program)
        self.section_entry.insert(0, self.student_section)
        self.contact_num_entry.insert(0, self.student_contact_number)
        self.address_entry.insert(0, self.student_address)

    def save_student_function(self):
        student_num_var = self.student_num_entry.get()
        student_firstname_var = self.first_name_entry.get()
        student_lastname_var = self.last_name_entry.get()
        student_middlename_var = self.mid_name_entry.get()
        student_program_var = self.program_entry.get()
        student_section_var = self.section_entry.get()
        student_contact_num_var = self.contact_num_entry.get()
        student_address_var = self.address_entry.get()
        student_status_var = self.stat_var.get()

        if (
            len(student_num_var) != 0
            and len(student_firstname_var) != 0
            and len(student_lastname_var) != 0
            and len(student_contact_num_var) != 0
            and len(student_program_var) != 0
            and len(student_section_var) != 0
            and len(student_address_var) != 0
            ):
            input_values = [
                student_num_var,
                student_firstname_var,
                student_lastname_var,
                student_middlename_var,
                student_program_var,
                student_section_var,
                student_contact_num_var,
                student_address_var,
                student_status_var,
            ]
            concatenated_inputs = "".join(input_values)
            pattern = re.compile("[^a-zA-Z0-9 .,-ñÑ]")

            if not pattern.search(concatenated_inputs):
                if student_num_var.isdigit() or (
                    student_num_var.startswith("-") and student_num_var[1:].isdigit()
                    ):
                    if ((student_contact_num_var.isdigit() or 
                        student_contact_num_var.startswith("-")
                        and student_contact_num_var[1:].isdigit())
                        and len(student_contact_num_var) == 10
                        ):
                        if ((student_firstname_var.replace(" ", "").isalpha()  or "-" in student_firstname_var) 
                            and( student_middlename_var.replace(" ", "").isalpha()or student_middlename_var == "" or "-" in student_middlename_var) 
                            and (student_lastname_var.replace(" ", "").isalpha() or "-" in student_lastname_var)
                            and (student_program_var.replace(" ", "").isalpha() or "-" in student_program_var)):
                            
                            path_check = self.img_path + "/000000000.jpg"
                            result = messbx.askokcancel("Confirm Action","Please review all the details you have inputted. Are you sure everything is final and correct?")
                            if result:
                                if os.path.exists(path_check):
                                    img_name = student_num_var
                                    os.remove(self.img_path + "/" + img_name + ".jpg")
                                    os.rename(
                                        path_check,
                                        self.img_path + "/" + img_name + ".jpg",
                                    )
                                    self.sql_query.update_student(
                                        student_num_var,
                                        student_firstname_var,
                                        student_lastname_var,
                                        student_middlename_var,
                                        student_program_var,
                                        student_section_var,
                                        student_contact_num_var,
                                        student_address_var,
                                        student_status_var,
                                    )
                                    messbx.showinfo(
                                        "Success",
                                        "The student's record has been successfully updated.",
                                    )
                                else:
                                    self.sql_query.update_student(
                                        student_num_var,
                                        student_firstname_var,
                                        student_lastname_var,
                                        student_middlename_var,
                                        student_program_var,
                                        student_section_var,
                                        student_contact_num_var,
                                        student_address_var,
                                        student_status_var,
                                    )
                                    messbx.showinfo(
                                        "Success",
                                        "The student's record has been successfully updated.",
                                    )

                        else:
                            messbx.showwarning(
                                "Warning",
                                "There is an invalid character in the input for the name or program of the student.",
                            )
                    else:
                        messbx.showwarning(
                            "Warning",
                            "The provided input for the contact number is "+
                            "invalid and does not correspond to a valid number.",
                        )
                else:
                    messbx.showwarning(
                        "Warning",
                        "The provided input for the student number is "+
                        "invalid and does not correspond to a valid number.",
                    )
            else:
                messbx.showwarning("Warning", "The input contains special characters.")
        else:
            messbx.showwarning(
                "Warning", "Kindly ensure all fields are filled by entering a value."
            )

    # this function will display the image into the canvas
    def disp_pic(self):
        self.load_image = PIL.Image.open(
            self.img_path + "/" + self.student_number + ".jpg"
        )
        # will use the ImageTK.PhotoImage() function to set the image
        # as a readable image.
        self.resized_image = self.load_image.resize((854, 480), PIL.Image.ANTIALIAS)
        self.student_image = PIL.ImageTk.PhotoImage(self.resized_image)
        # will display the image into the canvas
        self.camera_canvas.create_image(0, 0, image=self.student_image, anchor=tk.NW)

    def disp_temp_pic(self):
        self.show_revert_button()
        self.load_image = PIL.Image.open(self.img_path + "/000000000.jpg")
        # will use the ImageTK.PhotoImage() function to set the image
        # as a readable image.
        self.resized_image = self.load_image.resize((854, 480), PIL.Image.ANTIALIAS)
        self.student_image = PIL.ImageTk.PhotoImage(self.resized_image)
        # will display the image into the canvas
        self.camera_canvas.create_image(0, 0, image=self.student_image, anchor=tk.NW)

    def edit_student(self, event=None):
        # enables and disables the entry and optionmenu
        if self.edit_bool == True:
            self.enable_entry()
            self.edit_bool = False
        elif self.edit_bool == False:
            self.disable_entry()
            self.edit_bool = True

    def save_student(self, event=None):
        self.save_student_function()
        # save infos

    # this command will open the camera app
    def change_pic(self, event=None):
        self.show_cam_app_window()

    def revert_pic_func(self, event=None):
        self.disp_pic()
        self.hide_revert_button()
        if os.path.exists(self.img_path + "/000000000.jpg"):
            os.remove(self.img_path + "/000000000.jpg")

    def return_func(self, event=None):
        self.show_home_win()
        if os.path.exists(self.img_path + "/000000000.jpg"):
            os.remove(self.img_path + "/000000000.jpg")
