def symbol_check(password):
    length = len(password)
    number_of_symbols = 0
    for item in password:
        if item.isupper() == False and item.islower() == False:
            number_of_symbols += 1
    result = ((5 * float(number_of_symbols / length)))
    result = result % 5
    return (5 * result) % 5


def length_check(password):
    recomended_length = 16
    if len(password) >= recomended_length:
        return 5
    else:
        return 5 * (len(password) / 16)

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

    result = ((5 * float(upper_case / (length))))

    if upper_case > lower_case:
        numb = upper_case - lower_case
        result = 5 - ((5 * float(upper_case / (length))) * (numb / upper_case)) 
        return result
    return result * 2


def main():
    #implement early policy checking
    password = "9@97eMZB!v2Y@i"
    print(upper_case_check(password))
    print(length_check(password))
    print(symbol_check(password))
if __name__ == "__main__":
    main()
