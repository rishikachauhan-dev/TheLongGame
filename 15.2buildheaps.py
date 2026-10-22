#MAX heaps?
arr=[1,8,7,16,11,12,2,4]
class Heaps:
    n=len(arr)
    def Tree(self,arr):
        # n=len(arr)
        for i in range (self.n//2 -1,-1,-1):
            self.heapdown(arr,i)

    def heapdown(self,arr,i):
        # n=len(arr)
        li=i
        lech=2*i+1
        rech=2*i+2

        if lech<self.n and arr[lech]>arr[li]:
            li=lech
        if rech<self.n and arr[rech]>arr[li]:
            li=rech
        if li!=i:
            #swap
            arr[li],arr[i]=arr[i],arr[li]
            #call func
            self.heapdown(arr,li)
#Tc-o(n)


#MIN Heaps------------------------------------------------------------------
nums=[10, 5, 20, 1, 8, 15]

class Heaps:
    n=len(nums)
    def Tree(self,nums):
        # n=len(arr)
        for i in range (self.n//2 -1,-1,-1):
            self.heapup(nums,i)

    def heapup(self,nums,i):
        p=(i-1)//2
        if i>0 and nums[p]>nums[i]:
            nums[i],nums[p]=nums[p],nums[i]
            self.heapup(nums,p)
    return nums


