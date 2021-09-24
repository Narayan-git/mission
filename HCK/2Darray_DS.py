def hourglassSum(arr):
    # Write your code here
    ms = -99
    for i in range(4):
        for j in range(4):
            t = sum(arr[i][j:j+3])
            
            m = arr[i+1][j+1]
            
            b = sum(arr[i+2][j:j+3])
            
            hg = t + m + b
            ms = max(hg, ms)
    return ms