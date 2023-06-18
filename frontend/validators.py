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