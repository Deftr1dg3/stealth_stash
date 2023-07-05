#!/usr/bin/env python3

import re
from dataclasses import dataclass
from typing import NamedTuple
from random import choice, shuffle
from string import ascii_uppercase, ascii_lowercase, digits, punctuation

punctuation = punctuation.replace("'", "")
punctuation = punctuation.replace('"', "")
punctuation = punctuation.replace("[", "")
punctuation = punctuation.replace("]", "")
punctuation = punctuation.replace("\\", "")

class StrengthSpecification(NamedTuple):
    uppercase: int 
    lowercase: int 
    digit: int
    special_symbol: int
    length: int
     
@dataclass
class PasswordStrength:
    STRONG = StrengthSpecification(uppercase=2, lowercase=3, digit=2, special_symbol=1, length=12)


class ValidatePassword:
    def __init__(self) -> None:
        self._uppercase = ".*[A-Z]"
        self._lowercase = ".*[a-z]"
        self._digit = ".*[0-9]"
        self._special_symbol = f".*[{','.join(list(punctuation))}]"
        
    def _gen_regex(self, spec: StrengthSpecification) -> str:
        upper = self._uppercase * spec.uppercase
        lower = self._lowercase * spec.lowercase
        digit = self._digit * spec.digit
        symbol = self._special_symbol * spec.special_symbol
        total_length = ".{" + f"{spec.length}," + "}"
        rgx = rf"^(?={upper})(?={lower})(?={digit})(?={symbol}){total_length}$"
        return rgx
        
    def _validate_password(self, password: str):
        spec = PasswordStrength.STRONG
        r = self._gen_regex(spec) 
        print(r)
        rgx = re.compile(r)
        result = re.match(rgx, password)
        print(result)
        

v = ValidatePassword()
p = "12A3g!Mnn5kn"
v._validate_password(p)


