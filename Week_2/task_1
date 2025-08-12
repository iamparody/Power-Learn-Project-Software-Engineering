def sum_integer_list():
    # Ask the user to input a list of integers separated by spaces
    input_str = input("Enter a list of integers separated by spaces: ")

    # Convert the input string into a list of integers
    try:
        integer_list = [int(num) for num in input_str.split()]
    except ValueError:
        print("Error: Please enter only integers separated by spaces.")
        return

    # Compute the sum of the integers in the list
    total_sum = sum(integer_list)

    # Print the result
    print(f"The sum of the integers in the list is: {total_sum}")

# Run the function
sum_integer_list()
