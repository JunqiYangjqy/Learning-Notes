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
    #Or utilise mathematical ways
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 负数和10，90，100等不是回文数
        if x < 0 or (x!=0 and x%10==0):
            return False
        # 0 is palindrome number；
        elif x == 0:
            return True
        # 其他情况， 分别计算出back和x的值， 判断。
        back = 0
        while x > back:
            back = back*10 + x%10
            x = x/10
        # 124421： x==back
        # 121: x==back/10
        return x==back or x==back/10
    
    #LeetCode: Roman to Integer
    #Quite hard
    #Others
    def romanToint(s):
        roman_dict = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        sum = 0
        for i in range(len(s)-1):
            if roman_dict[s[i]]<roman_dict[s[i+1]]:
                sum -= roman_dict[s[i]]
            else:
                sum += roman_dict[s[i]]
        return sum+roman_dict[s[-1]]
    #Integer to Roman
    def intToroman(num):
        num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X','IX','V','IV','I']
        res = ""
        for i in range(len(num_list)):
                while num>=num_list[i]:
                        num-=num_list[i]
                        res+=roman_list[i]
        return res
    
    #LeetCode: Longest Common Prefix
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        import os
        return os.path.commonprefix(strs)
    #Really Nice One
    #Utilising zip() function & the feature of Set
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if len(strs) == 0:
            return ""
        for each in zip(*strs):
            if len(set(each)) == 1:
                res += each[0]
            else:
                return res
        return res
    
    #LeetCode: Valid Parentheses
    #my stupid answer
    #my answer is wrong when the input is like '{[]}'
    def isValid(self, s: str) -> bool:
        if s=='':
            return True
        d={'(':'()','[':'[]','{':'[]'}
        n=len(s)
        if n<=1:
            return False
        for i in range(0,n,2):
            if s[i] not in d:
                return False
            if (s[i]+s[i+1]) == d[s[i]]:
                return True
            else:
                return False
            
    #The official answer, so amazing
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
    
    #LeetCode: Length of last word
    #my stupid answer
    def lengthOfLastWord(self, s: str) -> int:
        if len(s)==0 or s==" ":
            return 0
        ss=s.split( )
        if ss==[]:
            return 0
        n=len(str(ss[-1]))
        return n
    #Others
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(" ")[-1])

    #Swap the linked list
    class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head != None and head.next != None:
            next = head.next
            head.next = self.swapPairs(next.next)
            next.next = head
            return next
        return head
    
    #LeetCode: Plus One
    #Quite nice
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = 1
        for i in range(len(digits)-1, -1, -1):
            if flag == 1:
                digits[i] += 1
                if digits[i] >= 10:
                    digits[i] = 0
                else:
                    flag = 0
        if flag == 1:
            digits.insert(0,1)
        return digits
    
    #LeetCode: Climbing stairs
    #Anyway, it's a math problem
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        dp=[1,2]
        for i in range(2,n):
            dp.append(dp[i-1]+dp[i-2])
        return dp[n-1]
    
    #LeetCode: Remove Duplicates from Sorted Array
    #删除排序数组中的重复项
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        n = len(nums)
        while k < n:
            if nums[k] == nums[k - 1]:
                del nums[k]
                n -= 1
            else:
                k += 1
        return n
    """
    Or 
    n = len(nums)
        return n - len([nums.pop(i) for i in range(n -1, 0, -1) if nums[i] == nums[i - 1]])
    """
    
    #LeetCode: Remove Element
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        if n==0:
            return 0
        while n:
            if nums[n-1] == val:
                del nums[n-1]
                n -=1
            else:
                n-=1
        return len(nums)
    
    #LeetCode: implement strStr()
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        a=haystack.find(needle)
        return a
    
    """
    #In JAVA, we can use substring() function to match 
    #Example Java answer
        public int strStr(String haystack, String needle) {
        int res = -1;
        int len = needle.length();
        int lenhay = haystack.length();
        if ( lenhay < len )
            return -1;
        int star = 0 ;
        int end = len-1;
        while (end < lenhay){
             if (haystack.substring(star,end+1).equals(needle)){
                 return star;
             }
            end++;
            star++;
        }
        return -1;
    }
    Author：knightdax
    URL：https://leetcode-cn.com/problems/implement-strstr/solution/java-zi-fu-chuan-pi-pei-bi-jiao-jian-dan-de-fang-f/
    Source：LeetCode
    """
    
    #LeetCode: Search Insert Position
    #Seems my answer is really long
    #I used the bi-search as this is a sorted list. It costed 68ms and 14.8mb
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return -1
        if target in nums:
            return nums.index(target)
        else:
            n=len(nums)
            if nums[n-1]<target:
                return n
            elif nums[0]>target:
                return 0
            else:
                low = 0
                high = n-1
                insert_index=0
                if n>2:
                    while low < high-1:
                        mid = (low + high)//2

                        if nums[mid] == target:
                            insert_index == mid+1
                        elif nums[mid] > target:
                            high = mid
                            insert_index = high             
                        else:
                            low = mid
                            insert_index = low+1
                else:
                    if nums[0]>target:
                        insert_index=0
                    elif nums[1]<target:
                        insert_index=2
                    else:
                        insert_index=1
                return insert_index
            
    #A Java template for bi-search
    """       
            --------------------------------
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while(left <= right) {
            int mid = (left + right) / 2;
            if(nums[mid] == target) {
                return mid;
            } else if(nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
            --------------------------------
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length; // 注意
        while(left < right) { // 注意
            int mid = (left + right) / 2; // 注意
            if(nums[mid] == target) {
                // 相关逻辑
            } else if(nums[mid] < target) {
                left = mid + 1; // 注意
            } else {
                right = mid; // 注意
            }
        }
        // 相关返回值
        return 0;
    }
    """
    
    #LeetCode: Count and Say
    #Be honest, I don't like this question
    #Official Answer
    """
    具体思路
    先设置上一人为'1'
    开始外循环
    每次外循环先置下一人为空字符串，置待处理的字符num为上一人的第一位，置记录出现的次数为1
    开始内循环，遍历上一人的数，如果数是和num一致，则count增加。
    若不一致，则将count和num一同添加到next_person报的数中，同时更新num和count
    别忘了更新next_person的最后两个数为上一个人最后一个字符以及其出现次数！
    """
    def countAndSay(self, n: int) -> str:
        prev_person = '1'
        for i in range(1,n):
            next_person, num, count = '', prev_person[0], 1
            for j in range(1,len(prev_person)):
                if prev_person[j] == num:
                    count += 1
                else:
                    next_person += str(count) + num
                    num = prev_person[j]
                    count = 1
            next_person += str(count) + num
            prev_person = next_person
        return prev_person

    #LeetCode: Maximum Subarray
    #Just Brute it
    def maxSubArray(self, nums: List[int]) -> int:
        tmp = nums[0]
        maxvalue = tmp
        n = len(nums)
        for i in range(1,n):
            # 当当前序列加上此时的元素的值大于tmp的值，说明最大序列和可能出现在后续序列中，记录此时的最大值
            if tmp + nums[i]>nums[i]:
                maxvalue = max(maxvalue, tmp+nums[i])
                tmp = tmp + nums[i]
            else:
            #当tmp(当前和)小于下一个元素时，当前最长序列到此为止。以该元素为起点继续找最大子序列,
            # 并记录此时的最大值
                maxvalue = max(maxvalue, tmp, tmp+nums[i], nums[i])
                tmp = nums[i]
        return maxvalue
    
    #LeetCode: Merge Sorted Arrat
    #Java: arraycopy(); Python: sorted()
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2)
    
    """
    Java:
    public void merge(int[] nums1, int m, int[] nums2, int n) {
            System.arraycopy(nums2, 0, nums1, m, n);
            Arrays.sort(nums1);
            }
    
    Java 2:
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int len1 = m - 1;
        int len2 = n - 1;
        int len = m + n - 1;
        while(len1 >= 0 && len2 >= 0) {
            // 注意--符号在后面，表示先进行计算再减1，这种缩写缩短了代码
            nums1[len--] = nums1[len1] > nums2[len2] ? nums1[len1--] : nums2[len2--];
        }
        // 表示将nums2数组从下标0位置开始，拷贝到nums1数组中，从下标0位置开始，长度为len2+1
        System.arraycopy(nums2, 0, nums1, 0, len2 + 1);
    }

Author：guanpengchn
URL：https://leetcode-cn.com/problems/merge-sorted-array/solution/hua-jie-suan-fa-88-he-bing-liang-ge-you-xu-shu-zu-/
    """
    #Double Pointers Solution
    def mergeArray(self, nums1, m, nums2, n):
        # Make a copy of nums1.
        nums1_copy = nums1[:m] 
        nums1[:] = []
        # Two get pointers for nums1_copy and nums2.
        p1 = 0 
        p2 = 0
        
        # Compare elements from nums1_copy and nums2
        # and add the smallest one into nums1.
        while p1 < m and p2 < n: 
            if nums1_copy[p1] < nums2[p2]: 
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        # if there are still elements to add
        if p1 < m: 
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]

    #LeetCode: Sqrt(x)
    #Great answer
    def mySqrt(self, x: int) -> int:
        # 为了照顾到 0 把左边界设置为 0
        left = 0
        # 为了照顾到 1 把右边界设置为 x // 2 + 1
        right = x // 2 + 1
        while left < right:
            # 注意：这里一定取右中位数，如果取左中位数，代码可能会进入死循环
            # mid = left + (right - left + 1) // 2
            mid = (left + right + 1) >> 1
            square = mid * mid

            if square > x:
                right = mid - 1
            else:
                left = mid
        # 因为一定存在，因此无需后处理
        return left
#Author: liweiwei1419
#URL: https://leetcode-cn.com/problems/sqrtx/solution/er-fen-cha-zhao-niu-dun-fa-python-dai-ma-by-liweiw/

    #LeetCode: The Same Tree
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # p q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)
                    
                    