import math
import re
from itertools import count

def coprime_check(f):
    def _f(*args, **kwargs):
        if math.gcd(args[1], 26) > 1:
            raise ValueError("a and m must be coprime.")
        return f(*args, **kwargs)
    return _f

def E(a, b, num):
    return ((a * (ord(num) - ord('a')) + b) % 26)

def find_a(num):
    for i in count(0):
        if num * i % 26 == 1:
            return i

@coprime_check
def encode(plain_text, a, b):
    # E = (a*x + b) % 26
    res = ''
    plain_text = re.sub(r'[^\w]', '', plain_text.lower())
    print(''.join(c.lower() for c in plain_text if c.isalnum()))
    for t in plain_text:
        if not t.isdigit():
            res += chr(E(a, b, t) + ord('a'))
        else:
            res += t
    return ' '.join([res[i: i + 5] for i in range(0, len(res), 5)])


@coprime_check
def decode(ciphered_text, a, b):
    res = ''
    ciphered_text = re.sub(r'[^\w]', '', ciphered_text.lower())
    # D(E) = (a^-1 * (E - b)) % 26
    for c in ciphered_text:
        if not c.isdigit():
            res += chr((find_a(a) * (ord(c) - ord('a') - b) % 26) + ord('a'))
        else:
            res += c
    return res

print(encode('ybty?jhd---fs!123    !uhdfs', 11, 15))
