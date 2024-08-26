# Generates heading (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display instructions
def instructions():
    statement_generator("Instructions", "♦")

    print('''
Instructions go here.
- instruction 1
- instruction 2
- etc.

    ''')


# asks the users for file type (integer / image / text / xxx)
def get_filetype():

    while True:
        response = input("File type: ").lower()

        # check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response

        # check if it's and integer
        elif response in ['integer', 'int']:
            return "integer"

        # check for an image
        elif response in ['image', 'img', 'picture', 'p']:
            return "image"

        # check for text
        elif response in ['text', 'txt', 't']:
            return "text"

        # if the response is invalid output an error
        else:
            print("Enter a valid file type >:(")


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


# calculate how many bits are needed to represent an integer
def integer_calc():
    # Calculate number of bits needed to represent text in ascii
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

    # Calculate number of bits needed to represent text in ascii
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

# Main routine starts here
    statement_generator("Bit calculator for integers", "-")

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

while True:
    file_type = get_filetype()

    if file_type == "xxx":
        break

    # IF USER CHOSE 'i', ask if they want an image / integer
    if file_type == 'i':

        want_image = input("Press <enter> for an integer or any key image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)
    else:
        text_ans = calc_text_bits()
        print(text_ans)

    print(f"You choose {file_type}")

