def calculate_subtotal(unit_price, quantity):
    return unit_price * quantity

def calculate_tax(subtotal, tax_rate):
    return subtotal * (tax_rate / 100)

def calculate_invoice_total(unit_price, quantity, tax_rate):
    subtotal = calculate_subtotal(unit_price, quantity)
    tax = calculate_tax(subtotal, tax_rate)
    return subtotal + tax
