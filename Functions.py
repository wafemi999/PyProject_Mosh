''' functions:  a container for few lines of code that perform specific codes
types:in-built

'''


def greet_user():
    print("hi there")
    print("welcome aboard")


print("start")
greet_user()
print("finish")

'''parameters: are the placeholders for the argument 
argument is the actual  value you provide to A function '''


def greet_user_1(name):
    print(f"hi {name}")
    print("welcome aboard")


greet_user_1("femi")

'''Keyword argument SHOULD COME after positional argument: '''


def greet_user_2(f_name, l_name):
    print(f"hi {f_name} {l_name}")
    print("welcome aboard")


greet_user_2(l_name="emmanuel", f_name="femi")
greet_user_2("femi", l_name="Emmanuel")


# Return statement, all functions returns NONE, always use the return statement to avoid this in calculations
def square(number):
    print(number * number)  # use return to avoid "none"
    return None


result = int(input(" enter number: "))
square(result)


# EMOJI CONVERTER:
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "smiles",
        ":(": "sad"
    }

    output = " "
    for w in words:
        output += emojis.get(w, w) + " "
    return output


message = input("> ")
print(emoji_converter(message))
