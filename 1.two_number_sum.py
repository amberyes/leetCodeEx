#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' leetCode01 '


__author__='Amber Ye'


def solution(nums, target) :



    if len(nums)<2:
        return
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]

"""   
    # 新建立一个空字典用来保存数值及其在列表中对应的索引
    dict1 = {}
    # 遍历一遍列表对应的时间复杂度为O(n)
    for i in range(0, len(nums)):
        # 相减得到另一个数值
        num = target - nums[i]
        # 如果另一个数值不在字典中，则将第一个数值及其的索引报错在字典中
        # 因为在字典中查找的时间复杂度为O(1)，因此总时间复杂度为O(n)
        if num not in dict1:
            dict1[nums[i]] = i
        # 如果在字典中则返回
        else:
            return [dict1[num], i]
    ## 存在的问题：相同的数字，新的数会替旧的数
"""


print(solution([1,5,5,4,],9))