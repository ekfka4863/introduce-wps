def print_hello():
    num = int(input('How many numbers do you want to print?'))    
    for i in range(1, 10):
        if i % 2 == 0:        
            print('Hello, git for {}th time(s)!'.format(i))
        else:
            print('nope! i is odd ...')

if __name__ == '__main__':
    print_hello()
