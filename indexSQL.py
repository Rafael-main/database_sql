import mysql.connector
from tkinter import *
import tkinter.messagebox
from tkinter import ttk



class main():
	def __init__(self, master):
		self.master = master
		self.frame = Frame(self.master)
		self.ws = self.master.winfo_screenwidth()
		self.hs = self.master.winfo_screenheight()
		x = (self.ws/2) - (900/2)
		y = (self.hs/2) - (500/2)
		self.master.geometry("900x500+%d+%d"%(x,y))
		self.master.title("MySQL and Python Database GUI")



		self.firstname = StringVar()
		self.lastname = StringVar()
		self.idnumber = StringVar()
		self.course = StringVar()
		self.year = IntVar()

		# database
		self.mydb = mysql.connector.connect(
			host = "localhost",
			user = "root",
			password = "spacebemorebarrio3131-",
			database = "testdb"
			)
		self.mycursor = self.mydb.cursor()
		self.mycursor.execute("CREATE DATABASE IF NOT EXISTS testdb")
		self.mycursor.execute("CREATE TABLE IF NOT EXISTS student(firstName VARCHAR(255), lastName VARCHAR(255), idNumber VARCHAR(255), course VARCHAR(255), year INTEGER(10))")

	def selectedItemToDelete(self,a):
		curItem = self.tree.focus()
		self.sel_id = str(self.tree.item(self.tree.selection())['values'][2])
	
	def show(self):
		self.mycursor.execute(""" SELECT firstName,lastName,idNumber,course,year FROM student """)
		result = self.mycursor.fetchall()
		for i in self.tree.get_children():
			self.tree.delete(i)
		for row in result:
			print(row)
			self.tree.insert("", "end", values = row)

	def insert(self):
		fname = self.firstname.get()
		lname = self.lastname.get()
		id_num = self.idnumber.get()
		course = self.course.get()
		year = self.year.get()

		firstname = fname.capitalize()
		lastname = lname.capitalize()
		iscourse = course.upper()

		isID = id_num.split('-')
		print(isID)

		if (int(isID[0]) < 1900 or int(isID[0]) > 2999):
			tkinter.messagebox.showerror("Wrong Input", "Wrong input")
		else:
			self.mycursor.execute(""" INSERT INTO student (firstName, lastName, idNumber, course, year) VALUES (%s,%s,%s,%s,%s) """, 
				(firstname, lastname, id_num, iscourse, year))
			self.mydb.commit()

			self.show()

			tkinter.messagebox.showinfo("Record Added", "You have registered successfully")


	def delete(self):

		self.mycursor.execute(" DELETE FROM student WHERE idNumber = %s", (self.sel_id,))
		self.mydb.commit()

		self.show()

	def update(self):
		upd_fname = self.firstname.get()
		upd_lname = self.lastname.get()
		upd_id_num = self.idnumber.get()
		upd_course = self.course.get()
		upd_year = self.year.get()

		upd_firstname = upd_fname.capitalize()
		upd_lastname = upd_lname.capitalize()
		upd_iscourse = upd_course.upper()
		isID = upd_id_num.split('-')

		if (int(isID[0]) < 1900 or int(isID[0]) > 2999):
			tkinter.messagebox.showerror("Wrong Input", "Wrong Input")

			
		else:
			self.mycursor.execute("""UPDATE student SET firstName = %s, lastname= %s, idNumber= %s, course= %s, year= %s 
				WHERE idNumber = %s""", (upd_firstname, upd_lastname, upd_id_num, upd_iscourse, upd_year, self.sel_id))
			self.mydb.commit()
			tkinter.messagebox.showinfo("Record Updated", "You have updated successfully")
			self.show()
			


	def edit(self):
		add_win = Toplevel(self.master)
		size = tuple(int(_) for _ in add_win.geometry().split('+')[0].split('x'))
		x = self.ws/3 - size[0]/2
		y = self.hs/3 - size[1]/2
		add_win.geometry("+%d+%d" % (x, y))

		fname_lbl = Label(add_win, text = 'First name:' , width = 18, font = ("arial", 10, "bold")).grid(row = 0, column=0)
		self.up_fname_entry = Entry(add_win, textvar = self.firstname).grid(row=0,column=1)

		lname_lbl = Label(add_win, text = 'Last name:' , width = 18, font = ("arial", 10, "bold")).grid(row = 1, column=0)
		self.up_lname_entry = Entry(add_win, textvar = self.lastname).grid(row=1,column=1)

		id_lbl = Label(add_win, text = 'ID Number:' , width = 18, font = ("arial", 10, "bold")).grid(row = 2, column=0)
		self.up_id_entry = Entry(add_win, textvar = self.idnumber).grid(row=2,column=1)

		course_lbl = Label(add_win, text = 'Course:' , width = 18, font = ("arial", 10, "bold")).grid(row = 3, column=0)
		self.up_course_entry = Entry(add_win, textvar = self.course).grid(row=3,column=1)

		year_lbl = Label(add_win, text = 'Year:' , width = 18, font = ("arial", 10, "bold")).grid(row = 4, column=0)
		self.up_year_entry = Entry(add_win, textvar = self.year).grid(row=4,column=1)

		add_btn = Button(add_win, text = 'Update', width = 12, command = lambda:[self.update(), add_win.destroy()]).grid(row = 5, column=0)
		close_btn = Button(add_win, text = 'Close', width = 12, command = add_win.destroy).grid(row=5,column=1)

		

	def add(self):
		add_win = Toplevel(self.master)
		size = tuple(int(_) for _ in add_win.geometry().split('+')[0].split('x'))
		x = self.ws/3 - size[0]/3
		y = self.hs/3 - size[1]/3
		add_win.geometry("+%d+%d" % (x, y))

		fname_lbl = Label(add_win, text = 'First name:' , width = 18, font = ("arial", 10, "bold")).grid(row = 0, column=0)
		self.fname_entry = Entry(add_win, textvar = self.firstname).grid(row=0,column=1)

		lname_lbl = Label(add_win, text = 'Last name:' , width = 18, font = ("arial", 10, "bold")).grid(row = 1, column=0)
		self.lname_entry = Entry(add_win, textvar = self.lastname).grid(row=1,column=1)

		id_lbl = Label(add_win, text = 'ID Number:' , width = 18, font = ("arial", 10, "bold")).grid(row = 2, column=0)
		self.id_entry = Entry(add_win, textvar = self.idnumber).grid(row=2,column=1)

		course_lbl = Label(add_win, text = 'Course:' , width = 18, font = ("arial", 10, "bold")).grid(row = 3, column=0)
		self.course_entry = Entry(add_win, textvar = self.course).grid(row=3,column=1)

		year_lbl = Label(add_win, text = 'Year:' , width = 18, font = ("arial", 10, "bold")).grid(row = 4, column=0)
		self.year_entry = Entry(add_win, textvar = self.year).grid(row=4,column=1)

		add_btn = Button(add_win, text = 'Register', width = 12, command = lambda:[self.insert(), add_win.destroy()]).grid(row = 5, column=0)
		close_btn = Button(add_win, text = 'Close', width = 12, command = add_win.destroy).grid(row=5,column=1)

	def main(self):
		lbl = Label(self.master, text = "CRUD using MySQL and Python Database GUI", width = 40, relief = "solid", font = ("arial", 19, "bold")).place(x = 170, y = 15)

		self.reg_btn = Button(self.master, text = 'Register', width = 12, command = self.add).place(x=15,y=90)
		self.delete_btn = Button(self.master, text = 'Delete', width = 12, command = self.delete).place(x=15,y=120)
		self.update_btn = Button(self.master, text = 'Update', width = 12, command = self.edit).place(x=15,y=150)
		self.exit_btn = Button(self.master, text = 'Exit', width = 12, command = self.master.destroy).place(x=15,y=180)

		cols = ('First Name', 'Last Name', 'ID Number', 'Course', 'Year Level')
		self.tree = ttk.Treeview(self.master,height = 20, columns = cols, show = 'headings')

		for col in cols:
			self.tree.heading(col, text = col)
		self.tree.place(x = 120, y = 60)
		self.selectedItemD = self.tree.bind('<ButtonRelease-1>', self.selectedItemToDelete)

		self.show()




if __name__ == '__main__':
	root = Tk()
	m = main(root)
	m.main()
	root.mainloop()
