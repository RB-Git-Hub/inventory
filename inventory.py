# Import Libraries

from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk

# Tkinter root
root = Tk()
root.title("main")
root.attributes("-fullscreen",True)
download=False
entry_country = StringVar()
entry_code = StringVar()
entry_product = StringVar()
entry_cost = StringVar()
entry_quantity = StringVar()
search_code = StringVar()


class Shoe:
    '''
    The Shoe class formulates the product data.

    get_cost = Returns total value of product
    get_quantity = Returns highest and lowest quantities of product list

    '''
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self,line):
        value= int(line.cost)*int(line.quantity)
        return value
        
    def get_quantity(self,m):
        max_quantity=0
        min_quantity=10000000000000000
        for line in shoe_list:
            if m=="max":
                if int(line.quantity) > max_quantity: 
                    max_quantity=int(line.quantity)
            elif m=="min":
                if int(line.quantity) < min_quantity: 
                    min_quantity=int(line.quantity)
        return min_quantity, max_quantity 

    # Display format
    def __str__(self):
        return f"Code   \t: {self.code}\nProduct\t: {self.product}\nCountry\
 \t: {self.country}\nCost   \t: {self.cost}\nQuantity\t: {self.quantity}"

# List declaring
shoe_list = []

# Imports and checks data from inventory.txt
def read_shoes_data():
    global download
    b1["bg"] = "white"
    if download is True:
        frame1 = Frame(root,width=1000,height=600).place(x = 420,
y = 130)  
        Label(frame1, text=" Data already downloaded!\n\
Do you want to continue?",font=("Ariel", 15 )).place(x = 470, y = 190)
        Button(frame1, text="Continue", width=10, command=download_false)\
.place(x = 630, y = 250)
    else:    
        with open("inventory.txt", "r") as shoe:
            line_skip=0
            for line in (shoe):
                if line_skip== 0:
                    line_skip= 1
                else:
                    try: 
                        for i, word in enumerate(line.split(",")):
                            if i == 0:
                                country = word                      
                            elif i == 1:
                                code = word
                            elif i== 2:
                                product = word
                            elif i == 3:
                                cost = int(word)
                            elif i == 4:
                                quantity = int(word)
                        shoe_list.append(Shoe(country,code,product,cost\
,quantity))
                        frame1 = Frame(root,width=1000,height=600).place\
(x = 420, y = 130)  
                        Label(frame1, text="Data downloaded                      \
",font=("Ariel", 14 )).place(x = 470, y = 190) 
                        download = True
                    except:
                        frame1 = Frame(root,width=1000,height=600)\
.place(x = 470,y = 130)  
                        Label(frame1, text="Data not uploaded as corrupted",\
font=("Ariel", 14 )).place(x = 470, y = 190) 

# This enables duplicate download override 
def download_false():
    global download
    download=False
    read_shoes_data()

# Allows user to add a product to the shoe_list
def capture_shoes():
    frame1 = Frame(root,width=1000,height=600).place(x = 470, y = 130)  
    Label(frame1, text="Country",font=("Ariel", 14 )).place(x = 490, y = 190) 
    Entry(frame1, textvariable = entry_country, bd=5).place(x = 600, y = 190) 
    Label(frame1, text="Code",font=("Ariel", 14 )).place(x = 490, y = 240) 
    Entry(frame1,textvariable = entry_code, bd=5).place(x = 600, y = 240) 
    Label(frame1, text="Product",font=("Ariel", 14 )).place(x = 490, y = 280) 
    Entry(frame1, textvariable = entry_product, bd=5).place(x = 600, y = 280) 
    Label(frame1, text="Cost",font=("Ariel", 14 )).place(x = 490, y = 320) 
    Entry(frame1, textvariable = entry_cost, bd=5).place(x = 600, y = 320)
    Label(frame1, text="Quantity",font=("Ariel", 14 )).place(x = 490, y = 360) 
    Entry(frame1, textvariable = entry_quantity, bd=5).place(x = 600, y = 360)  
    Button(frame1, text="Submit", width=10, command= ap).place(x =600, y =400)
 
# Gets data from capture_shoes input form
def get_variables():
    country= entry_country.get()
    code= entry_code.get()
    product= entry_product.get()
    cost= entry_cost.get()
    quantity= entry_quantity.get()
    return country, code, product, cost, quantity

# Checks data is correct format
def data_check(country, code, product):
    code_pass=False
    for line in shoe_list:
        if code == line.code or code=="":
            code_pass=True
            Label(frame_error,text="Product code already used",\
font=("Ariel", 14 )).place(x = 770, y = 240) 
            entry_code.set("")   
    if country=="" or product=="":
        code_pass=True
    return code_pass

# Appends new product    
def ap():
    global shoe_list, frame_error
    country, code, product, cost, quantity=get_variables()
    frame_error= Frame(root,width=1000,height=600).place(x = 770, y = 130)
    code_pass=data_check(country, code, product)
    if code_pass is False:
        try:
            if (cost.isdecimal() or cost.isnumeric()) \
and quantity.isnumeric():
                shoe_list.append(Shoe(country,code,product,cost,quantity))
                frame1=Frame(root,width=1500,height=600)\
.place(x = 470, y = 130)
                Label(frame1,text="Product Added                                "\
,font=("Ariel", 14 )).place(x = 470, y = 190)
                form_reset()
            else:
                Label(frame_error,text="Use a number please",\
font=("Ariel", 14 )).place(x = 770, y = 340)
        except:
            pass

def form_reset():
    entry_country.set("")
    entry_code.set("")
    entry_product.set("")
    entry_cost.set("")
    entry_quantity.set("")
        
# Runs functions to view all list data
def view_all():
    view_prep("a")
    view_display() 

# Sets up table
def view_prep(view):
    global column1, column2, column3, column4, column5
    frame1 = Frame(root,width=400,height=600).place(x = 470, y = 190)
    # Enables joint column scrolling
    def scroll(*args):
        column1.yview(*args)
        column2.yview(*args)
        column3.yview(*args)
        column4.yview(*args)
        column5.yview(*args)
    scroll_bar = Scrollbar(root)
    # If all data selected
    if view == "a":
        Label(text="Code             Product                   Country       \
          Cost           Quantity\n\n", font=("ariel", 16, "bold"))\
.place(x = 470, y = 190)
        column5 = Listbox(frame1, width=10,height=20, bg="white", \
font=("ariel", 14), yscrollcommand = scroll_bar.set )
        column5.place(x = 1092, y = 250)
        scroll_bar.place(x=1205, y= 250, height=465)
    # If total value selected
    elif view == "v":
        Label(text="Code             Product                    Country      \
          Total                                 \n                           \
                          Value\n", font=("ariel", 16, "bold"))\
.place(x = 470, y = 190)    
        Frame(root,width=400,height=1000).place(x = 1105, y = 130)
        scroll_bar.place(x=1092, y= 250, height=465)
    #Rest of columns
    column1 = Listbox(frame1, width=20,height=20, bg="white",\
font=("ariel", 14), yscrollcommand = scroll_bar.set )
    column1.place(x = 470, y = 250)
    column2 = Listbox(frame1, width=20,height=20, bg="white",\
font=("ariel", 14), yscrollcommand = scroll_bar.set )
    column2.place(x = 600, y = 250)
    column3 = Listbox(frame1, width=25,height=20, bg="white",\
font=("ariel", 14), yscrollcommand = scroll_bar.set )
    column3.place(x = 800, y = 250)
    scroll_bar.config( command = scroll)
    column4 = Listbox(frame1, width=10,height=20, bg="white",\
font=("ariel", 14), yscrollcommand = scroll_bar.set )
    column4.place(x = 980, y = 250)

# Displays data for view all data
def view_display():
    for line in shoe_list: 
        column1.insert(END,line.code)  
        column2.insert(END,line.product)
        column3.insert(END,line.country)
        column4.insert(END,line.cost)
        column5.insert(END,line.quantity)

# Displays lowest quantity for restocking, user can add required quantity
def re_stock():
    global old_quantity, entry_code, entry_cost, entry_country, \
entry_product, index
    frame1 = Frame(root,width=1000,height=600).place(x = 420,y = 130)
    min, max =Shoe.get_quantity(Shoe,"min")
    for n,line in enumerate(shoe_list):
        try:
            if int(line.quantity) == min:
                index=n
                Label(frame1, text="This line is low on stock and needs \
re-stocking", font=("Ariel", 19 ), justify= LEFT).place(x = 470, y = 190)
                Label(frame1, text=line, font=("Ariel", 19 ), justify= LEFT)\
.place(x = 470, y = 250)
                Label(frame1, text="How much stock do you want to add?",\
 font=("Ariel", 14 ), justify= LEFT).place(x = 470, y = 440)
                Entry(frame1, textvariable = entry_quantity, bd=5)\
.place(x = 475, y = 475)
                Button(frame1, text="Add Stock", width=10,\
command=re_stock_process)\
.place(x = 610, y = 475)
        except:
            pass

# Used by re_stock
def re_stock_process():
    global shoe_list
    quantity=entry_quantity.get()
    for n,line in enumerate(shoe_list):
        if n==index:
            try:               
                quantity= int(quantity)
                old_quantity = int(line.quantity)
                new_quantity= old_quantity+quantity
                line.quantity=new_quantity
                txt_update()
                frame1=Frame(root,width=1000,height=600)\
.place(x = 470, y = 130)
                Label(frame1,text="Completed                                 \
            ", font=("ariel", 14)).place(x = 470, y = 190)
                entry_quantity.set("")
            except:
                Label(text="Please enter a number",font=("ariel", 14))\
.place(x = 470, y = 520)
                root.mainloop()
        else:
            pass   

# This updates the txt file with updated data            
def txt_update():
    global shoe_list
    new_file="Country,Code,Product,Cost,Quantity"
    for line in shoe_list:
        new_file += (f"\n{line.country},{line.code},{line.product}\
,{line.cost},{line.quantity}")
    with open("inventory.txt", "w") as list:
        list.write(new_file)             

# Input for selection and display of a product by code
def seach_shoe():
    frame1 = Frame(root,width=1000,height=600)\
.place(x = 470, y = 130)
    Label(frame1, text="What product code would you like to search for?",\
 font=("Ariel", 18 ), justify= LEFT).place(x = 470, y = 190)
    Entry(frame1, textvariable = search_code, bd=5).place(x = 475, y = 250)
    Button(frame1, text="Search", width=10, command=show_shoe)\
.place(x = 610, y = 248)    

# This works with search_shoe to display an individual product
def show_shoe():
    search=search_code.get()
    search.upper()
    for line in shoe_list:
        if line.code == search:
            Label(text=line, font=("Ariel", 18 ), justify= LEFT)\
.place(x = 470, y = 300)
            search_code.set("")


# This calls functions to display all products with total value for eacch
def value_per_item():
    view_prep("v")
    view_value()

# Populates table with product lines with total values
def view_value():
    for line in shoe_list: 
        value=Shoe.get_cost(Shoe,line)
        column1.insert(END,line.code)
        column2.insert(END,line.product)
        column3.insert(END,line.country)
        column4.insert(END,value)     


# This displays the product with the highest quantity.   
def highest_qty():
    frame1 = Frame(root,width=1000,height=600).place(x = 470, y = 130)
    min,max=Shoe.get_quantity(Shoe,"max")
    for line in shoe_list:
        try:
            if int(line.quantity) == max:
                Label(frame1, text="This line has the highest stock level\
 and is for sale.", font=("Ariel", 18 ), justify= LEFT)\
.place(x = 470, y = 190)
                Label(frame1, text=line, font=("Ariel", 18 ), justify= LEFT)\
.place(x = 470, y = 250)
        except:
            pass

# Main Menu 
# Hover text for each menu button
def b1_hover(e):
    hover_pop.config(text="Download the data file onto this system")

def hover_leave(e):
    hover_pop.config(text="")

def b2_hover(e):
    hover_pop.config(text="Add a product to the system")

def b3_hover(e):
    hover_pop.config(text="View all products on the system")

def b4_hover(e):
    hover_pop.config(text="Add stock quantity to the lowest\
 quantity product")

def b5_hover(e):
    hover_pop.config(text="Search for a product line using the product code")

def b6_hover(e):
    hover_pop.config(text="View all products with the total value of\
 each product line")

def b7_hover(e):
    hover_pop.config(text="View the product with the highest quantity")

# Menu Buttons
fm = Frame(root)
Label(fm,text = "   NIKE  ", font=("Impact", 100, "italic"))\
.grid(column=0, row=1, sticky="W")
fm.grid()
b1=Button(fm, text="Download Data", height= 1, width=20, fg="black",
bg="green", font=("Impact", 30 ),command=lambda: read_shoes_data() )
b1.grid(column=0, row=5, sticky="W")
b2=Button(fm, text="Add product", height= 1, width=20,fg="black",
bg="white", font=("Impact", 30 ),command=lambda: capture_shoes())
b2.grid(column=0, row=6, sticky="W")
b3=Button(fm, text="View all", height= 1, width=20, fg="black",
bg="white", font=("Impact", 30 ),command=lambda: view_all())
b3.grid(column=0, row=7, sticky="W")
b4=Button(fm, text="Re-stock", height= 1, width=20, fg="black",
bg="white", font=("Impact", 30 ), command=lambda: re_stock())
b4.grid(column=0, row=8, sticky="W")
b5=Button(fm, text="Product search", height= 1, width=20, fg="black",
bg="white", font=("Impact", 30 ), command=lambda: seach_shoe())
b5.grid(column=0, row=9, sticky="W")
b6=Button(fm, text="Product total value", height= 1, width=20, fg="black",
bg="white", font=("Impact", 30 ), command=lambda: value_per_item())
b6.grid(column=0, row=10, sticky="W")
b7=Button(fm, text="Highest quantity", height= 1, width=20, fg="black",
bg="white", font=("Impact", 30 ), command=lambda: highest_qty())
b7.grid(column=0, row=11, sticky="W")
Button(fm, text='Exit', height= 1, width=20, fg="black", bg="white",
font=("Impact", 30 ), command=root.destroy).grid(column=0,\
row=13, sticky="W")
frame1 = Frame(root,width=1000,height=600).place(x = 470, y = 130)
Label(frame1, text="<<< Click to start", font=("Ariel", 18))\
.place(x = 470, y = 190)
hover_pop = Label(frame1, text="", font=("Ariel", 18))
hover_pop.place(x = 470, y = 50)

# Bind for menu button hover text
b1.bind("<Enter>", b1_hover), b1.bind("<Leave>", hover_leave)
b2.bind("<Enter>", b2_hover), b2.bind("<Leave>", hover_leave)
b3.bind("<Enter>", b3_hover), b3.bind("<Leave>", hover_leave)
b4.bind("<Enter>", b4_hover), b4.bind("<Leave>", hover_leave)
b5.bind("<Enter>", b5_hover), b5.bind("<Leave>", hover_leave)
b6.bind("<Enter>", b6_hover), b6.bind("<Leave>", hover_leave)
b7.bind("<Enter>", b7_hover), b7.bind("<Leave>", hover_leave)
root.mainloop()