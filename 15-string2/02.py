# print(0b11111111) #vypise cislo v bin sust
# print(oct(123))
# print(0xff)     

# def dec_bin():
#     bin=""
#     while cis > 0:
#         zv=cis % 2
#         bin= str(zv) + bin
#         print(bin)
#         cis=cis // 2
#         return bin



def dec_hex(cis):
    hex=""
    while cis > 0:
        zv=cis % 16
        if zv<10:
            hex= str(zv) + hex
        # elif zv==10:
        #     hex="a"+hex
        # elif zv==11:
        #     hex="b"+hex
        # elif zv==12:
        #     hex="c"+hex
        # elif zv==13:
        #     hex="d"+hex
        # elif zv==14:
        #     hex="e"+hex
        # else:
        #     hex="f"+hex
        else:
            hex=chr(55+zv)+hex
        cis=cis // 16
    return hex

print(ord("A"))
print(dec_hex(253))