import secrets


# secrets.token_hex([nbytes=None]):
# Return a secure random text string in hexadecimal format.
# The string has n-bytes random bytes, and each byte is converted to two hex digits.
# If n-bytes are not supplied, a reasonable default gets used.

token = secrets.token_hex(64)
print(token)
# 429620bf304dc2dd85fe4d1e4e4056066ae0da5873210011afe6c11dbff979f54e3cc181e45610cc3ec54d7e76badd44bf0bc2119a822c3eeb13f36966b48ec5
