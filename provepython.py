
x=1233
# initialize a variable that will store the reversed number
reverse_num = ''
num_string = str(x)
        #start a for loop to reverse the number
for i in range(len(num_string)):
            #add the current digit to the start of the reversed number
            reverse_num = num_string[i] + reverse_num 
            print(reverse_num)
            
print(reverse_num)

# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:   
#         dummy = temp = ListNode(0)
#         while l1 != None and l2 != None: #1

#             if l1.val < l2.val: #2
#                 temp.next = l1 #3
#                 l1 = l1.next #4
#             else: 
#                 temp.next = l2
#                 l2 = l2.next
#             temp = temp.next
#         temp.next = l1 or l2  #5
#         return dummy.next #6

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix =""

        # for str_0 in strs:
        #     print(str_0)

        #print(strs.sort())

        for i in range(len(strs[0])):
            print(strs[0],strs[-1])
            print(strs[0][i],strs[-1][i])
            if strs[0][i]==strs[-1][i]:
                prefix = prefix + strs[0][i]
            else:
                break
        
        return prefix

obj = Solution()
strs = ["cir", "car"]
strs1 = ["flight", "flower", "flow"]

#print(obj.longestCommonPrefix(strs1))
    
dogs = []
dogs.append('willie')
dogs.append('hootz')
dogs.append('peso')
dogs.append('goblin')
for dog in dogs:
 print("Hello " + dog + "!")
print("I love these dogs!")
print("\nThese were my first two dogs:")
old_dogs = dogs[:2]
for old_dog in old_dogs:
 print(old_dog)
del dogs[0]
dogs.remove('peso')
print(dogs)
    