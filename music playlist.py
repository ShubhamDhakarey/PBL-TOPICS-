import tkinter as tk
from tkinter import filedialog, Listbox, messagebox
import pygame
import os

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x400")

        pygame.mixer.init()
        
        # Playlist and current track
        self.playlist = []
        self.current_track = None
        self.is_paused = False
        
        # GUI Components
        self.create_widgets()
        
    def create_widgets(self):
        # Playlist Listbox
        self.playlist_box = Listbox(self.root, selectmode=tk.SINGLE, bg="lightblue", fg="black", font=('arial', 12), width=40, height=10)
        self.playlist_box.pack(pady=20)
        
        # Control Buttons
        control_frame = tk.Frame(self.root)
        control_frame.pack()
        
        self.play_button = tk.Button(control_frame, text="Play", command=self.play_song)
        self.play_button.grid(row=0, column=0, padx=10)
        
        self.pause_button = tk.Button(control_frame, text="Pause", command=self.pause_song)
        self.pause_button.grid(row=0, column=1, padx=10)
        
        self.stop_button = tk.Button(control_frame, text="Stop", command=self.stop_song)
        self.stop_button.grid(row=0, column=2, padx=10)
        
        # Add and Remove Buttons
        add_button = tk.Button(self.root, text="Add Song", command=self.add_song)
        add_button.pack(pady=5)
        
        remove_button = tk.Button(self.root, text="Remove Song", command=self.remove_song)
        remove_button.pack(pady=5)

    def add_song(self):
        """Add a song to the playlist."""
        song_path = filedialog.askopenfilename(title="Choose a song", filetypes=(("MP3 Files", "*.mp3"),))
        if song_path:
            song_name = os.path.basename(song_path)
            self.playlist.append(song_path)
            self.playlist_box.insert(tk.END, song_name)

    def remove_song(self):
        """Remove the selected song from the playlist."""
        selected_song_index = self.playlist_box.curselection()
        if selected_song_index:
            song_index = selected_song_index[0]
            self.playlist_box.delete(song_index)
            del self.playlist[song_index]
        else:
            messagebox.showinfo("Remove Song", "No song selected to remove.")

    def play_song(self):
        """Play the selected song."""
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
        else:
            selected_song_index = self.playlist_box.curselection()
            if selected_song_index:
                song_index = selected_song_index[0]
                song_path = self.playlist[song_index]
                pygame.mixer.music.load(song_path)
                pygame.mixer.music.play(loops=0)
                self.current_track = song_path
            else:
                messagebox.showinfo("Play Song", "No song selected to play.")

    def pause_song(self):
        """Pause the current song."""
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.is_paused = True

    def stop_song(self):
        """Stop the current song."""
        pygame.mixer.music.stop()
        self.is_paused = False


# Create and run the music player
root = tk.Tk()
music_player = MusicPlayer(root)
root.mainloop()
