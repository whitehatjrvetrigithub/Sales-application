from tkinter import *

root = Tk()
root.title("Sales Application")
root.geometry("900x400")
root.configure(background = "yellow")

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits = (20000, 45000, 78000, 97000, 12000, 456000, 65000, 54000, 10000, 30000, 70000, 90000)

month_label = Label(root)
month_label["text"] = "Months : " + str(months)
month_label.place(relx = 0.5, rely = 0.2, anchor = CENTER)

profit_label = Label(root)
profit_label["text"] = "Profits : " + str(profits)
profit_label.place(relx = 0.5, rely = 0.3, anchor = CENTER)

max_label = Label(root)
max_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

min_label = Label(root)
min_label.place(relx = 0.5, rely = 0.7, anchor = CENTER)

def max_btn():
    max_profit = max(profits)
    max_profit_index = profits.index(max_profit)
    max_profit_month = months[max_profit_index]
    max_label["text"] = "Maximum profit of " + str(max_profit) + " was given in the month of " + str(max_profit_month) + " ."

def min_btn():
    min_profit = min(profits)
    min_profit_index = profits.index(min_profit)
    min_profit_month = months[min_profit_index]
    min_label["text"] = "Minimum profit of " + str(min_profit) + " was given in the month of " + str(min_profit_month) + " ."
    
btn_max = Button(root, text = "Show Max Profitable Month", command = max_btn, bg = "blue", fg = "white")
btn_max.place(relx = 0.5, rely = 0.4, anchor = CENTER)

btn_min = Button(root, text = "Show Min Profitable Month", command = min_btn, bg = "blue", fg = "white")
btn_min.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()