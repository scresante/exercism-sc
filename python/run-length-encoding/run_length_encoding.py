import collections

def decode(string):
    for ch in string:
        if ch.isc

decom = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
decom2 = "WWWWWBWWWWBBBWWWWWWWBBBB"

def encode8(string):
    result = []
    count = 1
    for i, ch in enumerate(string):
        try:
            if ch == string[i+1]:
                count += 1
            elif ch != string[i+1]:
                if count > 1:
                    res = str(count)+ch
                else:
                    res = ch
                count = 1
                # print(res)
                result.append(res)
        except IndexError:
            if ch != string[i-1]:
                res = ch
            else:
                res = str(count) + ch
            # print(res)
            result.append(res)
    return result


def encode(string):
    last, *string = string
    count = 0
    for i,ch in enumerate(string):
        if i == len(string)-1:
            if ch != last:
                print(f'{count+1}{last}{ch}',end='')
            else:
                print(f'{count+2}{last}',end='')
            continue
        if ch == last:
            count += 1
            continue
        print(f'{count+1}{last}',end='') if count else print(last,end='')
        count = 0
        last = ch
    print()
encode(decom2)
