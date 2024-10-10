# Dictionary for converting digits to words
num_to_words = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 
    17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 
    60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
}

# Helper function to convert numbers less than 1000
def convert_hundreds(n):
    if n < 100:
        return convert_tens(n)
    else:
        hundred_part = num_to_words[n // 100] + " hundred"
        rest = n % 100
        if rest != 0:
            return hundred_part + " and " + convert_tens(rest)
        return hundred_part

# Helper function to convert numbers less than 100
def convert_tens(n):
    if n < 20:
        return num_to_words[n]
    else:
        tens_part = num_to_words[(n // 10) * 10]
        ones = n % 10
        if ones != 0:
            return tens_part + "-" + num_to_words[ones]
        return tens_part

# Main function to convert any number up to 999999 into words
def number_to_words(n):
    if n == 0:
        return "zero"
    elif n < 1000:
        return convert_hundreds(n)
    else:
        thousand_part = convert_hundreds(n // 1000) + " thousand"
        rest = n % 1000
        if rest != 0:
            return thousand_part + ", " + convert_hundreds(rest)
        return thousand_part

# Example usage
print(number_to_words(115))  # Output: one hundred and fifteen
