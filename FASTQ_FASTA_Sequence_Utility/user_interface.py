"""
This piece of code aims to create a user interface for the previous methods created

This tool will have two options:
 - one to select a fastq file to convert in fasta
 - one to select a fasta file to find orfs in it and translate them
"""

import PySimpleGUI as sg #Import the PySimpleGUI library
from sequence_utility import find_orf #Import the find_orf method from sequence_utility.py
from fastq_to_fasta import fastq_to_fasta #Import the fastq_to_fasta method from fastq_to_fasta.py
import os.path

# Create the layout of the window
layout = [
    [
        sg.Text("FASTA file selector"), #Text for the FASTA file selector
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER_FASTA-", change_submits=True), #Input for the FASTA file selector
        sg.FileBrowse(), #Opens the file browser
        sg.Button("Find ORFS", key="-FIND_ORFS-", disabled=True), #Button to find ORFS and translate them
    ],
    [
        sg.Text("FASTQ file selector"), #Text for the FASTQ file selector
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER_FASTQ-", change_submits=True), #Input for the FASTQ file selector
        sg.FileBrowse(), #Opens the file browser
        sg.Button("Convert to FASTA", key="-FASTQ_TO_FASTA-", disabled=True), #Button to convert a FASTQ file to FASTA
    ]
]

# Create the window using the generated layout
window = sg.Window("Sequence Utility Tool", layout)

while True:
    event, values = window.read() #Opens the window
    if event == sg.WIN_CLOSED: #If the window is closed, the program stops
        break
    elif event == "-FOLDER_FASTA-": #If the FASTA file selector is used, the button to find ORFS is enabled
        filename = values["-FOLDER_FASTA-"] #Gets the filename from the FASTA file selector
        if filename: #If the filename is not empty the button is enabled
            window["-FIND_ORFS-"].update(disabled=False)
    elif event == "-FOLDER_FASTQ-": #If the FASTQ file selector is used, the button to convert to FASTA is enabled
        filename = values["-FOLDER_FASTQ-"] #Gets the filename from the FASTQ file selector
        if filename: #If the filename is not empty the button is enabled
            window["-FASTQ_TO_FASTA-"].update(disabled=False)

    elif event == "-FIND_ORFS-": #If the button to find ORFS is pressed, the find_orf method is called
        filename = values["-FOLDER_FASTA-"]
        if filename:
            find_orf(filename)
    elif event == "-FASTQ_TO_FASTA-": #If the button to convert to FASTA is pressed, the fastq_to_fasta method is called
        filename = values["-FOLDER_FASTQ-"]
        if filename:
            fastq_to_fasta(filename)

window.close() #Closes the window
