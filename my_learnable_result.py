#The function takes in the array and number needed to know it least occurance
def nth_most_rate_signature(array:list, n:int):

    # condition to check for items outside the scope of the array
    if n < len(array):

        #creating empty dictionary
        digitDict = {}
        #storing the list as a dictionary

        for digit in array:
            digitDict[digit] = digitDict.get(digit, 0) + 1
        #sort the dictionary into key value pairs
        # where the key = values and the values = no of time they occur
        sortedDict = sorted(digitDict.items(), key=lambda item: item[1])
        
        #return the sorted dictionary
        return sortedDict[n - 1][0]

    # condition when 
    else:
        return ("not in list")

nth_most_rate_signature([1,1,3,4,5,2,6,7],7)