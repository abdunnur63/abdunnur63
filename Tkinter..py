from tkinter import *

def show_table():
    num = int(entry.get())
    str1='Table of' + str(num) + '\...........\n'
    for i in range(1,11):
        str1 = str1 + " " + str(num) + " x " + str(i) + " = " + str(num*i) + "\n"

    output_label.configure(text = str1, justy=LEFT)

main_window = Tk()
main_window.titel("perfect python tkinter Tutorials : wwww.Easycodebook.com")
message_label = Label(text= 'Enter a number to \ndisplay its Tabel',
font= ( ' verdana ' , 12))
output_lavel = Lavel(font=( ' verdana' , 12))
entry = entry(font=( ' verdana ' , 12), width=6)
calc_buttom = Buttom(text= ' show Multiplaction Tabel ' , font=( ' verdana ' , 12), command=show_tabel)
message_label.grid(row=0, colum=0,padx=10,pady=10)
entry.grid(row=0,colum=1,padx=10,pady=10,ipady=10)
calc_buttom.grid(row=0, colum=2,padx=10,pady=10)
output_lavel.grid(row=1,colum=0, columnspan=3,padx=10,pady=10)
mainloop()