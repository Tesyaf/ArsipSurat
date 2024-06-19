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
        self.editing_item = None  # Track the item being edited
        self.setup_ui()
        self.load_surat()
