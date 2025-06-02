from typing import List

def _reflect(value: int, width: int) -> int:
    result = 0
    for i in range(width):
        if (value >> i) & 1:
            result |= 1 << (width - 1 - i)
    return result

def _generate_table() -> List[int]:
    poly = 0x1021
    table = []
    for byte in range(256):
        crc = byte << 8
        for _ in range(8):
            if crc & 0x8000:
                crc = ((crc << 1) ^ poly) & 0xFFFF
            else:
                crc = (crc << 1) & 0xFFFF
        table.append(crc)
    return table

_CRC16_TABLE = _generate_table()

def crc16_mcrf4xx(data: bytes, init_crc: int = 0xFFFF) -> int:
    crc = init_crc
    for b in data:
        rb = _reflect(b, 8)
        idx = ((crc >> 8) ^ rb) & 0xFF
        crc = ((crc << 8) ^ _CRC16_TABLE[idx]) & 0xFFFF
    return crc
