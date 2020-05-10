class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        answer = []
        idx = 0
        for num in range(1,n+1):
            answer.append("Push")
            if num == target[idx] and idx + 1 == len(target):
                return answer
            elif num != target[idx]:
                answer.append("Pop")
            else:
                idx += 1
        return answer
