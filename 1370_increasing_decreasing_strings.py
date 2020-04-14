class Solution:
    def sortString(self, s: str) -> str:
        # sort all characters and record frequencies
        # then loop through frequency dictionary until answer string is
        # as long as original string
        frequencies = []
        for char in sorted(list(s)):
            if not len(frequencies) or frequencies[-1][0] != char:
                frequencies.append([char,1])
            else:
                frequencies[-1][1] += 1
        answer = []
        while len(answer) < len(s):
            for i in range(len(frequencies)):
                if frequencies[i][1]:
                    answer += [frequencies[i][0]]
                    frequencies[i][1] -= 1
            for j in range(len(frequencies)-1,-1,-1):
                if frequencies[j][1]:
                    answer += [frequencies[j][0]]
                    frequencies[j][1] -= 1
        
        return "".join(answer)