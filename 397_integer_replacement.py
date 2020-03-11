class Solution:
    def integerReplacement(self, n: int) -> int:
        # intuitively want to make any n converge to 2^n because for shortest path
        # use binary representation
        # whenever n is even, then just divide by 2
        # whenever n is odd, then increment whenever next neighbor is 1
        # decrement whenever next neighbor is 0
        # i.e. count string length
        # count subgroups of non-leading 1's
        # ex. 10011010010 is 11 in length with 3 groups of non-leading 1's
        # almost right, except when no groups of 1's
        # next idea is that getting rid of leading 1 is cost-less
        # getting rid of single 1 costs 1 extra
        # getting rid of multiple 1 costs 2 extra
        # all that WAS NOT ENOUGH
        # final idea is that groups of 1 broken by a single zero actually have only
        # one "mulitple 1 payment" because it keeps getting passed.
        bin_n = str(bin(n))[2:]
        answer = len(bin_n)-1
        previous = 0
        print(bin_n, answer)
        for i in range(1,len(bin_n)):
            if bin_n[i]== "0" and previous:
                answer += 1
                previous -= 1
            elif bin_n[i] == "1" and previous < 2:
                previous += 1
        if previous:
            answer += previous
        return answer