from tkinter import filedialog
from tkinter import messagebox
import Ctkinter as Ctk
import tkinter as tk
import shutil
import glob
import os


class Get_music:
    def __init__(self, master, language='german') -> None:
        self.get_music_window = Ctk.CCanvas(master=master, bg='gray30', size=(500, 300), corners='rounded', max_rad=30)

        self.get_music_window.create_line(249, 0, 249, 300, width=2, fill='white')
        self.get_music_window.create_line(0, 50, 500, 50, width=2, fill='white')

        self.select_music_button = None
        self.select_thump_button = None
        self.confirm_button = None
        self.thump_box = None
        self.list_box = None  # Box with the songs in

        self.mp3_data = list()  # list with the song paths in
        self.nail = list()  # List with thumbnails paths in

        self._option_buttons()
        self._info_labels()

    def _option_buttons(self):
        self.select_music_button = Ctk.CButton(self.get_music_window, bg='green', highlight_color='lightgreen',
                                               pressing_color='darkgreen', width=180, height=80,
                                               text='Add Music', font=('Helvetica', 16), fg='white',
                                               rounded_corners='rounded', command=self._add_songs, max_rad=None)
        self.select_music_button.place(x=30, y=110)

        self.select_thump_button = Ctk.CButton(self.get_music_window, bg='green', highlight_color='lightgreen',
                                               pressing_color='darkgreen', width=180, height=80,
                                               text='Add Thumbnails', font=('Helvetica', 16), fg='white',
                                               rounded_corners='rounded', command=self._add_thumbnails, max_rad=None)
        self.select_thump_button.place(x=280, y=110)

        self.confirm_button = Ctk.CButton(self.get_music_window, bg='green', highlight_color='lightgreen',
                                          pressing_color='darkgreen', width=100, height=40, text='Confirm',
                                          font=('Helvetica', 13), fg='white', rounded_corners='round',
                                          command=self._confirm_selection, max_rad=None)

        self.confirm_button.place(x=390, y=250)

    def _add_thumbnails(self):
        find_directory = filedialog.askdirectory(title='Select Directory with Thumbnails (.jpg)')
        self.nail = glob.glob(find_directory + '/*.jpg')

        self.thump_box = tk.Listbox(self.get_music_window.get_canvas(), bg=self.get_music_window['background'], bd=-2,
                                    font=('Helvetica', 12), width=25, fg='white', selectmode=tk.MULTIPLE,
                                    highlightthickness=-4, exportselection=False)

        for thumb in self.nail:
            try:
                self.thump_box.insert("end", '  ' + thumb.split('/')[(len(thumb.split('/')))-1].split('\\')[1])
            except IndexError:
                break

        if len(self.nail) != 0:
            self.thump_box.place(x=260, y=60)

            self.select_thump_button.destroy()

    def _add_songs(self):
        find_directory = filedialog.askdirectory(title='Select Music Directory:')
        self.mp3_data = glob.glob(find_directory + '/*.mp3')

        self.list_box = tk.Listbox(self.get_music_window.get_canvas(), bg=self.get_music_window['background'], bd=-2,
                                   font=('Helvetica', 12), width=25, fg='white', selectmode=tk.MULTIPLE,
                                   highlightthickness=-4, exportselection=False)

        for song in self.mp3_data:
            self.list_box.insert("end", '  ' + song.split('/')[(len(song.split('/')) - 1)].split('\\')[1])

        self.list_box.place(x=10, y=60)

        if len(self.mp3_data) != 0:
            self.select_music_button.destroy()

    def _confirm_selection(self):
        # check data input (check if the selection could be right interpreted)

        song_paths = list()
        thumb_paths = list()
        for index in self.list_box.curselection():
            song_paths.append(self.mp3_data[index])

        for index1 in self.thump_box.curselection():
            thumb_paths.append(self.nail[index1])

        if len(thumb_paths) == 1 and len(song_paths) != 0:
            # case 2 (mostly selected mode (for one ore more songs the same thumbnail))
            for counter, item in enumerate(song_paths):
                item_name = item.split('/')[(len(item.split('/')) - 1)].split('\\')[1].split('.')[0]
                os.mkdir('Songs/' + item_name + '/')
                shutil.copy(song_paths[counter], 'Songs/' + item_name + '/')
                shutil.copy(thumb_paths[0], 'Songs/' + item_name + '/')
                os.rename('Songs/' + item_name + '/' + thumb_paths[0].split('/')[(len(thumb_paths[0].
                                                                                      split('/')) - 1)].
                          split('\\')[1], 'Songs/' + item_name + '/thump.jpg')

        else:
            # a error occurrence this is not allowed
            messagebox.showerror("This is not allowed", "Pleas select only one thumbnail for one or many songs")

    def _info_labels(self):
        info1 = tk.Label(master=self.get_music_window.get_canvas(), text='Songs:', font=('Helvetica', 19), fg='white',
                         bg=self.get_music_window['background'])
        info1.place(x=18, y=6)
        info2 = tk.Label(master=self.get_music_window.get_canvas(), text='Thumbs:', font=('Helvetica', 19), fg='white',
                         bg=self.get_music_window['background'])
        info2.place(x=265, y=6)




