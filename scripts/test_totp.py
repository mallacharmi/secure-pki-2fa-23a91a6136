import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.totp_utils import generate_totp_code, verify_totp_code

hex_seed = "c75bbaaefd2304886b635b4a4e8d5fa09043870cfa505581eb6ee24fe51ea419"

code = generate_totp_code(hex_seed)
print("Generated OTP:", code)

is_valid = verify_totp_code(hex_seed, code)
print("Is valid:", is_valid)