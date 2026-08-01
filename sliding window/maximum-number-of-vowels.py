class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")

        curr = 0 
        for char in s[:k]:
            if char in vowels:
                curr += 1

        best = curr

        # now performing sliding window

        for r in range(k,len(s)):
            if best == k:
                return k

            if s[r] in vowels:
                curr += 1

            if s[r-k] in vowels:
                curr -= 1

            best = max(curr,best)
    
        return best
