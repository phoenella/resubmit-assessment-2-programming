def my_decryption(value):

    charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<,"
    encText = "".join([charSet[(charSet.find(c)-3)%95] for c in value])
    return encText
