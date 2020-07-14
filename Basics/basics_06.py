# More string fun.

name = 'Zack'
favoriteFood = 'Pizza'

strConcat = name + "'s favorite food is " + favoriteFood + '!'
print(strConcat)

strFormat = '{}\'s favorite food is {}!'.format(name, favoriteFood)
print(strFormat)

strFstring = f'{name}\'s favorite food is {favoriteFood}!'
print(strFstring)

num = 5
print(f'num = {num}')

for num in range(10):
    print(f'Iteration {num+1}')