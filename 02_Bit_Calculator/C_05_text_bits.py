# Calculate number of bits needeed to represent text in ascii
def calc_text_bits():

    # Get text from user
    response = input("Enter some text:  ")

    # Calculate bits needed
    num_chars = len(response)
    num_bits = num_chars * 8

    # Set up answer and return it
    answer = f"{response} has {num_chars} characters." \
             f"\n we need {num_chars} x8 bits to represent it" \
             f"\n which is {num_bits} bits"

    return answer


# main routine starts here
text_ans = calc_text_bits()
print(text_ans)