# %%======

names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]
max_count = 0
print(counts)

for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

names.append('Rosalind')
import itertools

for name, count in itertools.zip_longest(names, counts):
    print(f'{name}: {count}')
