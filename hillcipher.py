# Author: David Thompson
# Date: 17 April, 2018
# Purpose: Encipher text using a hill cipher with
#          a randomly generated enciphering matrix


import random


LETTERS = ['Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']


## CLASS DEFINITIONS ##

class Matrix2x1:

    def __init__(self, row1, row2):

        self.row1 = row1
        self.row2 = row2


class Matrix2x2:

    def __init__(self, row1, row2):

        self.row1 = row1
        self.row2 = row2

    def multiply(self, other):

        newR1 = (self.row1[0]*other.row1 + self.row1[1]*other.row2) %26
        newR2 = (self.row2[0]*other.row1 + self.row2[0]*other.row2) %26

        return Matrix2x1(newR1, newR2)

    def det(self):

        return self.row1[0]*self.row2[1] - self.row1[1]*self.row2[0]

    def __str__(self):
        
        return str(self.row1) + '\n' + str(self.row2)



## CREATE ENCIPHERING MATRIX ##

cipherMatrix = Matrix2x2([0,0],[0,0])

while cipherMatrix.det()%2==0 or cipherMatrix.det()%13==0:

    # Make four random numbers for the matrix
    numbers = []

    for i in range(4):
        numbers.append(random.randrange(0,7)) # using 7 makes the matrices easier

    cipherMatrix = Matrix2x2([numbers[0],numbers[1]], [numbers[2],numbers[3]])

print("Cipher Matrix being used:")
print(cipherMatrix)


message = input("Please input the text to encode: ")


## PROCESS THE INPUT ##

message = message.upper()

# Make the
if len(message)%2 != 0:
    message += 'Z'

# Replace all the spaces with zeds
while message.find(" ") != -1:
    index = message.find(" ")
    first = message[:index]
    last = message[index + 1:]

    message = first + "Z" + last


## CHANGE THE TEXT INTO MATRICES ##

textMatrices = []

while message != "":

    textMatrices.append(Matrix2x1(LETTERS.index(message[0]),
                                LETTERS.index(message[1])))

    message = message[2:]


## ENCODE THE TEXT AND TURN TO OUTPUT ##

codedText = ""

for mat in textMatrices:

    encMat = cipherMatrix.multiply(mat)

    codedText += LETTERS[encMat.row1] + LETTERS[encMat.row2]

print("Encoded text:")
print(codedText)
