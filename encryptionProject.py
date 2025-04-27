#Functions for DES encryption

import random




#takes in char as 8 bits
def charDecrypt(binaryChar, k1, k2):
    #return charEncrypt(char, k2, k1)
    binaryChar = IP(binaryChar)                     #performs initial permutation


    #performs s-DES with key1
    charAfterK1 = charConversionAlgo(binaryChar, k2)

    #switches halves
    charAfterK1 = switchHalf(charAfterK1)


    #performs s-DES with key2
    charAfterK2 = charConversionAlgo(charAfterK1, k1)
    


    #performs inverse operation using the inverse table
    #IP_inv = [ 3, 0, 2, 4, 6, 1, 7, 5 ]
    afterInverse = "" + charAfterK2[3] + charAfterK2[0] + charAfterK2[2] + charAfterK2[4] + charAfterK2[6] + charAfterK2[1] + charAfterK2[7] + charAfterK2[5]


    return (chr(int(afterInverse, 2)))







#encrypts char with key one and key two
def charEncrypt(char, k1, k2):
    #converts the char to an 8 bit binary sequence (as a string)

    binaryChar = addZeros(bin(ord(char)), 8)



    binaryChar = IP(binaryChar)                     #performs initial permutation



    #performs s-DES with key1
    charAfterK1 = charConversionAlgo(binaryChar, k1)



    #switches halves
    charAfterK1 = switchHalf(charAfterK1)


    #performs s-DES with key2
    charAfterK2 = charConversionAlgo(charAfterK1, k2)
    


    #performs inverse operation using the inverse table
    #IP_inv = [ 3, 0, 2, 4, 6, 1, 7, 5 ]
    afterInverse = "" + charAfterK2[3] + charAfterK2[0] + charAfterK2[2] + charAfterK2[4] + charAfterK2[6] + charAfterK2[1] + charAfterK2[7] + charAfterK2[5]


    return afterInverse




#encryption algorithm
def charConversionAlgo(char, keyBinary):

#divide the bits in half
    lh = char[:4]
    rh = char[4:]
#EP

    afterEP = EP(rh)

#XORs the rh 
    #XOR the EP with key
    rhXORed = arrayXOR(afterEP, keyBinary)


#sTable

    afterSTables = sTable(rhXORed)

#P4 table

    afterP4 = P4(afterSTables)


#XORs lh and the afterP4, and combines it with rh

    return ("".join(arrayXOR(lh, afterP4))) + ("".join(rh)) 








###############################################################

#############        Bit Shuffle Functions           ##########

###############################################################


#IP
#moves bits of index according to the IP table
def IP(binaryChar):
     #IP = [ 1, 5, 2, 0, 3, 7, 4, 6 ]     #permutation combination
    return ""+ binaryChar[1] + binaryChar[5] + binaryChar[2] + binaryChar[0] + binaryChar[3] + binaryChar[7] + binaryChar[4] + binaryChar[6]







#EP
#takes the right half of IP and inputs it into the EP table
def EP(binaryCharRH):
    #EP = [3,0,1,2,1,2,3,0]

    return ""+ binaryCharRH[3] + binaryCharRH[0] + binaryCharRH[1] + binaryCharRH[2] + binaryCharRH[1] + binaryCharRH[2] + binaryCharRH[3] + binaryCharRH[0]






#sTable
#runs the 4 bits through the tables s0 and s1
def sTable(rhXORed):
    lh = rhXORed[:4]
    rh = rhXORed[4:]


    #second and third bits of the lefthalf
    lhSecondThird = int(("" + lh[1] + lh[2]),2)
    lhFirstFourth = int(("" + lh[0] + lh[3]),2)



    #second and third bits of the righthalf
    rhSecondThird = int(("" + rh[1] + rh[2]),2)
    rhFirstFourth = int(("" + rh[0] + rh[3]),2)



    #first and fourth bit as row 
    #second and third bit as a column

    #for lhrh
    S0 = [[1,0,3,2],
      [3,2,1,0],
      [0,2,1,3],
      [3,1,3,2]]

    #for rhrh
    S1=  [[0,1,2,3],
        [2,0,1,3],
        [3,0,1,0],
        [2,1,0,3]]


    #uses the first and fourth bit for row, and second and third bit for column
    return ("" + addZeros(bin(S0[lhFirstFourth][lhSecondThird]), 2)) + ("" + addZeros(bin(S1[rhFirstFourth][rhSecondThird]), 2))





#P4
#moves bits around according to P4 table
def P4(afterSTables):
    #P4 = [ 1, 3, 2, 0 ]
    
    #P4 permutation
    return ""+afterSTables[1] + afterSTables[3] + afterSTables[2] + afterSTables[0] 






#switchHalf
#swaps left half of bits with right half
def switchHalf(bitsToSwitch8):
    return  "" + bitsToSwitch8[4] + bitsToSwitch8[5] + bitsToSwitch8[6] + bitsToSwitch8[7] + bitsToSwitch8[0] + bitsToSwitch8[1] + bitsToSwitch8[2] + bitsToSwitch8[3]





#XOR operation but for arrays
def arrayXOR(lhArray, rhArray):

    if(len(lhArray) != len(rhArray)):
        raise Exception("Arrays are different sizes, can't XOR") 

    finalArray = ""

    rhValIndex = 0


    for lhVal in lhArray:
        if(lhVal == rhArray[rhValIndex]):
            finalArray += '0'
        else:
            finalArray += '1'
        rhValIndex += 1
    
    return finalArray








####################################################################

#######################     Key Functions      #####################

####################################################################





#key generator
def keyGen():
    key = int(random.uniform(0, 1024))       #generates random number between 0-1024                 
    return key




"""
1: Runs a key through P10 
2: Then runs that through halfLeftShiftBits
3: Goes through P8 once to get an 8 bit key = k1
4: Takes the keys from step 2 that were shifted, and run halfLeftShiftBits twice again
Take that key and run it through P8 to get another 8 bit key = k2
"""
def k1k2Gen(OGKey):
    if(OGKey > 1024 or OGKey < 0):
        return "ERROR: Sorry, your key is too big"
    afterP10 = P10(OGKey)
    afterP10 = halfLeftShiftBits(afterP10)
    k1 = P8(afterP10)
    afterP10 = halfLeftShiftBits(afterP10)
    afterP10 = halfLeftShiftBits(afterP10)
    k2 = P8(afterP10)
    return [k1,k2]







#P10
#moves bits according to the P10 Table
#Permutation 10 (P10)
def P10(key):
    ###############################################################
    #turn the key into binary bits for shuffling
    #
    #    Shuffles the 10 bits in the key around 
    #
    #    k(n) represents the bits in the number (left to right)
    #    P10(k1, k2, k3, k4, k5, k6, k7, k8, k9, k10) = (k3, k5, k2, k7, k4, k10, k1, k9, k8, k6) 
    #    EX: For the number 780 -> 202
    #
    #     0 1 2 3 4 5 6 7 8 9      2 4 1 6 3 9 0 8 7 5
    #    (1 1 0 0 0 0 1 1 0 0) -> (0 0 1 1 0 0 1 0 1 0) = 202
    ###############################################################

    #indexes = [2,4,1,6,3,9,0,8,7,5]
    binaryVKey = addZeros(bin(key), 10)
    return "" + binaryVKey[2] + binaryVKey[4] + binaryVKey[1] + binaryVKey[6] + binaryVKey[3] + binaryVKey[9] + binaryVKey[0] + binaryVKey[8] + binaryVKey[7] + binaryVKey[5]





#P8
#moves bits according to the P8 Table
def P8(key10):
    """
        removes the first and last bits
        Shuffles the 8 bits in the key around 

        k(n) represents the bits in the number (left to right)
        P8(k1, k2, k3, k4, k5, k6, k7, k8, k9, k10) = (k6, k3, k7, k4, k8, k5, k10, k9)
        (k1 and k2 are gone)

        EX:
        898 = 0b1110000010
                         0 1 2 3 4 5 6 7 8 9      5 2 6 3 7 4 9 8
                       ([1 1]1 0 0 0 0 0 1 0) -> (0 1 0 0 0 0 0 1) =    65
        804 = 0b1100100100
                         0 1 2 3 4 5 6 7 8 9      5 2 6 3 7 4 9 8
                       ([1 1]0 0 1 0 0 1 0 0) -> (0 0 0 0 1 1 0 0) =    12
        
    """

    #indexes = [5,2,6,3,7,4,9,8]
    return "" + key10[5] + key10[2] + key10[6] + key10[3] + key10[7] + key10[4] + key10[9] + key10[8]




def halfLeftShiftBits(key):
    lh = key[:int(len(key)/2)]
    rh = key[int((len(key)/2)):]


    lh = shiftLeft(lh)
    rh = shiftLeft(rh)


    return "".join(lh) + "".join(rh)





#does the shift with carry over in array form
def shiftLeft(bitArray):
    temp = bitArray[0]

    bitArray = bitArray[1:]
    bitArray += temp

    return bitArray





#extends the binary number (0bXXXXXXX to contain 8 bits(represented by "X" i.e. there will be 8 "X's"))
#gets rid of "0b" from beginning of binary string 
#adds extra 0s to binary number to make the number of length n - 2
def addZeros(binaryNum, n = 2):
    length = n - (len(binaryNum) - 2)
    zeroString = ""

    while(length > 0):
        zeroString += "0"
        length -= 1

    return zeroString + binaryNum[2:]

