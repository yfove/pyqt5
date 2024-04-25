# for loops
for i in range(4):
    print(i)

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + 'in supplies is: ' + supplies[i])

# single tuple value
# immutable so used to store values
type(('hello',))