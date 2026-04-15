nums=[2,7,11,15]
target=9
for i in nums:
    if target-i in nums:
        print("[%d,%d]" %(nums.index(i),nums.index(target-i)))
        break
