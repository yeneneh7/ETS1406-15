text = "apple"

# Encode the string to bytes
encoded_text = text.encode()

print(encoded_text)  # Output: b'apple'


or 


text = "apple"

# Encode using UTF-16
utf16_text = text.encode("utf-16")

print(utf16_text)  # Output: b'\xff\xfea\x00p\x00p\x00l\x00e\x00'
