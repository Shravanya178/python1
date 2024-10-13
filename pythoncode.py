# Function to print pyramid pattern
def print_pyramid(n):
    for i in range(n):
        # Print spaces
        print(' ' * (n - i - 1), end='')
        # Print stars
        print('*' * (2 * i + 1))

# Number of rows for the pyramid
n = 5
print_pyramid(n)
