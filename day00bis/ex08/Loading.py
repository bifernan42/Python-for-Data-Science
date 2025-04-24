import time as time

"""
100%|[===============================================================>]| 333/333
"""

def ft_tqdm(lst: range) -> None:
    """
        tqdm imitation
    """
    it_max = len(lst)
    #attention a la division par 0
    cpi = float(64 / it_max) # chars per iteration
    progress = 0
    it_count = 0
    tqdm_bar = ""
    stash = 0

    #if it_max = 0 => print 100%


#utiliser une range sur la range sera mieux
    for i in lst:
        time.sleep(0.05)
        it_count += 1
        progress = int(float(it_count / it_max) * 100)
        if cpi >= 1:
            tqdm_bar = "=" * int(cpi) * it_count
        else:
            stash += cpi
            tqdm_bar = "=" * int(stash) #formule pas mal, on le fera sans stash
        
        if i != lst[-1]:
            print(f"{progress}%|[{tqdm_bar:64}]| {it_count}/{it_max}\r", end="", flush=True)
        else:
            print(f"{progress}%|[{tqdm_bar:63}>]| {it_count}/{it_max}", end="", flush=True)
        #yield i
    print("\n")
    print("CHARS PER ITERATION :" + str(cpi))
    print("RESULT BAR          :" + tqdm_bar)
    print("BAR LEN             :" + str(len(tqdm_bar)))
    print("ITERATION COUNT     :" + str(it_count))
    print("PROGRESS            :" + str(progress))
    print("STASH               :" + str(stash))

#for i in ft_tqdm(range(22)):
 #   time.sleep(0.25)

ft_tqdm(range(250))
