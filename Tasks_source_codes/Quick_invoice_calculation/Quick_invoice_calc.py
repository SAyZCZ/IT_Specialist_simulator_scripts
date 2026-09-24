# Read unit_price, quantity and tax_rate from the console.
# Calculate net_total, tax_amount and gross_total.
# Print all results.

unit_price = float(input())
quantity = int(input())
tax_rate = float(input())

net_total = round(unit_price * quantity, 2)
tax_amount = round(( net_total * tax_rate ) / 100 , 2 )
gross_total = round(net_total+tax_amount,2)

print(net_total,tax_amount,gross_total)
