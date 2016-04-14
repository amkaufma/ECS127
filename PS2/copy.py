import math
import random
import string

def bernoulli(p):
    r = random.random()
    return (r < p)

def bigram():
    count = 0
    filename = 'war-and-peace.txt'
    wordArray = []
    bigrams = [[1.0 for x in range(27)] for x in range(27)]

    with open(filename, 'r') as infile:
        for line in infile:
            line2 = ''
            for i in line:
                if i.islower():
                    line2 += i
                else:
                    line2 += ' '

            words = line2.split()
            for word in words:
                fixed = ''
                for i in word:
                    if i.islower():
                        fixed += i

                wordArray.append(fixed)

    for word in wordArray:
        length = len(word)

        position = string.ascii_lowercase.index(word[0]) + 1
        bigrams[0][position] += 1
        count += 1

        for i in range(length):
            position = string.ascii_lowercase.index(word[i]) + 1
            position2 = 0

            if i < (length - 1):
                position2 = string.ascii_lowercase.index(word[i + 1]) + 1

            bigrams[position][position2] += 1
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

def plausability(decipherText, bigrams):
    pl = 1.0
    for word in decipherText:
        length = len(word)

        pl = bigrams[0][string.ascii_lowercase.index(word[0])]
        for i in range(length):
            p = string.ascii_lowercase.index(word[i])
            p2 = 0
            if (i + 1) < length:
                p2 = string.ascii_lowercase.index(word[i + 1])

            pl *= bigrams[p][p2]

    return pl

def decipher(bigrams):
    cipherFile = 'cipher.txt'

    f = permute()
    f2 = swap(f)

    cipherString = ''

    cipherText = []
    decipher1 = []
    decipher2 = []


    with open(cipherFile, 'r') as infile:
        for line in infile:
            line2 = ''
            for i in line:
                cipherString += i
                if i.islower():
                    line2 += i
                else:
                    line2 += ' '

            words = line2.split()
            for word in words:
                fixed = ''
                for i in word:
                    if i.islower():
                        fixed += i

                cipherText.append(fixed)

    count = 0
    while (1):
        count += 1
        if (count % 1000) == 0:
            print(count)
        decipherString = ''
        for word in cipherText:
            temp = ''
            temp2 = ''
            for c in word:
                temp += (string.ascii_lowercase[f.index(c)])
                temp2 += (string.ascii_lowercase[f2.index(c)])

            decipher1.append(temp)
            decipher2.append(temp2)

        plf = math.log(plausability(decipher1, bigrams))
        plf2 = math.log(plausability(decipher2, bigrams))

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