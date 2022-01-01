res = []

def subsetsUtil(A, subset, index):
    global res
    print(*subset)
    if subset is not None:
        res.append(subset.copy())
    for i in range(index, len(A)):
         
        subset.append(A[i])
        subsetsUtil(A, subset, i + 1)
        subset.pop(-1)
    return
    
def subsets(A):
    global res
    res = []
    subset = []
     
    index = 0
    subsetsUtil(A, subset, index)
    return res.copy()

