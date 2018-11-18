import time
import hashlib

def get_hsh():
    now = str(time.time())
    now = now.replace('.', '')
    hsh = hashlib.sha512(now.encode()).hexdigest()
    return hsh
    
