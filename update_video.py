import tkinter as tk  # adding tkinter from the library and changing its name
import tkinter.scrolledtext as tkst  # This will allow to have a scroll bar
from tkinter import ttk
import video_library as lib  # adding video from library which will be used as lib
import font_manager as fonts  # adding fonts from library which will be used as fonts


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class UpdateVideo():
    def __init__(self, root):
        if root is None:
            window = tk.Tk()
            fonts.configure()
        else:
            window = tk.Toplevel(root)
        window.geometry("800x350")
        window.title("Update Video")
        window.iconbitmap("images/player.ico")

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Select Video Number to Update")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        rating = tk.StringVar()
        self.drop_list_rating = ttk.Combobox(window, textvariable=rating, width=3, state="readonly")
        self.drop_list_rating["values"] = [
                                            "1",
                                            "2",
                                            "3",
                                            "4",
                                            "5"
                                          ]
        self.drop_list_rating.current(0)
        self.drop_list_rating.grid(column=2, row=1, sticky="N", padx=10, pady=10)

        video = tk.StringVar()
        self.drop_list_video = ttk.Combobox(window, textvariable=video, width=3, state="readonly")
        self.drop_list_video["values"] = [
                                    "01",
                                    "02",
                                    "03",
                                    "04",
                                    "05"
                                    ]
        self.drop_list_video.current(0)
        self.drop_list_video.grid(column=2, row=0, padx=15, pady=10)

        update_video_btn = tk.Button(window, text="Update Rating", command=self.update_video_clicked)
        update_video_btn.grid(row=1, column=3, sticky="N", padx=10, pady=10)

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        if root is None:
            window.mainloop()

    def check_video_clicked(self):
        key = self.drop_list_video.get()
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details)
        else:
            set_text(self.video_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Checking for Videos...")

    def update_video_clicked(self):
        try:
            key = self.drop_list_video.get()
            name = lib.get_name(key)
            if name is not None:
                director = lib.get_director(key)
                rating = self.drop_list_rating.get()
                lib.set_rating(key, int(rating))
                play_count = lib.get_play_count(key)
                video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
                set_text(self.video_txt, video_details)
                self.status_lbl.configure(text="Video Updated!")
        except set_text(self.video_txt, f"Please Enter Rating"):
            return -1

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="Listing Videos...")


if __name__ == "__main__":
    UpdateVideo(None)
