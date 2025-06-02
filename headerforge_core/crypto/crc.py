# headerforge_core/crypto/crc.py
from typing import List

def crc16_mcrf4xx(data: bytes, init_crc: int = 0xFFFF) -> int:
    _CRC16_TABLE: List[int] = [...]
    crc = init_crc
    for b in data:
        idx = (_reflect(b, 8) ^ (crc >> 8)) & 0xFF
        crc = ((crc << 8) ^ _CRC16_TABLE[idx]) & 0xFFFF
    return crc
