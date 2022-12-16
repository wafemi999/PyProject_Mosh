prices = [10, 20, 30]
total = 0
for p in prices:
    total += p
print(f'total = {[total]}')

# nested lo;ps: in here iteration is done y finishing the inner loop b4 next outer loop
for x in range(4):
    for y in range(3):
        print(f' ({x}, {y}) ')

# exercise
numbers = [5, 2, 5, 2, 2] #prints f
numbers_2 = [2, 2, 2, 2, 7] #prints L
for n in numbers_2:
    output = ''
    for count in range(n):
        output += 'x'
    print(output)
