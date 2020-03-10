class Solution:
    def generateTheString(self, n: int) -> str:
        # note there are a few cases
        # first case is when n == 1
        # second case is when n is divisible by 2
        # third case is when n is not divisible by 2
        # there is easy solution where there's odd or even
        # also learned about bitwise & where returns smaller corresponding
        # i.e. if 4 & 28 then returns 4
        def _return_odd_pair(num):
            if not (num//2 % 2):
                return (num//2-1,num//2)
            else:
                return (num//2,num//2)
        answer = ""
        if n == 1:
            return "a"
        elif not n % 2:
            number_of_loops = _return_odd_pair(n)
            for i in range(number_of_loops[0]):
                answer += "bc"
            for j in range(number_of_loops[0], number_of_loops[1]):
                answer += "cc"
        else:
            answer = "a"
            number_of_loops = _return_odd_pair(n-1)
            print(number_of_loops)
            for i in range(number_of_loops[0]):
                answer += "bc"
            for j in range(number_of_loops[0],number_of_loops[1]):
                answer += "cc"
        return answer
        