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

# Main routine goes here
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue")
# Display functions if requested
if want_instructions == "":
    instructions()

    print("program continues")
