Totaling credit card bill by store
Realizing that keeping track of credit card expenses is a particularly good use of your computer science skills, you decide to write a program that helps you track how much money you are spending at each store in a given month. Your program should read a string, which contains your credit card bill for a given month. Each line of the credit card bill represents one transaction. Each line starts with the date of the purchase, followed by a space, then the name of the store enclosed in square brackets, like so: [name] (you can assume no store names contain square bracket characters and store names also do not include the dollar sign ($) character), followed by a space, and then a dollar sign, and then the amount of the purchase (as an integer, since we assume here that transactions are just rounded to a whole dollar amount). 
Your program should print to the screen the total amount that was purchased at each store on the bill. For example, given:
bill1 = """
9/2/19 [Target] $12
9/21/19 [Stanford Bookstore] $102
9/30/19 [Jamba Juice] $5
10/7/19 [Target] $17
10/22/19 [Jamba Juice] $8
10/28/19 [Target] $45
"""


Your program should output:


Target: $74
Stanford Bookstore: $102
Jamba Juice: $13

The output printed by your program should match the sample output as closely as possible, but you don't need to worry about the order in which the stores are printed.

