def crazystring(test_string):
    is_odd = True  # Start with odd position
    result = []

    for char in test_string:
        if char.isalpha():
            result.append(char.upper() if is_odd else char.lower())
            is_odd = not is_odd
        else:
            result.append(char)

    return ''.join(result)

# Example usage:
input_string = "das IST ein s4tring DER umgewANDELT W4dern kann"
output_string = crazystring(input_string)
print(output_string)  # Output: "das IST ein s4tring DER umgewANDELT W4dern kann"