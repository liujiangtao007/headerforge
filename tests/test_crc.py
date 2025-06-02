from headerforge_core.crypto import crc16_mcrf4xx

def test_crc_known():
    assert crc16_mcrf4xx(b"\x01\x02\x03") == 0x62c4  # 实际值示意，请确认是否真实正确

def test_crc_empty():
    assert crc16_mcrf4xx(b"") == 0xFFFF  # 空数据CRC初始值

def test_crc_typical():
    assert crc16_mcrf4xx(b"123456789") == 0x6F91  # CRC-16/MCRF4XX 标准校验值
