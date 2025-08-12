# Function to get a set of integers from user input
def get_integer_set(prompt):
    input_str = input(prompt)
    try:
        # Convert the input string into a set of integers
        integer_set = {int(num) for num in input_str.split()}
        return integer_set
    except ValueError:
        print("Error: Please enter only integers separated by spaces.")
        return set()

# Get the first set of integers from the user
set1 = get_integer_set("Enter the first set of integers, separated by spaces: ")

# Get the second set of integers from the user
set2 = get_integer_set("Enter the second set of integers, separated by spaces: ")

# Create a new set that contains only the common elements
common_elements = set1.intersection(set2)

# Print the result
print("The common elements in both sets are:", common_elements)
