"""Problem2 - MaxHeap tests (per-file)
"""
def solve():
    class MaxHeap:
        def __init__(self): self.H=[None]
        def size(self): return len(self.H)-1
        def max_element(self): return self.H[1]
        def bubble_up(self,i):
            if i==1: return
            p=i//2
            if self.H[p]>=self.H[i]: return
            self.H[p],self.H[i]=self.H[i],self.H[p]; self.bubble_up(p)
        def bubble_down(self,i):
            l=2*i; r=2*i+1
            lval=self.H[l] if l<len(self.H) else float('-inf')
            rval=self.H[r] if r<len(self.H) else float('-inf')
            if self.H[i]>=max(lval,rval): return
            child = l if lval>=rval else r
            self.H[i],self.H[child]=self.H[child],self.H[i]
            self.bubble_down(child)
        def insert(self,elt): self.H.append(elt); self.bubble_up(len(self.H)-1)
        def delete_max(self):
            if self.size()==0: return
            if self.size()==1: self.H.pop(); return
            self.H[1]=self.H.pop(); self.bubble_down(1)

    h=MaxHeap()
    h.insert(5); assert h.max_element()==5
    h.insert(2); assert h.max_element()==5
    h.insert(4); assert h.max_element()==5
    h.insert(-1); assert h.max_element()==5
    h.insert(7); assert h.max_element()==7
    h.delete_max(); assert h.max_element()==5
    h.delete_max(); assert h.max_element()==4
    h.delete_max(); assert h.max_element()==2
    h.delete_max(); assert h.max_element()==-1
    h.delete_max(); assert h.size()==0
    return True
