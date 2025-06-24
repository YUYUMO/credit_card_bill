def credit_card_bill():
    # This function collects credit card expenditure data and summarizes it by store.
    # Create a dictionary to hold data of store and expenditure
    expenditure = {}
    # Prompt the user for input until they choose to finish
    while True:
        date = input("Enter the date of expenditure in MM/DD/YY (or press Enter to finish): ")
        # If the user presses Enter without inputting a date, break the loop.
        if not date:
            break
        store = input("Enter the store name (or press Enter to finish): ")
        # If the user presses Enter without inputting a store, break the loop.
        if not store:
            break
        amount = input("Enter the amount spent at the store (or press Enter to finish): ")
        # If the user presses Enter without inputting an amount, break the loop.
        if not amount:
            break
        int_amount = int(amount)  # Convert amount to integer 
        # if the store already exists in the expenditure dictionary, add the amount to it; otherwise, create a new entry.
        if store in expenditure:
            expenditure[store] += int_amount
        else:
            expenditure[store] = int_amount
        print(f"{date} [{store}] ${int_amount}")
    # Print the current expenditure for the store
    print("\nExpenditure Summary:")
    # Iterate through the expenditure dictionary and print each store with its total expenditure
    for store, total in expenditure.items():
        print(f"{store}: ${total}")
 
credit_card_bill()