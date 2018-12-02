"""Functionalities for manipulation of hexadecimal strings."""


def _to_base_ten(nums):
    # Ex; receive [15, 15, 15, 15], return 65535
    dec = 0
    for i, num in enumerate(reversed(nums)):
        if num == 1:
            dec += 16 ** i
        elif num > 1:
            dec += num * 16 ** i
    return dec


def _to_nums_list(chars):
    # Ex; receive [F, F, F, F], return [15, 15, 15, 15]
    nums = []
    for ch in chars:
        cd = ord(ch)
        if cd >= 65 and cd <= 70:
            nums.append(10 + (cd - 65))  # Append A .. F values (10 .. 15)
        elif cd >= 48 and cd <= 57:
            nums.append(int(ch))  # Append 0 .. 9
        else:
            return 0  # Invalid char
    return nums


def hex_to_dec(hex):
    """Convert a str representation of a hexadecimal to a decimal (int).
    
    Args:
        hex (str): The hexadecimal str. For readability,
            it can have as many whitespaces as you want
            and can be passed with the following prefixes;
            '0x', '&', '$', '#', '%'.
            Input examples: "0xFF", "FFFF FFFF", "&FF" 
            (not case-sensitive).

    Returns:
        int/str: The hexadecimal converted to decimal (int),
            or an error message (str). 
    """
    if not isinstance(hex, str): 
        return 'Error! Expected a str, received: {}'.format(type(hex))
    else:
        chars = list(hex.upper().lstrip('0X&$#% ').replace(' ', ''))
        nums = _to_nums_list(chars)
        if isinstance(nums, list):
            return _to_base_ten(nums)
        else:
            return 'Error! Invalid 0x str format.'