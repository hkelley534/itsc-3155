
def get_invoice(invoice):
    item = []
    price = []
    for x in invoice:
        item[x.index()] = x.split(" ")
        
item_num = input("Number of items: ")
invoice = []
for x in item_num:
    invoice[x] = input("Input item and price: ")