HEADER_CRC_POLY  = 0x8408          # CRC‑16/MCRF4XX (reflected)

def crc16_mcrf4xx(data: bytes, init_crc: int = 0xFFFF) -> int:
    poly = HEADER_CRC_POLY
    crc  = init_crc
    for b in data:
        crc ^= b
        for _ in range(8):
            crc = (crc >> 1) ^ poly if (crc & 1) else crc >> 1
    return crc & 0xFFFF