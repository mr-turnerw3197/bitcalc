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
def image_calc():

    width = int_check(question="Width: ", low=1)
    print(width)

    height = int_check(question="Height: ", low=1)
    print(height)

    # Calculate the number of pixels, and then multiply them by 24 to get the number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # set up answer and return it
    answer = (f"Number of pixels:  {width} x {height} = {num_pixels}" 
             f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer

# Main routine goes here
image_ans = image_calc()
print(image_ans)
