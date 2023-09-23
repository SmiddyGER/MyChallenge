def crazystring(test_string):
    return ''.join((char.upper() if i % 2 == 0 else char.lower()) if char.isalpha() else char for i, char in enumerate(test_string))

# Example usage:
input_string = "das IST ein s4tring DER umgewANDELT W4dern kann"
output_string = crazystring(input_string)
print(output_string)  # Output: "das IST ein s4tring DER umgewANDELT W4dern kann"
