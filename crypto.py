# Transposition Cipher

# original:This_is_a_secret_message_that_i_want_to_transmit
# encrypted:hsi__ertmsaeta__att_rnmtti_sasce_esg_htiwn_otasi


def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
            charCount = charCount + 1
            cipherText = oddChars + evenChars
            return cipherText


def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:]
    oddChars = cipherText[:halfLength]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText


# write a stripSpaces(text function here

# write a caesarEncrypt(plainText, shift)
# write a caesarDecrypt(cipherText, shift)

# Encrypt:ymj itl yzwsji tzy yt gj f rtsxyjw(shift 5)
# Decrypt:The dog turned out to be a monster(shift 5)


def caesarEncrypt(cipherText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in cipherText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
            charCount = charCount + 1
            cipherText = oddChars + evenChars
            return cipherText


def caesarDecrypt(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:]
    oddChars = cipherText[:halfLength]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText
