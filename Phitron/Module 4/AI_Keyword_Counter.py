from collections import Counter
lis = list(input().lower().split())
if len(lis)<=200:
    counter = Counter(lis)
    total = counter["ai"] + counter["data"]+ counter["model"]+ counter["train"]+ counter["neural"]+ counter["learn"]
    if total>=2 :
        print("AI Detected")
    else:
        print("Not AI Related")