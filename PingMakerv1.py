from ping3 import ping, verbose_ping

p=input("Enter IP address: ")

def ip_checkv4(ip):
        parts=ip.split(".")
        if len(parts)<4 or len(parts)>4:
            return "invalid IP length should be 4 not greater or less than 4"
        else:
            while len(parts)== 4:
                a=int(parts[0])
                b=int(parts[1])
                c=int(parts[2])
                d=int(parts[3])
                if a<= 0 or a == 127 :
                    return "invalid IP address"
                elif d == 0:
                    return "host id  should not be 0 or less than zero " 
                elif a>=255:
                    return "should not be 255 or greater than 255 or less than 0 A"
                elif b>=255 or b<0: 
                    return "should not be 255 or greater than 255 or less than 0 B"
                elif c>=255 or c<0:
                    return "should not be 255 or greater than 255 or less than 0 C"
                elif d>=255 or c<0:
                    return "should not be 255 or greater than 255 or less than 0 D"
                else:
                    return 1

g=ip_checkv4(p)
if g == 1:
    print(verbose_ping(p, count=0))
else :
    print(ip_checkv4(p))
