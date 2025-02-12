import tkinter as tk
import tkinter.messagebox as messbx
import tkinter as tk
import face_recognition
import cv2
import PIL.Image, PIL.ImageTk
import client_add_visitor as cAV
import os
import sys

class CameraApp:
    def __init__(self, vid_source, login_mod, sel_cam, home_mod,file_path ):

    #PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        # Color ------------
        self.sub_complimentary_color = "#808080" #gray
        self.main_color = "#0072bc" #Blue
        self.sub_color = "#FFF875" #light Yellow
        self.complimentary_color_1 = "#E7E7E7" #light  gray
        self.complimentary_color_2 = "#F7FAE9" #Cream Color
        self.hover_color = "#FFF200" #pure Yellow
        # Color ------------
        self.video_source = vid_source
        self.login_window = login_mod
        self.sel_cam_window = sel_cam
        self.home_window = home_mod
        self.img_path = file_path
    #PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        # build ui
        self.snapshot_app = tk.Toplevel()
        self.snapshot_app.configure(
            background=self.complimentary_color_2, height=200, width=200)
        width= self.snapshot_app.winfo_screenwidth()               
        height= self.snapshot_app.winfo_screenheight()               
        self.snapshot_app.geometry("%dx%d" % (width, height))
        self.snapshot_app.resizable(False, False)
        self.snapshot_app.title("SeekU - Client Camera App")
        self.snapshot_app.iconbitmap(".\SeekU\SeekU.ico")
        self.snapshot_app.bind('<Return>',lambda event:self.take_pic_func())
    #Contains-Camera-Canvas---------------------------------------------------------------------------------------------------
        self.snapshot_frame4 = tk.Frame(self.snapshot_app)
        self.snapshot_frame4.configure(
            background=self.main_color, height=200, width=200)
        self.camera_canvas = tk.Canvas(self.snapshot_frame4)
        self.camera_canvas.configure(
            background=self.main_color,
            highlightbackground=self.main_color)
        self.camera_canvas.place(
            anchor="center",
            relheight=1.0,
            relwidth=1.0,
            relx=.5,
            rely=.5,
            x=0,
            y=0)
        self.snapshot_frame4.place(
            anchor="center",
            relheight=0.50,
            relwidth=0.50,
            relx=0.5,
            rely=0.575)
        self.vid = MyVideoCapture(self.video_source, 1280, 720)
    #Contains-Camera-Canvas---------------------------------------------------------------------------------------------------
    #Contains-the-logo-and-logotype--------------------------------------------------------------------------------------------------------- 
        self.snapshot_frame3 = tk.Frame(self.snapshot_app)
        self.snapshot_frame3.configure(
            background=self.complimentary_color_2, height=200, width=200)
        self.app_name_logo = tk.Label(self.snapshot_frame3)
        self.img_SeekULogotypesmall = tk.PhotoImage(
            file=".\SeekU\SeekU Logotype large.png")
        self.app_name_logo.configure(
            anchor="w",
            background=self.complimentary_color_2,
            font="{arial black} 100 {}",
            foreground=self.main_color,
            image=self.img_SeekULogotypesmall,
            justify="left",
            text='SEEK')
        self.app_name_logo.place(anchor="center", relx=0.575, rely=.5)
        self.app_logo_label = tk.Label(self.snapshot_frame3)
        self.img_SeekUlarge = tk.PhotoImage(file=".\SeekU\SeekU large.png")
        self.app_logo_label.configure(
            background=self.complimentary_color_2,
            image=self.img_SeekUlarge,
            text='label1')
        self.app_logo_label.place(anchor="center", relx=0.35, rely=0.5)
        self.snapshot_frame3.place(
            anchor="center",
            relheight=0.16,
            relwidth=1.0,
            relx=0.50,
            rely=0.21)
        self.snapshot_frame2 = tk.Frame(self.snapshot_app)
        self.snapshot_frame2.configure(
            background=self.sub_color, height=200, width=200)
        self.school_logo_label = tk.Label(self.snapshot_frame2)
        self.img_STICollegeBalagtasLogomedium = tk.PhotoImage(
            file=".\SeekU\STI College Balagtas Logo medium.png")
        self.school_logo_label.configure(
            background=self.sub_color,
            image=self.img_STICollegeBalagtasLogomedium,
            text='label1')
        self.school_logo_label.place(anchor="center", relx=.25, rely=0.5)
    #Contains-the-logo-and-logotype--------------------------------------------------------------------------------------------------------- 
    #Contains-snapshot-and-logout-button--------------------------------------------------------------------------------------------------------- 
        self.snapshot_frame2.place(
            anchor="center",
            relheight=0.13,
            relwidth=1.0,
            relx=0.5,
            rely=0.065)
        self.snapshot_frame1 = tk.Frame(self.snapshot_app)
        self.snapshot_frame1.configure(
            background=self.complimentary_color_2, height=200, width=200)
        self.snapshot_button = tk.Button(self.snapshot_frame1)
        self.snapshot_button.configure(
            background=self.main_color,
            font="{arial black} 36 {}",
            foreground=self.complimentary_color_2,
            text='Snapshot')
        self.snapshot_button.place(
            anchor="center",
            relheight=0.6,
            relwidth=0.2,
            relx=.5,
            rely=0.5)
        self.snapshot_button.bind("<ButtonPress>", self.take_picture, add="")
        self.return_button = tk.Button(self.snapshot_frame1)
        self.return_button.configure(
            background=self.main_color,
            font="{arial black} 20 {}",
            foreground=self.complimentary_color_2,
            text='Return')
        self.return_button.place(
            anchor="center",
            relheight=0.35,
            relwidth=0.11,
            relx=0.93,
            rely=0.775)
        self.return_button.bind("<ButtonPress>", self.return_func, add="")
        self.snapshot_frame1.place(
            anchor="center",
            relheight=0.15,
            relwidth=1.0,
            relx=0.5,
            rely=0.925)
    #Contains-snapshot-and-logout-button--------------------------------------------------------------------------------------------------------

        # see function for description
        self.cam_update()

        # Main widget
        self.mainwindow = self.snapshot_app
        # will set the window to fullscreen
        self.mainwindow.wm_attributes('-fullscreen', 'True')
        # this protocol will do a function after pressing the close button.
        self.mainwindow.protocol("WM_DELETE_WINDOW", self.exit_program )
    #--------------------------------------------------------------------------------------------------------- 

    # this function will destroy the window and closes the system/program.
    def exit_program(self):
        sys.exit() 

    # this function will hide this window
    def hide_this_window(self):
        self.snapshot_app.withdraw()

    # this will show the home window and destroy this window
    def show_home_window(self):
        self.home_window.deiconify()
        self.snapshot_app.destroy()

    # this function updates the canvas content - shows the camera
    def cam_update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        if ret:
            resized = cv2.resize(frame, (self.camera_canvas.winfo_width(), self.camera_canvas.winfo_height()), interpolation=cv2.INTER_AREA)
            # turning the image into gray for the haar cascade to be read
            gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
            # pu tthe image/frame into the canvas
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(resized))
            self.camera_canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)

        self.snapshot_app.after(15, self.cam_update)

    # this function will save the frame (image) taken 
    def take_pic_func(self):
        ret, frame = self.vid.get_frame()
        resized = cv2.resize(frame, (1280, 720), interpolation=cv2.INTER_AREA)
        if ret:
            cv2.imwrite(os.path.join(self.img_path ,("000000000.jpg")), cv2.cvtColor(resized, cv2.COLOR_RGB2BGR))

            image = image = face_recognition.load_image_file(self.img_path + "/000000000.jpg")
            face_locations = face_recognition.face_locations(image)
            
            if face_locations:
                 # this will open the window that saves the info of the visitor.
                cAV.AddVisitorApp(self.home_window, self.snapshot_app, self.img_path)
                self.hide_this_window()
            else:
                 messbx.showerror(
                "Error", "Face detection failed. Please adjust your posture and capture a clear image."
            )
           


    # this command will return to the home window
    def return_func(self, event=None):
        self.show_home_window()
        self.snapshot_app.destroy()
        if os.path.exists(self.img_path + "/000000000.jpg"):
            os.remove(self.img_path + "/000000000.jpg")

    # this command will take a picture
    def take_picture(self, event=None):
        self.take_pic_func()
    

#this class returns the frames taken by the camera
class MyVideoCapture:
    def __init__(self, video_source,  xsize,ysize):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source, cv2.CAP_DSHOW)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
        # setting the height and width of the camera
        self.vid.set(cv2.CAP_PROP_FRAME_WIDTH,xsize)
        self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT,ysize)
        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            # flipping the image so it is not inverted
            frame = cv2.flip(frame, 1)
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)
