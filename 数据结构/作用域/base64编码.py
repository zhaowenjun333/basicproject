alphabet=b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
teststr="abcde"
def base64(src):
    ret=bytearray()
    length=len(src)
    r=0
    for offset in range(0,length,3):
        if offset +3<=length:
            triple=src[offset:offset+3]
        else:
            triple=src[offset:]
            r=3-len(triple)
            triple=triple+'\x00' *r
        b=int.from_bytes(triple.encode(),'big')
        for i in range(18,-1,-6):
            # if i==18:
            #     index=b>>i
            # else:
            index=b>>i & 0x3F
            ret.append(alphabet[index])
        for i in range(1,r+1):
             ret[-i]=0x3D
    return bytes(ret)

print(base64(teststr))

