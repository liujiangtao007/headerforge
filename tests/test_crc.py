from headerforge_core.crypto.crc import crc16_mcrf4xx

def test_crc_simple():
    data = b"123456789"
    assert crc16_mcrf4xx(data) == 0x6F91  # CRC-16/MCRF4XX of that input
