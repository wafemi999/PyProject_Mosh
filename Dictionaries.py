# when you want store info as key value pairs
customer = {"name": "smith",
            "age": 30,
            "is_verified": True
            }
print(customer["name"])
print(customer.get("age"))
# update A key / add new key:value pairs:

customer["name"] = "jack Manuel"
customer["birthdate"] = "21 Apr 1995"
print(customer["name"])
print(customer["birthdate"])

# exercise a program that translates no to text
phone = input("Phone: ")

digit_mapping = {"1": "one",
                 "2": "two",
                 "3": "three",
                 "4": "four"

                 }
output = " "
for i in phone:
    output += digit_mapping.get(i, "!") + " "
print(output)

# EMOJI CONVERTER:
message = input("> ")
words = message.split(" ")
emojis = {
    ":)": "smiles",
    ":(": "sad"
}

output = " "
for w in words:
    output += emojis.get(w, w) + " "
print(output)