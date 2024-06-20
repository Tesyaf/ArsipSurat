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

    def merge_sort(self, data, column):
        if len(data) > 1:
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]

            self.merge_sort(left_half, column)
            self.merge_sort(right_half, column)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if column == 1:  # Sort by perihal
                    if left_half[i][column].lower() < right_half[j][column].lower():
                        data[k] = left_half[i]
                        i += 1
                    else:
                        data[k] = right_half[j]
                        j += 1
                else:  # Sort by Nomor Surat
                    if left_half[i][column] < right_half[j][column]:
                        data[k] = left_half[i]
                        i += 1
                    else:
                        data[k] = right_half[j]
                        j += 1
                k += 1

            while i < len(left_half):
                data[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                data[k] = right_half[j]
                j += 1
                k += 1
        return data


    def sort_by_perihal(self):
        self.sort_treeview(1)  # Sort by perihal

    def sort_by_nomor_surat(self):
        self.sort_treeview(0)  # Sort by nomor surat

    def sort_treeview(self, column):
        if column == 1:  # Sort by perihal
            data = [(self.my_tree.item(item, 'values')) for item in self.my_tree.get_children()]
            sorted_data = self.merge_sort(data, column)
            # Clear existing treeview
            for item in self.my_tree.get_children():
                self.my_tree.delete(item)
            # Insert sorted data
            for row in sorted_data:
                self.my_tree.insert('', 'end', values=row)
        else:  # Sort by Nomor Surat
            data = [(self.my_tree.item(item, 'values')) for item in self.my_tree.get_children()]
            sorted_data = self.merge_sort(data, column)
            # Clear existing treeview
            for item in self.my_tree.get_children():
                self.my_tree.delete(item)
            # Insert sorted data
            for row in sorted_data:
                self.my_tree.insert('', 'end', values=row)

    
    def add_surat(self):
        nomor = self.nomorsuratEntry.get()
        perihal = self.perihalEntry.get()
        tanggal = self.tglEntry.get()
        pengirim = self.pengirimEntry.get()
        penerima = self.penerimaEntry.get()

        if nomor and perihal and tanggal and pengirim and penerima:
            self.my_tree.insert('', 'end', values=(nomor, perihal, tanggal, pengirim, penerima))
            with open('arsip_surat.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([nomor, perihal, tanggal, pengirim, penerima])
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Semua bidang harus diisi!")


     
    def clear_entries(self):
        self.nomorsuratEntry.delete(0, END)
        self.perihalEntry.delete(0, END)
        self.tglEntry.delete(0, END)
        self.pengirimEntry.delete(0, END)
        self.penerimaEntry.delete(0, END)

    def remove_surat(self):
        selected_item = self.my_tree.selection()
        if selected_item:
            item_values = self.my_tree.item(selected_item, 'values')
            self.my_tree.delete(selected_item)
            with open('arsip_surat.csv', 'r') as file:
                rows = list(csv.reader(file))
            with open('arsip_surat.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                for row in rows:
                    if row != list(item_values):
                        writer.writerow(row)
        else:
            messagebox.showwarning("Selection Error", "Pilih surat yang ingin dihapus!")

    def load_surat(self):
        try:
            with open('arsip_surat.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.my_tree.insert('', 'end', values=row)
        except FileNotFoundError:
            pass

    def edit_surat(self):
        selected_item = self.my_tree.selection()
        if selected_item:
            item_values = self.my_tree.item(selected_item, 'values')
            self.clear_entries()
            self.nomorsuratEntry.insert(0, item_values[0])
            self.perihalEntry.insert(0, item_values[1])
            self.tglEntry.insert(0, item_values[2])
            self.pengirimEntry.insert(0, item_values[3])
            self.penerimaEntry.insert(0, item_values[4])
            self.editing_item = selected_item
        else:
            messagebox.showwarning("Selection Error", "Pilih surat yang ingin diedit!")

    def save_edit_surat(self):
        if self.editing_item:
            nomor = self.nomorsuratEntry.get()
            perihal = self.perihalEntry.get()
            tanggal = self.tglEntry.get()
            pengirim = self.pengirimEntry.get()
            penerima = self.penerimaEntry.get()

            if nomor and perihal and tanggal and pengirim and penerima:
                # Update the selected item in the Treeview
                self.my_tree.item(self.editing_item, values=(nomor, perihal, tanggal, pengirim, penerima))

                # Read all rows from the CSV
                with open('arsip_surat.csv', 'r') as file:
                    rows = list(csv.reader(file))

                # Update the specific row
                with open('arsip_surat.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    for row in rows:
                        if row == list(self.my_tree.item(self.editing_item, 'values')):
                            writer.writerow([nomor, perihal, tanggal, pengirim, penerima])
                        else:
                            writer.writerow(row)

                self.clear_entries()
                self.editing_item = None
            else:
                messagebox.showwarning("Input Error", "Semua bidang harus diisi!")
        else:
            messagebox.showwarning("Edit Error", "Tidak ada surat yang sedang diedit!")
