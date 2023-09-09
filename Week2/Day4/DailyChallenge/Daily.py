mat = [[7, 'i', 'i'], 
['T', 's', 'x'], 
['h', '%', '?'], 
['i', 0, '#'], 
['s', 'M', 0],
['$', 'a', 0],
['#', 't', '%'],
['^', 'r', '!']]

for c in zip(*mat):
    for r in c:
        if (str(r).isalpha()):
            print(r, end="")

