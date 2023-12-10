## This program is a GUI created to display a hypothetical crochet ordering system. User should be able to view items, add them to their order,
## and generate an ongoing list of said order. Remove button does not always work correctly, but there are many other working buttons.
## AdamsEmilyFinalProject.py // "Emily's Fiberworks"
## Final Edit: 12/09/23
## SDEV140

import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import random
from datetime import date
from datetime import datetime

prices = {
    "Cotton Beanie" : 30,
    "Wool Beanie" : 40,
    "Cotton Scarf" : 25,
    "Wool Scarf" : 50,
    "Cotton Blanket" : 75,
    "Wool Blanket" : 150,
    }

root = Tk()

root.title("Emily's Fiberworks")

# -- Functions -- #
#region Generating the order number
def ORDER_ID():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    order_id = "ORD_"
    random_letters = ""
    random_digits = ""
    for i in range(0,3):
        random_letters += random.choice(letters)
        random_digits += str(random.choice(numbers))

    order_id += random_letters + random_digits
    return order_id
#endregion

#region Add to Order Button
def add():
    #Transaction label gets updated
    current_order = orderTransaction.cget("text")
    added_item = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")]) + "$" + "\n"
    updated_order = current_order + added_item
    orderTransaction.configure(text = updated_order)

    #Order total label updated
    order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
    order_total = order_total.replace("$", "")
    updated_total = int(order_total) + prices[displayLabel.cget("text")]
    orderTotalLabel.configure(text = "TOTAL : " + str(updated_total) + "$")
#end region

#region Remove Button
#Button does not always work - unsure of why.
def remove():
    item_to_remove = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")])
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    if item_to_remove in transaction_list:
        # label update
        transaction_list.remove(item_to_remove)
        updated_order = ""
        for item in transaction_list:
            updated_order += item + "$ "

        orderTransaction.configure(text = updated_order)

            # total update
        order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
        order_total = order_total.replace("$", "")
        updated_total = int(order_total) - prices[displayLabel.cget("text")]
        orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")

#endregion

#region Display Button Functions
def displayCottonBeanie():
    cottonHatOptionFrame.configure(
        relief = "sunken",
        style = "SelectedOption.TFrame"
        )
    woolHatOptionFrame.configure(style = "OptionFrame.TFrame")
    cottonScarfOptionFrame.configure(style = "OptionFrame.TFrame")
    woolScarfOptionFrame.configure(style = "OptionFrame.TFrame")
    cottonBlanketOptionFrame.configure(style = "OptionFrame.TFrame")
    woolBlanketOptionFrame.configure(style = "OptionFrame.TFrame")
    displayLabel.configure(
        image = cottonHatImage,
        text = "Cotton Beanie",
        font = ("Times New Roman", 14, "bold"),
        foreground = "white",
        compound = "bottom",
        padding = (5, 5, 5, 5),
        )

def displayWoolBeanie():
    woolHatOptionFrame.configure(
        relief = "sunken",
        style = "SelectedOption.TFrame"
        )
    cottonScarfOptionFrame.configure(style = "OptionFrame.TFrame")
    woolScarfOptionFrame.configure(style = "OptionFrame.TFrame")
    cottonBlanketOptionFrame.configure(style = "OptionFrame.TFrame")
    woolBlanketOptionFrame.configure(style = "OptionFrame.TFrame")
    cottonHatOptionFrame.configure(style = "OptionFrame.TFrame")
    displayLabel.configure(
        image = woolHatImage,
        text = "Wool Beanie",
        font = ("Times New Roman", 14, "bold"),
        foreground = "white",
        compound = "bottom",
        padding = (5, 5, 5, 5),
        )

def displayCottonScarf():
    cottonScarfOptionFrame.configure(
        relief = "sunken",
        style = "SelectedOption.TFrame"
        )
    cottonHatOptionFrame.configure(style = "OptionFrame.TFrame")
    woolHatOptionFrame.configure(style = "OptionFrame.TFrame")
    woolScarfOptionFrame.configure(style = "OptionFrame.TFrame")
    cottonBlanketOptionFrame.configure(style = "OptionFrame.TFrame")
    woolBlanketOptionFrame.configure(style = "OptionFrame.TFrame")
    displayLabel.configure(
        text = "Cotton Scarf",
        font = ("Times New Roman", 14, "bold"),
        foreground = "white",
        image = cottonScarfImage,
        compound = "bottom",
        padding = (5, 5, 5, 5),
        )

def displayWoolScarf():
    woolScarfOptionFrame.configure(
        relief = "sunken",
        style = "SelectedOption.TFrame"
        )
    cottonHatOptionFrame.configure(style = "OptionFrame.TFrame")
    woolHatOptionFrame.configure(style = "OptionFrame.TFrame")
    cottonScarfOptionFrame.configure(style = "OptionFrame.TFrame")
    cottonBlanketOptionFrame.configure(style = "OptionFrame.TFrame")
    woolBlanketOptionFrame.configure(style = "OptionFrame.TFrame")
    displayLabel.configure(
        text = "Wool Scarf",
        font = ("Times New Roman", 14, "bold"),
        foreground = "white",
        image = woolScarfImage,
        compound = "bottom",
        padding = (5, 5, 5, 5),
        )

def displayCottonBlanket():
    cottonBlanketOptionFrame.configure(
        relief = "sunken",
        style = "SelectedOption.TFrame"
        )
    cottonHatOptionFrame.configure(style = "OptionFrame.TFrame")
    woolHatOptionFrame.configure(style = "OptionFrame.TFrame")
    cottonScarfOptionFrame.configure(style = "OptionFrame.TFrame")
    woolScarfOptionFrame.configure(style = "OptionFrame.TFrame")
    woolBlanketOptionFrame.configure(style = "OptionFrame.TFrame")
    displayLabel.configure(
        text = "Cotton Blanket",
        font = ("Times New Roman", 14, "bold"),
        foreground = "white",
        image = cottonBlanketImage,
        compound = "bottom",
        padding = (5, 5, 5, 5),
        )

def displayWoolBlanket():
    woolBlanketOptionFrame.configure(
        relief = "sunken",
        style = "SelectedOption.TFrame"
        )
    cottonHatOptionFrame.configure(style = "OptionFrame.TFrame")
    woolHatOptionFrame.configure(style = "OptionFrame.TFrame")
    cottonScarfOptionFrame.configure(style = "OptionFrame.TFrame")
    woolScarfOptionFrame.configure(style = "OptionFrame.TFrame")
    cottonBlanketOptionFrame.configure(style = "OptionFrame.TFrame")
    displayLabel.configure(
        text = "Wool Blanket",
        font = ("Times New Roman", 14, "bold"),
        foreground = "white",
        image = woolBlanketImage,
        compound = "bottom",
        padding = (5 ,5 ,5 ,5),
        )

#region Receipt Generation
def order():
    new_receipt = orderIDLabel.cget("text")
    new_receipt = new_receipt.replace("ORDER NUMBER : ","")
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    order_day = date.today()
    order_time = datetime.now()

    for item in transaction_list:
        item += "$ "

    with open(new_receipt, 'w') as file:
        file.write("Emily's Fiberworks")
        file.write("\n")
        file.write("________________________________________________________")
        file.write("\n")
        file.write(order_day.strftime("%x"))
        file.write("\n")
        file.write(order_time.strftime("%X"))
        file.write("\n\n")
        for item in transaction_list:
            file.write(item + "\n")
        file.write("\n\n")
        file.write(orderTotalLabel.cget("text"))

    orderTotalLabel.configure(text = "TOTAL : 0$")
    orderIDLabel.configure(text = "ORDER NUMBER: " + ORDER_ID())
    orderTransaction.configure(text = "")

#endregion
        
# -- Styling and Images -- #
s = ttk.Style()
s.configure('MainFrame.TFrame', background = "gray22")
s.configure('MenuFrame.TFrame', background = "black")
s.configure('DisplayFrame.TFrame', background = "black")
s.configure('OrderFrame.TFrame', background = "dim gray")
s.configure('OptionFrame.TFrame', background = "dim gray", relief = "raised")
s.configure('SelectedOption.TFrame', background = "pale goldenrod")
s.configure('MenuLabel.TLabel',
            background = "black",
            font = ("Times New Roman", 13, "italic"),
            foreground = "white",
            padding = (5, 5, 5, 5),
            width = 21
            )
s.configure('orderTotalLabel.TLabel',
            background = "dim gray",
            font = ("Times New Roman", 10, "bold"),
            foreground = "white",
            padding = (2, 2, 2, 2),
            anchor = "w"
            )
s.configure('orderTransaction.TLabel',
            background = "dim gray",
            font = ("Times New Roman", 12),
            foreground = "white",
            wraplength = 170,
            anchor = "nw",
            padding = (3, 3, 3, 3)
            )

# endregion


# region Images
# Top Banner images
LogoImageObject = Image.open(r"C:\Users\emily\Downloads\Emily’s.png").resize((130, 130))
LogoImage = ImageTk.PhotoImage(LogoImageObject)

TopBannerImageObject = Image.open(r"C:\Users\emily\Downloads\YarnBanner.jpg").resize((800, 130))
TopBannerImage = ImageTk.PhotoImage(TopBannerImageObject)

# Option images
displayDefaultImageObject = Image.open(r"C:\Users\emily\Downloads\DisplayDefault.png").resize((350, 360))
displayDefaultImage = ImageTk.PhotoImage(displayDefaultImageObject)

cottonHatImageObject = Image.open(r"C:\Users\emily\Downloads\Cotton Hat.jpg").resize((350, 334))
cottonHatImage = ImageTk.PhotoImage(cottonHatImageObject)

woolHatImageObject = Image.open(r"C:\Users\emily\Downloads\Wool Hat.jpg").resize((350, 334))
woolHatImage = ImageTk.PhotoImage(woolHatImageObject)

cottonScarfImageObject = Image.open(r"C:\Users\emily\Downloads\Cotton Scarf.jpg").resize((350, 334))
cottonScarfImage = ImageTk.PhotoImage(cottonScarfImageObject)

woolScarfImageObject = Image.open(r"C:\Users\emily\Downloads\Wool Scarf.jpg").resize((350, 334))
woolScarfImage = ImageTk.PhotoImage(woolScarfImageObject)

cottonBlanketImageObject = Image.open(r"C:\Users\emily\Downloads\Cotton Blanket.jpg").resize((350, 334))
cottonBlanketImage = ImageTk.PhotoImage(cottonBlanketImageObject)

woolBlanketImageObject = Image.open(r"C:\Users\emily\Downloads\Wool Blanket.jpg").resize((350, 334))
woolBlanketImage = ImageTk.PhotoImage(woolBlanketImageObject)

#endregion

# -- Widgets -- #
# region Frames
# Section Frames
mainFrame = ttk.Frame(root, width = 800, height = 580, style = 'MainFrame.TFrame')
mainFrame.grid(row = 0, column = 0, sticky = "NSEW")

topBannerFrame = ttk.Frame(mainFrame)
topBannerFrame.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 3)

menuFrame = ttk.Frame(mainFrame, style = "MenuFrame.TFrame")
menuFrame.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = "NSEW")

displayFrame = ttk.Frame(mainFrame, style = "DisplayFrame.TFrame")
displayFrame.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = "NSEW")

orderFrame = ttk.Frame(mainFrame, style = "OrderFrame.TFrame")
orderFrame.grid(row = 1, column = 2, padx = 3, pady = 3, sticky = "NSEW")

# Option Frames
cottonHatOptionFrame = ttk.Frame(menuFrame, style = "OptionFrame.TFrame")
cottonHatOptionFrame.grid(row = 1, column = 0, sticky = "NSEW")

woolHatOptionFrame = ttk.Frame(menuFrame, style = "OptionFrame.TFrame")
woolHatOptionFrame.grid(row = 2, column = 0, sticky = "NSEW")

cottonScarfOptionFrame = ttk.Frame(menuFrame, style = "OptionFrame.TFrame")
cottonScarfOptionFrame.grid(row = 3, column = 0, sticky = "NSEW")

woolScarfOptionFrame = ttk.Frame(menuFrame, style = "OptionFrame.TFrame")
woolScarfOptionFrame.grid(row = 4, column = 0, sticky = "NSEW")

cottonBlanketOptionFrame = ttk.Frame(menuFrame, style = "OptionFrame.TFrame")
cottonBlanketOptionFrame.grid(row = 5, column = 0, sticky = "NSEW")

woolBlanketOptionFrame = ttk.Frame(menuFrame, style = "OptionFrame.TFrame")
woolBlanketOptionFrame.grid(row = 6, column = 0, sticky = "NSEW")

#endregion

# region Top Banner Section

LogoLabel = ttk.Label(topBannerFrame, image = LogoImage, background = "gray22")
LogoLabel.grid(row = 0, column = 0, sticky = "W")

CrochetBannerLabel = ttk.Label(topBannerFrame, image = TopBannerImage, background = "gray22")
CrochetBannerLabel.grid(row = 0, column = 1, sticky = "NSEW")

# endregion

#region Options Section
MainMenuLabel = ttk.Label(menuFrame, text = "100% Handmade, Guaranteed", style = "MenuLabel.TLabel")
MainMenuLabel.grid(row = 0, column = 0, sticky = "WE")
MainMenuLabel.configure(
    anchor = "center",
    font = ("Times New Roman", 14, "bold", "italic")
)

cottonHatOptionLabel = ttk.Label(cottonHatOptionFrame, text = "Cotton Beanie ..... $30", style = "MenuLabel.TLabel")
cottonHatOptionLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

woolHatOptionLabel = ttk.Label(woolHatOptionFrame, text = "Wool Beanie ..... $40", style = "MenuLabel.TLabel")
woolHatOptionLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

cottonScarfOptionLabel = ttk.Label(cottonScarfOptionFrame, text = "Cotton Scarf ..... $25", style = "MenuLabel.TLabel")
cottonScarfOptionLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

woolScarfOptionLabel = ttk.Label(woolScarfOptionFrame, text = "Wool Scarf ..... $50", style = "MenuLabel.TLabel")
woolScarfOptionLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

cottonBlanketOptionLabel = ttk.Label(cottonBlanketOptionFrame, text = "Cotton Blanket ..... $75", style = "MenuLabel.TLabel")
cottonBlanketOptionLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

woolBlanketOptionLabel = ttk.Label(woolBlanketOptionFrame, text = "Wool Blanket ..... $150", style = "MenuLabel.TLabel")
woolBlanketOptionLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

#Buttons
cottonHatDisplayButton = ttk.Button(cottonHatOptionFrame, text = "Display", command = displayCottonBeanie)
cottonHatDisplayButton.grid(row = 0, column = 1, padx = 10)

woolHatDisplayButton = ttk.Button(woolHatOptionFrame, text = "Display", command = displayWoolBeanie)
woolHatDisplayButton.grid(row = 0, column = 1, padx = 10)

cottonScarfDisplayButton = ttk.Button(cottonScarfOptionFrame, text = "Display", command = displayCottonScarf)
cottonScarfDisplayButton.grid(row = 0, column = 1, padx = 10)

woolScarfDisplayButton = ttk.Button(woolScarfOptionFrame, text = "Display", command = displayWoolScarf)
woolScarfDisplayButton.grid(row = 0, column = 1, padx = 10)

cottonBlanketDisplayButton = ttk.Button(cottonBlanketOptionFrame, text = "Display", command = displayCottonBlanket)
cottonBlanketDisplayButton.grid(row = 0, column = 1, padx = 10)

woolBlanketDisplayButton = ttk.Button(woolBlanketOptionFrame, text = "Display", command = displayWoolBlanket)
woolBlanketDisplayButton.grid(row = 0, column = 1, padx = 10)
#endregion

# region Order Section
orderTitleLabel = ttk.Label(orderFrame, text = "ORDER")
orderTitleLabel.configure(
    foreground = "white", background = "black",
    font = ("Times New Roman", 14, "bold"), anchor = "center",
    padding = (5, 5, 5, 5),
    )
orderTitleLabel.grid(row = 0, column = 0, sticky = "EW")

orderIDLabel = ttk.Label(orderFrame, text = "ORDER NUMBER : " + ORDER_ID())
orderIDLabel.configure(
    background = "black",
    foreground = "white",
    font = ("Times New Roman", 11, "italic"),
    anchor = "center",
    )
orderIDLabel.grid(row = 1, column = 0, sticky = "EW", pady = 1)

orderTransaction = ttk.Label(orderFrame, style = 'orderTransaction.TLabel')
orderTransaction.grid(row = 2, column = 0, sticky = "NSEW")

orderTotalLabel = ttk.Label(orderFrame, text = "TOTAL : 0$", style = "orderTotalLabel.TLabel")
orderTotalLabel.grid(row = 3, column = 0, sticky = "EW")

orderButton = ttk.Button(orderFrame, text = "ORDER", command = order)
orderButton.grid(row = 4, column = 0, sticky = "EW")

# endregion

# region Display Section
displayLabel = ttk.Label(displayFrame, image = displayDefaultImage)
displayLabel.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 2)
displayLabel.configure(background = "dim gray")

addOrderButton = ttk.Button(displayFrame, text = "ADD TO ORDER", command = add)
addOrderButton.grid(row = 1, column = 0, padx = 2, sticky = "NSEW")

removeOrderButton = ttk.Button(displayFrame, text = "REMOVE", command = remove) # button that does not always work
removeOrderButton.grid(row = 1, column = 1, padx = 2, sticky = "NSEW")

# -- Grid Configurations -- #
mainFrame.columnconfigure(2, weight = 1)
mainFrame.rowconfigure(1, weight = 1)
menuFrame.columnconfigure(0, weight = 1)
menuFrame.rowconfigure(1, weight = 1)
menuFrame.rowconfigure(2, weight = 1)
menuFrame.rowconfigure(3, weight = 1)
menuFrame.rowconfigure(4, weight = 1)
menuFrame.rowconfigure(5, weight = 1)
menuFrame.rowconfigure(6, weight = 1)
orderFrame.columnconfigure(0, weight = 1)
orderFrame.rowconfigure(2, weight = 1)



root.mainloop()
