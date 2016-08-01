#!/us/bin/env python
cipher_text = 'Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'

def decipher(cipher):
    plain_text = ''
    #The ascii value of A-Z is 65-90, a-z is 90-122
    #The shift is 13, that means cipher 'n' corresponding with plain text 'a'
    #TODO: implment it

    for letter in cipher:
        v = ord(letter)
        limits = [('a', 'z'), ('A', 'Z')]
        for pair in limits:
            if ord(pair[0]) <= ord(letter) <= ord(pair[1]):
                v = v-13
                if v < ord(pair[0]):
                    v += 26
                break
        plain_text += chr(v)

    return plain_text



if __name__ == '__main__':
    plain_text = decipher(cipher_text)
    print ("The cipher text: %s" % cipher_text)
    print ("The plain  text: %s" % plain_text)
