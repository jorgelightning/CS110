n = 10

# Upper half of the diamond
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end=' ')
    for j in range(i + 1):
        print('x', end=' ')
    for j in range(i):
        print('x', end=' ')
    print()

# Lower half of the diamond
for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end=' ')
    for j in range(n - i - 1):
        print('x', end=' ')
    for j in range(n - i - 2):
        print('x', end=' ')
    print()