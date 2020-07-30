from ex import AESCipher

# 32文字のパスフレーズ(ランダムキー)
pass_phrase = 'WCWYmSP9eR9nhRidXBDCjMMfUsVfb4Ec'

cipher = AESCipher(pass_phrase)

# 暗号化
encryptText = cipher.encrypt('plain text')
print(encryptText)

#復号
plainText = cipher.decrypt(encryptText)
print(plainText)
