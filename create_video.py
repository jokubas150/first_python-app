import tkinter as tk  # adding tkinter from the library and changing its name
from tkinter import ttk
import tkinter.scrolledtext as tkst  # This will allow to have a scroll bar
import video_library as lib  # adding video from library which will be used as lib
import font_manager as fonts  # adding fonts from library which will be used as fonts


# Function to set text for a particular area
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


# Creating a class for "Create Videos List" to be displayed in a window
class CreateVideoList():
    def __init__(self, root):
        self.playlist = []
        if root is None:
            window = tk.Tk()
            fonts.configure()
        else:
            window = tk.Toplevel(root)
        window.geometry("750x350")
        window.title("Create Video List")
        window.iconbitmap("images/player.ico")

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Select Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # combobox to select the video
        variable = tk.StringVar()
        self.drop_list = ttk.Combobox(window, textvariable=variable, width=3, state="readonly")
        self.drop_list["values"] = ["01",
                                    "02",
                                    "03",
                                    "04",
                                    "05"
                                    ]
        self.drop_list.current(0)
        self.drop_list.grid(column=2, row=0)

        add_video_btn = tk.Button(window, text="Add to Playlist", command=self.add_video_clicked)
        add_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.video_txt = tk.Text(window, width=24, height=3, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.volume_slider = tk.Scale(window, from_=0, to=100, font=("Helvetica", 8), resolution=2)
        self.volume_slider.grid(row=1, column=1, columnspan=3, sticky="SE", padx=15, pady=15)

        self.volume_lbl = tk.Label(window, text="", font=("Helvetica", 8))
        self.volume_lbl.grid(row=2, column=1, columnspan=3, padx=5, sticky="E")

        volume_button = tk.Button(window, text="Set Volume", font=("Helvetica", 8), command=self.volume_button)
        volume_button.grid(row=2, column=3, columnspan=3, padx=5)

        play_button = tk.Button(window, text="Play", width=5, command=self.play_button)
        play_button.grid(row=2, column=0, sticky="W", pady=5, padx=5, columnspan=2)

        clear_button = tk.Button(window, text="Clear", width=5, command=self.clear_button)
        clear_button.grid(row=2, column=1, sticky="W", pady=5, padx=5, columnspan=2)

        self.playing_lbl = tk.Label(window, text="", font=("Helvetica", 12))
        self.playing_lbl.grid(row=2, column=1, sticky="E", columnspan=2)

        if root is None:
            window.mainloop()

    # Function for "Add" button
    def add_video_clicked(self):
        key = self.drop_list.get()
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details)
            self.playlist.append(key)
            self.make_playlist()
        else:
            set_text(self.video_txt, f"Video {key} not found")

    # Function for "List Videos" button
    def list_videos_clicked(self):  # function for clicking a List Video label
        video_list = lib.list_all()  # list all details
        set_text(self.list_txt, video_list)

    # Function for volume button
    def volume_button(self):
        volume = self.volume_slider.get()
        self.volume_lbl.configure(text=f"Volume {volume}")

    # Function for play button
    def play_button(self):
        try:
            self.playing_lbl.configure(text="Playing My Playlist")
            for key in self.playlist:
                lib.increment_play_count(key)
            self.make_playlist()
        except self.playing_lbl.configure(text="Empty Playlist"):
            return

    # Function to to show what user add to the playlist
    def make_playlist(self):
        output = "My Playlist:\n"
        for key in self.playlist:
            name = lib.get_name(key)
            play_count = lib.get_play_count(key)
            output += f"{key} {name} has been played {play_count} times\n"
        set_text(self.list_txt, output)

    # function for a clear button
    def clear_button(self):
        self.playlist.clear()
        self.make_playlist()


if __name__ == "__main__":
    CreateVideoList(None)
