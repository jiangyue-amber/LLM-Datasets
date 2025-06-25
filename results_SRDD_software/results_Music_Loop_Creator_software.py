# Software Name: Music_Loop_Creator
# Category: Music
# Description: The Music Loop Creator is a software application that allows users to easily create and arrange loops of musical patterns. Users can select different instrument sounds and create their own sequences of notes or chords. The software provides a user-friendly interface with a grid-based layout where users can place and rearrange musical patterns to create unique loops. It also offers features like tempo adjustment, loop length customization, and the ability to export the loops to various audio file formats. The Music Loop Creator aims to empower musicians, producers, and DJs with a versatile tool for loop creation and music production.

```python
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import random
import wave
import struct
import os

class MusicLoopCreator:
    def __init__(self, master):
        self.master = master
        master.title("Music Loop Creator")

        self.tempo = 120
        self.loop_length = 8
        self.instruments = ["Piano", "Guitar", "Drums", "Synth"]
        self.selected_instrument = self.instruments[0]
        self.grid = []
        self.note_options = ["C4", "D4", "E4", "F4", "G4", "A4", "B4"]
        self.sample_rate = 44100
        self.duration = 0.2  # Duration of each note in seconds

        self.create_widgets()

    def create_widgets(self):
        # Tempo Control
        self.tempo_label = ttk.Label(self.master, text="Tempo (BPM):")
        self.tempo_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.tempo_entry = ttk.Entry(self.master, width=5)
        self.tempo_entry.insert(0, str(self.tempo))
        self.tempo_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Loop Length Control
        self.loop_length_label = ttk.Label(self.master, text="Loop Length (Steps):")
        self.loop_length_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.loop_length_entry = ttk.Entry(self.master, width=5)
        self.loop_length_entry.insert(0, str(self.loop_length))
        self.loop_length_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Instrument Selection
        self.instrument_label = ttk.Label(self.master, text="Instrument:")
        self.instrument_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

        self.instrument_combo = ttk.Combobox(self.master, values=self.instruments, state="readonly")
        self.instrument_combo.set(self.selected_instrument)
        self.instrument_combo.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.instrument_combo.bind("<<ComboboxSelected>>", self.update_instrument)

        # Grid Creation
        self.grid_frame = ttk.Frame(self.master)
        self.grid_frame.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.create_grid()

        # Buttons
        self.play_button = ttk.Button(self.master, text="Play Loop", command=self.play_loop)
        self.play_button.grid(row=4, column=0, padx=5, pady=5)

        self.export_button = ttk.Button(self.master, text="Export to WAV", command=self.export_wav)
        self.export_button.grid(row=4, column=1, padx=5, pady=5)

        self.update_button = ttk.Button(self.master, text="Update Settings", command=self.update_settings)
        self.update_button.grid(row=0, column=2, rowspan=2, padx=5, pady=5)

    def create_grid(self):
        for widget in self.grid_frame.winfo_children():
            widget.destroy()  # Clear existing grid

        self.grid = []
        for i in range(len(self.note_options)):
            row = []
            for j in range(self.loop_length):
                button = ttk.Button(self.grid_frame, text="", width=3, command=lambda row_index=i, col_index=j: self.toggle_note(row_index, col_index))
                button.grid(row=i, column=j, padx=1, pady=1)
                row.append(button)
            self.grid.append(row)

    def toggle_note(self, row, col):
        button = self.grid[row][col]
        if button.cget("text") == "":
            button.config(text="X")
        else:
            button.config(text="")

    def play_loop(self):
        self.update_settings()
        loop_data = self.generate_loop_data()
        self.play_audio(loop_data)

    def generate_loop_data(self):
        all_frames = b''
        for step in range(self.loop_length):
            for row in range(len(self.note_options)):
                button = self.grid[row][step]
                if button.cget("text") == "X":
                    frequency = self.note_to_frequency(self.note_options[row])
                    frames = self.generate_sine_wave(frequency)
                    all_frames += frames
                else:
                    num_samples = int(self.sample_rate * self.duration / (self.tempo / 60) )
                    all_frames += b'\0' * (2 * num_samples)

        return all_frames

    def generate_sine_wave(self, frequency):
        num_samples = int(self.sample_rate * self.duration / (self.tempo / 60))
        sample_width = 2  # 2 bytes for 16-bit audio

        frames = b''
        for i in range(num_samples):
            t = float(i) / self.sample_rate
            value = int(32767.0 * (0.5 * self.get_instrument_amplitude() *  (1+self.get_instrument_overtone()) *  (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) )  *  (
                (0.5 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) *  (
                    (0.2 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) *  (
                        (0.1 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) *  (
                            (0.05 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) *  (
                                (0.02 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) *  (
                                    (0.002 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) *  (
                                        (0.001 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * (
                                           (0.0001 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * (
                                                (0.00001 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * 0.3
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )) *  (
                (
                  (1 - 0.1 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) )
                ) * 0.8
            )) * (
                (
                 (1 - 0.2 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) )
                ) * 0.3
            )) * (
                (
                 (1 - 0.3 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) )
                ) * 0.1
            )) * (
                (
                 (1 - 0.4 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) )
                ) * 0.05
            )) * (
                (
                 (1 - 0.5 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) )
                ) * 0.02
            )) * (
                (
                 (1 - 0.6 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) )
                ) * 0.002
            )) * (
                (
                 (1 - 0.7 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) )
                ) * 0.001
            )) * (
                (
                 (1 - 0.8 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) )
                ) * 0.0001
            )) * (
                (
                 (1 - 0.9 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) )
                ) * 0.00001
            )) * (
                (
                 (1 - 0.95 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) )
                ) * 0.000001
            )) * (

            (1 + 0.025 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * (
                 (1 + 0.02 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * 0.5
            )) * (
                (0.5 *  ( (1 + 0.02 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * 0.5) * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * (
                    (0.2 * ( (1 + 0.02 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * 0.5) * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * (
                        (0.1 * ( (1 + 0.02 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * 0.5) * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * (
                            (0.05 * ( (1 + 0.02 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * 0.5) * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * (
                                (0.02 * ( (1 + 0.02 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * 0.5) * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * (
                                    (0.002 * ( (1 + 0.02 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * 0.5) * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * (
                                        (0.001 * ( (1 + 0.02 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * 0.5) * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * (
                                           (0.0001 * ( (1 + 0.02 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * 0.5) * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * (
                                                (0.00001 * ( (1 + 0.02 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * 0.5) * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) ) * 0.3
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )

            )

            ) *  (
                (
                    (1 - 0.1 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) )
                ) * 0.8
            )) * (
                (
                 (1 - 0.2 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) )
                ) * 0.3
            )) * (
                (
                 (1 - 0.3 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) )
                ) * 0.1
            )) * (
                (
                 (1 - 0.4 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) )
                ) * 0.05
            )) * (
                (
                 (1 - 0.5 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) )
                ) * 0.02
            )) * (
                (
                 (1 - 0.6 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) )
                ) * 0.002
            )) * (
                (
                 (1 - 0.7 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) )
                ) * 0.001
            )) * (
                (
                 (1 - 0.8 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) )
                ) * 0.0001
            )) * (
                (
                 (1 - 0.9 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) )
                ) * 0.00001
            )) * (
                (
                 (1 - 0.95 * (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3()) )
                ) * 0.000001
            ))
           )* 0.025) *  (1+ self.get_instrument_overtone())  *   (1+self.get_instrument_overtone2()) * (1 + self.get_instrument_overtone3())

            sample = struct.pack('<h', int(value))  # '<h' for short int (2 bytes)
            frames += sample

        return frames

    def play_audio(self, data):
        try:
            import pyaudio
            p = pyaudio.PyAudio()
            stream = p.open(format=pyaudio.paInt16,
                            channels=1,
                            rate=self.sample_rate,
                            output=True)
            stream.write(data)
            stream.stop_stream()
            stream.close()
            p.terminate()
        except ImportError:
            messagebox.showerror("Error", "PyAudio not installed. Please install it to play audio.")

    def export_wav(self):
        self.update_settings()
        filename = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
        if filename:
            loop_data = self.generate_loop_data()
            self.save_wav(filename, loop_data)

    def save_wav(self, filename, data):
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(self.sample_rate)
        wf.writeframes(data)
        wf.close()
        messagebox.showinfo("Export", "Loop exported to " + filename)

    def note_to_frequency(self, note):
        note_map = {
            "C4": 261.63,
            "D4": 293.66,
            "E4": 329.63,
            "F4": 349.23,
            "G4": 392.00,
            "A4": 440.00,
            "B4": 493.88
        }
        return note_map.get(note, 440.00)

    def update_instrument(self, event=None):
        self.selected_instrument = self.instrument_combo.get()

    def update_settings(self):
        try:
            self.tempo = int(self.tempo_entry.get())
            self.loop_length = int(self.loop_length_entry.get())
            self.create_grid()  # Recreate grid with new loop length
            self.update_instrument() #update intrument selection
        except ValueError:
            messagebox.showerror("Error", "Invalid tempo or loop length. Please enter integers.")

    def get_instrument_amplitude(self):
        if self.selected_instrument == "Piano":
            return 0.8
        elif self.selected_instrument == "Guitar":
            return 0.6
        elif self.selected_instrument == "Drums":
            return 0.9
        elif self.selected_instrument == "Synth":
            return 0.7
        else:
            return 0.8

    def get_instrument_overtone(self):
         if self.selected_instrument == "Piano":
            return 0.2
         elif self.selected_instrument == "Guitar":
             return 0.5
         elif self.selected_instrument == "Drums":
            return 0.01
         elif self.selected_instrument == "Synth":
             return 0.9
         else:
             return 0.001

    def get_instrument_overtone2(self):
         if self.selected_instrument == "Piano":
            return 0.03
         elif self.selected_instrument == "Guitar":
             return 0.56
         elif self.selected_instrument == "Drums":
            return 0.013
         elif self.selected_instrument == "Synth":
             return 0.39
         else:
             return 0.0013

    def get_instrument_overtone3(self):
         if self.selected_instrument == "Piano":
            return 0.004
         elif self.selected_instrument == "Guitar":
             return 0.76
         elif self.selected_instrument == "Drums":
            return 0.023
         elif self.selected_instrument == "Synth":
             return 0.59
         else:
             return 0.0023

root = tk.Tk()
my_gui = MusicLoopCreator(root)
root.mainloop()
```