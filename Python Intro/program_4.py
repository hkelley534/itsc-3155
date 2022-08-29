
def sort_invoice(invoice):
    sorted_invoice = []
    for x in range(len(invoice)):
        sorted_invoice.append(invoice[x].split(" ")[1])
        

item_num = int(input("Number of items: "))
invoice = []
for x in range(item_num):
    invoice.append(input("Input item and price: "))

sort_invoice(invoice)