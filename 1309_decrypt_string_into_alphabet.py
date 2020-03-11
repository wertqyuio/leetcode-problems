class Solution:
    def freqAlphabets(self, s: str) -> str:
        # read string backwards
        # whenever a # is encountered, then take in next two strings
        # otherwise read only single number
        idx = len(s)-1
        answer = ""
        while idx >= 0:
            if s[idx] == "#":
                answer += chr(ord("a")+int(s[idx-2:idx])-1)
                idx -= 2
            else:
                answer += chr(ord("a")+int(s[idx])-1)
            idx -= 1
        return answer[::-1]