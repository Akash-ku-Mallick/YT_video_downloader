import time
from pytube import YouTube
import tkinter as ui
from PIL import ImageTk, Image
import wget
from tkinter import messagebox, ttk
import os.path

link = ''


class Ytd(ui.Tk):
    def machine(self):
        global link

        def download():
            root = ui.Tk()
            root.geometry('300x120')
            root.grid()
            pb = ttk.Progressbar(root, orient='horizontal', mode='indeterminate', length=280)
            pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
            yd = yt.streams.get_highest_resolution()
            # ADD FOLDER HERE
            yd.download('C:\\Users\\Akash\\OneDrive\\Desktop\\test')
            pb.start()

        def update(title):

            w2 = ui.Tk()
            w2.geometry('640x480')
            canvas = ui.Canvas(w2, background='black', width=640, height=480)
            canvas.pack()
            img = ImageTk.PhotoImage(Image.open(imm))
            canvas.create_image(0, 0, image=img)
            canvas.waitvar(imm)
            canvas.wait_variable(imm)
            canvas.configure(image_url)
            lbl2 = ui.Label(w2, text=title)
            lbl2.pack(side=ui.TOP)
            b2 = ui.Button(w2, text=" DOWNLOAD ", command=download, activeforeground="black",
                           activebackground="light gray",
                           padx=10,
                           pady=5, borderwidth=3)
            b2.pack(side=ui.RIGHT)
            w2.mainloop()

        flag = False
        try:
            yt = YouTube(link)
            t = "Title: " + yt.title
            image_url = yt.thumbnail_url
            imm = wget.download(image_url)

            if os.path.exists(imm):
                print('yes found' + imm)
            else:
                print('Waiting..')
                time.sleep(2000)
        except:
            messagebox.showinfo("ERROR", "Invalid Link")
            flag = True
        if flag:
            pass
        else:
            update(t)

    def __init__(self):
        super().__init__()

        def take():
            global link
            link = url.get()
            url.delete(0, ui.END)
            self.machine()

        self.title("Get It")
        self.geometry("480x300+590+300")
        self.minsize(width=480, height=300)
        self.maxsize(width=480, height=300)

        b1 = ui.Button(self, text=" GET ", command=take, activeforeground="black", activebackground="light gray",
                       padx=10,
                       pady=5, borderwidth=3)
        url = ui.Entry(self, width=50)

        url.pack()
        b1.pack()


if __name__ == "__main__":
    new = Ytd()
    new.mainloop()
