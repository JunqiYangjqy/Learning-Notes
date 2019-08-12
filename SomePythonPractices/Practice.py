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
    
    
    
    
                    
                    