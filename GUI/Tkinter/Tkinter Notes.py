from tkinter import *

window_name = Tk()   # Assigns window name. Make sure 'T' is capital.

window_name.title('Put title here')

lbl_name = Label(window_name, text='Hello')   # Assigns label name. Make sure 'Label' is capitalized.
lbl_name.grid(column=0, row=0)

window_name.mainloop()