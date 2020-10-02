'''
This is a type of divide and conquer algorithm which divides the search space into
3 parts and finds the target value based on the property of the array or list
(usually monotonic property).

Time Complexity  : O(log3 N)
Space Complexity : O(1)
'''
# import sys
#
# # This is the precision for this function which can be altered.
# # It is recommended for users to keep this number greater than or equal to 10.
# precision = 10
#
# # This is the linear search that will occur after the search space has become smaller.
# def lin_search(left, right, A, target):
#     for i in range(left, right+1):
#         if(A[i] == target):
#             return i
#
# # This is the iterative method of the ternary search algorithm.
# def ite_ternary_search(A, target):
#     left = 0
#     right = len(A) - 1;
#     while(True):
#         if(left<right):
#
#             if(right-left < precision):
#                 return lin_search(left,right,A,target)
#
#             oneThird = (left+right)/3+1;
#             twoThird = 2*(left+right)/3+1;
#
#             if(A[oneThird] == target):
#                 return oneThird
#             elif(A[twoThird] == target):
#                 return twoThird
#
#             elif(target < A[oneThird]):
#                 right = oneThird-1
#             elif(A[twoThird] < target):
#                 left = twoThird+1
#
#             else:
#                 left = oneThird+1
#                 right = twoThird-1
#         else:
#             return None
#
# # This is the recursive method of the ternary search algorithm.
# def rec_ternary_search(left, right, A, target):
#     if(left<right):
#
#         if(right-left < precision):
#             return lin_search(left,right,A,target)
#
#         oneThird = (left+right)/3+1;
#         twoThird = 2*(left+right)/3+1;
#
#         if(A[oneThird] == target):
#             return oneThird
#         elif(A[twoThird] == target):
#             return twoThird
#
#         elif(target < A[oneThird]):
#             return rec_ternary_search(left, oneThird-1, A, target)
#         elif(A[twoThird] < target):
#             return rec_ternary_search(twoThird+1, right, A, target)
#
#         else:
#             return rec_ternary_search(oneThird+1, twoThird-1, A, target)
#     else:
#         return None
#
# # This function is to check if the array is sorted.
# def __assert_sorted(collection):
#     if collection != sorted(collection):
#         raise ValueError('Collection must be sorted')
#     return True
#

# if __name__ == '__main__':
import sys
import random
from algorithms4.searches import ternary_search

# user_input = input('Enter numbers separated by coma:\n').strip()
# collection = [int(item) for item in user_input.split(',')]
collection=[random.randint(1,100) for i in range(100)]
collection.sort()
try:
    ternary_search.__assert_sorted(collection)
except ValueError:
    sys.exit('Sequence must be sorted to apply the ternary search')

# target_input = input('Enter a single number to be found in the list:\n')
# target = int(target_input)
target=25
result1 = ternary_search.ite_ternary_search(collection, target)
result2 = ternary_search.rec_ternary_search(0, len(collection)-1, collection, target)

if result2 is not None:
    print('Iterative search: {} found at positions: {}'.format(target, result1))
    print('Recursive search: {} found at positions: {}'.format(target, result2))
else:
    print('Not found')