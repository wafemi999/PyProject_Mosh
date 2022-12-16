names = ['femi', 'kamal', 'eniola', 'dinho']
print(names[0])

names[0] = 'seun'  # changing item in index 0

print(names)

# exercise 2 find largest no in a list

numbers = [3, 6, 20, 2, 8, 4, 2, 2, 2, 2, 2, 9]
highest = numbers[0]
for n in numbers:
    if n > highest:
        highest = n
print(f'MAx = {highest}')

# 2D LIST:

''' list methods: .insert(index, oject)

    .pop .remove. replace .clear(clears entires content of a list)
    
    .sort(you orint list after say: number.sort(), print(number)
    .reverse(does opposite of 
     .COPY() '''

# duplicates

numbers = [2, 2, 4, 5, 6, 33, 8, 5, 6, 33]
uniques = []

for n in numbers:
    if n not in uniques:
        uniques.append(n)
print(uniques)
