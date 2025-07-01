bill1 = """
9/2/19 [Target] $12
9/21/19 [Stanford Bookstore] $102
9/30/19 [Jamba Juice] $5
10/7/19 [Target] $17
10/22/19 [Jamba Juice] $8
10/28/19 [Target] $45
"""

def credit_card_bill():
    # This function processes a credit card bill and calculates the total expenditure per store.
    # Initialize a dictionary to hold the total expenditure for each store
    expenditure_per_store = {}
    # Split the bill into lines and process each line
    for line in bill1.strip().split("\n"):
        # find the start bracket and end bracket positions
        start_bracket_position = line.find("[")
        end_bracket_position = line.find("]")
        # Extract the store based on the bracket positions
        store = line[start_bracket_position + 1: end_bracket_position]
        # Find the dollar sign position 
        dollar_sign_position = line.find("$")
        # extract the expenditure amount based on the dollar sign position, delete the spaces and convert to integer
        expenditure = int(line[dollar_sign_position + 1: ].strip())
        # If the store already exists in the dictionary, add the expenditure to the existing total
        if store in expenditure_per_store:
            expenditure_per_store[store] += expenditure
            # Otherwise, create a new entry in the dictionary for the store
        else:
            expenditure_per_store[store] = expenditure
    #iterate through the dictionary and print the total expenditure for each store 
    for store, total in expenditure_per_store.items():
        print(f"{store}: ${total}")
        print("")

# Call the function to execute the code
credit_card_bill()