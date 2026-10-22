
'''
if nums[i]>val:
heapify down

else:
heapify up

MIN HEAP''' 
class Heaps:
    def Tree(self,nums,ind,val):
        if nums[ind]>val:
            nums[ind]=val
            self.heapifyDown(nums,ind)
        else:
            nums[ind]=val # put that value in the current index given
            self.heapifyUp(nums,ind)

    '''2 functions shpuld be at same level as Tree :
    heapifyDown is created only when Tree runs. It does not exist until Tree is called.
self.heapifyDown will fail. When Tree tries to call self.heapifyDown, Python looks for a method named heapifyDown on the Heaps object. 
It won't find it there because heapifyDown is a local variable inside Tree, not a method of the class.
Recursion breaks. 
Even if you called it as a local function heapifyDown(...), the recursive call inside it (self.heapifyDown(...)) would fail because self (the class instance) doesn't know about that local function.'''
    def heapifyDown(self,nums,ind):
        n=len(nums)
        largest_ind=ind # implicit way of the base case can do w/ if this return
        leftChild_ind=2*ind+1
        rightChild_ind=2*ind+2

        #check if left child exists and if ists gretater that largestindex
        if leftChild_ind<n and nums[leftChild_ind]>nums[largest_ind]: # we have already assinhed the value in the index that was given now to try to find its correct pos
            largest_ind=leftChild_ind
        if rightChild_ind<n and nums[rightChild_ind]>nums[largest_ind]: # if rightchild >left child which is now largestindex
            largest_ind=rightChild_ind
        if largest_ind!=ind: # NO ELIFS cuz check all condition independently
            #swap
            nums[ind],nums[largest_ind]=nums[largest_ind],nums[ind]
            # recursive call
            self.heapifyDown(nums,largest_ind)



    def heapifyUp(self,nums,ind):
        parentInd=(ind-1)//2 # go up to the parent of the current child in the array its this way
        if ind>0 and nums[ind]>nums[parentInd]: #ind> 0 means its dowm
            #swap
            nums[ind],nums[parentInd]=nums[parentInd],nums[ind]
            self.heapifyUp(nums,parentInd)
        return nums