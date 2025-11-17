print('* * * * *')
print('*\t*')
print('*\t*')
print('*\t*')
print('* * * * *')

print("* * * * *\n* \t*\n* \t*\n* \t*\n* * * * *")

print('*\n* *\n* * *\n* * * *\n* * * * *')

print('\t   __\n\t  / _)\n   .-^^^-/ /\n__/       /\n<__.|_|-|_|\n')

print("(\/)\n(..)\n(>♥)\n")

def pyramid(n=5):
    for i in range(1, n+1):
        print(' '*(n-i) + ('* ' * i).rstrip())

def diamond(n=5):
    for i in range(n):
        print(' '*(n-i-1) + ('* '*(i+1)).rstrip())
    for i in range(n-1):
        print(' '*(i+1) + ('* '*(n-i-1)).rstrip())

def checkerboard(rows=6, cols=6):
    for r in range(rows):
        line = []
        for c in range(cols):
            line.append('# ' if (r+c) % 2 == 0 else '  ')
        print(''.join(line).rstrip())

if __name__ == '__main__':
    print("Pyramid:")
    pyramid(5)
    print("\nDiamond:")
    diamond(5)
    print("\nCheckerboard:")
    checkerboard(6, 12)