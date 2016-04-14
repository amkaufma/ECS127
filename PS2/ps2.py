import math
import random
import string

def bernoulli(p):
    r = random.random()
    return (r < p)

def bigram():
    count = 0
    filename = 'war-and-peace.txt'
    bigrams = [[1.0 for x in range(27)] for x in range(27)]

    with open(filename, 'r') as infile:
        for line in infile:
            for i in range(len(line)):
                pos1 = 0
                pos2 = 0
                if line[i].islower():
                    pos1 = string.ascii_lowercase.index(line[i]) + 1
                if (i+1) < len(line):
                    if line[i+1].islower():
                      pos2 = string.ascii_lowercase.index(line[i+1]) + 1
                bigrams[pos1][pos2] += 1
                count += 1

    for i in range(27):
        for j in range(27):
            bigrams[i][j] /= count

    return bigrams


def permute():
    s = ''
    arr = [0 for x in range(26)]
    for i in range(26):
        x = random.randint(0, 25)
        if arr[x] == 1:
            while (arr[x] == 1):
                x = random.randint(0, 25)

        arr[x] = 1
        c = string.ascii_lowercase[x]
        s += c
    return s

def plausability(decipherString, bigrams):
    pl = 1.0
    for i in range(len(decipherString)):
        print(pl)
        pos1 = 0
        pos2 = 0

        if decipherString[i].islower():
            pos1 = string.ascii_lowercase.index(decipherString[i]) + 1
        if (i + 1) < len(decipherString):
            if decipherString[i + 1].islower():
                pos2 = string.ascii_lowercase.index(decipherString[i + 1]) + 1

        pl *= bigrams[pos1][pos2]

    return pl

def decipher(bigrams):
    cipherFile = 'cipher.txt'

    f = permute()
    f2 = swap(f)

    cipherString = ''

    decipher1 = ''
    decipher2 = ''


    with open(cipherFile, 'r') as infile:
        for line in infile:
            for i in line:
                cipherString += i


    count = 0
    while (1):
        count += 1
        if (count % 1000) == 0:
            print(count)

        for i in range(len(cipherString)):
            if cipherString[i].islower():
                decipher1 += string.ascii_lowercase[f.index(cipherString[i])]
                decipher2 += string.ascii_lowercase[f2.index(cipherString[i])]
            else:
                decipher1 += cipherString[i]
                decipher2 += cipherString[i]

        plf = math.log(plausability(decipher1, bigrams))
        plf2 = math.log(plausability(decipher2, bigrams))

        print(plf)

        print(plf)
        if plf2 > plf:
            f = f2
            f2 = swap(f)
        else:
            p = plf2 / plf
            coin = bernoulli(p)

            if coin == 1:
                f = f2
                f2 = swap(f)
            else:
                f2 = swap(f)

def swap(f):
    pos1 = random.randint(0, 25)
    pos2 = random.randint(0, 25)
    s = ''

    length = len(f)
    if pos2 == pos1:
        while (pos2 == pos1):
            pos2 = random.randint(0, 25)

    for i in range(length):
        if i == pos1:
            s += f[pos2]
        elif i == pos2:
            s += f[pos1]
        else:
            s += f[i]

    return s



def main():
    bigrams = bigram()
    decipher(bigrams)

    # print(bigrams[8][5])

if __name__ == '__main__': main()