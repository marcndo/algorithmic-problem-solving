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






