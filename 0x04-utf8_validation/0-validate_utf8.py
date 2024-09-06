#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """Check if the byte_list represents a valid UTF-8 encoding."""
    i = 0
    total_bytes = len(data)

    while i < total_bytes:
        if data[i] < 128:
            i += 1
            continue
        byte_count = 1
        leading_bit_mask = 1 << 6

        while data[i] & leading_bit_mask:
            byte_count += 1
            leading_bit_mask >>= 1

        if byte_count < 2 or byte_count > 4 or byte_count + i > total_bytes:
            return False
        byte_count += i
        i += 1
        while i < byte_count:

            if data[i] < 128 or data[i] > 191:
                return False
            i += 1

    return True
