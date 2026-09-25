WAREHOUSE STOCK CALCULATOR
==========================

The program must calculate the current warehouse stock and the number of usable products.

1. Read four values separately with input() and convert them to numbers:
   opening_stock     stock before today's operations,
   delivered_items   number of received products,
   issued_items      number of issued products,
   damaged_items     damaged products remaining in the current stock.

2. Calculate stock after deliveries and issues using exactly:
   available_items = opening_stock + delivered_items - issued_items

3. Calculate usable products using exactly:
   usable_items = available_items - damaged_items
   Do not replace the result with zero, even when the provided values produce a negative number.

4. Print available_items and usable_items in the terminal.
   The program must work for any numbers entered by the user.

Example: for opening_stock = 100, delivered_items = 30, issued_items = 25 and damaged_items = 4, the results are available_items = 105 and usable_items = 101.
