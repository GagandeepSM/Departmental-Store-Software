from tkinter import *

storeWindow = Tk()
storeWindow.withdraw()

aWindow = Toplevel(storeWindow)
def change_window():
    aWindow.destroy()
    storeWindow.iconify()
    storeWindow.deiconify()

Button(aWindow, text="Enter Gagan's Store!!", command=change_window).pack()


storeWindow.title("Apps Cart")


STORE_ITEM_LIST = ["PACMAN,1.99,1234,4.5,games",
                   "waether channel,0,42348,3.5,weather",
                   "icalc,2.99,4739,2.3,utilities"]

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
    storeLabelFrame = LabelFrame(storeWindow)
    storeLabelFrame.pack(side='top')

    storeItemsFrame = Frame(storeLabelFrame)
    storeItemsFrame.pack()
    store = Store()
    storeItems = store.getStoreItems()
    
    COUNTER = 0
    for item in storeItems:
        itemFrame = Frame(storeItemsFrame,  pady="5")
        itemFrame.pack(fill="both", expand="yes")
        BUTTONS[COUNTER] = IntVar()
        nameLabel    = Checkbutton(itemFrame, variable=BUTTONS[COUNTER] ,text=item.name)
        priceLabel   = Label(itemFrame, text="$ %s"%item.price  )
        idLabel      = Label(itemFrame, text=" %s"%item.id_num  )
        ratingLabel  = Label(itemFrame, text=" %s"%item.rating  )
        categoryLabel= Label(itemFrame, text=" %s"%item.category) 

        nameLabel.pack(side="left")
        priceLabel.pack(side="left",fill="both", expand="yes" )
        idLabel.pack(side="left",fill="both", expand="yes" )
        ratingLabel.pack(side="left",fill="both", expand="yes" )
        categoryLabel.pack(side="left",fill="both", expand="yes" )
        COUNTER+=1


def getTotal():
    TOTAL_PRICE = 0.0  
    for idx in range(len(BUTTONS)):
        if BUTTONS[idx].get():
            PRICE = STORE_ITEM_LIST[idx].split(",")[1]
            TOTAL_PRICE += float(PRICE)
    subTotalLabel['text'] = f'Subtotal: {TOTAL_PRICE}'



viewStore()
subTotalLabel = Label(storeWindow, text="Subtotal: 0.0")
subTotalLabel.pack(side='left')

addToCart = Button(storeWindow, text="Add To Cart",command=lambda : getTotal() )
addToCart.pack(pady="6", side='left')
storeWindow.mainloop()
