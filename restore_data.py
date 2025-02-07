#!/usr/bin/python3
import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messbx
import backup_restore_mod as bR

class RestoreApp:
    def __init__(self):
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        # Color ------------
        self.sub_complimentary_color = "#808080" #gray
        self.main_color = "#0072bc" #Blue
        self.sub_color = "#FFF875" #light Yellow
        self.complimentary_color_1 = "#E7E7E7" #light  gray
        self.complimentary_color_2 = "#F7FAE9" #Cream Color
        self.hover_color = "#FFF200" #pure Yellow
        # Color ------------

        self.restore_database_query = bR.BackupRestore()
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        # build ui
        self.restore_db = tk.Toplevel()
        self.restore_db.configure(background=self.main_color, height=200, width=200)
        self.restore_db.geometry("700x350")
        self.restore_db.resizable(False, False)
        self.restore_db.title("SeekU - Restore data")
        self.restore_db_frame2 = tk.Frame(self.restore_db)
        self.restore_db_frame2.configure(
            background=self.main_color, height=200, width=200)
        self.section_rec_label = tk.Label(self.restore_db_frame2)
        self.section_rec_label.configure(
            background=self.main_color,
            font="{lucida} 20 {bold}",
            foreground=self.complimentary_color_2,
            text='Records')
        self.section_rec_label.place(anchor="center", relx=0.45, rely=0.35)
        self.student_rec_button = tk.Button(self.restore_db_frame2)
        self.student_rec_button.configure(
            background=self.complimentary_color_2,
            default="active",
            font="{arial Black} 14 {}",
            foreground=self.main_color,
            justify="center",
            relief="ridge",
            text='Import',
            width=10)
        self.student_rec_button.place(
            anchor="center",
            relheight=0.1,
            relwidth=0.20,
            relx=0.45,
            rely=0.475)
        self.student_rec_button.bind(
            "<ButtonPress>", self.import_s_records, add="")
        self.student_rec_label = tk.Label(self.restore_db_frame2)
        self.student_rec_label.configure(
            background=self.main_color,
            font="{lucida} 20 {bold}",
            foreground=self.complimentary_color_2,
            text='Students')
        self.student_rec_label.place(anchor="center", relx=0.2, rely=0.475)
        self.personnel_rec_button = tk.Button(self.restore_db_frame2)
        self.personnel_rec_button.configure(
            background=self.complimentary_color_2,
            default="active",
            font="{arial Black} 14 {}",
            foreground=self.main_color,
            justify="center",
            relief="ridge",
            text='Import',
            width=10)
        self.personnel_rec_button.place(
            anchor="center",
            relheight=0.1,
            relwidth=0.20,
            relx=0.45,
            rely=0.6)
        self.personnel_rec_button.bind(
            "<ButtonPress>", self.import_p_records, add="")
        self.personnel_rec_label = tk.Label(self.restore_db_frame2)
        self.personnel_rec_label.configure(
            background=self.main_color,
            font="{lucida} 20 {bold}",
            foreground=self.complimentary_color_2,
            text='Personnels')
        self.personnel_rec_label.place(anchor="center", relx=0.2, rely=0.6)
        self.visitor_rec_button = tk.Button(self.restore_db_frame2)
        self.visitor_rec_button.configure(
            background=self.complimentary_color_2,
            default="active",
            font="{arial Black} 14 {}",
            foreground=self.main_color,
            justify="center",
            relief="ridge",
            text='Import',
            width=10)
        self.visitor_rec_button.place(
            anchor="center",
            relheight=0.1,
            relwidth=0.20,
            relx=0.45,
            rely=0.725)
        self.visitor_rec_button.bind(
            "<ButtonPress>", self.import_v_records, add="")
        self.visitor_rec_label = tk.Label(self.restore_db_frame2)
        self.visitor_rec_label.configure(
            background=self.main_color,
            font="{lucida} 20 {bold}",
            foreground=self.complimentary_color_2,
            text='Visitors')
        self.visitor_rec_label.place(anchor="center", relx=0.2, rely=0.725)
        self.section_rep_label = tk.Label(self.restore_db_frame2)
        self.section_rep_label.configure(
            background=self.main_color,
            font="{lucida} 20 {bold}",
            foreground=self.complimentary_color_2,
            text='Reports')
        self.section_rep_label.place(anchor="center", relx=0.75, rely=0.35)
        self.student_rep_button = tk.Button(self.restore_db_frame2)
        self.student_rep_button.configure(
            background=self.complimentary_color_2,
            default="active",
            font="{arial Black} 14 {}",
            foreground=self.main_color,
            justify="center",
            relief="ridge",
            text='Import',
            width=10)
        self.student_rep_button.place(
            anchor="center",
            relheight=0.1,
            relwidth=0.20,
            relx=0.75,
            rely=0.475)
        self.student_rep_button.bind(
            "<ButtonPress>", self.import_s_reports, add="")
        self.personnel_rep_button = tk.Button(self.restore_db_frame2)
        self.personnel_rep_button.configure(
            background=self.complimentary_color_2,
            default="active",
            font="{arial Black} 14 {}",
            foreground=self.main_color,
            justify="center",
            relief="ridge",
            text='Import',
            width=10)
        self.personnel_rep_button.place(
            anchor="center",
            relheight=0.1,
            relwidth=0.20,
            relx=0.75,
            rely=0.6)
        self.personnel_rep_button.bind(
            "<ButtonPress>", self.import_p_reports, add="")
        self.visitor_rep_button = tk.Button(self.restore_db_frame2)
        self.visitor_rep_button.configure(
            background=self.complimentary_color_2,
            default="active",
            font="{arial Black} 14 {}",
            foreground=self.main_color,
            justify="center",
            relief="ridge",
            text='Import',
            width=10)
        self.visitor_rep_button.place(
            anchor="center",
            relheight=0.1,
            relwidth=0.20,
            relx=0.75,
            rely=0.725)
        self.visitor_rep_button.bind(
            "<ButtonPress>", self.import_v_reports, add="")
        self.users_label = tk.Label(self.restore_db_frame2)
        self.users_label.configure(
            background=self.main_color,
            font="{lucida} 20 {bold}",
            foreground=self.complimentary_color_2,
            text='Users')
        self.users_label.place(anchor="center", relx=0.2, rely=0.85)
        self.users_button = tk.Button(self.restore_db_frame2)
        self.users_button.configure(
            background=self.complimentary_color_2,
            default="active",
            font="{arial Black} 14 {}",
            foreground=self.main_color,
            justify="center",
            relief="ridge",
            text='Import',
            width=10)
        self.users_button.place(
            anchor="center",
            relheight=0.1,
            relwidth=0.20,
            relx=0.45,
            rely=0.85)
        self.users_button.bind("<ButtonPress>", self.import_users, add="")
        self.restore_db_frame2.place(
            anchor="center",
            relheight=1.0,
            relwidth=1.0,
            relx=0.5,
            rely=0.5)
        self.restore_db_frame = tk.Frame(self.restore_db)
        self.restore_db_frame.configure(
            background=self.complimentary_color_2, height=200, width=200)
        self.seeku_logo = tk.Label(self.restore_db_frame)
        self.img_SeekUsmall = tk.PhotoImage(file="./SeekU/SeekU small.png")
        self.seeku_logo.configure(
            background=self.complimentary_color_2,
            image=self.img_SeekUsmall,
            text='label1')
        self.seeku_logo.place(anchor="center", relx=0.3, rely=0.5)
        self.app_name_label = tk.Label(self.restore_db_frame)
        self.img_SeekULogotypemicro = tk.PhotoImage(
            file="./SeekU/SeekU Logotype micro.png")
        self.app_name_label.configure(
            background=self.complimentary_color_2,
            font="{arial black} 40 {}",
            foreground=self.main_color,
            image=self.img_SeekULogotypemicro,
            relief="flat",
            text='SEEK')
        self.app_name_label.place(anchor="center", relx=0.65, rely=0.5)
        self.restore_db_frame.place(
            anchor="center",
            relheight=0.20,
            relwidth=1,
            relx=.5,
            rely=.1)

        self.mainwindow = self.restore_db
        self.center(self.mainwindow)
        self.mainwindow.protocol("WM_DELETE_WINDOW", self.exit_window)
        self.mainwindow.attributes("-topmost", True)
        self.mainwindow.attributes("-topmost", False)
        self.mainwindow.grab_set()

    def exit_window(self):
        self.show_home_window()

    # this function will return to the login window
    def show_home_window(self):
        self.restore_db.grab_release()
        self.restore_db.destroy()

    def select_file(self):
        self.restore_db.attributes("-topmost", False)
        dialog_parent = tk.Toplevel(self.mainwindow)
        dialog_parent.withdraw()
        dialog_parent.grab_set()
        file_select = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

        if file_select == "":
            dialog_parent.grab_release()
            dialog_parent.destroy()
            self.restore_db.grab_set()
            return False
        elif not file_select.endswith(".csv"):
            dialog_parent.grab_release()
            dialog_parent.destroy()
            self.restore_db.grab_set()
            messbx.showerror("Error", "The selected file is not a CSV file.")
            return False
        else:
            dialog_parent.grab_release()
            dialog_parent.destroy()
            self.restore_db.grab_set()
            return file_select

    def import_students_rec_logic(self):
        selected_file = self.select_file()
        if selected_file:
            self.restore_database_query.restore_student(selected_file)
            

    def import_personnels_rec_logic(self):
        selected_file = self.select_file()
        if selected_file:
            self.restore_database_query.restore_personnel(selected_file)

    def import_visitors_rec_logic(self):
        selected_file = self.select_file()
        if selected_file:
            self.restore_database_query.restore_visitor(selected_file)

    def import_students_rep_logic(self):
        selected_file = self.select_file()
        if selected_file:
            self.restore_database_query.restore_student_report(selected_file)

    def import_personnels_rep_logic(self):
        selected_file = self.select_file()
        if selected_file:
            self.restore_database_query.restore_personnel_report(selected_file)

    def import_visitors_rep_logic(self):
        selected_file = self.select_file()
        if selected_file:
            self.restore_database_query.restore_visitor_report(selected_file)

    def import_users_logic(self):
        selected_file = self.select_file()
        if selected_file:
            self.restore_database_query.restore_user(selected_file)

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


    def import_s_records(self, event=None):
        self.import_students_rec_logic()

    def import_p_records(self, event=None):
        self.import_personnels_rec_logic()

    def import_v_records(self, event=None):
        self.import_visitors_rec_logic()

    def import_s_reports(self, event=None):
        self.import_students_rep_logic()

    def import_p_reports(self, event=None):
        self.import_personnels_rep_logic()

    def import_v_reports(self, event=None):
        self.import_visitors_rep_logic()

    def import_users(self, event=None):
        self.import_users_logic()


