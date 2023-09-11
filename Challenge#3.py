def crazystring(test_string):
    result = []  # To store the modified characters

    # Helper function to check if a character is a letter (not digit or special character)
    def is_letter(char):
        return char.isalpha()

    # Initialize a variable to keep track of the character position
    position = 0

    for char in test_string:
        if is_letter(char):
            # Determine whether the position is odd or even
            if position % 2 == 0:
                # Even position, convert to lowercase
                result.append(char.lower())
            else:
                # Odd position, convert to uppercase
                result.append(char.upper())
            
            # Increment the position counter
            position += 1
        else:
            # Non-letter character, append it as is
            result.append(char)

    # Join the modified characters back into a string
    modified_string = ''.join(result)
    
    return modified_string

# Example usage:
input_string = "guten ta2ag dÜsselDorf"
output_string = crazystring(input_string)
print(output_string)  # Output: "ThIs Is A tEsT StRiNg"
