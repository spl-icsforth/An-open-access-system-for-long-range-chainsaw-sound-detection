
import os
import sys
sys.path.append("./functions")
              
import pdb
import tkinter as tk

from main import main
from tkinter import E, W, N, S


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pathIN = tk.StringVar() 
        self.pathIN.set("[No directory selected]")
        self.btn_lbl = tk.StringVar()
        self.dir_lbl_text = tk.StringVar()
        self.prob_th = tk.DoubleVar()
        self.prob_th.set(0.75)
        self.cpus = tk.IntVar()
        self.cpus.set(6)
        self.vad_th = tk.DoubleVar()
        self.vad_th.set(0.078)
        

        self.btn_lbl.set("Click to choose directory with target .wav files")
        dir_frame = tk.Frame(parent)
        dir_frame.grid(row=1, column=0, columnspan=3, sticky=E+W+N+S)        
        self.dir_lbl_text.set(f"Directory chosen: {self.pathIN.get()}")
        dir_lbl = tk.Label(dir_frame, textvariable = self.dir_lbl_text, wraplength=500, justify='left')
        dir_lbl.grid(row=0, column=0, padx=(10), pady=10)
        dir_btn = tk.Button(dir_frame, textvariable = self.btn_lbl, command=self.clicked_dir_button)
        dir_btn.grid(row=0, column=1, padx=(10), pady=10)

        vad_frame = tk.Frame(parent)
        vad_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky=E+W+N+S)
        vad_lbl = tk.Label(vad_frame, text = f"VAD threshold chosen: \n[Can take values between 0.078-0.15]")
        vad_lbl.grid(row=0, column=0, padx=(10), pady=10)
        vad_textbox = tk.Entry(vad_frame, textvariable=self.vad_th)
        vad_textbox.grid(row=0, column=1, padx=(10), pady=10)
        vad_slider = tk.Scale(vad_frame, 
                    from_=0.078, to=0.15, resolution = 0.0001, 
                    orient=tk.HORIZONTAL, variable = self.vad_th)
        vad_slider.grid(row=0, column=2, padx=(10), pady=10, sticky='NSEW')


        prob_frame = tk.Frame(parent)
        prob_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky=E+W+N+S)
        prob_lbl = tk.Label(prob_frame, text = f"Probability threshold chosen: \n[Can take value between 0-1]")
        prob_lbl.grid(row=0, column=0, padx=(10), pady=10,sticky=E+W+N+S)
        prob_textbox = tk.Entry(prob_frame, textvariable=self.prob_th)
        prob_textbox.grid(row=0, column=1, padx=(10), pady=10)
        prob_slider = tk.Scale(prob_frame, 
                    from_=0, to=1, resolution = 0.01, 
                    orient=tk.HORIZONTAL, variable = self.prob_th)
        prob_slider.grid(row=0, column=2, padx=(10), pady=10)

        cpu_frame = tk.Frame(parent)
        cpu_frame.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky=E+W+N+S)
        cpu_lbl = tk.Label(cpu_frame, text = f"Number of CPU units employed:")
        cpu_lbl.grid(row=0, column=0, padx=(10), pady=10)
        cpu_textbox = tk.Entry(cpu_frame, textvariable=self.cpus)
        cpu_textbox.grid(row=0, column=1, padx=(10), pady=10)
        cpu_slider = tk.Scale(cpu_frame, 
                    from_=1,to=16, resolution = 1, 
                    orient=tk.HORIZONTAL, variable = self.cpus)
        cpu_slider.grid(row=0, column=2, padx=(10), pady=10)


        ok_frame = tk.Frame(parent)
        ok_frame.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky=E+W+N+S)
        self.run_btn = tk.Button(parent, text = 'Run', 
        command=self.run_main, state=tk.DISABLED)
        self.run_btn.grid(row=0, column=0, padx=(10), pady=10)

    def run_main(self):
        from main import main
        main(self.pathIN.get(), self.vad_th.get(), \
             self.prob_th.get(), self.cpus.get())

    def clicked_dir_button(self, *args):
        import tkinter.filedialog
        newdir = tkinter.filedialog.askdirectory(parent=self.parent, 
        initialdir=os.getcwd(), 
        title='Please select the directory containing the target .wav files.')
        if newdir: self.pathIN.set(newdir)
        print(newdir)
        ch_txt = self.pathIN.get()
        # width = 50; begin = 8;
        # if len(ch_txt)>width: ch_txt = f"{ch_txt[:begin]}...{ch_txt[-(width-begin-3):]}"
        self.dir_lbl_text.set(f"Directory chosen: {ch_txt}")          
        self.btn_lbl.set("Click to change directory")
        self.run_btn.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Chainsaw detection software")
    MainApplication(root)#.pack(side="top", fill="both", expand=True)
    root.mainloop()

    
