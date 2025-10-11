nums = list(map(float,input().split()))

total=sum(nums)

avg = total/len(nums)
if avg<85:
    print("Dark Image")
elif 85<=avg<=170:
    print("Normal Image")
elif avg>170:
    print("Bright Image")