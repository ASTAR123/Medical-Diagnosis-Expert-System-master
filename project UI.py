# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


from tkinter import *
from tkinter.tix import Tk, Control, ComboBox
from tkinter.messagebox import showinfo, showwarning, showerror
from PIL import Image, ImageTk

root = Tk()

root.title("Medical Expert System")
root.geometry("800x1000")
root.resizable(width=True, height=True)
root.tk.eval('package require Tix')


# activebackground, activeforeground, anchor,
# background, bitmap, borderwidth, cursor,
# disabledforeground, font, foreground,
# highlightbackground, highlightcolor,
# highlightthickness, image, justify,
# padx, pady, relief, takefocus, text,
# textvariable, underline, wraplength
# height, state, width

#lable = Label(root, text="label", bg="pink",bd=10, font=("Time New Roman",28), width=8, height=3)

lable = Label(root, text="Medical Expert System", fg = "navy", bg="pink", font=("Cooper Black",18), width=50, height=2)
lable.pack(side=TOP)

# cb1=ComboBox(root,label='please inout your initial location:',editable=True, bg = "pink")
# for place1 in ('Ly 3','D5','D6','Ly 5'):
#     cb1.insert(END,place1)
# cb1.pack()
#
# cb2=ComboBox(root,label='please inout your target location:',editable=True, bg = "pink")
# for place2 in ('Ly 3','D5','D6','Ly 5'):
#     cb2.insert(END,place2)
# cb2.pack()

def processing_Button():
    print('your recommended way is: ')


button=Button(root,text='Process',command=processing_Button, bg = "pink", height= 2, width= 25)

button.pack()

"""回调多个函数：all_command = lamba: [func1(), func2()]          command = all_command"""
# def mini_interface():
#     showinfo("mini_interface","The ways are: \n The recommended way is: ")
# button=Button(root,text="(Result in a mini interface)",command=mini_interface, bg = "pink").pack()

# Booleans
NO = FALSE = OFF = 0
YES = TRUE = ON = 1

# -anchor and -sticky
N = 'n'
S = 's'
W = 'w'
E = 'e'
NW = 'nw'
SW = 'sw'
NE = 'ne'
SE = 'se'
NS = 'ns'
EW = 'ew'
NSEW = 'nsew'
CENTER = 'center'

# -fill
NONE = 'none'
X = 'x'
Y = 'y'
BOTH = 'both'

# -side
LEFT = 'left'
TOP = 'top'
RIGHT = 'right'
BOTTOM = 'bottom'

# -relief
RAISED = 'raised'
SUNKEN = 'sunken'
FLAT = 'flat'
RIDGE = 'ridge'
GROOVE = 'groove'
SOLID = 'solid'

# -orient
HORIZONTAL = 'horizontal'
VERTICAL = 'vertical'

# -tabs
NUMERIC = 'numeric'

# -wrap
CHAR = 'char'
WORD = 'word'

# -align
BASELINE = 'baseline'

# -bordermode
INSIDE = 'inside'
OUTSIDE = 'outside'

# Special tags, marks and insert positions
SEL = 'sel'
SEL_FIRST = 'sel.first'
SEL_LAST = 'sel.last'
END = 'end'
INSERT = 'insert'
CURRENT = 'current'
ANCHOR = 'anchor'
ALL = 'all'  # e.g. Canvas.delete(ALL)

# Text widget and button states
NORMAL = 'normal'
DISABLED = 'disabled'
ACTIVE = 'active'
# Canvas state
HIDDEN = 'hidden'

# Menu item types
CASCADE = 'cascade'
CHECKBUTTON = 'checkbutton'
COMMAND = 'command'
RADIOBUTTON = 'radiobutton'
SEPARATOR = 'separator'

# Selection modes for list boxes
SINGLE = 'single'
BROWSE = 'browse'
MULTIPLE = 'multiple'
EXTENDED = 'extended'

# Activestyle for list boxes
# NONE='none' is also valid
DOTBOX = 'dotbox'
UNDERLINE = 'underline'

# Various canvas styles
PIESLICE = 'pieslice'
CHORD = 'chord'
ARC = 'arc'
FIRST = 'first'
LAST = 'last'
BUTT = 'butt'
PROJECTING = 'projecting'
ROUND = 'round'
BEVEL = 'bevel'
MITER = 'miter'

# Arguments to xview/yview
MOVETO = 'moveto'
SCROLL = 'scroll'
UNITS = 'units'
PAGES = 'pages'


root.geometry("600x600+400+400")

text_blank = Text(root)
text_blank.pack()

text_blank.insert(END,
                  "Introduction\nThis project is used to diagnose the user's condition")

text_blank.insert(END,
                  "The software will show whether the user is healthy or not")

text_blank.insert(END,
                  "It will give the symptom and solution for the corresponding medical disease.")


quit = Button(root, text="See you", command=root.quit, bg ="red", activeforeground="white", activebackground="red",
              width = 8, height = 1)

quit.pack()

root.mainloop()





















