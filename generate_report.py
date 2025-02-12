#!/usr/bin/python3
import tkinter as tk
import tkcalendar as tkc
import tkinter.messagebox as messbx
import query_mod as qry
import report_mod as rM
import Treeview_table_mod as tbl
import datetime
from tkinter import filedialog
import re


class SavePrintReportApp:
    def __init__(self, optionmenu, ufname, ulname):
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        # Color ------------
        self.sub_complimentary_color = "#808080"  # gray
        self.main_color = "#0072bc"  # Blue
        self.sub_color = "#FFF875"  # light Yellow
        self.complimentary_color_1 = "#E7E7E7"  # light  gray
        self.complimentary_color_2 = "#F7FAE9"  # Cream Color
        self.hover_color = "#FFF200"  # pure Yellow
        # Color ------------
        self.client_type = optionmenu
        self.users_firstname = ufname
        self.users_lastname = ulname
        self.today = datetime.date.today()
        self.today_day = self.today.day
        self.today_month = self.today.month
        self.today_year = self.today.year
        # self.mindate =  min date is set as when the first attendance

        self.maxdate = self.today - datetime.timedelta(days=1)  # max date is yesterday
        self.sql_query = qry.dbQueries()
        self.treeview = tbl.TreeviewGUI()
        self.excel_class = rM.excelClass()
        self.docx_class = rM.docxClass()
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.generate_report_app = tk.Toplevel()
        self.generate_report_app.configure(
            background=self.main_color, height=200, width=200
        )
        self.generate_report_app.geometry("640x700")
        self.generate_report_app.resizable(False, False)
        self.generate_report_app.title("SeekU-Save & Print-Report")
        self.generate_report_app.iconbitmap(".\SeekU\SeekU.ico")

        if self.client_type == "Students Report":
            self.gen_report_frame2 = tk.Frame(self.generate_report_app)
            self.gen_report_frame2.configure(
                background=self.main_color, height=200, width=200
            )
            self.from_label = tk.Label(self.gen_report_frame2)
            self.from_label.configure(
                background=self.main_color,
                font="{arial} 20 {}",
                foreground=self.complimentary_color_2,
                text="From",
            )
            self.from_label.place(anchor="center", relx=0.20, rely=0.23)

            self.calendar1 = tkc.Calendar(
                self.gen_report_frame2,
                selectmode="day",
                maxdate=self.maxdate,
                year=self.today_year,
                month=self.today_month,
                day=self.today_day,
            )
            self.calendar1.place(anchor="center", relx=0.25, rely=0.4)

            self.calendar2 = tkc.Calendar(
                self.gen_report_frame2,
                selectmode="day",
                maxdate=self.maxdate,
                year=self.today_year,
                month=self.today_month,
                day=self.today_day,
            )
            self.calendar2.place(anchor="center", relx=0.75, rely=0.4)

            self.to_label = tk.Label(self.gen_report_frame2)
            self.to_label.configure(
                background=self.main_color,
                font="{arial} 20 {}",
                foreground=self.complimentary_color_2,
                justify="left",
                text="To",
            )
            self.to_label.place(anchor="center", relx=0.65, rely=0.23)
            self.save_button = tk.Button(self.gen_report_frame2)
            self.save_button.configure(
                background=self.complimentary_color_2,
                default="active",
                font="{arial Black} 20 {}",
                foreground=self.main_color,
                justify="center",
                relief="ridge",
                text="Save",
                width=10,
            )
            self.save_button.place(
                anchor="center", relheight=0.09, relwidth=0.325, relx=0.5, rely=0.92
            )
            self.save_button.bind("<ButtonPress>", self.save_press, add="")
            self.section_label = tk.Label(self.gen_report_frame2)
            self.section_label.configure(
                background=self.main_color,
                font="{arial} 20 {}",
                foreground=self.complimentary_color_2,
                justify="left",
                text="Student Section",
            )
            self.section_label.place(anchor="center", relx=0.25, rely=0.59)
            self.sections_var = tk.StringVar(value="Section")
            __values = self.sql_query.get_all_sections()
            self.sections_optionmenu = tk.OptionMenu(
                self.gen_report_frame2,
                self.sections_var,
                *__values,
            )
            self.sections_optionmenu.configure(font="{arial} 20 ")
            self.sections_optionmenu.place(anchor="center", relx=0.75, rely=0.59)
            self.sections_options = self.generate_report_app.nametowidget(
                self.sections_optionmenu.menuname
            )
            self.sections_options.config(font="{arial} 16")

            self.file_type_var = tk.StringVar(value="Pdf")
            self.pdf_radiobutton = tk.Radiobutton(self.gen_report_frame2)
            self.pdf_radiobutton.configure(
                background=self.main_color,
                font="{arial} 24 {}",
                foreground=self.complimentary_color_2,
                text="Pdf",
                selectcolor="black",
                value="Pdf",
                variable=self.file_type_var,
            )
            self.pdf_radiobutton.place(
                anchor="center", relx=0.2, rely=0.7, relheight=0.05
            )
            self.docx_radiobutton = tk.Radiobutton(self.gen_report_frame2)
            self.docx_radiobutton.configure(
                background=self.main_color,
                font="{arial} 24 {}",
                foreground=self.complimentary_color_2,
                selectcolor="black",
                text="Docx",
                value="Docx",
                variable=self.file_type_var,
            )
            self.docx_radiobutton.place(
                anchor="center", relx=0.5, rely=0.7, relheight=0.05
            )
            self.excel_radiobutton = tk.Radiobutton(self.gen_report_frame2)
            self.excel_radiobutton.configure(
                background=self.main_color,
                font="{arial} 24 {}",
                foreground=self.complimentary_color_2,
                selectcolor="black",
                text="Excel",
                value="Excel",
                variable=self.file_type_var,
            )
            self.excel_radiobutton.place(
                anchor="center", relx=0.8, rely=0.7, relheight=0.05
            )

            self.file_name_label = tk.Label(self.gen_report_frame2)
            self.file_name_label.configure(
                background=self.main_color,
                font="{arial} 20 {}",
                foreground=self.complimentary_color_2,
                text="File Name",
            )
            self.file_name_label.place(anchor="center", relx=0.28, rely=0.8)
            self.file_name = tk.Entry(self.gen_report_frame2)
            self.file_name.configure(font="{arial} 20 {}")
            self.file_name.place(
                anchor="center", relwidth=0.4, relx=0.63, rely=0.8, x=0, y=0
            )
            self.gen_report_frame2.place(
                anchor="center", relheight=1.0, relwidth=1.0, relx=0.5, rely=0.5
            )
        elif self.client_type == "Personnels Report":
            self.gen_report_frame2 = tk.Frame(self.generate_report_app)
            self.gen_report_frame2.configure(
                background=self.main_color, height=200, width=200
            )
            self.from_label = tk.Label(self.gen_report_frame2)
            self.from_label.configure(
                background=self.main_color,
                font="{arial} 20 {}",
                foreground=self.complimentary_color_2,
                text="From",
            )
            self.from_label.place(anchor="center", relx=0.20, rely=0.23)

            self.calendar1 = tkc.Calendar(
                self.gen_report_frame2,
                selectmode="day",
                maxdate=self.maxdate,
                year=self.today_year,
                month=self.today_month,
                day=self.today_day,
            )
            self.calendar1.place(anchor="center", relx=0.25, rely=0.4)

            self.calendar2 = tkc.Calendar(
                self.gen_report_frame2,
                selectmode="day",
                maxdate=self.maxdate,
                year=self.today_year,
                month=self.today_month,
                day=self.today_day,
            )
            self.calendar2.place(anchor="center", relx=0.75, rely=0.4)

            self.to_label = tk.Label(self.gen_report_frame2)
            self.to_label.configure(
                background=self.main_color,
                font="{arial} 20 {}",
                foreground=self.complimentary_color_2,
                justify="left",
                text="To",
            )
            self.to_label.place(anchor="center", relx=0.65, rely=0.23)
            self.save_button = tk.Button(self.gen_report_frame2)
            self.save_button.configure(
                background=self.complimentary_color_2,
                default="active",
                font="{arial Black} 20 {}",
                foreground=self.main_color,
                justify="center",
                relief="ridge",
                text="Save",
                width=10,
            )
            self.save_button.place(
                anchor="center", relheight=0.09, relwidth=0.325, relx=0.5, rely=0.92
            )
            self.save_button.bind("<ButtonPress>", self.save_press, add="")
            self.personnel_type_label = tk.Label(self.gen_report_frame2)
            self.personnel_type_label.configure(
                background=self.main_color,
                font="{arial} 20 {}",
                foreground=self.complimentary_color_2,
                justify="left",
                text="Personnel Type",
            )
            self.personnel_type_label.place(anchor="center", relx=0.25, rely=0.59)
            self.personnel_type_var = tk.StringVar(value="Personnel Type")
            __values = ["Professor", "Non-Teaching Personnel"]
            self.personnel_type_optionmenu = tk.OptionMenu(
                self.gen_report_frame2,
                self.personnel_type_var,
                *__values,
            )
            self.personnel_type_optionmenu.configure(font="{arial} 20 ")
            self.personnel_type_optionmenu.place(anchor="center", relx=0.75, rely=0.59)
            self.personnel_type_options = self.generate_report_app.nametowidget(
                self.personnel_type_optionmenu.menuname
            )
            self.personnel_type_options.config(font="{arial} 16")

            self.file_type_var = tk.StringVar(value="Pdf")
            self.pdf_radiobutton = tk.Radiobutton(self.gen_report_frame2)
            self.pdf_radiobutton.configure(
                background=self.main_color,
                font="{arial} 24 {}",
                foreground=self.complimentary_color_2,
                text="Pdf",
                selectcolor="black",
                value="Pdf",
                variable=self.file_type_var,
            )
            self.pdf_radiobutton.place(
                anchor="center", relx=0.2, rely=0.7, relheight=0.05
            )
            self.docx_radiobutton = tk.Radiobutton(self.gen_report_frame2)
            self.docx_radiobutton.configure(
                background=self.main_color,
                font="{arial} 24 {}",
                foreground=self.complimentary_color_2,
                selectcolor="black",
                text="Docx",
                value="Docx",
                variable=self.file_type_var,
            )
            self.docx_radiobutton.place(
                anchor="center", relx=0.5, rely=0.7, relheight=0.05
            )
            self.excel_radiobutton = tk.Radiobutton(self.gen_report_frame2)
            self.excel_radiobutton.configure(
                background=self.main_color,
                font="{arial} 24 {}",
                foreground=self.complimentary_color_2,
                selectcolor="black",
                text="Excel",
                value="Excel",
                variable=self.file_type_var,
            )
            self.excel_radiobutton.place(
                anchor="center", relx=0.8, rely=0.7, relheight=0.05
            )

            self.file_name_label = tk.Label(self.gen_report_frame2)
            self.file_name_label.configure(
                background=self.main_color,
                font="{arial} 20 {}",
                foreground=self.complimentary_color_2,
                text="File Name",
            )
            self.file_name_label.place(anchor="center", relx=0.28, rely=0.8)
            self.file_name = tk.Entry(self.gen_report_frame2)
            self.file_name.configure(font="{arial} 20 {}")
            self.file_name.place(
                anchor="center", relwidth=0.4, relx=0.63, rely=0.8, x=0, y=0
            )
            self.gen_report_frame2.place(
                anchor="center", relheight=1.0, relwidth=1.0, relx=0.5, rely=0.5
            )
        elif self.client_type == "Visitors Report":
            self.gen_report_frame2 = tk.Frame(self.generate_report_app)
            self.gen_report_frame2.configure(
                background=self.main_color, height=200, width=200
            )
            self.from_label = tk.Label(self.gen_report_frame2)
            self.from_label.configure(
                background=self.main_color,
                font="{arial} 20 {}",
                foreground=self.complimentary_color_2,
                text="From",
            )
            self.from_label.place(anchor="center", relx=0.20, rely=0.23)

            self.calendar1 = tkc.Calendar(
                self.gen_report_frame2,
                selectmode="day",
                maxdate=self.maxdate,
                year=self.today_year,
                month=self.today_month,
                day=self.today_day,
            )
            self.calendar1.place(anchor="center", relx=0.25, rely=0.4)

            self.calendar2 = tkc.Calendar(
                self.gen_report_frame2,
                selectmode="day",
                maxdate=self.maxdate,
                year=self.today_year,
                month=self.today_month,
                day=self.today_day,
            )
            self.calendar2.place(anchor="center", relx=0.75, rely=0.4)

            self.to_label = tk.Label(self.gen_report_frame2)
            self.to_label.configure(
                background=self.main_color,
                font="{arial} 20 {}",
                foreground=self.complimentary_color_2,
                justify="left",
                text="To",
            )
            self.to_label.place(anchor="center", relx=0.65, rely=0.23)
            self.save_button = tk.Button(self.gen_report_frame2)
            self.save_button.configure(
                background=self.complimentary_color_2,
                default="active",
                font="{arial Black} 20 {}",
                foreground=self.main_color,
                justify="center",
                relief="ridge",
                text="Save",
                width=10,
            )
            self.save_button.place(
                anchor="center", relheight=0.09, relwidth=0.325, relx=0.5, rely=0.92
            )
            self.save_button.bind("<ButtonPress>", self.save_press, add="")
            self.print_button = tk.Button(self.gen_report_frame2)
            self.print_button.configure(
                background=self.complimentary_color_2,
                default="active",
                font="{arial Black} 20 {}",
                foreground=self.main_color,
                justify="center",
                relief="ridge",
                text="Print",
                width=10,
            )
            """
            self.print_button.place(
                anchor="center", relheight=0.08, relwidth=0.3, relx=0.70, rely=0.92
            )
            """
            self.print_button.bind("<ButtonPress>", self.print_press, add="")
            self.pdf_radiobutton = tk.Radiobutton(self.gen_report_frame2)
            self.file_type_var = tk.StringVar(value="Pdf")
            self.pdf_radiobutton.configure(
                background=self.main_color,
                font="{arial} 24 {}",
                foreground=self.complimentary_color_2,
                text="Pdf",
                selectcolor="black",
                value="Pdf",
                variable=self.file_type_var,
            )
            self.pdf_radiobutton.place(
                anchor="center", relx=0.485, rely=0.575, relheight=0.05
            )
            self.docx_radiobutton = tk.Radiobutton(self.gen_report_frame2)
            self.docx_radiobutton.configure(
                background=self.main_color,
                font="{arial} 24 {}",
                foreground=self.complimentary_color_2,
                selectcolor="black",
                text="Docx",
                value="Docx",
                variable=self.file_type_var,
            )
            self.docx_radiobutton.place(
                anchor="center", relx=0.5, rely=0.64, relheight=0.05
            )
            self.excel_radiobutton = tk.Radiobutton(self.gen_report_frame2)
            self.excel_radiobutton.configure(
                background=self.main_color,
                font="{arial} 24 {}",
                foreground=self.complimentary_color_2,
                selectcolor="black",
                text="Excel",
                value="Excel",
                variable=self.file_type_var,
            )
            self.excel_radiobutton.place(
                anchor="center", relx=0.505, rely=0.715, relheight=0.05
            )
            self.file_name_label = tk.Label(self.gen_report_frame2)
            self.file_name_label.configure(
                background=self.main_color,
                font="{arial} 20 {}",
                foreground=self.complimentary_color_2,
                text="File Name",
            )
            self.file_name_label.place(anchor="center", relx=0.28, rely=0.8)
            self.file_name = tk.Entry(self.gen_report_frame2)
            self.file_name.configure(font="{arial} 20 {}")
            self.file_name.place(
                anchor="center", relwidth=0.4, relx=0.63, rely=0.8, x=0, y=0
            )
            self.gen_report_frame2.place(
                anchor="center", relheight=1.0, relwidth=1.0, relx=0.5, rely=0.5
            )

        self.gen_report_frame = tk.Frame(self.generate_report_app)
        self.gen_report_frame.configure(
            background=self.complimentary_color_2, height=200, width=200
        )
        self.sti_logo = tk.Label(self.gen_report_frame)
        self.img_SeekUsmall = tk.PhotoImage(file=".\SeekU\SeekU small.png")
        self.sti_logo.configure(
            background=self.complimentary_color_2,
            font="TkDefaultFont",
            image=self.img_SeekUsmall,
        )
        self.sti_logo.place(anchor="center", relx=0.30, rely=0.5)
        self.app_name_logo = tk.Label(self.gen_report_frame)
        self.img_SeekULogotypemicro = tk.PhotoImage(
            file=".\SeekU\SeekU Logotype micro.png"
        )
        self.app_name_logo.configure(
            background=self.complimentary_color_2,
            foreground=self.main_color,
            image=self.img_SeekULogotypemicro,
            relief="flat",
            text="SEEK",
        )
        self.app_name_logo.place(anchor="center", relx=0.65, rely=0.5)
        self.gen_report_frame.place(
            anchor="center", relheight=0.2, relwidth=1, relx=0.5, rely=0.1
        )

        self.generate_report_app.attributes("-topmost", True)

        # Main widget
        self.mainwindow = self.generate_report_app
        self.mainwindow.protocol("WM_DELETE_WINDOW", self.destroy_this_window)
        self.mainwindow.grab_set()

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
            self.mainwindow.grab_set()
            return folder_select

    def destroy_this_window(self):
        self.generate_report_app.grab_release()
        self.generate_report_app.destroy()

    def save_press(self, event=None):
        folder = self.select_folder()
        filename = self.file_name.get()
        pattern = re.compile("[^a-zA-Z0-9 ]")
        if not pattern.search(filename):
            if len(filename) != 0:
                if folder:
                    date1 = self.calendar1.selection_get()
                    date2 = self.calendar2.selection_get()

                    edited_date1 = date1.strftime("%Y-%m-%d")
                    edited_date2 = date2.strftime("%Y-%m-%d")

                    datefrom = datetime.datetime.strptime(edited_date1, "%Y-%m-%d")
                    dateto = datetime.datetime.strptime(edited_date2, "%Y-%m-%d")

                    print(datefrom)
                    print(dateto)
                    filepath = folder

                    if self.client_type == "Students Report":
                        if self.sections_var.get() != "Section":
                            if self.file_type_var.get() == "Excel":
                                self.excel_class.save_student(
                                    filepath,
                                    filename,
                                    datefrom,
                                    dateto,
                                    str(self.sections_var.get()),
                                    self.users_firstname,
                                    self.users_lastname,
                                )

                            if self.file_type_var.get() == "Docx":
                                self.docx_class.save_doc_student(
                                    filepath,
                                    filename,
                                    datefrom,
                                    dateto,
                                    str(self.sections_var.get()),
                                    self.users_firstname,
                                    self.users_lastname,
                                )

                            if self.file_type_var.get() == "Pdf":
                                self.docx_class.save_pdf_student(
                                    filepath,
                                    filename,
                                    datefrom,
                                    dateto,
                                    str(self.sections_var.get()),
                                    self.users_firstname,
                                    self.users_lastname,
                                )
                        else:
                            messbx.showwarning("Warning", "Select a section.")

                    if self.client_type == "Personnels Report":
                        if self.personnel_type_var.get() != "Personnel Type":
                            if self.file_type_var.get() == "Excel":
                                self.excel_class.save_personnel(
                                    filepath,
                                    filename,
                                    datefrom,
                                    dateto,
                                    str(self.personnel_type_var.get()),
                                    self.users_firstname,
                                    self.users_lastname,
                                )

                            if self.file_type_var.get() == "Docx":
                                self.docx_class.save_doc_personnel(
                                    filepath,
                                    filename,
                                    datefrom,
                                    dateto,
                                    str(self.personnel_type_var.get()),
                                    self.users_firstname,
                                    self.users_lastname,
                                )

                            if self.file_type_var.get() == "Pdf":
                                self.docx_class.save_pdf_personnel(
                                    filepath,
                                    filename,
                                    datefrom,
                                    dateto,
                                    str(self.personnel_type_var.get()),
                                    self.users_firstname,
                                    self.users_lastname,
                                )
                        else:
                            messbx.showwarning("Warning", "Select a Personnel Type.")
                    if self.client_type == "Visitors Report":

                        if self.file_type_var.get() == "Excel":
                            self.excel_class.save_visitor(
                                filepath,
                                filename,
                                datefrom,
                                dateto,
                                self.users_firstname,
                                self.users_lastname,
                            )

                        if self.file_type_var.get() == "Docx":
                            self.docx_class.save_doc_visitor(
                                filepath,
                                filename,
                                datefrom,
                                dateto,
                                self.users_firstname,
                                self.users_lastname,
                            )

                        if self.file_type_var.get() == "Pdf":
                            self.docx_class.save_pdf_visitor(
                                filepath,
                                filename,
                                datefrom,
                                dateto,
                                self.users_firstname,
                                self.users_lastname,
                            )

            else:
                messbx.showwarning(
                    "Warning",
                    "Kindly ensure all fields are filled by entering a value.",
                )
        else:
            messbx.showwarning("Warning", "The input contains special characters.")

    def print_press(self, event=None):

        folder = self.select_folder()
        filename = self.file_name.get()
        pattern = re.compile("[^a-zA-Z0-9 @]")
        if not pattern.search(filename):
            if len(filename) != 0:
                if folder:
                    date1 = self.calendar1.selection_get()
                    date2 = self.calendar2.selection_get()

                    edited_date1 = date1.strftime("%Y-%m-%d")
                    edited_date2 = date2.strftime("%Y-%m-%d")

                    datefrom = datetime.datetime.strptime(edited_date1, "%Y-%m-%d")
                    dateto = datetime.datetime.strptime(edited_date2, "%Y-%m-%d")

                    filepath = folder

                    if self.client_type == "Students Report":

                        if self.file_type_var.get() == "Excel":
                            self.excel_class.print_student(
                                filepath, filename, datefrom, dateto
                            )

                        if self.file_type_var.get() == "Docx":
                            self.docx_class.print_doc_student(
                                filepath, filename, datefrom, dateto
                            )

                        if self.file_type_var.get() == "Pdf":
                            self.docx_class.print_pdf_student(
                                filepath, filename, datefrom, dateto
                            )

                    if self.client_type == "Personnels Report":

                        if self.file_type_var.get() == "Excel":
                            self.excel_class.print_personnel(
                                filepath, filename, datefrom, dateto
                            )

                        if self.file_type_var.get() == "Docx":
                            self.docx_class.print_doc_personnel(
                                filepath, filename, datefrom, dateto
                            )

                        if self.file_type_var.get() == "Pdf":
                            self.docx_class.print_pdf_personnel(
                                filepath, filename, datefrom, dateto
                            )

                    if self.client_type == "Visitors Report":

                        if self.file_type_var.get() == "Excel":
                            self.excel_class.print_visitor(
                                filepath, filename, datefrom, dateto
                            )

                        if self.file_type_var.get() == "Docx":
                            self.docx_class.print_doc_visitor(
                                filepath, filename, datefrom, dateto
                            )

                        if self.file_type_var.get() == "Pdf":
                            self.docx_class.print_pdf_visitor(
                                filepath, filename, datefrom, dateto
                            )
            else:
                messbx.showwarning(
                    "Warning",
                    "Kindly ensure all fields are filled by entering a value.",
                )
        else:
            messbx.showwarning("Warning", "The input contains special characters.")
