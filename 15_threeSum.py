from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    n = len(nums)

    # 步骤 1：对输入数组进行升序排序
    nums.sort()  # 对数组进行排序是使用双指针法的前提
    ans = list()  # 存储结果三元组的列表

    # 步骤 2：枚举三元组中的第一个元素 'a'
    for first in range(n):
        # 跳过重复的 'a' 值
        if first > 0 and nums[first] == nums[first - 1]:
            continue  # 通过跳过重复的 'a' 值避免重复

        third = n - 1  # 初始化 'third' 指针指向数组的最右端
        target = -nums[first]  # 计算剩余两个数的目标和

        # 步骤 3：枚举三元组中的第二个元素 'b'
        for second in range(first + 1, n):
            # 跳过重复的 'b' 值
            if second > first + 1 and nums[second] == nums[second - 1]:
                continue  # 通过跳过重复的 'b' 值避免重复

            # 步骤 4：使用双指针法调整 'second' 和 'third' 指针
            while second < third and nums[second] + nums[third] > target:
                third -= 1  # 如果当前和过大，向左移动 'third' 指针
            # 如果 'second' 和 'third' 指针交叉或相遇，退出循环
            if second == third:
                break

            # 步骤 5：检查当前三元组是否满足目标和的条件
            if nums[second] + nums[third] == target:
                ans.append([nums[first], nums[second], nums[third]])  # 找到满足条件的三元组

    return ans  # 返回有效三元组的列表


# 示例测试
nums1 = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums1))  # 输出: [[-1, -1, 2], [-1, 0, 1]]

nums2 = [0, 1, 1]
print(threeSum(nums2))  # 输出: []

nums3 = [0, 0, 0]
print(threeSum(nums3))  # 输出: [[0, 0, 0]]


