def find(s):
    givenString = [char for char in s]
    givenStringLength = len(givenString)

    start = 0
    leftSide = ''

    for i in range(len(givenString)):
        leftSide += givenString[i]
        # print(f'LeftSide: {leftSide} Round {i+1} Repeats in rightSide {s.count(leftSide)} LeftSide length {len(leftSide)} RightSide length {len(givenString)} LeftSideLength * Repeats in rightSide {len(leftSide)*s.count(leftSide)}')

        matchFound = len(givenString) == len(leftSide) * s.count(leftSide)
        matchNotFound = not matchFound

        # Match found
        if matchFound:
            return len(leftSide)

        # Last round, no match
        isLastRound = ( i == len(givenString) - 1 )

        if matchNotFound and isLastRound:
            return len(givenString)






if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7
    print(find('asdkhgasdkhgö'))