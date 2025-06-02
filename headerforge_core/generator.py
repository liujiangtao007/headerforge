# headerforge_core/generator.py
from pathlib import Path
from .crypto import crc16_mcrf4xx, rsa_sign

class FlashHeaderGenerator:
    def __init__(self, layout: dict, cfg: dict):
        self.layout = layout
        self.cfg = cfg
        self.buffer = bytearray()

    def generate(self, image: bytes | None = None, privkey_pem: Path | None = None) -> bytes:
        self._pack_static_fields()
        if image:
            self._insert_hash(image)
        if privkey_pem:
            self._insert_signature(privkey_pem)
        self._insert_crc()
        return bytes(self.buffer)
