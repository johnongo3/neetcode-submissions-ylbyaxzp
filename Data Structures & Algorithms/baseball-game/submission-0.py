class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for op in operations:
            if op not in ["+", "C", "D"]:
                scores.append(int(op))
            
            if op == "+":
                res = scores[len(scores) - 1] + scores[len(scores) - 2]
                scores.append(res)
            elif op == "C":
                scores.pop()
            elif op == "D":
                scores.append(scores[-1] * 2)
                    
        return sum(scores)