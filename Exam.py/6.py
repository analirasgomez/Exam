def reverse_string(input_string):
    reversed_string = ""

    # Iterate through the characters in the string in reverse order
    for i in range(len(input_string) - 1, -1, -1):
        reversed_string += input_string[i]

    return reversed_string

# Example usage:
original_string = "Hello, World!"
reversed_result = reverse_string(original_string)

print("Original String:", original_string)
print("Reversed String:", reversed_result)
