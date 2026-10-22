#insert(), extractmax(), changekey(), getmax(), getsize()
class Maxheap:
    def __init__(self) -> None:
        self.nums=[]
        self.count=0

    def heapUp(self,ind):
        p=(ind-1)//2 #parent index
        if self.count>0 and self.nums[ind]>self.nums[p]: # if max send up
            #swap-
            self.nums[ind],self.nums[p]=self.nums[p],self.nums[ind]
            return self.heapUp(p)

    def heapDown(self,ind):
        li=ind
        lech=2*ind+1
        rech=2*ind+2
        if self.count>0 and self.nums[lech]>self.nums[ind]:
            li=lech
        if self.count>0 and self.nums[rech]>self.nums[ind]:
            li=rech
        return self.heapDown(li)

    def changekey(self,val,ind):#max heap
        if val<self.nums[ind]:
            self.nums[ind]=val
            self.heapDown(ind)
        else:
            self.nums[ind]=val
            self.heapUp(ind)
        return self.nums
    def get


        
