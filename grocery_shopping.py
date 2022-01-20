from tkinter import *
from tkinter.ttk import *
from tkinter.ttk import Treeview, Combobox
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3


class ContainerWidget:

    def __init__(self):

        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()

        self.menubar = Menu(root)
        root.config(menu=self.menubar)

        self.container_Layout()
        self.create_connection()

        self.fileMenu()
        self.editMenu()
        self.storeMenu()
        self.listMenu()
        self.reportMenu()
        self.helpMenu()

    def container_Layout(self):

        # Create the layout containers.
        self.container = tk.Frame(root, background='red')
        self.container.grid(row=0, column=0, sticky=NSEW)
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        self.header_container = tk.Frame(self.container, background='red')
        self.header_container.grid(row=0, column=0, sticky=NSEW)
        self.header_container.rowconfigure(0, weight=1)
        self.header_container.columnconfigure(0, weight=1)

        self.top_container = tk.Frame(self.container, background='light blue')
        self.top_container.grid(row=1, column=0, columnspan=2, sticky=NSEW)
        self.top_container.rowconfigure(1, weight=1)
        self.top_container.columnconfigure(0, weight=1)

        self.topL_container = tk.Frame(self.top_container, background='light blue')
        self.topL_container.grid(row=0, column=0, sticky=W)
        self.topL_container.rowconfigure(0, weight=1)
        self.topL_container.columnconfigure(0, weight=1)

        self.topR_container = tk.Frame(self.top_container, background='light blue')
        self.topR_container.grid(row=0, column=1, sticky=E)
        self.topR_container.rowconfigure(0, weight=1)
        self.topR_container.columnconfigure(0, weight=1)

        self.mid_container = tk.Frame(self.container, background='white')
        self.mid_container.grid(row=2, column=0, sticky=NSEW)
        self.mid_container.rowconfigure(2, weight=1)
        self.mid_container.columnconfigure(0, weight=1)

        self.bottom_container = tk.Frame(self.container, background='red')
        self.bottom_container.grid(row=3, column=0, pady=4, sticky=NSEW)
        self.bottom_container.rowconfigure(3, weight=1)
        self.bottom_container.columnconfigure(0, weight=1)

    def create_connection(self):

        # Create the SQLite3 database tables.
        self.conn = sqlite3.connect('grocery.db')
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Price_list(id INTEGER PRIMARY KEY, Location TEXT, Manufacture TEXT, Product TEXT, Category TEXT, Price INTEGER, Item TEXT NOT NULL UNIQUE, Total INTEGER)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS Shopping_list(id INTEGER PRIMARY KEY, Location TEXT, Manufacture TEXT, Product TEXT, Category TEXT, Price INTEGER, Item TEXT NOT NULL UNIQUE, Total INTEGER)")
        self.conn.commit()
        self.conn.close()

    def fileMenu(self):

        # File menu.
        self.filemenu = Menu(self.menubar, tearoff=0)

        self.filemenu.add_command(label="Close", command=root.quit)

        self.menubar.add_cascade(label="File", menu=self.filemenu)

    def editMenu(self):

        # Edit menu.
        self.editmenu = Menu(self.menubar, tearoff=0)

        self.editmenu.add_command(label="Cut")
        self.editmenu.add_command(label="Copy")
        self.editmenu.add_command(label="Paste")
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Find")

        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

    def storeMenu(self):

        # Store menu.
        self.storemenu = Menu(self.menubar, tearoff=0)

        self.storemenu.add_command(label="Add Item")
        self.storemenu.add_command(label="Edit Item")
        self.storemenu.add_command(label="Delete Item")
        self.storemenu.add_separator()

        self.menubar.add_cascade(label="Store", menu=self.storemenu)

    def listMenu(self):

        self.listmenu = Menu(self.menubar, tearoff=0)

        self.menubar.add_cascade(label="List", menu=self.listmenu)

    def reportMenu(self):

        # Report menu.
        self.reportmenu = Menu(self.menubar, tearoff=0)

        self.menubar.add_cascade(label="Reports", menu=self.reportmenu)

    def helpMenu(self):

        # Help menu
        self.helpmenu = Menu(self.menubar, tearoff=0)

        self.helpmenu.add_command(label="Help Index")
        self.helpmenu.add_command(label="About...")

        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

    def autocapitalize(self, event):

        # Make the first letter the user inputs a capital.
        self.var1.set(self.var1.get().capitalize())
        self.var2.set(self.var2.get().capitalize())
        self.var3.set(self.var3.get().capitalize())
        self.var4.set(self.var4.get().capitalize())

    def price_format(self, dollars):

        # Convert the integer values in to money.
        pattern = re.compile(r'^(\d*\.?\d*)$')
        if pattern.match(dollars) is not None:
            return True
        elif dollars is "":
            return True
        else:
            return False

    def words(self, letter):

        if letter.isdigit():
            return False
        elif letter is '':
            return True
        else:
            return True


class Main(ContainerWidget):

    def __init__(self):
        ContainerWidget.__init__(self)

        self.header_Widget()
        self.top_Widget()
        self.mid_Widget()
        self.bottom_Widget()

    def header_Widget(self):

        # Title
        self.title = Label(self.header_container, text="Groceries", font=('Times 30 bold'), background='red')
        self.title.grid(row=0, column=0)

    def top_Widget(self):

        # Get images for the buttons.
        self.add_icon = PhotoImage(file='icons/add_cart_shopping1.gif').subsample(20, 20)
        self.edit_icon = PhotoImage(file='icons/edit_pen_write.gif').subsample(6, 6)
        self.delete_icon = PhotoImage(file='icons/can_trash.gif').subsample(6, 6)

        # Create the buttons with the images.
        self.add_btn = tk.Button(self.topL_container, font=('Times 12 bold'), highlightbackground='light blue', image=self.add_icon, compound="top", width=30, height=20, command=self.entry_Widget)
        self.edit_btn = tk.Button(self.topL_container, font=('Times 12 bold'), highlightbackground='light blue', image=self.edit_icon, compound="left", width=30, height=20, command=self.edit_Widget)
        self.delete_btn = tk.Button(self.topL_container, font=('Times 12 bold'), highlightbackground='light blue', image=self.delete_icon, compound="left", width=30, height=20, command=self.delete_item)

        self.add_btn.grid(row=0, column=0)
        self.edit_btn.grid(row=0, column=1)
        self.delete_btn.grid(row=0, column=2)

        self.shop_list_btn = tk.Button(self.topR_container, highlightbackground='light blue', text="Grocery List", font=('Times 12'), command=Shopping_Widget)
        self.shop_list_btn.grid(row=0, column=0)

    def mid_Widget(self):

        # Create the treeview.
        self.tree = Treeview(self.mid_container)

        self.tree["columns"] = ('one', 'two', 'three', 'four', 'five', 'six')
        self.tree.column('#0', width=30)
        self.tree.column('one', width=0, anchor=W)
        self.tree.column("two", width=100, anchor=CENTER)
        self.tree.column("three", width=100, anchor=CENTER)
        self.tree.column("four", width=100, anchor=CENTER)
        self.tree.column("five", width=100, anchor=CENTER)
        self.tree.column("six", width=70, anchor=E)
        self.tree.heading("#0", text='ID')
        self.tree.heading('one', text='SQL ID')
        self.tree.heading("two", text='Store')
        self.tree.heading("three", text='Manufacture')
        self.tree.heading("four", text='Product Name')
        self.tree.heading("five", text='Category')
        self.tree.heading("six", text='Price')
        self.tree["displaycolumns"] = ("two", "three", "four", "five", "six")

        self.ysb = ttk.Scrollbar(self.mid_container, orient='vertical', command=self.tree.yview)
        self.xsb = ttk.Scrollbar(self.mid_container, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)

        self.tree.grid(row=0, column=0, padx=2, sticky=NSEW)
        self.ysb.grid(row=0, column=1, sticky="ns")
        self.xsb.grid(row=1, column=0, sticky="ew")

        # Add style.
        self.style = Style()

        # Pick a theme.
        self.style.theme_use('default')

        # Configure our treeview colors.
        self.style.configure('Treeview', background='white', foreground='black', rowheight=25, fieldbackground='white')

        # Configure our combobox colors.
        self.style.configure('TCombobox', background='white', foreground='black', rowheight=25, fieldbackground='white')

        # Style the combobox.
        self.style.map('TCombobox', fieldbackground=[('readonly', 'white')])

        # Change selected color.
        self.style.map('treeview', background=[('selected', 'blue')])

        # # Create striped row tags.
        self.tree.tag_configure('oddrow', background='white')
        self.tree.tag_configure('evenrow', background='lightblue')

        # Load the items when the application starts.
        self.View()

    def bottom_Widget(self):

        # Create the button to go to the next frame.
        self.list_icon = PhotoImage(file='icons/cart_insert_shopping.gif').subsample(10, 10)
        self.list_button = tk.Button(self.bottom_container, highlightbackground='red', text="Add To List", font=('arial', 12, ''), image=self.list_icon, compound="left", width=60, height=15, command=self.add_list)
        self.list_button.grid(row=1, column=0, sticky=E, padx=10)

    def View(self):

        # Load the database table and show it in the treeview.
        self.conn = sqlite3.connect('grocery.db')
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT ID, Location, Manufacture, Product, Category, Price FROM Price_list")

        # Remove all the data from the treeview so not to add at the bottom.
        self.removeall = self.tree.get_children()
        if self.removeall != '()':
            for child in self.removeall:
                self.tree.delete(child)

        # Insert data in to the treeview.
        self.rows = self.cur.fetchall()
        for row in self.rows:
            self.item_count = len(self.tree.get_children()) + 1
            if self.item_count % 2 == 0:
                self.tree.insert('', 'end', text=self.item_count, values=row, tags=('evenrow',))
            else:
                self.tree.insert('', 'end', text=self.item_count, values=row, tags=('oddrow',))
        self.conn.commit()
        self.conn.close()

    def entry_Widget(self):

        # Create the widget to insert the data.
        self.item_frame = Toplevel()

        # Create entry the frame.
        self.entry_x = root.winfo_x()
        self.entry_y = root.winfo_y()

        self.item_frame.geometry("%dx%d+%d+%d" % (300, 200, self.entry_x, self.entry_y))

        self.button_frame = Frame(self.item_frame)
        self.button_frame.grid(row=5, column=1, columnspan=2, pady=5, padx=2, sticky=E)

        # Add labels, entry widgets and buttons.
        self.store_labels = tk.Label(self.item_frame, text="Store")
        self.store_labels.grid(row=0, column=0, sticky=W)

        self.stores_entry = ttk.Combobox(self.item_frame, state='readonly', width=14, values=('', 'Massy Stores', 'Cost-U-Less', 'Pricesmart', 'Popular Discount', 'Cherish', 'iMart', 'Fresh Market', 'Other'))
        self.stores_entry.grid(row=0, column=1)

        self.brand_label = tk.Label(self.item_frame, text="Manufacture")
        self.brand_label.grid(row=1, column=0, sticky=W)

        self.brand_entry = tk.Entry(self.item_frame, width=15, textvariable=self.var1)
        self.brand_entry.grid(row=1, column=1)
        self.brand_entry_word = root.register(self.words)
        self.brand_entry.config(validate='key', validatecommand=(self.brand_entry_word,'%P'))
        self.brand_entry.bind("<KeyRelease>", self.autocapitalize)

        self.product_label = tk.Label(self.item_frame, text="Product Name")
        self.product_label.grid(row=2, column=0, sticky=W)

        self.product_entry = tk.Entry(self.item_frame, width=15, textvariable=self.var2)
        self.product_entry.grid(row=2, column=1)
        self.product_entry.bind("<KeyRelease>", self.autocapitalize)

        self.category_label = tk.Label(self.item_frame, text="Category")
        self.category_label.grid(row=3, column=0, sticky=W)

        self.category_entry = Combobox(self.item_frame, state='readonly', width=14, values=('', 'Beverages', 'Bakery', 'Jarred Goods', 'Dairy', 'Baking Goods', 'Frozen Foods', 'Meat', 'Produce', 'Cleaners', 'Paper Goods', 'Personal Care', 'Other'))
        self.category_entry.grid(row=3, column=1)

        self.price_label = tk.Label(self.item_frame, text="Price")
        self.price_label.grid(row=4, column=0, sticky=W)

        self.price_entry = tk.Entry(self.item_frame, width=15)
        self.price_entry.grid(row=4, column=1)
        self.price_entry_num = root.register(self.price_format)
        self.price_entry.config(validate='key', validatecommand=(self.price_entry_num, '%P'))

        self.add_btn = tk.Button(self.button_frame, text="Save", command=self.add_item)
        self.add_btn.grid(row=0, column=0)

        self.close_btn = tk.Button(self.button_frame, text="Close", command=self.close_toplevel)
        self.close_btn.grid(row=0, column=1)

    def add_item(self):

        # Retrieve the data and save to the database table.
        self.stores_g = self.stores_entry.get()
        self.brand_g = self.brand_entry.get()
        self.product_g = self.product_entry.get()
        self.category_g = self.category_entry.get()
        self.item_g = self.stores_g + ' ' + self.product_g
        self.price_g = self.price_entry.get()

        if self.stores_entry.get() == '':
            messagebox.showwarning('Error', 'Please fill in all the fields!')

        elif self.brand_entry.get() == '':
            messagebox.showwarning('Error', 'Please fill in all the fields!')

        elif self.product_entry.get() == '':
            messagebox.showwarning('Error', 'Please fill in all the fields!')

        elif self.category_entry.get() == '':
            messagebox.showwarning('Error', 'Please fill in all the fields!')

        elif self.price_entry.get() == '':
            messagebox.showwarning('Error', 'Please fill in all the fields!')

        else:
            self.amount = float(self.price_entry.get())
            self.money = '$ {:,.2f}'.format(self.amount)

            self.tree.insert('', 'end', values=(self.stores_g, self.brand_g, self.product_g, self.category_g, self.money))

            self.conn = sqlite3.connect('grocery.db')
            self.cur = self.conn.cursor()
            self.cur.execute('INSERT OR IGNORE INTO Price_list(Location, Manufacture, Product, Category, Price, Item, Total) VALUES(?,?,?,?,?,?,?)', (self.stores_g, self.brand_g, self.product_g, self.category_g, self.money, self.item_g, self.price_g))
            self.conn.commit()
            self.conn.close()

            self.View()

    def close_toplevel(self):

        self.item_frame.destroy()

    def edit_Widget(self):

        # Retrieve selected data from the treeview.
        self.select_item = self.tree.focus()
        self.store_item = self.tree.item(self.select_item, 'values')[1]
        self.brand_item = self.tree.item(self.select_item, 'values')[2]
        self.product_item = self.tree.item(self.select_item, 'values')[3]
        self.category_item = self.tree.item(self.select_item, 'values')[4]
        self.pricing = self.tree.item(self.select_item, 'values')[5]
        self.price_item = self.pricing.strip('$')

        # Create the edit widget.
        self.edit_x = root.winfo_x()
        self.edit_y = root.winfo_y()

        self.edit_frame = Toplevel()

        self.edit_frame.geometry("%dx%d+%d+%d" % (300, 200, self.edit_x, self.edit_y))

        # Add labels, entry widgets and buttons.
        self.button_frame = Frame(self.edit_frame)
        self.button_frame.grid(row=5, column=1, columnspan=2, pady=5, padx=2, sticky=E)

        self.store_labels = tk.Label(self.edit_frame, text="Store")
        self.store_labels.grid(row=0, column=0, sticky=W)

        self.stores_edit = ttk.Combobox(self.edit_frame, state='readonly', width=14, values=('Massy Stores', 'Cost-U-Less', 'Pricesmart', 'Popular Discount', 'Cherish', 'iMart', 'Fresh Market', 'Other'))
        self.stores_edit.set(self.store_item)
        self.stores_edit.grid(row=0, column=1)

        self.brand_label = tk.Label(self.edit_frame, text="Manufacture")
        self.brand_label.grid(row=1, column=0, sticky=W)

        self.brand_edit = tk.Entry(self.edit_frame, width=15, textvariable=self.var3)
        self.brand_edit.grid(row=1, column=1)
        self.brand_edit.insert(0, self.brand_item)
        self.brand_edit_word = root.register(self.words)
        self.brand_edit.config(validate='key', validatecommand=(self.brand_edit_word,'%P'))
        self.brand_edit.bind("<KeyRelease>", self.autocapitalize)

        self.product_label = tk.Label(self.edit_frame, text="Product Name")
        self.product_label.grid(row=2, column=0, sticky=W)

        self.product_edit = tk.Entry(self.edit_frame, width=15, textvariable=self.var4)
        self.product_edit.grid(row=2, column=1)
        self.product_edit.insert(0, self.product_item)
        self.product_edit.bind("<KeyRelease>", self.autocapitalize)

        self.category_label = tk.Label(self.edit_frame, text="Category")
        self.category_label.grid(row=3, column=0, sticky=W)

        self.category_edit = Combobox(self.edit_frame, state='readonly', width=14, values=('Beverages', 'Bakery', 'Jarred Goods', 'Dairy', 'Baking Goods', 'Frozen Foods', 'Meat', 'Produce', 'Cleaners', 'Paper Goods', 'Personal Care', 'Other'))
        self.category_edit.set(self.category_item)
        self.category_edit.grid(row=3, column=1)

        self.price_label = tk.Label(self.edit_frame, text="Price")
        self.price_label.grid(row=4, column=0, sticky=W)

        self.price_edit = tk.Entry(self.edit_frame, width=15)
        self.price_edit.grid(row=4, column=1)
        self.price_edit.insert(0, self.price_item)

        self.edit_btn = tk.Button(self.button_frame, text="Update", command=self.edit_item)
        self.edit_btn.grid(row=0, column=0)

    def edit_item(self):

        # Retrieve the data and update to the database table.
        self.stores_get_edit = self.stores_edit.get()
        self.brand_get_edit = self.brand_edit.get()
        self.product_get_edit = self.product_edit.get()
        self.category_get_edit = self.category_edit.get()
        self.item_get_edit = self.stores_get_edit + ' ' + self.product_get_edit
        self.price_get_edit = self.price_edit.get()

        if self.stores_edit.get() == '':
            messagebox.showwarning('Error', 'Please fill in all the fields!')

        elif self.brand_edit.get() == '':
            messagebox.showwarning('Error', 'Please fill in all the fields!')

        elif self.product_edit.get() == '':
            messagebox.showwarning('Error', 'Please fill in all the fields!')

        elif self.category_edit.get() == '':
            messagebox.showwarning('Error', 'Please fill in all the fields!')

        elif self.price_edit.get() == '':
            messagebox.showwarning('Error', 'Please fill in all the fields!')

        else:
            self.amount = float(self.price_edit.get())
            self.money = '$ {:,.2f}'.format(self.amount)

            self.conn = sqlite3.connect('grocery.db')
            self.cur = self.conn.cursor()
            self.select_item = self.tree.focus()
            self.edit_selected = self.tree.item(self.select_item, 'values')[0]
            self.cur.execute('''UPDATE Price_list SET Location=?, Manufacture=?, Product=?, Category=?, Price=?, Item=?, Total=? WHERE id = ?''', (self.stores_get_edit, self.brand_get_edit, self.product_get_edit, self.category_get_edit, self.money, self.item_get_edit, self.price_get_edit, self.edit_selected))
            self.conn.commit()
            self.conn.close()

            self.edit_frame.destroy()

            self.View()

    def delete_item(self):

        # Delete selected data from treeview and database.
        self.tree_selected = self.tree.selection()[0]

        self.conn = sqlite3.connect('grocery.db')
        self.cur = self.conn.cursor()
        self.cur.fetchall()
        self.select_item = self.tree.focus()
        self.selected_item = self.tree.item(self.select_item, 'values')[0]
        self.query = 'DELETE FROM Price_list WHERE id = ?'
        self.cur.execute(self.query, (self.selected_item,))
        self.conn.commit()
        self.tree.delete(self.tree_selected)
        self.conn.close()

        self.View()

    def add_list(self):

        # Insert selected data in to the second database table.
        self.conn = sqlite3.connect('grocery.db')
        self.cur = self.conn.cursor()
        self.cur.fetchall()
        self.select_item = self.tree.focus()
        self.selected_item = self.tree.item(self.select_item, 'values')[0]
        self.query = 'INSERT INTO Shopping_list SELECT * FROM Price_list WHERE id=?'
        self.cur.execute(self.query, (self.selected_item,))
        self.conn.commit()
        self.conn.close()


class Shopping_Widget(ContainerWidget):

    def __init__(self):
        ContainerWidget.__init__(self)

        self.shop_header()
        self.shop_mid()
        self.shop_top()
        self.shop_Bottom()

    def shop_header(self):

        # Title.
        self.title = Label(self.header_container, text="Shopping List", font=('Times 30 bold'), background='red')
        self.title.grid(row=0, column=0)

    def shop_top(self):

        # Insert menu buttons.
        self.delete_icon = PhotoImage(file='icons/can_trash.gif').subsample(6, 6)
        self.clear_icon = PhotoImage(file='icons/clear.gif').subsample(20, 20)

        self.delete_btn = tk.Button(self.topL_container, highlightbackground='light blue', font=('Times 12 bold'), image=self.delete_icon, compound="left", width=30, height=20, command=self.shop_delete)
        self.delete_btn.grid(row=0, column=0)
        self.clear_btn = tk.Button(self.topL_container, highlightbackground='light blue', font=('Times 12 bold'), image=self.clear_icon, compound="left", width=30, height=20, command=self.shop_deleteall)
        self.clear_btn.grid(row=0, column=1)

        self.shop_list_btn = tk.Button(self.topR_container, highlightbackground='light blue', text="Item List", font=('Times 12'), command=Main)
        self.shop_list_btn.grid(row=0, column=0)

    def shop_mid(self):

        # Create the treeview.
        self.shop_tree = Treeview(self.mid_container)

        self.shop_tree["columns"]=('one','two','three','four','five', 'six')
        self.shop_tree.column('#0', width=30)
        self.shop_tree.column('one', width=120, anchor=W)
        self.shop_tree.column("two", width=100, anchor=CENTER)
        self.shop_tree.column("three", width=100, anchor=CENTER)
        self.shop_tree.column("four", width=100, anchor=CENTER)
        self.shop_tree.column("five", width=100, anchor=CENTER)
        self.shop_tree.column("six", width=70, anchor=E)
        self.shop_tree.heading("#0", text='ID')
        self.shop_tree.heading('one', text='SQL ID')
        self.shop_tree.heading("two", text='Stores')
        self.shop_tree.heading("three", text='Manufacture')
        self.shop_tree.heading("four", text='Product Name')
        self.shop_tree.heading("five", text='Category')
        self.shop_tree.heading("six", text='Price')
        self.shop_tree["displaycolumns"] = ("two", "three", "four", "five", "six")

        self.shop_tree.grid(row=0, column=0, padx=2, sticky=NSEW)

        # Add style
        self.style = Style()
        # Pick a theme
        self.style.theme_use('default')

        # Configure our treeview colors
        self.style.configure('Treeview', background='white', foreground='black',
                             rowheight=25, fieldbackground='white')
        # Change selected color
        self.style.map('treeview', background=[('selected', 'blue')])

        # # Create striped row tags
        self.shop_tree.tag_configure('oddrow', background='white')
        self.shop_tree.tag_configure('evenrow', background='lightblue')

        self.shop_View()

    def shop_Bottom(self):

        # Insert the sum of the prices in to a listbox.
        self.item_total = Listbox(self.bottom_container, width=10, height=1)
        self.item_total.grid(row=0, column=0, sticky=E, pady=10, padx=10)
        self.conn = sqlite3.connect('grocery.db')
        self.cur = self.conn.cursor()
        self.cur.execute('SELECT Sum(Total) FROM Shopping_list')
        self.total = self.cur.fetchone()
        self.item_total.insert(1, self.total)
        self.conn.commit()
        self.conn.close()

    def shop_View(self):

        # Load the database table and show it in the treeview.
        self.conn = sqlite3.connect('grocery.db')
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT ID, Location, Manufacture, Product, Category, Price FROM Shopping_list")

        # Remove all the data from the treeview so not to add at the bottom.
        self.removeall = self.shop_tree.get_children()
        if self.removeall != '()':
            for child in self.removeall:
                self.shop_tree.delete(child)

        # Insert data in to the treeview.
        self.rows = self.cur.fetchall()
        for row in self.rows:
            self.item_count = len(self.shop_tree.get_children()) + 1
            if self.item_count % 2 == 0:
                self.shop_tree.insert('', 'end', text=self.item_count, values=row, tags=('evenrow',))
            else:
                self.shop_tree.insert('', 'end', text=self.item_count, values=row, tags=('oddrow',))
        self.conn.commit()
        self.conn.close()

    def shop_delete(self):

        # Delete selected data from treeview and database.
        self.selected_item1 = self.shop_tree.selection()[0]

        self.conn = sqlite3.connect('grocery.db')
        self.cur = self.conn.cursor()
        self.cur.fetchall()
        self.select_item = self.shop_tree.focus()
        self.selected_item = self.shop_tree.item(self.select_item, 'values')[0]
        self.query = 'DELETE FROM shopping_list WHERE id = ?'
        self.cur.execute(self.query, (self.selected_item,))
        self.conn.commit()
        self.shop_tree.delete(self.selected_item1)
        self.conn.close()

        self.shop_View()
        self.shop_Bottom()

    def shop_deleteall(self):

        # Delete all the data from treeview and database.
        self.conn = sqlite3.connect('grocery.db')
        self.cur = self.conn.cursor()
        self.query = 'DELETE FROM Shopping_list'
        self.cur.execute(self.query)
        self.conn.commit()
        self.conn.close()

        self.shop_View()
        self.shop_Bottom()


if __name__=='__main__':
    root = Tk()
    root.title("Grocery Shopping")
    width_value = root.winfo_screenwidth()
    height_value = root.winfo_screenheight()
    root.geometry('%dx%d+0+0' % (width_value, height_value))
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=0)
    root.columnconfigure(2, weight=0)
    root.columnconfigure(3, weight=0)
    Main()
    root.mainloop()