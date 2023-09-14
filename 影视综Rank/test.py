import base64

def base64_encode(text):
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    encoded_text = encoded_bytes.decode('utf-8')
    return encoded_text

# 示例用法
plaintext = "Hello, World!"
encoded_text = base64_encode(plaintext)

print("原始文本：", plaintext)
print("加密后：", encoded_text)
