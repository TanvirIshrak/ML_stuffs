N = int(input())
Yes_c=0
No_c=0
for i in range(N):
    vote = input()
    if vote == "YES":
        Yes_c+=1
    if vote == "NO":
        No_c+=1
if Yes_c>=No_c:
    print("ACCEPT")
else:
    print("REJECT")