import  random
otp  = random.randint(100000,999999)
print("Your otp is:",otp)
entered_otp=int(input("Enter the otp:"))
if entered_otp == otp:
    print("OTP Verified Successfully1:")
else:
    print("Invalid OTP")
