INVOICE CALCULATOR
==================

The program must calculate invoice totals from the net price of one service, the quantity and the tax rate.

1. Read the net unit price with input(), convert it to a number and store it in unit_price.
2. Read the quantity, convert it to a number and store it in quantity.
3. Read the tax percentage, convert it to a number and store it in tax_rate. The user enters 23 for 23%, not 0.23.
4. Calculate net_total as unit_price multiplied by quantity and round it to two decimal places.
5. Calculate tax_amount as net_total multiplied by tax_rate and divided by 100. Round it to two decimal places.
6. Calculate gross_total as net_total plus tax_amount. Round it to two decimal places.
7. Print net_total, tax_amount and gross_total in the terminal.

Example: for unit_price 19.99, quantity 3 and tax_rate 23, the result should be net_total = 59.97, tax_amount = 13.79 and gross_total = 73.76.
The program must calculate correctly for any values entered by the user.
