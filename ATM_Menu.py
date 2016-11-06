#App Name: Virtual ATM Menu
#Python Version 3.5
#Developper: Larry Georges Muala

import tkinter
from tkinter import messagebox
import time

window = tkinter.Tk()

#window title
window.title('Virtual ATM')

#window size
window.geometry("190x280")

#code to disable maximize
window.resizable(0,0)

#window background color
window.configure(background="light slate gray")

#modify icon
#window.wm_iconbitmap('lelu.ico')


#Menu Bar

def about_app():
	print("App Name: Virtual ATM")
	print("App Description: ATM menu with deposit, withdrawal and statements printing options")
	print("Python Version 3.5")
	print("Developper: Larry Georges Muala")
	
	messagebox.showinfo("App Info", "App Name: Virtual ATM\n" + 
						"\nApp description:  ATM menu with deposit, withdrawal and statements printing options\n" + 
						"\nPython Version 3.5 \n" + 
						"\nDevelopper: Larry Georges Muala")

menubar = tkinter.Menu(window)
myMenu = tkinter.Menu(menubar, tearoff=0)
myMenu.add_command(label="About", command=about_app)
myMenu.add_separator()
myMenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="App Info", menu=myMenu)

#display the menu bar
window.config(menu=menubar)


#ATM Visual Menu headers and blank space labels
lbl_main = tkinter.Label(window, text="MENU", font=("Helvetica", 20), bg="gray1", fg="white")
lbl_main.pack(fill=tkinter.X)

lbl_blank = tkinter.Label(window, text=" ", bg="light slate gray")
lbl_blank.pack()

lbl_main = tkinter.Label(window, text="Choose Your Option", font=("Helvetica", 10), bg="light slate gray")
lbl_main.pack(fill=tkinter.X)

lbl_blank = tkinter.Label(window, text=" ", font=("Helvetica", 1), bg="light slate gray")
lbl_blank.pack()

#ATM Initial Balances and Buttons Menu
initial_balance = 1000

deposit_statement = ""

withdrawal_statement = ""

time_statement = ""

statement_list = []

#Checking balance function on pop up window
def check_balance():
	messagebox.showinfo("Balance", "Amount Available: R" + str(initial_balance))
	
btn_check = tkinter.Button(window, text="Check Balance", command=check_balance)
btn_check.pack(fill=tkinter.X)


#Deposit balance function on pop up window
def deposit_balance():

	toplevel = tkinter.Toplevel()
	toplevel.resizable(0,0)
	toplevel.configure(background="light slate gray")
	#toplevel.wm_iconbitmap('lelu.ico')
	
	label1 = tkinter.Label(toplevel, text="Deposit Menu", font=("Helvetica", 20), bg="gray1", fg="white")
	label1.pack()
	
	lbl_top_name = tkinter.Label(toplevel, text="Enter Amount To Deposit: ", bg="light slate gray")
	lbl_top_name.pack()
	
	ent_top_name = tkinter.Entry(toplevel)
	ent_top_name.pack()
	ent_top_name.focus()
	
	def save_deposit():
		var_save = ent_top_name.get()
		
		
		global initial_balance
		global deposit_statement
		global statement_list
		
		if var_save.isdigit():
			var_save = int(var_save)
			initial_balance = var_save + initial_balance
			
			#deposit time and date
			time_deposit = time.strftime('%H:%M:%S')
			date_deposit = time.strftime('%Y-%m-%d')

			deposit_statement = "Deposit of R" + str(var_save) + " made at " + str(time_deposit) + " on date: " + str(date_deposit)
		
			statement_list.append(deposit_statement)
		
			print(" ")
			print(deposit_statement)
			print(" ")
			print(initial_balance)
		
			toplevel.destroy()
			
		else:
			messagebox.showinfo("Error", "Invalid Entry")
			ent_top_name.delete(0, tkinter.END)
			ent_top_name.focus()
			
	btn_save = tkinter.Button(toplevel, text="Validate", command=save_deposit)
	btn_save.pack()
	
	lbl_blank = tkinter.Label(toplevel, text=" ", bg="light slate gray")
	lbl_blank.pack()
	
	btn_cancel = tkinter.Button(toplevel, text="Cancel Transaction", command=toplevel.destroy)
	btn_cancel.pack(fill=tkinter.X)
	
btn_deposit = tkinter.Button(window, text="Make Deposit", command=deposit_balance)
btn_deposit.pack(fill=tkinter.X)


#Draw balance function on pop up window
def draw_balance():
	toplevel = tkinter.Toplevel()
	toplevel.resizable(0,0)
	toplevel.configure(background="light slate gray")
	#toplevel.wm_iconbitmap('lelu.ico')
	
	label1 = tkinter.Label(toplevel, text="Withdrawal Menu", font=("Helvetica", 20), bg="gray1", fg="white")
	label1.pack()
	
	lbl_top_name = tkinter.Label(toplevel, text="Enter Amount To Withdraw: ", bg="light slate gray")
	lbl_top_name.pack()
	
	ent_top_name = tkinter.Entry(toplevel)
	ent_top_name.pack()
	ent_top_name.focus()
	
	def save_draw():
		var_draw = ent_top_name.get()
		var_draw = int(var_draw)
		
		global initial_balance
		global withdrawal_statement
		global statement_list
		
		if initial_balance >= var_draw:
			initial_balance = initial_balance - var_draw
			
			#withdrawal time and date
			time_draw = time.strftime('%H:%M:%S')
			date_draw = time.strftime('%Y-%m-%d')

			withdrawal_statement = "Withdrawal of R" + str(var_draw) + " made at " + str(time_draw) + " on date: " + str(date_draw)
			
			statement_list.append(withdrawal_statement)
		else:
			messagebox.showinfo("Error", "Insufficient Funds" + "\nMax Balance Allowed: R" + str(initial_balance))
			ent_top_name.delete(0, tkinter.END)
			draw_balance()
			ent_top_name.focus()
			
		print(initial_balance)
		
		toplevel.destroy()
		
	btn_save = tkinter.Button(toplevel, text="Validate", command=save_draw)
	btn_save.pack()
	
	lbl_blank = tkinter.Label(toplevel, text=" ", bg="light slate gray")
	lbl_blank.pack()

	btn_cancel = tkinter.Button(toplevel, text="Cancel Transaction", command=toplevel.destroy)
	btn_cancel.pack(fill=tkinter.X)
	
btn_draw = tkinter.Button(window, text="Withdraw Money", command=draw_balance)
btn_draw.pack(fill=tkinter.X)


#Print statement function on pop up window
def statement():
	
	global statement_list
	global time_statement
	global initial_balance
	
	time1 = time.strftime('%H:%M:%S')
	
	date1 = time.strftime('%Y-%m-%d')
	
	time_statement = "Statement printed at " + str(time1) + " on date: " + str(date1)
	blank_space = " "
	account_balance = "Account Balance: R" + str(initial_balance)
	
	statement_list.append(blank_space)
	statement_list.append(account_balance)
	statement_list.append(blank_space)
	statement_list.append(time_statement)
	statement_list.append(blank_space)
	
	toplevel = tkinter.Toplevel()
	toplevel.wm_geometry("800x300")
	toplevel.configure(background="beige")
	#toplevel.wm_iconbitmap('lelu.ico')
	
	label1 = tkinter.Label(toplevel, text="Statement Menu", font=("Helvetica", 20), bg="gray1", fg="white")
	label1.pack(fill=tkinter.X)
	
	lbl_top_name = tkinter.Label(toplevel, text="Statement Summary: ")
	lbl_top_name.pack(side=tkinter.TOP)
	
	Scrolls = tkinter.Scrollbar(toplevel)
	Scrolls.pack(side=tkinter.RIGHT,fill=tkinter.Y)

	listboxPrintStatement = tkinter.Listbox(toplevel, height=12, yscrollcommand=Scrolls.set)
	listboxPrintStatement.pack(fill=tkinter.X)

	for item in statement_list:
		listboxPrintStatement.insert(tkinter.END, item)

	Scrolls.configure(command=listboxPrintStatement.yview)
	
	btn_close = tkinter.Button(toplevel, text="Close Statement", command=toplevel.destroy)
	btn_close.pack()
	
btn_print = tkinter.Button(window, text="Print Statement", command=statement)
btn_print.pack(fill=tkinter.X)


#blank space labels for separator and Cancel Button
lbl_blank = tkinter.Label(window, text=" ", bg="light slate gray")
lbl_blank.pack()

lbl_blank = tkinter.Label(window, text=" ", bg="light slate gray")
lbl_blank.pack()

btn_cancel = tkinter.Button(window, text="Cancel Transaction", command=window.destroy)
btn_cancel.pack(fill=tkinter.X)



window.mainloop()