from tkinter import *

root=Tk()
root.title('Note Pad')
root.geometry('600x400')

my_menu=Menu(root)
root.configure(menu=my_menu)

def our_command():
    pass

file_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label='File',menu=file_menu)

file_menu.add_command(label='new',command=our_command)
file_menu.add_separator()
file_menu.add_command(label='save',command=our_command)
file_menu.add_command(label='save as',command=our_command)
file_menu.add_command(label='print',command=our_command)
file_menu.add_separator()
file_menu.add_command(label='exit',command=our_command)

edit_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label='Edit',menu=edit_menu)

edit_menu.add_command(label='Undo',command=our_command)
edit_menu.add_separator()
edit_menu.add_command(label='Cut',command=our_command)
edit_menu.add_command(label='paste',command=our_command)
edit_menu.add_command(label='copy',command=our_command)
edit_menu.add_command(label='Delete',command=our_command)
edit_menu.add_separator()
edit_menu.add_command(label='Goto',command=our_command)
edit_menu.add_separator()
edit_menu.add_command(label='Select all',command=our_command)
edit_menu.add_command(label='Time/Date',command=our_command)
edit_menu.add_separator()
edit_menu.add_command(label='Font',command=our_command)

edit_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label='View',menu=edit_menu)

edit_menu.add_command(label='Zoom',command=our_command)
edit_menu.add_command(label='Status bar',command=our_command)
edit_menu.add_command(label='Word wrap',command=our_command)

root.mainloop()
