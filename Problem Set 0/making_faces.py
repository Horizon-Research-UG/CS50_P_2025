# Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!

# In a file called faces.py, 
# implement a function called convert that accepts a str as input
"""
def convert():
    input("wie geht es dir heute? : ")
"""
#  and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) 
# and any :( converted to 🙁 (otherwise known as a slightly frowning face). 
# All other text should be returned unchanged.
"""
def convert(text):
    text = input("wie geht es dir heute? : ")
    con_text = text.replace(": )", "🙂").replace(": (", "🙁")
    print(con_text)

# Then, in that same file, implement a function called main 
# that prompts the user for input, 
""""
def main():
    input("")
 """
# calls convert on that input, and prints the result. 
"""
def main():
    print(convert())

main()
"""
# You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.