#!/usr/bin/env python3


import os
from hashlib import pbkdf2_hmac
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode


# AES key can be either 16, 24, or 32 bytes long.
# AES block size is always 16 bytes.


class AES_Encripton:
	
    def __init__(self, password: str) -> None:
        self._password = password
        self._key_iterations_count = 100_000
        self._salt_size = AES.block_size
        self._salt = self._get_salt()
        self._encryption_key = self._get_key(self._salt)
        
    def _get_salt(self) -> bytes:
        salt = os.urandom(self._salt_size)
        return salt
         
    def _get_key(self, salt: bytes) -> bytes:
        key = pbkdf2_hmac("sha256", self._password.encode("utf-8"), salt, self._key_iterations_count)
        return key

    def encrypt(self, bytes_data: bytes) -> str:
        padded_bytes_data = pad(bytes_data, AES.block_size) 
        cipher = AES.new(self._encryption_key, AES.MODE_CBC)
        encrypted_bytes_data = cipher.encrypt(padded_bytes_data)
        encrypted_bytes_packet = cipher.iv + self._salt + encrypted_bytes_data  # type: ignore
        return b64encode(encrypted_bytes_packet).decode('utf-8')

    def decrypt(self, encrypted_str_packet: str) -> str:
        encrypted_bytes_packet = b64decode(encrypted_str_packet)
        iv = encrypted_bytes_packet[:AES.block_size]
        salt = encrypted_bytes_packet[AES.block_size: AES.block_size + self._salt_size]
        encrypted_bytes_data = encrypted_bytes_packet[self._salt_size + AES.block_size:]
        decryption_key = self._get_key(salt) 
        cipher = AES.new(decryption_key, AES.MODE_CBC, iv=iv)
        padded_bytes_data = cipher.decrypt(encrypted_bytes_data)
        bytes_data = unpad(padded_bytes_data, AES.block_size)
        return bytes_data.decode("utf-8")
        


if __name__ == "__main__":

    import json 

    a = AES_Encripton("pass")

    def enc():
        with open("zen.txt", "r") as f:
            str_data = f.read()
            
        json_data = json.dumps(str_data)
        bytes_data = json_data.encode("utf-8")

        edata = a.encrypt(bytes_data)

        with open("enc.kkdb", "w") as f:
            f.write(edata)

    def dec():
        with open("zen.txt", "r") as f:
            edata = f.read()
        try:
            json_data = a.decrypt(edata)
        except ValueError:
            print("The passwrod is incorrect !!!")
            exit(1)
        str_data = json.loads(json_data)

        print(str_data)

    # enc()
    dec()