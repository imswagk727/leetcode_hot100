# leetcode_hot100
 LeetCode_HOT 100 刷题笔记

1. twoSum两字之和
    i.暴力
        使用双循环 -> 如果 nums[i + j] == target 则return [i, j].  (j是i+1 右边一位)

    ii.哈希表  
        创建一个hashtable = dict().  边enumerate每个index和num，边查找target-num。若在hashtable中，则return[hashtable[target - num], index]. 若不在，就插入当前index和num到hashtable中hashtable[nums[i]] = i
        
