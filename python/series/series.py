def slices(series, length):
    if not (0 < int(length) <= len(series)):
        raise ValueError(f"Length needs to be in [1,{len(series)}], you asked for {length} which lies outside this range.")
    return [ series[i:i+int(length)] for i in range(1+len(series)-int(length)) ]



