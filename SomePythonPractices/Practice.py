# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 22:48:24 2019

@author: Jarry
"""

class Solution:
    #1. Replace all the ' ' is a string with %20
    # s is source string
    def replaceSpace(self, s):
        self.s=s
        a=[]
        for i in s:
            if i==' ':
                a.append('%20')
            else:
                a.append(i)
        return ''.join(a)
    
    #2. Output the occurance of each character in a string
    def countOccurance(str):
        count={}
        for i in str:
            count[i]=str.count(i)
        return count
    
    #3.Find a specific number in an array
    def targetFind(target, array):
        n=len(array)
        if n==0:
            return 0
        else:
            for i in range(n):
                if target in array[i]:
                    print("Found the target")
                    return target
                else:
                    print("No such number")
                    
    #Or 
    def targetFindNew(target,array):
        if len(array)==0:
            print("The array cannot be empty")
            return 0
        else:
            rown=len(array)
            coln=len(array[0])
            startrow=0
            startcol=coln-1
            while startrow<=rown-1 and startcol>=0:
                if array[rown][startcol]==target:
                    print("Found the number")
                    return True,target
                elif array[rown][startcol]<target:
                    startrow += 1
                    print("Move to next row: "+startrow)
                elif array[rown][startcol]>target:
                    rown -= 1
                else:
                    print("No such number")
                    return False
                
    #4. Print linked list from tail to head
    def printListFromTailToHead(self, listNode):
        # write code here
        answer = []    
        head = listNode
        while head:
            answer.append( head.val)
            head = head.next
        #or maybe use answer.reverse()
        return answer[::-1]
    
    #5. Give the preorder traversal and the in-order traversal of a binary tree
    #   please reconstruct the binary tree
    #   Recursive process
    #   前序第一个为root，通过中序遍历找到左右子树，然后递归
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        root = TreeNode(pre[0])
        pos = tin.index(pre[0])
        root.left = self.reConstructBinaryTree( pre[1:1+pos], tin[:pos])
        root.right = self.reConstructBinaryTree( pre[pos+1:], tin[pos+1:])
        return root
    
    #6. Fibonacci
    def recur_fibo(n):
        if n <= 1:
            return n
        else:
            return(recur_fibo(n-1) + recur_fibo(n-2))  
    #or
    def Fibonacci(self, n):
        # write code here
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return a
    #or
    def newFibonacci(self, n):
        # write code here
        self.n=n
        value=[0,1]
        if n>0 and n<=1:
            return n
        elif n<=39:
            for i in range(2,n+1):
                value.append(value[i-1]+value[i-2])
            #value= Fibonacci(n-1)+Fibonacci(n-2)
            return value[n]
    
    # LeetCode Two Sum
    #my stupid version
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        answer=[]
        for i in range(n):
            a=nums
            for j in range(n):
                if nums[i]+a[j]==target and i!=j:
                    if i<j:
                        answer=[i,j]
                    else:
                        answer=[j,i]
        return answer
    #Use hashmap (dict in python)
    #求差值、把差值存进字典里作为键、索引作为值，第一次循环理解：d[7]=0 即字典d={7:0}，
    #表示为索引0需要数组里值为7的元素配对。 if 判断是否为前面元素所需要配对的值 ， 
    #是则返回两个索引值。（补充：nums[x] in d  是判断值是否在字典某个key里面）
    class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """           
        n = len(nums)
        #创建一个空字典
        d = {}
        for x in range(n):
            a = target - nums[x]
            #字典d中存在nums[x]时
            if nums[x] in d:
                return d[nums[x]],x
            #否则往字典增加键/值对
            else:
                d[a] = x
        #边往字典增加键/值对，边与nums[x]进行对比
    
    #Leet Code: reverse integer
    #my stupid answer used 60ms and 14mb 
    def reverse(self, x: int) -> int:
        self.x=x
        if -10<x<10:
            return x
        if x>=10:
            strx=str(x)
            strx=strx[::-1]
            x=int(strx)
        else:
            strx=str(x)
            strx=strx[1:][::-1]
            x=int(strx)
            x=-x
        return x if -2**31 < x < 2**31 - 1 else 0
    
    #Leet Code: Palindrome Number
    #Simple one
    def isPalindrome(self, x: int) -> bool:
        strx=str(x)
        if strx[::]==strx[::-1]:
            return True
        else:
            return False
    
                    
                    