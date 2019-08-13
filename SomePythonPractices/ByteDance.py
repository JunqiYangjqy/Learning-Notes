# -*- coding: utf-8 -*-

#Use Singly linked lists to represent decimal numbers
#Such as 1->2->3-4 = 1234 in decimal
#add to numbers and output the result
#the data structure is Linked List ONLY
#this solution was written by 「壹Sir」from CSDN, following the CC 4.0 by-sa
#URL:https://blog.csdn.net/Thomas0713/article/details/83052257

class Node():
   # def __init__(self, dataval=None):
   #     self.dataval = dataval
   #     self.nextval = None
   #def __init__(self, data, p=0):
   #     self.data = data
   #     self.next = p
   value=None
   next=None
        
class LinkList(object):
    def __init__(self):
        self.head = None
    
    def getInput(nums):
        data=[]
        for i in nums:
            data.append(i)
        #print(data)
             
        #initialise the Linkedlist
    def initList(self, data):
        #创建头结点
        #self.head = Node(data[0])
        #p = self.head
        #list(data)
        link=Node()
        last_node=link
        data=str(data)
        #遍历data内的数据并创建结点建立链表
        for i in data:
            i = int(i)
            value = i
            node=Node()
            node.value = value
            last_node.next=node
            last_node = node
        return link
        """
        for i in data[1:]:
            node =Node(i)
            p.next = node
            p = p.next
        """
        
    def isEmpty(self):
        if self.head.next == 0:
            print ("Empty")
            return 1
        else:
            return 0
        
    def getLength(self):
        if self.isEmpty():
            exit(0)
        p = self.head
        len = 0
        while p:
            len += 1
            p = p.next
        return len

    #遍历链表
    def traveList(self):
        if self.isEmpty():
            exit(0)
        print ('\rLinked list\'s order is: ')
        p = self.head
        while p:
            print (p.data)
            p = p.next
    
    def print_link(link):
        """打印链表"""
        if not link:
            return None
        if link.value is None:
            node = link.next
        else:
            node = link
 
        s = ''
        while node:
            # print(type(node.value))
            ss = str(node.value) + '->'
            s += ss
            node = node.next
        print(s)
    
    def addLists(self,a,b):       
        #pass
        if not a:
            return None
        if a.value is None:
            node1=a.next
        else:
            node1=a
            
        if not b:
            return None
        if b.value is None:
            node2=b.next
        else:
            node2=b
            
        s1=''
        s2=''
        while node1:
            ss = str(node1.value)
            s1 =+ ss
            node2 = node2.next
        
        s2=int(s2)
        
        res = s1+s2
        res_link=self.initList(res)
        self.print_link(res_link)
    
        
linkedlist=LinkList()
a=linkedlist.initList(1234)
b=linkedlist.initList(34)
linkedlist.print_link(a)
linkedlist.print_link(b)
linkedlist.addLists(a,b)



        