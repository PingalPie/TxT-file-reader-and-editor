from tkinter import *
from tkinter import filedialog
# Modules required


root = Tk()
# making root which is used in most things of tkinter

root.title('Txt Opener and editor')
# Your own title

root.iconbitmap('you can change location')
# For location of logo you can remove it default logo will come

root.geometry("450x450")
# Size of Tkinter project you can change
'''
Read only r  
Read and Write r+  (beginning of file)
Write Only w   (over-written)
Write and Read w+  (over written)
Append Only a  (end of file)
Append and Read a+  (end of file)

Some variables to remember
these are used in open file 
in python

'''


def open_txt():
	text_file = filedialog.askopenfilename(initialdir="C:/", title="Open Text File", filetypes=(("Text Files", "*.txt"), ))
	# Open file dialog
  name = text_file
  # converting text_file variable into name
	name = name.replace("C:/", "")
	name = name.replace(".txt", "")
	
	text_file = open(text_file, 'r')
	stuff = text_file.read()
  # Data to which you guys will see when you will open txt file
	
  my_text.insert(END, stuff)
	text_file.close()
	root.title(f'{name} - Textpad')
  # Opening file in tkinter

def save_txt():
	text_file = filedialog.askopenfilename(initialdir="C:/", title="Open Text File", filetypes=(("Text Files", "*.txt"), ))
	text_file = open(text_file, 'w')
	text_file.write(my_text.get(1.0, END))
  # Making save txt button
  
my_frame = Frame(root)
my_frame.pack(pady=10)

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)
# Create scrollbar

my_text = Text(my_frame, width=40, height=10, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", yscrollcommand=text_scroll.set, undo=True)
my_text.pack()
# For design you may not see it because it is in background

text_scroll.config(command=my_text.yview)
# Configure our scrollbar

open_button = Button(root, text="Open Text File", command=open_txt)
open_button.pack(pady=20)
# Making open file button

save_button = Button(root, text="Save File", command=save_txt)
save_button.pack(pady=20)
# Making save file button

root.mainloop()
# Starting the program
# If root.mainloop() is not there program will not run
