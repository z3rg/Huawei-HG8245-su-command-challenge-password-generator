import hashlib

def suPassword(chall):
    #El challenge esta compuesto de 0123456789ABCDEFGHIJKLMNOPQRSTUYWXYZ
    premd5 = bytearray(8)
    for i in range(8):
        if ord(chall[i]) <= 0x47:
            premd5[i]=ord(chall[i])<<1
        else:
            premd5[i]=ord(chall[i])>>1
    print('premd5:',premd5)
    
    md5hash = hashlib.md5()
    md5hash.update(premd5)
    print('md5: ',md5hash.hexdigest())
    prepass = bytearray(md5hash.digest())

    challpass = bytearray(8)
    for i in range(8):
        temp2=(prepass[i]>>1)*0xB60B60B7
        temp2=temp2>>(5+32)
        temp1=temp2<<3
        temp1=temp1-(temp2<<1)
        temp3=(temp1<<4)
        temp3=temp3-temp1
        temp0=prepass[i]-temp3+0x21
        temp0=temp0&0xFF
        if temp0 == 0x3F:
            challpass[i]=0x3E
        else:
            challpass[i]=temp0
    print('PASSWORD!: ',challpass)
        

if __name__=='__main__':
    print('Huawei HG8245 su command challenge-password generator by adiaz_32')
    print('Challenge: ')
    challenge = 'B7Q3YS1E'
    #if len(challenge)==8:
    suPassword(challenge)
    #else:
    #    print 'ERROR: Challenge must have 8 chars'
