import pyautogui
import time
import tkinter as tk

# Function to perform a copy operation using keyboard shortcuts
def copyClick():
    time.sleep(0.1)  # Small delay to ensure the keypresses are registered
    pyautogui.hotkey('alt', 'tab')  # Switch to the previous window
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'c')  # Copy the selected text

# Function to perform a paste operation using keyboard shortcuts
def pasteClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'v')  # Paste the copied text

# Function to perform an undo operation using keyboard shortcuts
def undoClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'z')  # Undo the last action

# Function to simulate right arrow key presses
def rightClick():
    times = int(option_var.get())  # Get the number of times to press the key from the GUI
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    for _ in range(times):
        pyautogui.press('right')  # Press the right arrow key
    pyautogui.hotkey('alt', 'tab')

# Function to simulate left arrow key presses
def leftClick():
    times = int(option_var.get())
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    for _ in range(times):
        pyautogui.press('left')  # Press the left arrow key
    pyautogui.hotkey('alt', 'tab')

# Function to perform a cut operation using keyboard shortcuts
def cutClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'k')  # Cut the selected text

# Function to simulate the delete key press
def deleteClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('delete')  # Delete the selected item

# Function to perform a ripple delete operation using keyboard shortcuts
def RippleDeleteClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('shift', 'delete')  # Ripple delete

# Function to save a project using keyboard shortcuts
def saveProjectClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'shift', 's')  # Save project

# Function to open a project using keyboard shortcuts
def openProjectClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'o')  # Open project

# Function to insert text or item
def insertClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.press(',')  # Press comma key
    pyautogui.hotkey('shift', '3')  # Type '#'

# Function to open in Source Monitor using keyboard shortcuts
def openInSourceMonitorClick():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('shift', '8')  # Type '*'
    pyautogui.hotkey('shift', 'o')  # Open source monitor

# Function to switch to the Source Monitor screen
def sourceMonitorScreen():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('shift', '2')  # Switch to source monitor

# Function to switch to the Timeline screen
def timelineScreen():
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('shift', '3')  # Switch to timeline

# Function to increase a value in the GUI
def increase_value():
    current_value = int(option_var.get())
    if current_value < 10:  # Set a maximum limit
        option_var.set(str(current_value + 1))

# Function to decrease a value in the GUI
def decrease_value():
    current_value = int(option_var.get())
    if current_value > 1:  # Set a minimum limit
        option_var.set(str(current_value - 1))

# Initialize the main window
window = tk.Tk()
window.title("talSystem")

# Create a frame for buttons
buttonFrame = tk.Frame(window, relief=tk.RAISED, borderwidth=1)
buttonFrame.pack(fill='both', expand=True)
buttonFrame.columnconfigure(0, minsize=370, weight=1)
buttonFrame.columnconfigure(1, minsize=370, weight=1)
buttonFrame.columnconfigure(2, minsize=370, weight=1)
buttonFrame.rowconfigure(0, minsize=50, weight=1)
buttonFrame.rowconfigure(1, minsize=50, weight=1)
buttonFrame.rowconfigure(2, minsize=50, weight=1)
buttonFrame.rowconfigure(3, minsize=50, weight=1)
buttonFrame.rowconfigure(4, minsize=50, weight=1)

# Create an option menu for selecting the number of key presses
option_var = tk.StringVar(buttonFrame)
option_var.set("1")  # Default value

options = [str(i) for i in range(1, 11)]  # Options from 1 to 10
option_menu = tk.OptionMenu(buttonFrame, option_var, *options)
option_menu.config(font=('arial', 40), cursor="hand2", relief=tk.RAISED, borderwidth=4)
option_menu.grid(row=0, column=2, sticky='NSEW')

# Create buttons for increasing and decreasing values
increase_button = tk.Button(buttonFrame, text="+", font=('arial', 35), command=increase_value, cursor="hand2", relief=tk.RAISED, borderwidth=4)
increase_button.grid(row=1, column=2, sticky='NSEW')

decrease_button = tk.Button(buttonFrame, text="-", font=('arial', 35), command=decrease_value, cursor="hand2", relief=tk.RAISED, borderwidth=4)
decrease_button.grid(row=2, column=2, sticky='NSEW')

# Create buttons for various operations and assign commands
left_Click_Button = tk.Button(buttonFrame, text="←", font=('arial', 60), command=leftClick, cursor="hand2", relief=tk.RAISED, borderwidth=4)
left_Click_Button.grid(row=0, column=0, sticky='NSEW')

right_Click_Button = tk.Button(buttonFrame, text="→", font=('arial', 60), command=rightClick, cursor="hand2", relief=tk.RAISED, borderwidth=4)
right_Click_Button.grid(row=0, column=1, sticky='NSEW')

delete_Click_Button = tk.Button(buttonFrame, text="DELETE", height=2, font=('arial', 25), command=deleteClick, cursor="hand2", relief=tk.RAISED, borderwidth=4)
delete_Click_Button.grid(row=1, column=0, sticky='NSEW')

cut_Click_Button = tk.Button(buttonFrame, text="CUT", height=2, font=('arial', 25), command=cutClick, cursor="hand2", relief=tk.RAISED, borderwidth=4)
cut_Click_Button.grid(row=1, column=1, sticky='NSEW')

save_Project_Button = tk.Button(buttonFrame, text="SAVE PROJECT", height=2, font=('arial', 25), command=saveProjectClick, cursor="hand2", relief=tk.RAISED, borderwidth=4)
save_Project_Button.grid(row=3, column=2, sticky='NSEW')

open_Project_Button = tk.Button(buttonFrame, text="OPEN PROJECT", height=2, font=('arial', 25), command=openProjectClick, cursor="hand2", relief=tk.RAISED, borderwidth=4)
open_Project_Button.grid(row=4, column=2, sticky='NSEW')

insert_Button = tk.Button(buttonFrame, text="INSERT", height=2, font=('arial', 25), command=insertClick, cursor="hand2", relief=tk.RAISED, borderwidth=4)
insert_Button.grid(row=2, column=0, sticky='NSEW')

copy_Button = tk.Button(buttonFrame, text="COPY", height=2, font=('arial', 25), command=copyClick, cursor="hand2", relief=tk.RAISED, borderwidth=4)
copy_Button.grid(row=3, column=0, sticky='NSEW')

paste_Button = tk.Button(buttonFrame, text="PASTE", height=2, font=('arial', 25), command=pasteClick, cursor="hand2", relief=tk.RAISED, borderwidth=4)
paste_Button.grid(row=3, column=1, sticky='NSEW')

undo_Button = tk.Button(buttonFrame, text="UNDO", height=2, font=('arial', 25), command=undoClick, cursor="hand2", relief=tk.RAISED, borderwidth=4)
undo_Button.grid(row=2, column=1, sticky='NSEW')

Ripple_Delete_Button = tk.Button(buttonFrame, text="RIPPLE & DELETE", height=2, font=('arial', 25), command=RippleDeleteClick, cursor="hand2", relief=tk.RAISED, borderwidth=4)
Ripple_Delete_Button.grid(row=4, column=0, sticky='NSEW')

timeline_Button = tk.Button(buttonFrame, text="TIMELINE", height=2, font=('arial', 25), command=timelineScreen, cursor="hand2", relief=tk.RAISED, borderwidth=4)
timeline_Button.grid(row=4, column=1, sticky='NSEW')

# Start the GUI main loop
window.mainloop()


