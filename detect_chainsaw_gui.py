import argparse
import os
import numpy as np
import librosa
import glob
import multiprocessing
import sys
sys.path.append("./functions")

from extract_pcen_feature import extract_pcen_feature as extract_features
from classify_features import classify_features 
              
import pdb
import tkinter as tk

from main import main
from tkinter import E, W, N, S
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pathIN = tk.StringVar() 
        self.btn_lbl = tk.StringVar()
        self.dir_lbl_text = tk.StringVar()
        

        self.btn_lbl.set("Click to choose directory with target .wav files")

        dir_frame = tk.Frame(parent)
        dir_frame.grid(row=1, column=0, columnspan=3, sticky=E+W+N+S)        
        self.dir_lbl_text.set(f"Directory chosen: {self.pathIN.get()}")

        dir_lbl = tk.Label(dir_frame, textvariable = self.dir_lbl_text)
        dir_lbl.grid(row=0, column=0, padx=(10), pady=10)
        dir_btn = tk.Button(dir_frame, textvariable = self.btn_lbl, command=self.clicked_dir_button)
        dir_btn.grid(row=0, column=1, padx=(10), pady=10)



    def clicked_dir_button(self, *args):
        import tkinter.filedialog
        newdir = tkinter.filedialog.askdirectory(parent=self.parent, 
        initialdir=os.getcwd(), 
        title='Please select the directory containing the target .wav files.')
        if newdir: self.pathIN.set(newdir)
        print(newdir)
        self.dir_lbl_text.set(f"Directory chosen: {self.pathIN.get()}")          
        self.btn_lbl.set("Click to change directory")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Chainsaw detection software")
    MainApplication(root)#.pack(side="top", fill="both", expand=True)
    root.mainloop()

    
