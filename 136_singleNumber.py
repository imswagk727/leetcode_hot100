# 异或运算XOR(^): 两数相同->返回0, 不同->返回1.
def singleNumber(nums):
    result = 0  # 初始结果
    for num in nums:
        result ^= num  # 使用异或运算(XOR)更新结果，相同元素异或会抵消
     
    return result

# 利用异或运算的有趣性质，对于同一个数进行两次异或运算会得到之前的数字。eg. x^a^a = x
# print(4^2^2)
# 所以结合这题，只有一个元素会出现一次，其余每个元素都出现两次，都会抵消为0，result就会得到那个数字。


nums1 = [2, 2, 1]
print(singleNumber(nums1))  # 1

nums2 = [4, 1, 2, 1, 2]
print(singleNumber(nums2))  # 4

nums3 = [1]
print(singleNumber(nums3))  # 1


