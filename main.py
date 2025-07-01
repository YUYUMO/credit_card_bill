bill1 = """
9/2/19 [Target] $12
9/21/19 [Stanford Bookstore] $102
9/30/19 [Jamba Juice] $5
10/7/19 [Target] $17
10/22/19 [Jamba Juice] $8
10/28/19 [Target] $45
"""

def credit_card_bill():
    expenditure_per_store = {}
    for line in bill1.strip().split("\n"):
        start_bracket_position = line.find("[")
        end_bracket_position = line.find("]")
        store = line[start_bracket_position + 1: end_bracket_position]
        dollar_sign_position = line.find("$")
        expenditure = int(line[dollar_sign_position + 1: ].strip())
        if store in expenditure_per_store:
            expenditure_per_store[store] += expenditure
        else:
            expenditure_per_store[store] = expenditure
     
    for store, total in expenditure_per_store.items():
        print(f"{store}: ${total}")
        print("")

credit_card_bill()