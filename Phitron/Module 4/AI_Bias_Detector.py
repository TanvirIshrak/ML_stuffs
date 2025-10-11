let = list(input().upper().split())
a = let.count("A")
b = let.count("B")
if a*100/len(let)> 70 or b*100/len(let)>70:
    print("Biased Model")
else:
    print("Fair Model")








