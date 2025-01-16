"""Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the
function with a short program."""
def upper_or_lower(string):
    uppercase = 0
    lowercase = 0
    for char in string:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase +=1
        else:
            pass

    print(f"Uppercase letters: {uppercase}")
    print(f"Lowercase letters: {lowercase}")

upper_or_lower("Beautiful Day")            
                