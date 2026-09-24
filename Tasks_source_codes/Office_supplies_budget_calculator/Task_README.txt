OFFICE BUDGET CALCULATOR
========================

The program must calculate the total cost of office purchases and the amount remaining in the budget.

1. Read four values separately with input() and store them in:
   paper_cost      paper cost,
   toner_cost      toner cost,
   delivery_cost   delivery cost,
   budget          available budget.
   Convert every value to a number with int() or float().

2. Calculate the total cost using exactly:
   total_cost = paper_cost + toner_cost + delivery_cost

3. Calculate the remaining budget using exactly:
   remaining_budget = budget - total_cost
   If spending exceeds the budget, remaining_budget should be negative. Do not replace it with zero.

4. Print total_cost and remaining_budget in the terminal.
   The program must work for any numbers entered by the user.

Example: for costs 120, 250 and 35 and a budget of 1000, total_cost should be 405 and remaining_budget should be 595.
