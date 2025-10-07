def generate_demon_id(lot, method, demon, bus=0):
    key = ""
    if method == 0:
        key += "OG"
    elif method == 1:
        key += "WK"
    elif method == 2:
        key += "WKF"
    elif method == 3:
        key += "BS"
    elif method == 4:
        key += "BSF"
    elif method == 5:
        key += "M"

    key += "-L"
    key += str(lot)

    

    if bus!=0:
        key += "-B"
        key += str(bus)
    
    key += "-D"
    key += str(demon)

    return key