N = int(input())
target = float(input())

total =0.0
for i in range(N):
    loss = float(input())
    total+=loss

avg = total/N
if avg<=target:
    print("PASS")
else:
    print("RETRY")