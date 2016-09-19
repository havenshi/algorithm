def coinChange(centsNeeded, coinValues):      # online method
    minCoins = [[0 for j in range(centsNeeded + 1)] for i in range(len(coinValues))]
    minCoins[0] = range(centsNeeded + 1)

    for i in range(1,len(coinValues)):
        for j in range(0, centsNeeded + 1):
            if j < coinValues[i]:
                minCoins[i][j] = minCoins[i-1][j]
            else:
                minCoins[i][j] = min(minCoins[i-1][j], 1 + minCoins[i][j-coinValues[i]])
    return minCoins[-1][-1]

print coinChange(63,[1,5,10,25])


def recDC(coinValueList,change,knownResults): # example method
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   elif knownResults[change] > 0:             # if our table contains the minimum number of coins for a certain amount of change
      return knownResults[change]
   else:                                      # If it does not, we compute the minimum recursively and store the computed minimum in the table
       for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
   return minCoins

print(recDC([1,5,10,25],63,[0]*64))
