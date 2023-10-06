# Given a roman numeral, this program converts it to decimal

def integer_value(char):
    if char == 'I':
        return 1
    if char == 'V':
        return 5
    if char == 'X':
        return 10
    if char == 'L':
        return 50
    if char == 'C':
        return 100
    if char == 'D':
        return 500
    if char == 'M':
        return 1000
    return -1


def romanToInt(romanNum, numOfChars):
    ans = 0
    for i in range(numOfChars):
        current_char = integer_value(romanNum[i])  # Convert first char into decimal value
        if i + 1 < numOfChars:  # If another char exists in string then find its decimal value
            nextChar = integer_value(romanNum[i+1])
            if current_char >= nextChar:
                ans += current_char
            else:
                ans -= current_char  # A symbol of greater value is on the right of one of lesser value
        else:
            ans += current_char

    return ans

def main():
    roman = input("Please input a Roman numeral string: ")
    numOfChars = len(roman)
    ans = romanToInt(roman, numOfChars)
    print(ans)

main()