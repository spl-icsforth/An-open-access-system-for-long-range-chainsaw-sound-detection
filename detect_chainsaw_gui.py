
import os
import sys
sys.path.append("./functions")

import pdb
import tkinter as tk
import tkinter.ttk  as ttk

from main import main
from tkinter import E, W, N, S

citation = 'N. Stefanakis, K. Psaroulakis, N. Simou and C. Astaras, "An open access system for long-range chainsaw sound detection" submitted for publication in EUSIPCO 2021.'


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
        self.run_btn_text = tk.StringVar()
        self.run_btn_text.set("Run\n(Please select a directory)")
        self.fpos = [1, 3, 6, 8]
        

        self.btn_lbl.set("Click to choose directory with target .wav files")
        dir_frame = ttk.LabelFrame(parent, text='Target directory')
        #dir_frame = tk.Frame(parent)
        dir_frame.grid(row=self.fpos[0], column=1, columnspan=3)        
        self.dir_lbl_text.set(f"Directory chosen: {self.pathIN.get()}")
        dir_lbl = tk.Label(dir_frame, textvariable = self.dir_lbl_text, wraplength=350, justify='left')
        dir_lbl.grid(row=0, column=0, padx=(10), pady=10)
        dir_btn = tk.Button(dir_frame, textvariable = self.btn_lbl, command=self.clicked_dir_button)
        dir_btn.grid(row=0, column=1, padx=(10), pady=10)

        pf = ttk.Labelframe(parent, text='Parameters')
        pf.grid(row=self.fpos[1], column=0, columnspan=3, sticky=E+W+N+S)        
        vad_frame = tk.Frame(pf)
        vad_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky=E+W+N+S)
        vad_lbl = tk.Label(vad_frame, text = f"VAD threshold chosen: \n[Can take values between 0.078-0.15]")
        vad_lbl.grid(row=0, column=0, padx=(10), pady=10)
        vad_textbox = tk.Entry(vad_frame, textvariable=self.vad_th)
        vad_textbox.grid(row=0, column=1, padx=(10), pady=10)
        vad_slider = tk.Scale(vad_frame, 
                    from_=0.078, to=0.15, resolution = 0.0001, 
                    orient=tk.HORIZONTAL, variable = self.vad_th)
        vad_slider.grid(row=0, column=2, padx=(10), pady=10, sticky='NSEW')


        prob_frame = tk.Frame(pf)
        prob_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky=E+W+N+S)
        prob_lbl = tk.Label(prob_frame, text = f"Probability threshold chosen: \n[Can take value between 0-1]")
        prob_lbl.grid(row=0, column=0, padx=(10), pady=10,sticky=E+W+N+S)
        prob_textbox = tk.Entry(prob_frame, textvariable=self.prob_th)
        prob_textbox.grid(row=0, column=1, padx=(10), pady=10)
        prob_slider = tk.Scale(prob_frame, 
                    from_=0, to=1, resolution = 0.01, 
                    orient=tk.HORIZONTAL, variable = self.prob_th)
        prob_slider.grid(row=0, column=2, padx=(10), pady=10)

        max_cpus = self.count_processors()
        cpu_frame = tk.Frame(pf)
        cpu_frame.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky=E+W+N+S)
        cpu_lbl = tk.Label(cpu_frame, text = f"Number of CPU units employed:")
        cpu_lbl.grid(row=0, column=0, padx=(10), pady=10)
        cpu_textbox = tk.Entry(cpu_frame, textvariable=self.cpus)
        cpu_textbox.grid(row=0, column=1, padx=(10), pady=10)
        cpu_slider = tk.Scale(cpu_frame, 
                    from_=1,to=max_cpus, resolution = 1, 
                    orient=tk.HORIZONTAL, variable = self.cpus)
        cpu_slider.grid(row=0, column=2, padx=(10), pady=10)

        # tkinter.ttk.Separator(master, orient=VERTICAL).grid(column=0, row=1, rowspan=4, sticky='ew')
        # tkinter.ttk.Separator(master, orient=VERTICAL).grid(column=,0 row=1, rowspan=4, sticky='ew')

        ok_frame = tk.Frame(parent)
        ok_frame.grid(row=self.fpos[2], column=2, columnspan=1, padx=10, pady=10, sticky=E+W+N+S)
        self.run_btn = tk.Button(ok_frame, textvariable = self.run_btn_text, 
        command=self.run_main, state=tk.DISABLED)
        self.run_btn.grid(row=0, column=0, padx=(10), pady=10)

        cite_frame = ttk.Labelframe(parent, text='Cite')
        cite_frame.grid(row=self.fpos[3], column=2, columnspan=1, padx=10, pady=10, sticky=E+W+N+S)
        
        cite_txt = 'If you find any of this library useful for your research please cite as:'
        cite_lbl = tk.Label(cite_frame, text = f"{cite_txt}\n\n{citation}", wraplength=350, justify='left')
        cite_lbl.grid(row=0, column=0, padx=(10), pady=10)
        copy_btn = tk.Button(cite_frame, text = "Copy to clipboard", command=self.copy_citation)
        copy_btn.grid(row=3, column=2, padx=(10), pady=10)
        self.copied_lbl_txt = tk.StringVar()
        copied_lbl = tk.Label(cite_frame, textvariable = self.copied_lbl_txt)
        copied_lbl.grid(row=4, column=2, padx=(10), pady=10)
        

    def copy_citation(self):
        self.parent.clipboard_clear()
        self.parent.clipboard_append(citation)
        self.parent.update() # the text will stay there after the window is closed
        self.copied_lbl_txt.set("(Copied!)")
        
    def run_main(self):
        # from main import main
        global vpathIN, vvad_th,vprob_th, vcpus 
        vpathIN = self.pathIN.get()
        vvad_th = self.vad_th.get()
        vprob_th = self.prob_th.get()
        vcpus = self.cpus.get()
        self.parent.destroy()
        # print("Starting execution. Please wait...")
        # main(self.pathIN.get(), self.vad_th.get(), \
        #      self.prob_th.get(), self.cpus.get())


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
        self.run_btn_text.set("Run")
        self.run_btn.config(state="normal")

    def count_processors(self):
        import multiprocessing
        import numpy as np
        nop=multiprocessing.cpu_count()
        print(str(int(nop)) + 'cpus found')
        return np.max([1,nop-1])

    def on_closing():
        import tkinter.messagebox
        if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
            print('Thank you for using our tool!')
            exit()

if __name__ == "__main__":
    global vpathIN, vvad_th,vprob_th, vcpus 
    root = tk.Tk()
    root.title("Chainsaw detection (GUI version)")
    MainApplication(root)
    root.protocol("WM_DELETE_WINDOW", MainApplication.on_closing)
    root.mainloop()
    print("Starting execution. Please wait...")
    main(vpathIN, vvad_th, \
         vprob_th, vcpus)
    
