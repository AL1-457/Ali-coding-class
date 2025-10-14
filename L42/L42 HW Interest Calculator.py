import tkinter as tk


#Set-up the window
window = tk.Tk()
window.title("Length Converter")
window.geometry("250x75")
window.resizable(width=False, height=False)

def inch_to_cm():
    interest = float(ent_length.get())
    principal = interest * 2.54

    LbL_result["text"] = f"{principal} principal"

    
#Create Widgets
frm_entry = tk.Frame(master=window)

ent_length = tk.Entry(master=frm_entry, width=10)

LbL_temp = tk.Label(master=frm_entry, text="inch")

btn_convert = tk.Button(master=window, text="-->", command=inch_to_cm)

LbL_result = tk.Label(master=window, text="cm")

# arrange the widgets
frm_entry.grid(row=0, column=0, padx=10)

ent_length.grid(row=0, column=0, sticky="e")
LbL_temp.grid(row=0, column=1, sticky="w")

btn_convert.grid(row=0, column=1, padx=10)
LbL_result.grid(row=0, column=2, padx=10)

window.mainloop()