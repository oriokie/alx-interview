#!/usr/bin/env python3
"""
UTF-8 validation module
"""


def validUTF8(data):
    """
    Determines if the given data is valid UTF-8 encoded text.
    """
    def is_continuation(byte):
        """
        Returns True if the given byte is a continuation byte, False otherwise
        """
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        """ Get the current byte (ensuring we only
        use the 8 least significant bits)"""
        first_byte = data[i] & 0xFF

        if first_byte >> 7 == 0:  # 1-byte character (0xxxxxxx)
            i += 1
        elif first_byte >> 5 == 0b110:  # 2-byte character (110xxxxx 10xxxxxx)
            if i + 1 >= len(data) or not is_continuation(data[i + 1]):
                return False
            i += 2
        elif first_byte >> 4 == 0b1110:  # 3-byte (1110xxxx 10xxxxxx 10xxxxxx)
            if i + 2 >= len(data) or not is_continuation(data[i + 1]) \
                    or not is_continuation(data[i + 2]):
                return False
            i += 3
        elif first_byte >> 3 == 0b11110:  # 4-byte (11110xxx 10x 10x 10xxxxxx)
            if i + 3 >= len(data) or not is_continuation(data[i + 1]) or not \
                    is_continuation(data[i + 2]) \
                    or not is_continuation(data[i + 3]):
                return False
            i += 4
        else:
            return False  # Invalid start byte

    return True  # All characters are valid
