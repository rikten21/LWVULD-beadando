def longestWord(list):
    length = 0
    for i in list:
        if len(i)>length:
            length = len(i)
    return length

def framer(list):
    width = longestWord(list)+4
    for i in range(width):
        print('*', end='')
    print()
    for i in list:
        i+=' '*(longestWord(list)-len(i))
        print('* {0} *'.format(i))
    for i in range(width):
        print('*', end='')

L = ["Hello", "World", "in", "a", "frame"]
framer(L)