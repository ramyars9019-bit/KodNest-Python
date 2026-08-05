registered = input()
fee_paid = input()
identity_verified = input()
system_check = input()

# Check whether the student can access the online exam

if registered != "Yes":
    print("Access Denied: Registration Incomplete")

elif registered == "Yes" and (fee_paid != "Yes" or identity_verified != "Yes"):
    print("Access Denied: Verification Pending")

elif system_check != "Pass":
    print("Access Denied: System Check Failed")

else:
    print("Access Granted")