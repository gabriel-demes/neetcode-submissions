class Solution:
    def isAnagram(self, w1: str, w2: str) -> bool:
        if len(w1) != len(w2):
            return False

        letters = {}

        for letter in w1:
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
        
        for letter in w2:
            if letter not in letters:
                return False
            letters[letter] -= 1
            if letters[letter] < 0:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []

        for word in strs:
            found = False
            for group in anagrams:
                if self.isAnagram(group[0], word):
                    group.append(word)
                    found = True
                    break
            if found == False:
                anagrams.append([word])

        return anagrams
            











        