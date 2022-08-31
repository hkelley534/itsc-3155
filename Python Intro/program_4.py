def make_invoice():
    item_num = int(input("Number of items: "))
    invoice = []
    for x in range(item_num):
        invoice.append(input("Input item and price: "))
    return invoice

def price(x):
    item = x.split(" ") 
    return item[1]    

invoice = make_invoice()
invoice.sort(key=price)
print(invoice)