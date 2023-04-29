import tkinter as tk  # adding tkinter from the library and changing its name
import tkinter.scrolledtext as tkst  # This will allow to have a scroll bar
from tkinter import ttk  # importing ttk from tkinter
import video_library as lib  # adding video from library which will be used as lib
import font_manager as fonts  # adding fonts from library which will be used as fonts


def set_text(text_area, content):  # function to allow insert content in text boxes
    text_area.delete("1.0", tk.END)  # clears the text
    text_area.insert(1.0, content)  # new text inserted


class CheckVideos():  # defining class
    def __init__(self, root):  # constructor for CheckVideos
        if root is None:  # if check videos runs as a standalone
            window = tk.Tk()  # Change Tkinter name
            fonts.configure()  # configure the fonts
        else:  # if CheckVideos is being run by video player
            window = tk.Toplevel(root)  # get the window from the TopLevel
        window.geometry("750x350")  # defining window size
        window.title("Check Videos")  # adding title for a GUI
        window.iconbitmap("images/player.ico")  # adding logo

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked) # adding button for List All Videos
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)  # positioning the button at row 0 and column 0

        enter_lbl = tk.Label(window, text="Select Video Number")  # code to add "enter video number" label
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)  # adding to the 0th row and 1st column, with padding from up and down

        variable = tk.StringVar()
        self.drop_list = ttk.Combobox(window, textvariable=variable, width=3, state="readonly") # Creating dropdown list
        self.drop_list["values"] = ["01",  # Adding values to the dropdown list
                                    "02",
                                    "03",
                                    "04",
                                    "05"
                                    ]
        self.drop_list.current(0)  # When program runs set selection at 0th item
        self.drop_list.grid(column=2, row=0, padx=15, pady=10)  # Where the dropdown list will be displayed

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)  # Creating "Check Video" button
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)  # adding to the 0th row and 3rd column, with padding from up and down

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")  # textbox to list name, director, rating, num of plays
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10) #

        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")  # text box to display video information
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)  # displaying at the top left and changing the size of it

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))  # code to add label when "List Videos" clicked
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)  # Displaying the label to the left

        if root is None:  # If root is none display empty window
            window.mainloop()

    def check_video_clicked(self):  # function if the Check Video button is clicked
        key = self.drop_list.get()  # getting the selection from user and making it as key variable
        name = lib.get_name(key)  # getting a name from a library
        if name is not None:  # if user enters a name, then
            director = lib.get_director(key)  # get director details
            rating = lib.get_rating(key)  # get rating details
            play_count = lib.get_play_count(key)  # get play count details
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"  # display details with line breaks
            set_text(self.video_txt, video_details)  # set what will be displayed in video details box
        else:
            set_text(self.video_txt, f"Video {key} not found")  # statement displayed if the video is not found
        self.status_lbl.configure(text="Check Video button was clicked!")  # Add this text to label when button clicked

    def list_videos_clicked(self):  # function for clicking a List Video label
        video_list = lib.list_all()  # list all details
        set_text(self.list_txt, video_list)  # what and where text will be displayed
        self.status_lbl.configure(text="List Videos button was clicked!")  # Display text when button clicked


if __name__ == "__main__": # Allows to open a program as a standalone
    CheckVideos(None)
