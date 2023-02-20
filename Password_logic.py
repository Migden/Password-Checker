import pyperclip

def add_to_clipboard(text):
    pyperclip.copy(text)
    return

def length_check(length): ## It takes over a centurie to crack a password over the length of 16 characters
    pass_standard = 16
    if length > pass_standard:
        return 5
    return float((5 * (length / pass_standard)))


def upper_case_check(password):
    number_of_symbols = 0
    for symbol in password:
        if symbol.isupper() == False and symbol.islower() == False:
            number_of_symbols += 1
    length = (len(password) - number_of_symbols)
    upper_case = 0
    lower_case = 0
    for item in password:
        if item.isupper():
            upper_case += 1
        elif item.islower():
            lower_case += 1
    if upper_case > lower_case:
        numb = upper_case - lower_case
        result = 5 - ((5 * float(upper_case / (length))) * (numb / upper_case))
        return result
    return ((5 * float(upper_case / (length)))) * 2


def main():
    ### Password length has to be greater than 0
    ### Make nemonic genarator
    password = "AAAaaa"
    print(upper_case_check(password))
    print(length_check(len(password)))

if __name__ == "__main__":
    main()