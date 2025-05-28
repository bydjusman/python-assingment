#01_phonebook

#In this program we show an example of using dictionaries to keep track of information in a phonebook.

def read_phone_numbers():
    """
    Asks the user for names and numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook

def print_phonebook(phonebook):
    """
    Prints all the names and numbers in the phonebook.
    """
    for name, number in phonebook.items():
        print(f"{name} -> {number}")

def lookup_numbers(phonebook):
    """
    Allows the user to look up phone numbers in the phonebook by name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name in phonebook:
            print(phonebook[name])
        else:
            print(f"{name} is not in the phonebook")

def main():
    """
    Reads phone numbers, prints the phonebook, and allows lookups.
    """
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

if __name__ == '__main__':
    main()