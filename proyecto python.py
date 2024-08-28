import tkinter as tk
from tkinter import filedialog
import pygame

class ReproductorMusica:
    def __init__(self, root):
        self.root = root 
        self.root.title("Reproductor de Música")
        self.playlist = []
        self.current_track = 0
        self.paused = False
        self.init_ui()

    def init_ui(self):
        self.label = tk.Label(self.root, text="Reproductor de Música", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.button_load = tk.Button(self.root, text="Cargar Canciones", command=self.load_songs)
        self.button_load.pack()

        self.button_play = tk.Button(self.root, text="Play", command=self.play_pause)
        self.button_play.pack()

        self.button_next = tk.Button(self.root, text="Siguiente", command=self.next_track)
        self.button_next.pack()

        self.button_prev = tk.Button(self.root, text="Anterior", command=self.prev_track)
        self.button_prev.pack()

        self.button_stop = tk.Button(self.root, text="Detener", command=self.stop_music)
        self.button_stop.pack()

        pygame.mixer.init()

    def load_songs(self):
        self.playlist = filedialog.askopenfilenames(filetypes=[("Archivos MP3", "*.mp3")])

    def play_pause(self):
        if not self.playlist:
            return
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            pygame.mixer.music.load(self.playlist[self.current_track])
            pygame.mixer.music.play()

    def next_track(self):
        if not self.playlist:
            return
        self.current_track = (self.current_track + 1) % len(self.playlist)
        self.play_pause()

    def prev_track(self):
        if not self.playlist:
            return
        self.current_track = (self.current_track - 1) % len(self.playlist)
        self.play_pause()

    def stop_music(self):
        pygame.mixer.music.stop()

def main():
    root = tk.Tk()
    reproductor = ReproductorMusica(root)
    root.mainloop()

if __name__ == '__main__':
    main()
        