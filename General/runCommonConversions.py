import sys
from commonConversions import u_int_conversion

if __name__ == '__main__':
    val = int(sys.argv[1])
    bitSize = int(sys.argv[2])

    onesComp, twosComp, signedMag, hx, bit = u_int_conversion(val, bitSize)

    print "User Value: %s Bit Size: %s" % (val, bitSize)
    print "Your Ones Complement is: ", onesComp
    print "Your Twos Complement is: ", twosComp
    print "Your Signed Magnitude is:", signedMag
    print "Your Hex Value is:       ", hx
    print "Your Binary Value is:    ", bit
