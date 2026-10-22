'''class Solution:
    def extractMax(self):
        if not None:
            return H[0] # will be at top for max element.
        else:
            return None
            
        #to fill the void, swap the last element to 0
        H[0]=H[len(H)-1]
        #now shift it down
        shiftdown(0)
        
        def shiftdown(self,i):
            n=len(arr)
            li=i
            lech=2*i+1
            rech=2*i+2
            
            if lech<n and H[li]<H[lech]:
                li=lech
            if rech<n and H[li]<H[rech]:
                li=rech
            if li!=i:
                H[li],H[i]=H[i],H[li]
                return self.shiftdown(li)'''
#The function should be outside not nested,
# and wrong way to return max need to return at last cuz first pop the last element that swapped and tstore the maximum in max, then shift down


class Solution:
    def shiftDown(self, i):
        while True:
            largest = i

            left = 2 * i + 1
            right = 2 * i + 2

            if left <= s and H[left] > H[largest]:
                largest = left

            if right <= s and H[right] > H[largest]:
                largest = right

            if largest == i:
                break

            H[i], H[largest] = H[largest], H[i]

            i = largest

    def extractMax(self):
        global s, H

        maximum = H[0]

        H[0] = H[s]

        s -= 1

        self.shiftDown(0)

        return maximum

