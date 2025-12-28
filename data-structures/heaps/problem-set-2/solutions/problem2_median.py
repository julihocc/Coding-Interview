"""Problem2 - MedianMaintainingHeap tests (per-file)
"""
def solve():
    class MinHeap:
        def __init__(self): self.H=[None]
        def size(self): return len(self.H)-1
        def min_element(self): return self.H[1]
        def insert(self,elt):
            self.H.append(elt); idx=len(self.H)-1
            while idx>1:
                p=idx//2
                if self.H[p]<=self.H[idx]: break
                self.H[p],self.H[idx]=self.H[idx],self.H[p]; idx=p
        def delete_min(self):
            if self.size()==0: return
            if self.size()==1: self.H.pop(); return
            self.H[1]=self.H.pop(); idx=1
            while True:
                l=2*idx; r=2*idx+1
                lval=self.H[l] if l<len(self.H) else float('inf')
                rval=self.H[r] if r<len(self.H) else float('inf')
                if self.H[idx]<=min(lval,rval): break
                child = l if lval<=rval else r
                self.H[idx],self.H[child]=self.H[child],self.H[idx]; idx=child

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

    class MedianMaintainingHeap:
        def __init__(self):
            self.hmin=MinHeap(); self.hmax=MaxHeap()
        def balance_heap_sizes(self):
            if self.hmax.size()>self.hmin.size():
                mv=self.hmax.max_element(); self.hmax.delete_max(); self.hmin.insert(mv); return
            if self.hmin.size()>self.hmax.size()+1:
                mv=self.hmin.min_element(); self.hmin.delete_min(); self.hmax.insert(mv)
        def insert(self,elt):
            if self.hmin.size()==0: self.hmin.insert(elt); return
            if self.hmax.size()==0:
                if elt>self.hmin.min_element(): cur=self.hmin.min_element(); self.hmin.delete_min(); self.hmin.insert(elt); self.hmax.insert(cur)
                else: self.hmax.insert(elt)
                return
            if elt>=self.hmin.min_element(): self.hmin.insert(elt)
            else: self.hmax.insert(elt)
            self.balance_heap_sizes()
        def get_median(self):
            if self.hmin.size()==0: raise AssertionError('empty')
            if self.hmax.size()==0: return self.hmin.min_element()
            if self.hmin.size()==self.hmax.size(): return (self.hmax.max_element()+self.hmin.min_element())/2.0
            return self.hmin.min_element()

    m=MedianMaintainingHeap()
    m.insert(1); assert m.get_median()==1
    m.insert(5); assert m.get_median()==3
    m.insert(2); assert m.get_median()==2
    m.insert(4); assert m.get_median()==3
    m.insert(18); assert m.get_median()==4
    m.insert(-4); assert m.get_median()==3
    m.insert(7); assert m.get_median()==4
    m.insert(9); assert m.get_median()==4.5
    return True
