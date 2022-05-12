import tkinter as tk
window = tk.Tk("")
window.geometry("300x200")
button = tk.Button(text='switch light off', bg="white", fg="black")
button.pack(pady = 20, padx = 20)


def click():
    
    if button.config('text')[-1] == 'switch light on':
        button.config(text='switch light off')
        window.config(bg="Black")
        print("light is off")
    else:
        button.config(text='switch light on')
        window.config(bg="Yellow")
        print("light is on")
        
# schijf hier tussen je code
button.config(command=click)



# schijf hier tussen je code

window.mainloop()