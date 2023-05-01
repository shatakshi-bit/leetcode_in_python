class Solution:
    def average(self, salary: List[int]) -> float:
        l=len(salary)
        s=0
        salary.sort()
        print(salary)
        for i in range(1,l-1):
            s=s+salary[i]
        return s/(l-2)
        
        
        