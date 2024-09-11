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

# Main Routine goes Here
# Check Weight
for item in range(0, 2):
    integer = int_check(question="integer: ", low=0)
    print(integer)

print()
# check Height
for item in range(0, 2):
     height = int_check(question="Height: ", low=1)
     print(height)
