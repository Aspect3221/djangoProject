def validateCreditCard(param):
    #create a list of integers
    param = [int(num) for num in param]

    #Pop the last number in the list as we will never multiple this number
    lastDigit = param.pop(-1)

    #Reverse the other numbers
    param.reverse()

    #Multiply the number by 2 if at even indice
    param = [num * 2 if idx % 2 == 0
                   else num for idx, num in enumerate(param)]

    #Subtract that number by 9 if the number at even indice is greater than 9, else add the numbers
    #For example if the doubled number was 18 then it is subtrated by 9 to give 9
    param = [num - 9 if idx % 2 == 0 and num > 9
                   else num for idx, num in enumerate(param)]

    #Add the last digit back
    param.append(lastDigit)

    #Add all the digits
    checksum = sum(param)

    #Check if sum can be divided by 10 by using modulus
    return checksum % 10 == 0


def getParity(encodeInput):
    parity1 = encodeInput[0]
    parity2 = encodeInput[1]
    parity4 = encodeInput[3]
    return parity1, parity2, parity4

def calculateError(input):
    input = [int(bit) for bit in input]
    input.reverse()
    print(input)
    parity1, parity2, parity4 = getParity(input)

    #Create a list of the parity bits

    #index[2]= d3 index[4] = d5 index[5] = d6 index[6] = d7

    #p1 = d3 , d5 , d7
    p1 = str(parity1 ^ input[2] ^ input[4] ^ input[6])
    #p2 = d3, d6 , d7
    p2 = str(parity2 ^ input[2] ^ input[5] ^ input[6])
    #p3 = d5, d6, d7
    p4 = str(parity4 ^ input[4] ^ input[5] ^ input[6])
    error = p1+p2+p4

    error = int(error, 2)

    if error > 0:
        index = error - 1
        if input[index] == 0:
            input[index] = 1
        elif input[index] == 1:
            input[index] = 0

        correctedCode = [parity1, parity2, input[2], parity4, input[4], input[5], input[6]]
        correctedCode.reverse()
        correctedCodeStr = ''.join(str(bit) for bit in correctedCode)
        response = 'Error at d'+ str(error) +'. After Correction hamming code looks like this: '+str(correctedCodeStr)
        print(response)
        return response
    else:
        return 'No error'






