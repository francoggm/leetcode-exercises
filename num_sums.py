
nums = [1,2,3,4]
nums_sums = []

for n, i in enumerate(nums):
    print(n, i)
    sum = 0
    if n == 0:
        nums_sums.append(i)
    else:
        for y in nums[:n+1]:
            print(y)
            sum += y
        nums_sums.append(sum)
  


    