 
#  Remove duplicates from a list


# Givin input
nums = [1,1,2]

# Remove the duplicate number using set and sort
num = sorted(set(nums))

# Find the rangr and replace the value
for i in range(len(num)):
    nums[i] = num[i]
    
# Output
     
print(len(num))
print(num)