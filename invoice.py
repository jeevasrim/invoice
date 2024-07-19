def generate_invoice(invoice_number, date, customer, items):
    # Create invoice header
    invoice = f"""
================================
            INVOICE            
================================
Invoice Number: {invoice_number}
Date: {date}
Customer: {customer}
================================

Item                Qty   Unit Price   Total
--------------------------------------------
"""

    total_amount = 0
    for item in items:
        total_price = item['quantity'] * item['unit_price']
        total_amount += total_price
        invoice += f"{item['name']:<20} {item['quantity']:<5} ${item['unit_price']:<11.2f} ${total_price:<10.2f}\n"

    # Add total amount
    invoice += "--------------------------------------------\n"
    invoice += f"{'Total Amount:':>37} ${total_amount:.2f}\n"
    invoice += "============================================\n"

    return invoice

def get_invoice_details():
    invoice_number = input("Enter invoice number: ")
    date = input("Enter date (YYYY-MM-DD): ")
    customer = input("Enter customer name: ")

    items = []
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        item_quantity = int(input(f"Enter quantity for {item_name}: "))
        item_unit_price = float(input(f"Enter unit price for {item_name}: "))
        items.append({'name': item_name, 'quantity': item_quantity, 'unit_price': item_unit_price})

    return invoice_number, date, customer, items

# Get invoice details from the user
invoice_number, date, customer, items = get_invoice_details()

# Generate the invoice
invoice = generate_invoice(invoice_number, date, customer, items)

# Print invoice to console
print(invoice)

# Save invoice to a file
with open('invoice.txt', 'w') as file:
    file.write(invoice)
