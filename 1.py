from tkinter import*
from tkinter import messagebox
root = tk.Tk()

root.title("ML")

root.minsize(180,290)
root.resizable(height='false', width='false')

 

frame = tk.Frame(root)
frame.grid()

v1 = tk.DoubleVar() 
lbl1 = tk.Label(frame, text='1').grid(row=0, column=0, pady=10)
a1 = tk.Entry(frame, width=12, textvariable=v1).grid(row=0,column=1,  sticky='W', padx=10, pady=5)


v2 = tk.IntVar()
lbl2 = tk.Label(frame, text='2').grid(row=4, column=0)
a2 = tk.Entry(frame, width=12, textvariable=v2).grid(row=4,column=1, sticky='W', padx=10, pady=5)

v3 = tk.IntVar()
lbl3 = tk.Label(frame, text='3').grid(row=4, column=0)
a3 = tk.Entry(frame, width=12, textvariable=v3).grid(row=4,column=1, sticky='W', padx=10, pady=5)

v4 = tk.DoubleVar()
lbl4 = tk.Label(frame, text='4').grid(row=5, column=0)
a4 = tk.Entry(frame, width=12, textvariable=v4).grid(row=5,column=1, sticky='W', padx=10, pady=5)

v5 = tk.DoubleVar()
lbl5 = tk.Label(frame, text='5').grid(row=6, column=0)
a5 = tk.Entry(frame, width=12, textvariable=v5).grid(row=6,column=1, sticky='W', padx=10, pady=5)

v6 = tk.IntVar()
lbl6 = tk.Label(frame, text='6').grid(row=7, column=0)
a6 = tk.Entry(frame, width=12, textvariable=v6).grid(row=7,column=1, sticky='W', padx=10, pady=5)

v7 = tk.IntVar()
lbl7 = tk.Label(frame, text='7').grid(row=8, column=0)
a7 = tk.Entry(frame, width=12, textvariable=v7).grid(row=8,column=1, sticky='W', padx=10, pady=5)

v8 = tk.IntVar()
lbl8 = tk.Label(frame, text='8').grid(row=9, column=0)
a8 = tk.Entry(frame, width=12, textvariable=v8).grid(row=9,column=1, sticky='W', padx=10, pady=5)



txt1='credit score = '
def creditinfo():
    messagebox.showinfo("ML predict 1.0", txt1)      


btn1 = tk.Button(text='Рассчитать',command=creditinfo).grid(row=14, column=0, pady=15, padx=20, sticky='W')


root.mainloop()
