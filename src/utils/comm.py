import string

def str_clear(txt):
    return txt.translate(str.maketrans('', '', string.punctuation))

def int_val(val):
    bl_int = isinstance(val, int)
    if bl_int:
        return val
    bl_str =  isinstance(val, str)
    if bl_str:
        bl_str_int = val.isdigit()
        if bl_str_int:
            return int(val)
    return None