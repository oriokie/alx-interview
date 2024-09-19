#!/usr/bin/python3
"""
UTF-8 validation module
"""


def validUTF8(data):
    """
    Determines if the given data is valid UTF-8 encoded text.
    UTF-8 encoding uses specific patterns:
    1. 1-byte character: The first bit is 0 (e.g., 0xxxxxxx).
    2. Continuation byte: The first two bits are 10 (e.g., 10xxxxxx).
    3. n-byte character: The first n bits are 1 followed by a 0
       (e.g., 1110xxxx).
    """
    def is_continuation(byte):
        """
        Returns True if the given byte is a continuation byte, False otherwise

        A continuation byte in UTF-8 starts with the binary pattern 10xxxxxx,
        which means the two most significant bits must be 10.

        Bitwise AND (&): The result is 1 if both bits are 1, and 0 otherwise
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
            return False  # Invalid UTF-8 character

    return True  # All characters are valid
