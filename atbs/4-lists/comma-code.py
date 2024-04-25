spam = ['apples', 'bananas', 'tofu', 'cats']

result = ' '
for i in range(len(spam)):
    result += spam[i]
    if i < len(spam) - 1:
        result += ', '

print(result)