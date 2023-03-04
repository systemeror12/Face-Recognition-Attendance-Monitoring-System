#!/usr/bin/python3
import tkinter as tk


class AdmindashboardApp:
    def __init__(self, master=None):
        # build ui
        self.administrator_app = tk.Tk() if master is None else tk.Toplevel(master)
        self.administrator_app.configure(
            background="#E7E7E7", height=200, width=200)
        width= self.administrator_app.winfo_screenwidth()               
        height= self.administrator_app.winfo_screenheight()               
        self.administrator_app.geometry("%dx%d" % (width, height))
        self.administrator_app.resizable(False, False)
        
        self.administrator_db_frame = tk.Frame(self.administrator_app)
        self.administrator_db_frame.configure(
            background="#E7E7E7", height=200, width=200)
        self.administrator_db_ttl_frame = tk.Frame(self.administrator_db_frame)
        self.administrator_db_ttl_frame.configure(
            background="#F7FAE9", height=200, width=200)
        self.ttl_students_label = tk.Label(self.administrator_db_ttl_frame)
        self.ttl_students_label.configure(
            background="#F7FAE9",
            font="{arial} 24 {bold}",
            text='Total Students')
        self.ttl_students_label.place(
            anchor="center", relx=0.16, rely=0.25, x=0, y=0)
        self.ttl_personnels_label = tk.Label(self.administrator_db_ttl_frame)
        self.ttl_personnels_label.configure(
            anchor="n",
            background="#F7FAE9",
            font="{arial} 24 {bold}",
            text='Total Personnels')
        self.ttl_personnels_label.place(
            anchor="center", relx=0.5, rely=0.25, x=0, y=0)
        self.ttl_visitor_label = tk.Label(self.administrator_db_ttl_frame)
        self.ttl_visitor_label.configure(
            background="#F7FAE9",
            font="{arial} 24 {bold}",
            text='Total Visitors')
        self.ttl_visitor_label.place(
            anchor="center", relx=0.84, rely=0.25, x=0, y=0)
        self.administrator_db_ttl_frame.place(
            anchor="center",
            relheight=0.35,
            relwidth=0.9,
            relx=0.5,
            rely=0.33,
            x=0,
            y=0)
        self.administrator_db_ol_frame = tk.Frame(self.administrator_db_frame)
        self.administrator_db_ol_frame.configure(
            background="#F7FAE9", height=200, width=200)
        self.ol_students_label = tk.Label(self.administrator_db_ol_frame)
        self.ol_students_label.configure(
            background="#F7FAE9",
            font="{arial} 24 {bold}",
            text='Present Students')
        self.ol_students_label.place(
            anchor="center", relx=0.16, rely=0.25, x=0, y=0)
        self.ol_personnels_label = tk.Label(self.administrator_db_ol_frame)
        self.ol_personnels_label.configure(
            anchor="n",
            background="#F7FAE9",
            font="{arial} 24 {bold}",
            text='Present Personnels')
        self.ol_personnels_label.place(
            anchor="center", relx=0.5, rely=0.25, x=0, y=0)
        self.ol_visitor_label = tk.Label(self.administrator_db_ol_frame)
        self.ol_visitor_label.configure(
            background="#F7FAE9",
            font="{arial} 24 {bold}",
            text='Present Visitors')
        self.ol_visitor_label.place(
            anchor="center", relx=0.84, rely=0.25, x=0, y=0)
        self.administrator_db_ol_frame.place(
            anchor="center",
            relheight=0.35,
            relwidth=0.9,
            relx=0.5,
            rely=0.72,
            x=0,
            y=0)
        self.dashboard_label = tk.Label(self.administrator_db_frame)
        self.dashboard_label.configure(
            background="#E7E7E7",
            font="{arial black} 48 {}",
            text='Dashboard')
        self.dashboard_label.place(
            anchor="center", relheight=0.1,
            relwidth=0.3, relx=0.5, rely=0.09,)
        self.time_and_date_label = tk.Label(self.administrator_db_frame)
        self.time_and_date_label.configure(
            background="#F7FAE9",
            font="{arial} 30 {bold}",
            text='Time and Date')
        self.time_and_date_label.place(
            anchor="center",
            relwidth=1,
            relx=0.5,
            rely=0.97,
            x=0,
            y=0) 
        self.administrator_db_frame.place(
            anchor="center",
            relheight=0.95,
            relwidth=.78,
            relx=0.61,
            rely=0.525)
        self.administrator_frame3 = tk.Frame(self.administrator_app)
        self.administrator_frame3.configure(
            background="#0072bc", height=200, width=200)
        self.dashboard_section_label = tk.Label(self.administrator_frame3)
        self.dashboard_section_label.configure(
            background="#0072bc",
            font="{arial } 19 {bold}",
            foreground="#F7FAE9",
            justify="center",
            relief="flat",
            text='Dashboard')
        self.dashboard_section_label.place(anchor="w", relx=.1, rely=0.1)
        self.dashboard_section_label.bind("<1>", self.dashboard_appear, add="")
        self.dashboard_section_label.bind(
            "<Enter>", self.dashboard_hover, add="")
        self.dashboard_section_label.bind(
            "<Leave>", self.dashboard_hover_out, add="")
        self.client_section_label = tk.Label(self.administrator_frame3)
        self.client_section_label.configure(
            background="#0072bc",
            font="{arial } 19 {bold}",
            foreground="#F7FAE9",
            justify="center",
            relief="flat",
            text='Client')
        self.client_section_label.place(anchor="w", relx=.1, rely=0.16)
        self.client_section_label.bind("<1>", self.client_appear, add="")
        self.client_section_label.bind("<Enter>", self.client_hover, add="")
        self.client_section_label.bind(
            "<Leave>", self.client_hover_out, add="")
        self.user_section_label = tk.Label(self.administrator_frame3)
        self.user_section_label.configure(
            background="#0072bc",
            font="{arial } 19 {bold}",
            foreground="#F7FAE9",
            justify="center",
            relief="flat",
            text='User')
        self.user_section_label.place(anchor="w", relx=.1, rely=0.22)
        self.user_section_label.bind("<1>", self.user_appear, add="")
        self.user_section_label.bind("<Enter>", self.user_hover, add="")
        self.user_section_label.bind("<Leave>", self.user_hover_out, add="")
        self.report_section_label = tk.Label(self.administrator_frame3)
        self.report_section_label.configure(
            background="#0072bc",
            font="{arial } 19 {bold}",
            foreground="#F7FAE9",
            justify="center",
            relief="flat",
            text='Report')
        self.report_section_label.place(anchor="w", relx=.1, rely=0.28)
        self.report_section_label.bind("<1>", self.report_appear, add="")
        self.report_section_label.bind("<Enter>", self.report_hover, add="")
        self.report_section_label.bind(
            "<Leave>", self.report_hover_out, add="")
        self.settings_section_label = tk.Label(self.administrator_frame3)
        self.settings_section_label.configure(
            background="#0072bc",
            font="{arial } 19 {bold}",
            foreground="#F7FAE9",
            justify="center",
            relief="flat",
            text='Settings')
        self.settings_section_label.place(anchor="w", relx=.1, rely=0.34)
        self.settings_section_label.bind("<1>", self.settings_appear, add="")
        self.settings_section_label.bind(
            "<Enter>", self.settings_hover, add="")
        self.settings_section_label.bind(
            "<Leave>", self.settings_hover_out, add="")
        self.logout_label = tk.Label(self.administrator_frame3)
        self.logout_label.configure(
            background="#0072bc",
            font="{arial} 19 {bold}",
            foreground="#F7FAE9",
            justify="center",
            relief="flat",
            text='Log Out')
        self.logout_label.place(anchor="w", relx=.1, rely=0.85)
        self.logout_label.bind("<1>", self.logout, add="")
        self.logout_label.bind("<Enter>", self.logout_hover, add="")
        self.logout_label.bind("<Leave>", self.logout_hover_out, add="")
        self.administrator_frame3.place(
            anchor="center",
            relheight=.92,
            relwidth=0.22,
            relx=0.11,
            rely=.54)
        self.administrator_frame2 = tk.Frame(self.administrator_app)
        self.administrator_frame2.configure(
            background="#F7FAE9", height=200, width=200)
        self.app_name_label = tk.Label(self.administrator_frame2)
        self.app_name_label.configure(
            anchor="w",
            background="#F7FAE9",
            font="{arial} 36 {bold}",
            foreground="#0072bc",
            justify="left",
            text='SEEK')
        self.app_name_label.place(anchor="w", relx=0.08, rely=.5)
        self.app_name_labelU = tk.Label(self.administrator_frame2)
        self.app_name_labelU.configure(
            anchor="w",
            background="#F7FAE9",
            font="{Arial} 36 {bold}",
            foreground="#fff200",
            justify="left",
            text='U')
        self.app_name_labelU.place(anchor="w", relx=0.17, rely=0.5)
        self.app_logo_label = tk.Label(self.administrator_frame2)
        self.img_SeekUmicro = tk.PhotoImage(file=".\SeekU\SeekU micro.png")
        self.app_logo_label.configure(
            background="#F7FAE9",
            image=self.img_SeekUmicro,
            text='label1')
        self.app_logo_label.place(anchor="center", relx=0.05, rely=0.5)
        self.administrator_frame2.place(
            anchor="center",
            relheight=0.08,
            relwidth=1.0,
            relx=0.50,
            rely=0.04)

        # Main widget
        self.mainwindow = self.administrator_app
        self.mainwindow.wm_attributes('-fullscreen', 'True')

    def run(self):
        self.mainwindow.mainloop()

    def dashboard_appear(self, event=None):
        pass

    def dashboard_hover(self, event=None):
        pass

    def dashboard_hover_out(self, event=None):
        pass

    def client_appear(self, event=None):
        pass

    def client_hover(self, event=None):
        pass

    def client_hover_out(self, event=None):
        pass

    def user_appear(self, event=None):
        pass

    def user_hover(self, event=None):
        pass

    def user_hover_out(self, event=None):
        pass

    def report_appear(self, event=None):
        pass

    def report_hover(self, event=None):
        pass

    def report_hover_out(self, event=None):
        pass

    def settings_appear(self, event=None):
        pass

    def settings_hover(self, event=None):
        pass

    def settings_hover_out(self, event=None):
        pass

    def logout(self, event=None):
        pass

    def logout_hover(self, event=None):
        pass

    def logout_hover_out(self, event=None):
        pass


if __name__ == "__main__":
    app = AdmindashboardApp()
    app.run()
