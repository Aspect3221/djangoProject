def validateCreditCard(param):
    if len(param) == 0:
        return False
    # create a list of integers
    param = [int(num) for num in param]

    # Pop the last number in the list as we will never multiply this number
    lastDigit = param.pop(-1)

    # Reverse the other numbers
    param.reverse()

    # Multiply the number by 2 if at even indice
    param = [num * 2 if idx % 2 == 0
             else num for idx, num in enumerate(param)]

    # Subtract that number by 9 if the number at even indice is greater than 9, else add the numbers
    # For example if the doubled number was 18 then it is subtrated by 9 to give 9
    param = [num - 9 if idx % 2 == 0 and num > 9
             else num for idx, num in enumerate(param)]

    # Add the last digit back
    param.append(lastDigit)

    # Add all the digits
    checksum = sum(param)

    # Check if sum can be divided by 10 by using modulus
    return checksum % 10 == 0


def getParity(encodeInput):
    parity1 = encodeInput[0]
    parity2 = encodeInput[1]
    parity4 = encodeInput[3]
    return parity1, parity2, parity4


def is_binary(input_str):
    for char in input_str:
        if char != '0' and char != '1':
            return False
    return True


def calculateError(input):
    # Check whether passed input is in binary and is 7 bits
    if len(input) < 7:
        return "Input has fewer than 7 bits. Cannot perform Hamming code correction."
    if not is_binary(input):
        return "Input is not in binary format. Please provide a binary input."

    input = [int(bit) for bit in input]
    input.reverse()
    parity1, parity2, parity4 = getParity(input)

    # Create a list of the parity bits

    # index[2]= d3 index[4] = d5 index[5] = d6 index[6] = d7

    # p1 = d3 , d5 , d7
    p1 = str(parity1 ^ input[2] ^ input[4] ^ input[6])
    # p2 = d3, d6 , d7
    p2 = str(parity2 ^ input[2] ^ input[5] ^ input[6])
    # p3 = d5, d6, d7
    p4 = str(parity4 ^ input[4] ^ input[5] ^ input[6])
    error = p4 + p2 + p1

    # Convert error from binary to decimal places
    error = int(error, 2)

    # If error is greater than one
    if error > 0:
        index = error - 1
        if input[index] == 0:
            input[index] = 1
        elif input[index] == 1:
            input[index] = 0

        correctedCode = [parity1, parity2, input[2], parity4, input[4], input[5], input[6]]
        correctedCode.reverse()
        correctedCodeStr = ''.join(str(bit) for bit in correctedCode)
        response = 'Error at d' + str(error) + '. After Correction hamming code looks like this: ' + str(
            correctedCodeStr)
        print(response)
        return response
    else:
        return 'No error'


def passwordCracker(input):
    # import library to hash password
    import hashlib
    import itertools

    # init variables
    foundPassword = ""
    attackType = ""

    # hash the inputted password as most passwords are expected to be hashed currently
    hashInput = hashlib.sha256(input.encode('utf-8')).hexdigest()

    # read dictionary file of common passwords
    with open('common_passwords.txt', 'r') as file:
        commonPasswords = (file.read().splitlines())

    for password in commonPasswords:
        hashedPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
        # if hash password in dictionary is equal to hashed inputted password then return this
        if hashedPassword == hashInput:
            attackType = "Set B"
            foundPassword = password

    # if dictionary attack doesnt work then try to crack 4 character passwords
    if foundPassword == "":
        for password in itertools.product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', repeat=4):
            password = ''.join(password)
            hashedPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()

            if hashedPassword == hashInput:
                attackType = "Set A"
                foundPassword = password
                break

    return hashInput, foundPassword, attackType


def encrypt(plainMessage, toEncrypt):
    import random

    # generate a keystream that caters to the length of the input
    key = [random.randint(0, 255) for _ in range(len(toEncrypt))]

    # create a list of ascii for the characters for toEncrypt input
    convertedInput = [ord(i) for i in toEncrypt]

    # perform xor with key to encrypt converted input
    encryptedInput = [convertedInput[i] ^ key[i] for i in range(len(convertedInput))]

    # add the plain message to the encrypted message
    ciphertext = plainMessage + ''.join(chr(i) for i in encryptedInput)

    return encryptedInput, key, ciphertext


def decrypt(encryptedInput, key):
    # perform xor with key to decrypt
    decryptedInput = [encryptedInput[i] ^ key[i] for i in range(len(key))]

    # convert the message into string
    decryptedMessage = "".join(chr(value) for value in decryptedInput)
    return decryptedMessage
