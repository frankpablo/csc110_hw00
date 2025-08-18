###############################################################################
# Pablo Frank
# 2025-08-18
# This is a simple python program to get you started
#   All lines that begin with a "#" are comments (not executed)
#   Any text after a # is ignored as well (also a comment)
#   The lines below have a function called main and 
#   a conditional starting with "if"
#   The function is skipped, then the conditional will trigger and
#   line: main() # <-- function call "calls" the main function declared above
#   the function main() only prints a few lines to the terminal
###############################################################################

def main():
    """ This is a Docstring for the main function

    Docstrings are explanations for what a function does and how it works
    This particular function executes when called with the line: main()
    It runs 3 different print statements that simply print text to terminal
    Then, it ends and returns nothing. 
    NOTE: printing is different than returning a result
    """
    print("hello world")
    print("printed line 2: (the default it to add a line jump at the end)")
    print("printed line 3: (this line will not add a default jump)", end="")
    print("~~~ NOTE: this is NOT in a new line ~~~")


if __name__ == "__main__":
    main() # <-- function call
