from tkinter import *

storeWindow = Tk()
storeWindow.title("Gagan's Store")


STORE_ITEM_LIST = ["PACMAN,30,4212,7,GAME",
                   "NOMORE,35,4213,8,VIDEO",
                   "DREAMS,40,4214,9,SONG"]

class Item:
    def __init__(self, name, price, id_num, rating, category): 
        self.name = name
        self.price = price
        self.id_num = id_num
        self.rating = rating
        self.category = category

class Store:
    def __init__(self):
        self.storeItems = []
        self.readStoreItems()
    def readStoreItems(self):
        self.generateRandomStoreItems(4)
    def getStoreItems(self):
        return self.storeItems
    def generateRandomStoreItems(self, amt):
        for VALUE in STORE_ITEM_LIST:
            TEMP = VALUE.split(',')
            itemName = TEMP[0]
            itemPrice = TEMP[1]
            itemId = TEMP[2]
            itemRating = TEMP[3]
            itemCategory = TEMP[4]
            newItem = Item( name=itemName, price=itemPrice, id_num=itemId, rating=itemRating, category=itemCategory)
            self.storeItems.append(newItem)

BUTTONS = ["CHKBTN"+str(idx) for idx in range(1,len(STORE_ITEM_LIST)+1)]

def viewStore():
    global storeWindow 
    storeLabelFrame = LabelFrame(storeWindow, text="Store Items")
    storeLabelFrame.pack(fill="both", expand="yes", padx="20", pady="10")

    storeItemsFrame = Frame(storeLabelFrame)
    storeItemsFrame.pack(padx="10", pady="5")
    store = Store()
    storeItems = store.getStoreItems()
    
    COUNTER = 0
    for item in storeItems:
        itemFrame = Frame(storeItemsFrame,  pady="5")
        itemFrame.pack(fill="both", expand="yes")
        BUTTONS[COUNTER] = IntVar()
        nameLabel    = Checkbutton(itemFrame, variable=BUTTONS[COUNTER] ,text=item.name,font=("Candara",15),fg="black")
        priceLabel   = Label(itemFrame, text="$ %s"%item.price , font=("Candara",13),fg="green")
        idLabel      = Label(itemFrame, text=" %s"%item.id_num , font=("Candara",13),fg="black")
        ratingLabel  = Label(itemFrame, text=" %s"%item.rating , font=("Candara",13),fg="blue")
        categoryLabel= Label(itemFrame, text=" %s"%item.category , font=("Candara",13),fg="red") 

        nameLabel.pack(side="left")
        priceLabel.pack(side="left",fill="both", expand="yes" )
        idLabel.pack(side="left",fill="both", expand="yes" )
        ratingLabel.pack(side="left",fill="both", expand="yes" )
        categoryLabel.pack(side="left",fill="both", expand="yes" )
        COUNTER+=1

    addToCart = Button(storeWindow, text="Add To Cart", font=("Candara",15,"bold"),fg="red",bg="white",cursor="hand2",command=lambda : getTotal() )
    addToCart.pack(pady="6")

def getTotal():
    TOTAL_PRICE = 0.0  
    for idx in range(len(BUTTONS)):
        if BUTTONS[idx].get():
            PRICE = STORE_ITEM_LIST[idx].split(",")[1]
            TOTAL_PRICE += float(PRICE)
    subTotalLabel['text'] = f'Subtotal: {TOTAL_PRICE}'

subTotalLabel = Label(storeWindow, text="Subtotal: 0.0", font=("Candara",15,"bold"),fg="BLACK")
subTotalLabel.pack()

viewStore()
storeWindow.mainloop()
