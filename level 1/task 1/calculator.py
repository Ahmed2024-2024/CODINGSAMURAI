import customtkinter as ctk

def press(num):
    global expression
    expression += str(num)
    input_var.set(expression)

def clear():
    global expression
    expression = ""
    input_var.set("")

def calculate():
    global expression
    try:
        result = str(eval(expression))
        input_var.set(result)
        expression = result
    except:
        input_var.set("Syntax Error")
        expression = ""

expression = ""

root = ctk.CTk()
root.geometry("450x600") 
root.title("Calculator")

input_var = ctk.StringVar()
entry = ctk.CTkEntry(root, textvariable=input_var, font=('normal', 24),
                     corner_radius=15, justify='right', width=410, height=60)
entry.grid(row=0, column=0, columnspan=4, pady=15, padx=15)

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

for (text, row, col) in buttons:
    action = calculate if text == '=' else lambda my_text=text: press(my_text)
    ctk.CTkButton(root, text=text, width=90, height=70, font=('Arial', 20, 'normal'),
                  corner_radius=15, command=action).grid(row=row, column=col, padx=8, pady=8)

ctk.CTkButton(root, text='C', width=410, height=70, font=('Arial', 20, 'normal'),
              corner_radius=15, command=clear).grid(row=5, column=0, columnspan=4, padx=15, pady=15)

root.mainloop()
