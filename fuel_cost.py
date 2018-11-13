from tkinter import *
from tkinter import messagebox


def calculator():
    distance = float(entry_distance.get())
    fuel_consumption = float(entry_fuel_consumption.get())
    price = float(entry_price.get())
    result = (distance / 100) * fuel_consumption * price
    messagebox.showinfo(
        title='Fuel Cost Calculator',
        message=f'Fuel Cost: {result} PLN'
    )


root = Tk()

label_distance = Label(master=root, text='Trip Distance: ', font='bold', bd=5,
                       relief='raised')
label_distance.grid(row=0, column=0, sticky='E', padx=10)
entry_distance = Entry(master=root, bd=5, bg='#FAF0E6')
entry_distance.grid(row=0, column=1, pady=20)
entry_distance.focus()

label_km = Label(master=root, text='km', font='bold', bd=5, relief='raised')
label_km.grid(row=0, column=2, padx=10, sticky='W')

label_fuel_consumption = Label(master=root, text='Fuel consumption: ', font='bold',
                               bd=5, relief='raised')
label_fuel_consumption.grid(row=1, column=0, sticky='E', padx=10)
entry_fuel_consumption = Entry(master=root, bd=5, bg='#FAF0E6')
entry_fuel_consumption.grid(row=1, column=1)

label_liters_per_km = Label(master=root, text='l/km', font='bold', bd=5,
                            relief='raised')
label_liters_per_km.grid(row=1, column=2, padx=10, sticky='W')

label_price = Label(master=root, text='Fuel Price: ', font='bold', bd=5,
                    relief='raised')
label_price.grid(row=2, column=0, sticky='E', padx=10)
entry_price = Entry(master=root, bd=5, bg='#FAF0E6')
entry_price.grid(row=2, column=1, pady=20, sticky='W')

label_pln = Label(master=root, text='PLN', font='bold', bd=5, relief='raised')
label_pln.grid(row=2, column=2, padx=10)

button = Button(master=root, text='Calculate!', command=calculator, font='bold',
                bd=10, relief='raised')
button.grid(row=3, column=1)

root.title('Fuel Cost Calculator')
root.configure(bg='#D3D3D3')

root.resizable(width=False, height=False)
width = 440
height = 250
x_coordinate = int(root.winfo_screenwidth() / 2 - width / 2)
y_coordinate = int(root.winfo_screenheight() / 2 - height / 2)
root.geometry(f'{width}x{height}+{x_coordinate}+{y_coordinate}')

root.mainloop()
