#Easay
class Solution:
    def encode(self, word):
        return [ord(ch) for ch in word]
    
    def decode(self, encode):
        return "".join(chr(num) for num in encode)


#Complex
class EncodeDecode:
    def encoder(self, word):
        encode = []
        for ch in word:
            encode.append(ord(ch))
            encode.append(ord("?"))
        return encode
    
    def decoder(self, encode):
        decode = ""
        for i in range(0, len(encode), 2):
            decode += chr(encode[i])
        return decode

#==============method two====================
def encode(arr):
    encoded = ""
    for st in arr:
        encoded += str(len(st))
        encoded += "#"
        encoded += st
    return encoded

def decode(s):
    decoded = []
    i = 0
    n = len(s)
    while i < n:
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        decoded.append(s[j+1:j+1+length])
        i = j + 1 + length

    return decoded

if __name__ == "__main__":
    s = ["hello", "world"]
    encoded = encode(s)
    decoded = decode(encoded)
    result = ""
    for i in range(len(decoded)):
        print(decoded[i], end=" ")







