from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import csv
from tkinter import filedialog

class ArsipSuratApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Arsip Surat")
        self.root.geometry("1080x720")
        self.root.configure(bg='#102C57')

        self.btnColor = "#196e78"
        self.editing_item = None
        self.setup_ui()
        self.load_surat()
        
    def setup_ui(self):
        # Labels
        label = Label(self.root, text="Arsip Surat", fg="white",bg='#102C57', font=("Times New Roman", 27))
        label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

        nomorsuratLabel = Label(self.root, text="No Surat",fg="white",bg='#102C57', font=("Times New Roman", 12))
        perihalLabel = Label(self.root, text="Perihal",fg="white",bg='#102C57', font=("Times New Roman", 12))
        tglLabel = Label(self.root, text="Tanggal Surat",fg="white",bg='#102C57', font=("Times New Roman", 12))
        pengirimLabel = Label(self.root, text="Pengirim",fg="white",bg='#102C57', font=("Times New Roman", 12))
        penerimaLabel = Label(self.root, text="Penerima",fg="white",bg='#102C57', font=("Times New Roman", 12))

        nomorsuratLabel.grid(row=3, column=0, padx=50, pady=5)
        perihalLabel.grid(row=4, column=0, padx=50, pady=5)
        tglLabel.grid(row=5, column=0, padx=50, pady=5)
        pengirimLabel.grid(row=6, column=0, padx=50, pady=5)
        penerimaLabel.grid(row=7, column=0, padx=50, pady=5)
