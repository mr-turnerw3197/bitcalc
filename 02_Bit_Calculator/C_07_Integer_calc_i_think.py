# Ask the user for width and loop until they
# enter a number that is more than zero
def int_check(question, low):

    error = "ENTER A INTEGER MORE THAN ZERO, OR ELSE\n"
    while True:

        try:
            # Ask the user for a number
            response = int(input(question))

    # check that the number is more than zero
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# calculate how many bits are needed to represent an integer
def integer_calc():
    # Ask the user to enter an integer (more than / equal to 0)
    integer = int_check("Integer: ",0)

    # convert the integer to binary and work out the number of bits needed
    raw_binary = bin(integer)

    # remove the leading '0b' from the raw binary conversion
    binary = raw_binary[2:]
    num_bits = len(binary)

    # Set up answer and return it
    answer = f"{integer} in binary is {binary}. We need {num_bits} to represent it."

    return answer

# Main routine goes here
integer_ans = integer_calc()
print(integer_ans)