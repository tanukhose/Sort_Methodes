# i=1
# while i<=100:
#     j=1
#     c=0
#     while j<=i:
#         if i%j==0:
#             c+=1
#         j+=1
#     if c==2:
#         print(i)
#     i+=1


# bubble sort#

# a=[1,4,2,7,6,9,8,5,3]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
#         j+=1
#     i+=1
# print(a)
#_______________________________________________________________

# selection sort #

# a=[1,4,2,7,6,9,8,5,3]
# n=len(a)
# i=0
# while i<(n):
#     m=i
#     j=i+1
#     while j<n:
#         if a[m]>a[j]:
#             m=j
#         j+=1
#     a[i],a[m]=a[m],a[i]
#     i+=1
# print(a)

# Quick sort#

# def partition(a,low,high):
#     pivot=a[low]
#     j=high+1

#     for i in range(low,high):
#         if a[j]<=pivot:
#             j-=1
#             a[i],a[j]=a[j],a[i]
#     a[low],a[j]=a[j],a[low]
#     return j
# # def quick_sort(a,low,high):
# #     if low<high:
# #         pi=partition(a,low,high)
# #         quick_sort(a,low,pi)
# #         quick_sort(a,pi+1,high)
# a=[1,4,2,7,6,9,8,5,3]
# print(partition(a))

# _____________________________________________________________

# #Merge Sort #

# def MergeSort(a):
#     if len(a)>1:
#         mid=len(a)//2
#         L=a[ :mid]
#         R=a[mid: ]
#         MergeSort(L)
#         MergeSort(R)
#         i=j=k=0
#         while i<len(L) and j <len(R):
#             if L[i]<=R[j]:
#                 a[k]=L[i]
#                 i+=1
#             else:
#                 a[k]=R[j]
#                 j+=1
#             k+=1
#         while i<len(L):
#             a[k]=L[i]
#             i+=1
#             k+=1
#         while j<len(R):
#             a[k]=R[j]
#             j+=1
#             k+=1
#             print(a)
# a=[1,4,2,7,6,9,8,5,3]
# MergeSort(a)


# #Insertion Sort

# a=[1,4,2,7,6,9,8,5,3]
# n=len(a)
# i=1
# while i<n:
#     key=a[i]
#     j=i-1
#     while j>=0 and key<a[j]:
#         a[j+1]=a[j]
#         j-=1
#     a[j+1]=key
#     i+=1
# print(a)

# _________________________________________________