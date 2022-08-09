'''
Tehtäväsi on selvittää, kuinka pitkä on lyhin merkkijono, jota toistamalla voidaan muodostaa annettu merkkijono.
Esimerkiksi kun merkkijono on abcabcabcabc, lyhin toistettava merkkijono on abc.
Merkkijono muodostuu merkeistä a–z ja siinä on enintään 100 merkkiä.
'''


def find(s):
    givenString = [char for char in s]  # Right side
    givenStringLength = len(givenString)    # Right side length

    leftSide = ''

    for i in range(len(givenString)):
        leftSide += givenString[i]
        # print(f'LeftSide: {leftSide} Round {i+1} Repeats in rightSide {s.count(leftSide)} LeftSide length {len(leftSide)} RightSide length {len(givenString)} LeftSideLength * Repeats in rightSide {len(leftSide)*s.count(leftSide)}')

        # Can we build right just side by repeating left side?
        # Check and return a boolean
        matchFound = givenStringLength == len(leftSide) * s.count(leftSide)

        # We can't build right side just by repeating left side
        matchNotFound = not matchFound

        # Match found, we can build right just side by repeating left side
        if matchFound:
            return len(leftSide)

        # Have we reached last round?
        # Check and return a boolean
        isLastRound = ( i == givenStringLength - 1 )

        # Last round and last check, no match
        if matchNotFound and isLastRound:
            return givenStringLength


if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7