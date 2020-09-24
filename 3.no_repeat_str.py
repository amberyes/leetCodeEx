#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' leetCode03 '


__author__='Amber Ye'


class Solution:
    def noRepeat(self,s):
        """
        第一种
        # 记录最大长度
        maxLength=0

        # 判断字符串是否为空
        if s is None or len(s)==0:
            return maxLength

        # 记录每个出现字母及其下标
        dict={}

        # 存放每次循环子串长度
        temp=0
        # 记录最近重复位置+1
        start=0

        for i in range(len(s)):
            # 判断字母是否存在字典中，且下标大于等于重复位置
            if s[i] in dict and dict[s[i]]>=start:
                # 记录这样的字母
                start=dict[s[i]]+1
            # 本次循环中最大不重复子串长度
            temp=i-start+1
            # 把当前位置覆盖字典中的位置下标
            dict[s[i]]=i
            # 存放最大子串
            maxLength=max(maxLength,temp)
        return maxLength
        """

        """
        第二种
        max_length,n,temp=0,0,0
        dict={}
        for i,l in enumerate(s):
            if l in dict:
                if n>dict[l]:
                    temp=i-n
                else:
                    temp=i-dict[l]
                    n=dict[l]
            else:
                dict[l]=i
                temp+=1
            if max_length<temp:
                max_length=temp
        return max_length
        """
        dict,max_length,temp={},0,0
        for i,l in enumerate(s):
            if l in dict:
                max_length=max(max_length,i-temp)
                temp=max(temp,dict[l]+1)
            dict[l]=i
        return max(max_length, len(s) - temp)




if __name__=='__main__':
    str=input()
    a=Solution()
    print(a.noRepeat(str))
