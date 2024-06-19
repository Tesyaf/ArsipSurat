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
        
        # Entry fields
        self.nomorsuratEntry = Entry(self.root, font=("Times New Roman", 12))
        self.perihalEntry = Entry(self.root, font=("Times New Roman", 12))
        self.tglEntry = Entry(self.root, font=("Times New Roman", 12))
        self.pengirimEntry = Entry(self.root, font=("Times New Roman", 12))
        self.penerimaEntry = Entry(self.root, font=("Times New Roman", 12))
        self.searchEntry = Entry(self.root, font=("Times New Roman", 12))

        self.nomorsuratEntry.grid(row=3, column=1, padx=10, pady=5,sticky='ew')
        self.perihalEntry.grid(row=4, column=1, padx=10, pady=5,sticky='ew')
        self.tglEntry.grid(row=5, column=1, padx=10, pady=5,sticky='ew')
        self.pengirimEntry.grid(row=6, column=1, padx=10, pady=5,sticky='ew')
        self.penerimaEntry.grid(row=7, column=1, padx=10, pady=5,sticky='ew')
        self.searchEntry.grid(row=3, column=3, padx=10, pady=5, sticky='ew')
        
        # Buttons
        button_width = 20  # Set the width of the buttons

        addButton = Button(self.root, text="Tambah Surat", bg=self.btnColor, fg="white", font=("Times New Roman", 12), command=self.add_surat, width=button_width)
        addButton.grid(row=7, column=3, padx=10, pady=5, sticky='ew')

        removeButton = Button(self.root, text="Hapus Surat", bg=self.btnColor, fg="white", font=("Times New Roman", 12), command=self.remove_surat, width=button_width)
        removeButton.grid(row=9, column=0, padx=10, pady=20, sticky='ew')

        editButton = Button(self.root, text="Edit Surat", bg=self.btnColor, fg="white", font=("Times New Roman", 12), command=self.edit_surat, width=button_width)
        editButton.grid(row=10, column=0, padx=10, pady=20, sticky='ew')

        saveEditButton = Button(self.root, text="Simpan Edit", bg=self.btnColor, fg="white", font=("Times New Roman", 12), command=self.save_edit_surat, width=button_width)
        saveEditButton.grid(row=11, column=0, padx=10, pady=20, sticky='ew')

        sortPerihalButton = Button(self.root, text="Urutkan berdasarkan Perihal", bg=self.btnColor, fg="white", font=("Times New Roman", 12), command=self.sort_by_perihal)
        sortPerihalButton.grid(row=15, column=0, padx=10, pady=20, sticky='ew')

        sortNomorSuratButton = Button(self.root, text="Urutkan berdasarkan Nomor Surat", bg=self.btnColor, fg="white", font=("Times New Roman", 12), command=self.sort_by_nomor_surat)
        sortNomorSuratButton.grid(row=15, column=1, padx=10, pady=20, sticky='ew')
        
        searchButton = Button(self.root, text="Cari Surat", bg=self.btnColor, fg="white", font=("Times New Roman", 12), command=lambda: self.search_treeview(self.searchEntry.get()))  # Assuming searching in the first column
        searchButton.grid(row=3, column=4, padx=10, pady=5, sticky='ew')
        self.root.grid_columnconfigure(0, uniform="button")
        
        # Treeview
        columns = ['Nomor', 'Perihal', 'Tanggal', 'Pengirim', 'Penerima']
        self.my_tree = ttk.Treeview(self.root, columns=columns, show='headings')
        for col in columns:
            self.my_tree.heading(col, text=col)
            self.my_tree.column(col, width=150)

        self.my_tree.grid(row=8, column=1, columnspan=7, rowspan=4, padx=20, pady=20, sticky='nsew')
