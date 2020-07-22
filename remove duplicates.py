def remove_dups(astring):
    accum = ""
    retval = ""
    for x in astring:
        if x not in accum:
            accum += x
            retval += x
    return retval

print(remove_dups("zduplicatesduplicatesz"))  