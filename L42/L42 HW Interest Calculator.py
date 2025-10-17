import tkinter as tk


#Set-up the window
window = tk.Tk()
window.title("Interest Calculator App")
window.geometry("350x75")
window.resizable(width=False, height=False)

def Inamnt():
    Principle = float(ent_length.get())
    Interest = 0.05
    Timeperiod = 10.0
    Result=Principle*Interest*Timeperiod

    LbL_result["text"] = f"{Result} Result"

    
#Create Widgets
frm_entry = tk.Frame(master=window)

ent_length = tk.Entry(master=frm_entry, width=10)

LbL_temp = tk.Label(master=frm_entry, text="Principle")

btn_convert = tk.Button(master=window, text="-->", command=Inamnt)

LbL_result = tk.Label(master=window, text="Result")

# arrange the widgets
frm_entry.grid(row=0, column=0, padx=10)

ent_length.grid(row=0, column=0, sticky="e")
LbL_temp.grid(row=0, column=1, sticky="w")

btn_convert.grid(row=0, column=1, padx=10)
LbL_result.grid(row=0, column=2, padx=10)

window.mainloop()