def getDistance(original, new):
  if (len(original) != len(new)):
    return -1

  originalList = list(original)
  newList = list(new)

  matchCount = 0
  for i in range(len(original)):
    if (originalList[i] != newList[i]):
      matchCount += 1
  
  return matchCount
if __name__ == "__main__":
    s1 = 'matchcount'
    s2 = 'matchountu'
    print(getDistance(s1,s2))