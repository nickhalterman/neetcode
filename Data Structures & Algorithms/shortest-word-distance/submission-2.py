class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        word1Index = -1
        word2Index = -1

        minDistance = len(wordsDict)

        for i, r in enumerate(wordsDict):
            if word1 == r:
                word1Index = i
            elif word2 == r:
                word2Index = i

            if word1Index != -1 and word2Index != -1:
                minDistance = min(minDistance, abs(word1Index - word2Index))

        return minDistance