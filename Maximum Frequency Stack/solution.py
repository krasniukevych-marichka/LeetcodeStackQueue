from collections import deque, defaultdict
class FreqStack:

    def __init__(self):
        self.freq_numb = defaultdict(int)      
        self.group_freq = defaultdict(deque)     
        self.maxfreq = 0

    def push(self, val: int) -> None:
        self.freq_numb[val]+=1
        f = self.freq_numb[val]
        self.group_freq[f].append(val)
        if f > self.maxfreq:
            self.maxfreq = f

    def pop(self) -> int:
        val = self.group_freq[self.maxfreq].pop()
        self.freq_numb [val] -= 1
        if not self.group_freq[self.maxfreq]:
            self.maxfreq -= 1
        return val
