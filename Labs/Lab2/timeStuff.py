# timeStuff.py
"""Times various algorithms with different big-oh notation"""
from time import perf_counter

def main():

    timingResults = [[],[],[],[],[],[],[]]

    for n in range(0,51, 10):
        # Algorithm 0
        start = perf_counter()
        result = 0
        for i in range(10000000):
            result = result + i
        # end for
        end = perf_counter()
        runTime = end - start
        print("Algorithm 0: n %2d is %.6f sec." % (n, runTime))
        timingResults[0].append((n,runTime))

    print("-----------------------------------------------")

    for n in range(0,51, 10):
        # Algorithm 1
        start = perf_counter()
        result = 0
        for i in range(n):
            result = result + i
        # end for
        end = perf_counter()
        runTime = end - start
        print("Algorithm 1: n %2d is %.6f sec." % (n, runTime))
        timingResults[1].append((n,runTime))

    print("-----------------------------------------------")
    
    for n in range(0,51, 10):
        # Algorithm 2
        start = perf_counter()
        result = 0
        for r in range(n):
            c = n
            while c > 1:
                result = result + c
                c = c // 2
            # end while
        # end for
        end = perf_counter()
        runTime = end - start
        print("Algorithm 2: n %2d is %.6f sec." % (n, runTime))
        timingResults[2].append((n,runTime))

    print("-----------------------------------------------")
    
    for n in range(0,51, 10):
        # Algorithm 3
        start = perf_counter()
        result = 0
        for r in range(n):
            for c in range(n):
                result = result + c
            # end for
        # end for
        end = perf_counter()
        runTime = end - start
        print("Algorithm 3: n %2d is %.6f sec." % (n, runTime))
        timingResults[3].append((n,runTime))

    print("-----------------------------------------------")
    
    for n in range(0,51, 10):
        # Algorithm 4
        start = perf_counter()
        result = 0
        for r in range(n):
            for c in range(n):
                for d in range(n*n*n):
                    result = result + d
                # end for
            # end for
        # end for
        end = perf_counter()
        runTime = end - start
        print("Algorithm 4: n %2d is %.6f sec." % (n, runTime))
        timingResults[4].append((n,runTime))

    print("-----------------------------------------------")
    
    for n in range(0,31, 10):
        # Algorithm 5
        start = perf_counter()
        result = 0
        i = 0
        while i < 2**n:
            result = result + i
            i += 1
        # end while
        end = perf_counter()
        runTime = end - start
        print("Algorithm 5: n %2d is %.6f sec." % (n, runTime))
        timingResults[5].append((n,runTime))

    
main()
