#!/usr/bin/env python3


import os
from hashlib import pbkdf2_hmac
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from config import AESConst


# AES key can be either 16, 24, or 32 bytes long.
# AES block size is always 16 bytes.


class AES_Encripton:
	
    def __init__(self, password: str) -> None:
        self._password = password
        self._key_iterations_count = AESConst.ITERATIONS_COUNT
        self._salt_size = AES.block_size
        self._salt = self._get_salt()
        self._encryption_key = self._get_key(self._salt)
        
    def _get_salt(self) -> bytes:
        salt = os.urandom(self._salt_size)
        return salt
         
    def _get_key(self, salt: bytes) -> bytes:
        key = pbkdf2_hmac("sha256", self._password.encode("utf-8"), salt, self._key_iterations_count)
        return key

    def encrypt(self, bytes_data: bytes) -> bytes:
        padded_bytes_data = pad(bytes_data, AES.block_size) 
        cipher = AES.new(self._encryption_key, AES.MODE_CBC)
        encrypted_bytes_data = cipher.encrypt(padded_bytes_data)
        encrypted_bytes_packet = cipher.iv + self._salt + encrypted_bytes_data  # type: ignore
        return encrypted_bytes_packet

    def decrypt(self, encrypted_bytes_packet: bytes) -> bytes:
        iv = encrypted_bytes_packet[:AES.block_size]
        salt = encrypted_bytes_packet[AES.block_size: AES.block_size + self._salt_size]
        encrypted_bytes_data = encrypted_bytes_packet[self._salt_size + AES.block_size:]
        decryption_key = self._get_key(salt) 
        cipher = AES.new(decryption_key, AES.MODE_CBC, iv=iv)
        padded_bytes_data = cipher.decrypt(encrypted_bytes_data)
        bytes_data = unpad(padded_bytes_data, AES.block_size)
        return bytes_data