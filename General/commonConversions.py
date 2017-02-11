def u_int_conversion(x, num_bits):
    msb = x >> (num_bits - 1)

    if msb:
        mask = (2**num_bits) - 1
        ones_comp = -1 * (x ^ mask)
        twos_comp = -1 * ((x ^ mask) + 1)
        signed_mag = -1 * (x & (mask >> 1))
    else:
        ones_comp, twos_comp, signed_mag = x, x, x

    return [ones_comp, twos_comp, signed_mag, hex(x), bin(x)]
