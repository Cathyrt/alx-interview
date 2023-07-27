## 0x04-utf8 validation

- The `0x04-utf8_validation` module provides a Python method `validUTF8(data)` that allows you to determine whether a given data set, represented as a list of integers, represents a valid UTF-8 encoding.
- UTF-8 is a widely used character encoding that can represent characters from various languages and is designed to be backward compatible with ASCII.
- This method checks if the sequence of bytes in the input data adheres to the UTF-8 encoding rules, ensuring that each character is represented by 1 to 4 bytes as specified. The function returns `True` if the data set is a valid UTF-8 encoding and `False` otherwise.
