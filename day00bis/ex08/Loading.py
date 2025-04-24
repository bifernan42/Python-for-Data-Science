def ft_tqdm(lst: range) -> None:
    """
        tqdm imitation
    """
    try:
        it_max = len(lst)
    except Exception as e:
        print("Bad Input")
    tqdm_pct = 0
    tqdm_bar = ""
    segment_size = float(64 / it_max)

    for it in range(0, it_max + 1):
        tqdm_pct = int(round(float(it / it_max) * 100))
        if it < it_max:
            tqdm_bar = "=" * int(segment_size * it) + ">"
            print(f"{tqdm_pct:3}%|[{tqdm_bar:64}]| {it}/{it_max}\r", end="", flush=True)
            yield lst[it]
        else:
            tqdm_bar = 63 * "="
            print(f"{tqdm_pct:3}%|[{tqdm_bar:63}>]| {it}/{it_max}", end="", flush=True)
