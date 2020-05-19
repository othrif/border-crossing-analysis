#-----------------------------------------------------------------------------------------
# Check if a key exists in a dictionary, if not create it and initialize it to val
# if it exists, add val to its content
#-----------------------------------------------------------------------------------------
def checkKey(dict, key, val):
    if key not in dict:
        dict[key] = val
    else:
        dict[key] += val

#-----------------------------------------------------------------------------------------
# Calculates difference in months
#-----------------------------------------------------------------------------------------
def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

