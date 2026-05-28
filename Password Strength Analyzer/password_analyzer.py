import re

print("===== PASSWORD STRENGTH ANALYZER =====")

password = input("Enter your password: ")

score = 0

# Length Check
if len(password) >= 8:
    score += 1
else:
    print("❌ Password must contain at least 8 characters")

# Uppercase Check
if re.search(r"[A-Z]", password):
    score += 1
else:
    print("❌ Add at least one uppercase letter")

# Lowercase Check
if re.search(r"[a-z]", password):
    score += 1
else:
    print("❌ Add at least one lowercase letter")

# Number Check
if re.search(r"\d", password):
    score += 1
else:
    print("❌ Add at least one number")

# Special Character Check
if re.search(r"[@$!%*?&]", password):
    score += 1
else:
    print("❌ Add at least one special character")

# Final Result
print("\n===== RESULT =====")

if score == 5:
    print("✅ Password Strength: STRONG")
elif score >= 3:
    print("⚠ Password Strength: MEDIUM")
else:
    print("❌ Password Strength: WEAK")