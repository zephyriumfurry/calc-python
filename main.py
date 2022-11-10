from tkinter import *

problem = ""

def press(num):
	global problem

	problem = problem + str(num)

	result.set(problem)

def done():
	try:

		global problem

		total = str(eval(problem))

		result.set(total)

		problem = ""

	except:
		result.set("Ошибка!")
		problem = ""

def clear():
	global problem
	problem = ""
	result.set("")

def remove():
    global problem
    problem = problem[:-1]
    result.set(problem)

window = Tk()
window.title("Calculator")
window.geometry("192x252")
# window.resizable(False, False)
window.configure(background="grey")

result = StringVar()

problem_field = Entry(window, textvariable=result, width = 28)
problem_field.place(x = 10, y = 10)

button1 = Button(window, text=' 1 ', fg='black', bg='white', command=lambda: press(1), height=2, width=4)
button1.place(x = 10, y = 80)

button2 = Button(window, text=' 2 ', fg='black', bg='white', command=lambda: press(2), height=2, width=4)
button2.place(x = 48, y = 80)

button3 = Button(window, text=' 3 ', fg='black', bg='white', command=lambda: press(3), height=2, width=4)
button3.place(x = 86, y = 80)

button4 = Button(window, text=' 4 ', fg='black', bg='white', command=lambda: press(4), height=2, width=4)
button4.place(x = 10, y = 120)

button5 = Button(window, text=' 5 ', fg='black', bg='white', command=lambda: press(5), height=2, width=4)
button5.place(x = 48, y = 120)

button6 = Button(window, text=' 6 ', fg='black', bg='white', command=lambda: press(6), height=2, width=4)
button6.place(x = 86, y = 120)

button7 = Button(window, text=' 7 ', fg='black', bg='white', command=lambda: press(7), height=2, width=4)
button7.place(x = 10, y = 160)

button8 = Button(window, text=' 8 ', fg='black', bg='white', command=lambda: press(8), height=2, width=4)
button8.place(x = 48, y = 160)

button9 = Button(window, text=' 9 ', fg='black', bg='white', command=lambda: press(9), height=2, width=4)
button9.place(x = 86, y = 160)

button0 = Button(window, text=' 0 ', fg='black', bg='white', command=lambda: press(0), height=2, width=4)
button0.place(x = 48, y = 200)

plus = Button(window, text=' + ', fg='black', bg='white', command=lambda: press("+"), height=2, width=4)
plus.place(x = 144, y = 80)

minus = Button(window, text=' - ', fg='black', bg='white', command=lambda: press("-"), height=2, width=4)
minus.place(x = 144, y = 120)

multiply = Button(window, text=' * ', fg='black', bg='white', command=lambda: press("*"), height=2, width=4)
multiply.place(x = 144, y = 160)

divide = Button(window, text=' / ', fg='black', bg='white', command=lambda: press("/"), height=2, width=4)
divide.place(x = 144, y = 200)

equal = Button(window, text=' = ', fg='black', bg='white', command=done, height=2, width=4)
equal.place(x = 86, y = 200)

clear = Button(window, text='Clear', fg='black', bg='white', command=clear, height=2, width=4)
clear.place(x = 10, y = 35)

remove = Button(window, text='CL', fg='black', bg='white', command=remove, height=2, width=4)
remove.place(x = 48, y = 35)

decimal = Button(window, text='.', fg='black', bg='white', command=lambda: press('.'), height=2, width=4)
decimal.place(x = 10, y = 200)

window.mainloop()
