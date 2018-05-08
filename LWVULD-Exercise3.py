def lengthOfLongestWord(list): #a lista leghosszabb szavának hossza
    length = 0
    for i in list:
        if len(i)>length:
            length = len(i)
    return length

def framer(list):
    width = lengthOfLongestWord(list)+4
    for i in range(width): #a keret felső oldala
        print('*', end='')
    print()
    for i in list:
        i+=' '*(lengthOfLongestWord(list)-len(i)) #kiegészítjük szóközökkel, hogy egyenlő hosszú legyen a leghosszabb szóval
        print('* {0} *'.format(i))
    for i in range(width):
        print('*', end='')

L = ["Hello", "World", "in", "a", "frame"]
framer(L)
