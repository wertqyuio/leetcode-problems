class Solution:
    def countBits(self, num: int) -> List[int]:
        # at first glance, you want to simply initialize an array of zeroes and size-n
        # then, you increment every 2**n number by 1
        # but, the problem asks to do everything in one pass
        # note that there's a neat pattern that's reflected in code
        # below for ease of reading
        # about every 2**n numbers is the previous 2**n numbers + 1
        # ex. for n = 0, the answer is [0] and for n=1, the answer is [1]
        # for n = 2, the answer is [0,1] for the first two and [1,2] for the last 2
        # for n = 3, first half is [0,1,1,2] and [1,2,2,3] for latter half
        # for n = 4, [0,1,1,2,1,1,2,3] and [1,1,2,3,2,2,3,4] for each half
        answer = [0]
        base = len(answer)
        increment = 0
        while len(answer) < num+1:
            answer.append(answer[increment]+1)
            increment += 1
            if base == increment:
                base *= 2
                increment = 0
        return answer