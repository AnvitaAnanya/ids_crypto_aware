import string

def is_encrypted(data):
    # If most characters are non-printable, we assume it's encrypted
    printable = set(bytes(string.printable, 'ascii'))
    non_printables = sum(1 for byte in data if byte not in printable)
    ratio = non_printables / len(data)
    return ratio > 0.7  # More than 70% non-printable = encrypted
