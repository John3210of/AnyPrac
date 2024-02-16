data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]

ext = "date"
val_ext = 20300501
sort_by = 'remain'

def filter_func(item, ext, val_ext):
    if ext == 'date':
        return item[1] <= val_ext
    elif ext == 'code':
        return item[0] <= val_ext
    elif ext == 'maximum':
        return item[2] <= val_ext
    elif ext == 'remain':
        return item[3] <= val_ext
    else:
        return True

def sort_func(item, ext):
    if ext == 'date':
        return item[1]
    elif ext == 'code':
        return item[0]
    elif ext == 'maximum':
        return item[2]
    elif ext == 'remain':
        return item[3]
    else:
        return None

def solution(data, ext, val_ext, sort_by):
    filtered_data = list(filter(lambda x: filter_func(x, ext, val_ext), data))
    sorted_data = sorted(filtered_data, key=lambda x: sort_func(x, sort_by))
    return sorted_data