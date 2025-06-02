from headerforge_core.crypto import crc16_mcrf4xx
def test_crc_zero():
    assert crc16_mcrf4xx(b"") == 0xFFFF
def test_crc_known():
    assert crc16_mcrf4xx(b"\x01\x02\x03") == 0x29B1  # 举例
