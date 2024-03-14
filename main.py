import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
"""
# Label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="top")

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
def button_clicked():
    print("I got clicked")
    my_label.config(text=entry.get())
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

#create an entry
entry = tkinter.Entry(width=10)
entry.pack()
"""
#miles label
miles_label = tkinter.Label(text="Miles", font=("Arial", 12 ))
miles_label.config(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=20, pady=20)

miles_label.pack

#is equal to label
equal_label = tkinter.Label(text="I am a Label", font=("Arial", 12))
equal_label.config(text="is equal to")
equal_label.grid(column=0, row=1)
equal_label.config(padx=20, pady=20)

#Km label
km_label = tkinter.Label(text="Km", font=("Arial", 12))
km_label.config(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=20, pady=20)

#entry
input = tkinter.Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

#label
km_label = tkinter.Label(text="0", font=("Arial", 12))

km_label.grid(column=1, row=1)
km_label.config(padx=20, pady=20)


#button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    new_text = float(new_text) * 1.609
    new_text = round(new_text, 2)
    km_label.config(text=new_text)
    
    
button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)







window.mainloop()