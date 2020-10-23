hrs = input('Enter Hours:')
rate=input('Enter rate:')
h=float(hrs)
r=float(rate)
def computepay(h,r):
    if h<=40:
        pay=h*r
        return pay
    else:
        extra=h-40
        pay=(40*r)+(extra*r*1.5)
        return pay
print('Pay',computepay(h,r))
