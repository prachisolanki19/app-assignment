import re

# Input text
text = """
Contact us at student@gmail.com
or admin123@yahoo.com.
You can also reach us at test_user@mit.edu
"""

# Regular expression pattern for email
pattern = r'[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Find all email addresses
emails = re.findall(pattern, text)

# Display the result
print("Email addresses found:")
for email in emails:
    print(email)