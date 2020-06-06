class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        answer = []
        for num in candies:
            answer.append((num+extraCandies)>=max_candies)
        return answer
