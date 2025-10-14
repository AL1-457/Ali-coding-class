import tkinter as tk


#Set-up the window
window = tk.Tk()
window.title("Interest Calculator")
window.geometry("250x75")
window.resizable(width=False, height=False)

def interestCalculator():
    interest = float(ent_interest.get())
    time_period = 90
    principal = interest * 0.05

    LbL_result["text"] = f"{principal} principal"

    
#Create Widgets
frm_entry = tk.Frame(master=window)

ent_interest = tk.Entry(master=frm_entry, width=10)

LbL_temp = tk.Label(master=frm_entry, text="interest")

btn_principal = tk.Button(master=window, text="-->", command=interestCalculator)

LbL_result = tk.Label(master=window, text="principal")

# arrange the widgets
frm_entry.grid(row=0, column=0, padx=10)

ent_interest.grid(row=0, column=0, sticky="e")
LbL_temp.grid(row=0, column=1, sticky="w")

btn_principal.grid(row=0, column=1, padx=10)
LbL_result.grid(row=0, column=2, padx=10)

window.mainloop()