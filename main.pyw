from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import random, string

class password:
	def __init__(self, window):
		self.window = window
		self.window.title('Password Generator')
		self.window.resizable(0,0)

		# Creating a Frame Container
		frame = Frame(self.window)
		frame.grid(row = 0, column = 0, padx = 10, pady = 10)

		# Variables
		self.characters = ''
		self.letters = IntVar()
		self.digits = IntVar()
		self.punctuation = IntVar()
		self.length = IntVar()
		self.password = StringVar()

		# Labels
		Label(frame, text = 'Create a New Password', font = ('verdana', 10, 'bold')).grid(row = 0, column = 0)
		Label(frame, text = 'Select a Characters: ').grid(row = 1, column = 0, sticky = W)

		# Creating a Frame Container of CheckBoxs
		frame_check = ttk.Frame(frame)
		frame_check.grid(row = 2, column = 0)

		# CheckBox
		self.letters_check = Checkbutton(frame_check, text = 'Letters', variable = self.letters, onvalue = 1, offvalue = 0, command = self.get_characters)
		self.letters_check.grid(row = 0, column = 0)
		self.digits_check = Checkbutton(frame_check, text = 'Digits', variable = self.digits, onvalue = 1, offvalue = 0, command = self.get_characters)
		self.digits_check.grid(row = 0, column = 1, padx = 10)
		self.punctuation_check = Checkbutton(frame_check, text = 'Punctuation', variable = self.punctuation, onvalue = 1, offvalue = 0, command = self.get_characters)
		self.punctuation_check.grid(row = 0, column = 2)

		# Password Length
		Label(frame, text = 'Select a Length:').grid(row = 3, column = 0, sticky = W)
		self.length_spinbox = Scale(frame, variable = self.length, from_ = 5, to = 15, orient = 'horizontal', showvalue=0, tickinterval = 1)
		self.length_spinbox.grid(row = 4, column = 0, sticky=W + E)

		# Password Generator
		Label(frame, text = 'Password:').grid(row = 5, column = 0, sticky = W)
		self.password_entry=Entry(frame, textvariable = self.password, state='readonly', justify = 'center')
		self.password_entry.grid(row = 6,column = 0, sticky=W + E)

		# Creating a Frame Container of Buttons
		ttk.Button(frame, text = 'Generate', command = self.generate_password).grid(row = 7, column = 0, sticky = W + E)
		ttk.Button(frame, text = 'Copy', command = self.copy_password).grid(row = 8, column = 0, sticky = W + E)

	def generate_password(self):
		if self.characters == '':
			messagebox.showwarning('Warning','Select a Character')
			return

		password = []
		for x in range(self.length.get()):
			password.append(random.choice(self.characters))

		self.password.set(''.join(password))

	def get_characters(self):
		self.characters = ''

		if self.letters.get() == 1: self.characters += string.ascii_letters
		if self.digits.get() == 1: self.characters += string.digits
		if self.punctuation.get() == 1: self.characters += string.punctuation

	def copy_password(self):
		if self.password.get() == '':
			messagebox.showwarning('Warning','Generate a Password')
			return

		self.window.clipboard_clear()
		self.window.clipboard_append(self.password.get())

if __name__ == "__main__":
	window = Tk()
	password(window)
	window.mainloop()