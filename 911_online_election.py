class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.votes = defaultdict(int)
        self.record = [[0,persons[0]]]
        self.votes[persons[0]] = 1
        max_vote = [1,persons[0]]
        for idx in range(1,len(persons)):
            if persons[idx] not in self.votes:
                self.votes[persons[idx]] = 1
            else:
                self.votes[persons[idx]] += 1
            if self.votes[persons[idx]] >= max_vote[0]:
                max_vote = [self.votes[persons[idx]], persons[idx]]
                if persons[idx] != self.record[-1][1]:
                    self.record.append([times[idx],persons[idx]])
        self.record.append([10**9+1,self.record[-1][1]])
        print(self.record)

    def q(self, t: int) -> int:
        def _binary_search(start, end):
            midpt = (start+end)//2

            if self.record[midpt][0] == t or start > end - 2:
                return self.record[midpt][1]
            elif self.record[midpt][0] > t:
                return _binary_search(start, midpt)
            else:
                return _binary_search(midpt, end)
        
        return _binary_search(0, len(self.record))
            
        return idx
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
