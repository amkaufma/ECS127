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

            # print(position)
            # print(position2)
            bigrams[position][position2] += 1
            count += 1

    for i in range(27):
        for j in range(27):
            bigrams[i][j] /= count
            print(bigrams[i][j])





def main():
    bigram()

if __name__ == '__main__': main()