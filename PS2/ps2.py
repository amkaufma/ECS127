import math
import random
import string


def bigram():
    count = 0
    filename = 'war-and-peace.txt'
    wordArray = []
    bigrams = [[0.0 for x in range(27)] for x in range(27)]

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

        position = string.ascii_lowercase.index(word[0])
        bigrams[0][position] += 1
        count += 1

        for i in range(length):
            position = string.ascii_lowercase.index(word[i])
            position2 = 0

            if i < (length - 1):
                position2 = string.ascii_lowercase.index(word[i + 1])

            bigrams[position][position2] += 1
            count += 1

    for i in range(27):
        for j in range(27):
            if bigrams[i][j] == 0.0:
                bigrams[i][j] = 1.0
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
    pl = 0.0
    for word in decipherText:
        length = len(word)

        pl = bigrams[0][string.ascii_lowercase.index(word[0])]
        for i in range(length):
            p = string.ascii_lowercase.index(word[i])
            p2 = 0
            if (i+1) < length:
                p2 = string.ascii_lowercase.index(word[i+1])

            pl *= bigrams[p][p2]

    return pl

def decipher(bigrams):
    cipherFile = 'cipher.txt'
    f = permute()
    f2 = ''

    cipherText = []
    decipherText = []


    with open(cipherFile, 'r') as infile:
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

                cipherText.append(fixed)


    for i in range(5000):
        for word in cipherText:
            temp = ''
            for c in word:
                temp += (string.ascii_lowercase[f.index(c)])

            decipherText.append(temp)

        plf = plausability(decipherText, bigrams)
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