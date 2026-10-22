class heaps:
    def __init__(self) -> None:
        self.arr=[]
        self.count=0
#---------------------------
    def heapUp(self,i):
        # p=(i-1)//2 when wile inside while loop
        while i>0:
            p=(i-1)//2
            if self.arr[p]>self.arr[i]:
                self.arr[p],self.arr[i]=self.arr[i],self.arr[p]
                self.heapUp(p)

    def heapDown(self,i):
        si=i 
        lech=2*i+1
        rech=2*i+2

        if lech<self.count and self.arr[lech]<self.arr[si]: #> chooeses the larger child
            si=lech
        if rech<self.count and self.arr[rech]<self.arr[si]:
            si=rech
        if si!=i:
            #swap
            self.arr[si],self.arr[i]=self.arr[i],self.arr[si]
            #call func
            self.heapDown(si)
#-----------------------------------------
    def initialize(self):
        self.arr.clear()
        self.count=0
        

    def insert(self,key): # imagine it is in arr 
        self.arr.append(key)
        self.count+=1
        self.heapUp(self.count-1) # cuz it will append at last that whats append means
        
        return self.arr

    def changekey(self,ind,newkey): # we are doing this for min heap so first min heap
        if newkey<self.arr[ind]:
            self.arr[ind]=newkey
            self.heapUp(ind)
        else:
            self.arr[ind]=newkey
            self.heapDown(ind)
        return self.arr

    def extractmin(self):
        # swap index 0 element with last element and heap it up if small
        if self.count>0:
            self.arr[0],self.arr[len(self.arr)-1]=self.arr[len(self.arr)-1],self.arr[0]
            ele=self.arr.pop()
            self.count-=1
            self.heapDown(0)
        else:
            return None
        return ele

    def isEmpty(self): # is a ques
        return self.count==0

    def getMin(self):
        return self.arr[0] if self.count>0 else None

    def heapSize(self):
        return self.count
    
def main():
    heap = heaps()
    heap.initialize()

    heap.insert(4)
    print("Inserted 4")
    heap.insert(5)
    print("Inserted 5")
    heap.insert(10)
    print("Inserted 10")

    print(f"Min = {heap.getMin()}")
    print(f"Size = {heap.heapSize()}")
    print(f"Is empty = {heap.isEmpty()}")

    print("Extracting min")
    heap.extractmin()

    print("Changing index 0 to 10")
    heap.changekey(0, 10)

    print(f"Min = {heap.getMin()}")



if __name__ == "__main__":
    main()
'''
new value smaller
       ↓
needs to move UP

new value larger
       ↓
needs to move DOWN
'''