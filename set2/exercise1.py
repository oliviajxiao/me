"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# It will list the words
some_words = ["what", "does", "this", "line", "do", "?"] # it doesn't display it, it just puts it under 'variables'

# it'll print some_words
for word in some_words:
    print(word)#it prints all the words in the list

# Exact same as what happened above
for x in some_words:
    print(x) # Exact same as what happened above
# It will write the whole list out
print(some_words)
# It wrote the whole list out
# It will print "some_words contains more than 3 words"
if len(some_words) > 3:
    print("some_words contains more than 3 words")
# It will print "some_words contains more than 3 words"

# It prints nothing
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

# It prints nothing
usefulFunction()
# It printed nothing