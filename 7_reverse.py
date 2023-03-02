# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit 
# integer range [-2**31, 2**31 - 1], then return 0.

x = 2**31 +1

if x < 0:
    abs_x = abs(x)
    str_x = str(abs_x)
    rev = str_x[::-1] ##儲存reverse of abs(x)
    ans = - int(rev)
else:
    str_x = str(x)
    rev = str_x[::-1]
    ans = int(rev)

if abs(ans) > 2**(31):
    ans = 0

print(ans)
