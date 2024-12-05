import random
import pyotp
import yagmail

# Simulated User Database
USER_DB = {
    "user@example.com": {
        "password": "securepassword",
        "otp_secret": pyotp.random_base32(),  # Unique OTP secret for the user
    }
}

# Function to send OTP via email
def send_otp(email, otp):
    # Replace with your email credentials
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"  # Use app-specific password for Gmail if 2FA is enabled

    try:
        yag = yagmail.SMTP(sender_email, sender_password)
        yag.send(
            to=email,
            subject="Your Login OTP",
            contents=f"Your OTP is: {otp}",
        )
        print("OTP sent successfully!")
    except Exception as e:
        print(f"Failed to send OTP: {e}")

# Login function
def login():
    print("=== Login ===")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email in USER_DB and USER_DB[email]["password"] == password:
        print("Login successful! Generating OTP...")
        
        # Generate OTP
        otp = str(random.randint(100000, 999999))  # Random 6-digit OTP
        USER_DB[email]["otp"] = otp

        # Send OTP via email
        send_otp(email, otp)

        # OTP Verification
        verify_otp(email)
    else:
        print("Invalid email or password. Please try again.")

# OTP Verification function
def verify_otp(email):
    print("\n=== OTP Verification ===")
    entered_otp = input("Enter the OTP sent to your email: ")

    if entered_otp == USER_DB[email]["otp"]:
        print("OTP verified! Login complete.")
    else:
        print("Invalid OTP. Access denied.")

# Main program
if __name__ == "__main__":
    login()
