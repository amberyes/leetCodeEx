#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' leetCode04 '


__author__='Amber Ye'


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 +nums2
        l=len(nums)
        i=int(l/2)
        list.sort(nums)

        if l%2 == 0:

            center=(nums[i-1]+nums[i])/2*1.0
        else:

            center=nums[i]*1.0
        return center


if __name__=="__main__":
    nums1=[int(n) for n in input().split()]
    nums2=[int(n) for n in input().split()]
    a=Solution()

    print(a.findMedianSortedArrays(nums1,nums2))