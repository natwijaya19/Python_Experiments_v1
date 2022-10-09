#%% assignment expression 1
walrus = True
print(walrus)

#%% assignment expression 2
print(walrus := True)

#%% assignment expression 3
inputs = list()
while True:
    current = input('Write something: ')
    if current == 'quit':
        break
    inputs.append(current)
print(inputs)

#%% assignment expression 4
inputs = list()
while (current := input('Write something: ')) != 'quit':
    inputs.append(current)
print(inputs)


#%% assignment expression 5
