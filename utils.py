def format_amount(amount):
    """
    Formats an amount as INR with two decimal places.
    """
    return "INR " + str(round(amount, 2))
def print_line():
    """
    Prints a separator line for better output formatting.
    """
    print("--------------------------------")