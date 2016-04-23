# Andrew Kaufman
# 998048873
 
# run using Python3

import math
import random
import string


def keygen():
    key = []
    for i in range(16):
        byte = random.randint(0, 255)
        key.append(byte)

    return key

def init(key):
    length = len(key)
    S = list(range(256))

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % length]) % 256
        S[i], S[j] = S[j], S[i]

    return S

def stream(S):
    i = 0
    j = 0

    K = []

    for _ in range(2):
        i = (i + 1) % 256
        j = (j + S[i]) % 256

        S[i], S[j] = S[j], S[i]
        K.append(S[(S[i] + S[j]) % 256])

    return K


def main():
    table = [0 for i in range(10)]

    for i in range(100000):
        key = keygen()
        S = init(key)
        K = stream(S)

        if 0 <= K[1] <= 9:
            table[K[1]] += 1

    sum = 0
    for j in range(10):
        table[j] /= 100000
        print(str(j) + ": " + str(table[j]))

if __name__ == '__main__' : main()
