roommates = {'vishal': ['fat ass guy', 25], 'tanmay': ['A blithering idiot', 23], 'ashutosh': ['a social extrovert', 19]}

print(roommates)
roommates['ashutosh'] = ['cool guy', 18]
print(roommates['ashutosh'])
# for removing an element of dictionary
del roommates['vishal']
print(roommates)
# following loop works best when only've string or char values
for k, v in roommates.items():  #   k for key and v for value
    print(k + ": " + v)
