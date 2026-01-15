def greet(name):
    print(f"Hello, {name}!")

# Security issues that CodeQL will detect:

# 1. Use of eval() - code injection vulnerability
def execute_user_input(user_code):
    result = eval(user_code)  # Dangerous: allows arbitrary code execution
    return result

# 2. SQL injection vulnerability
import sqlite3
def get_user_by_name(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # SQL injection: user input directly concatenated into query
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

# 3. Hardcoded credentials
API_KEY = "sk-1234567890abcdef"  # Hardcoded secret
PASSWORD = "admin123"  # Hardcoded password

# 4. Command injection vulnerability
import os
def ping_host(hostname):
    # Command injection: user input in shell command
    os.system(f"ping {hostname}")

# 5. Path traversal vulnerability
def read_file(filename):
    # No validation - allows reading any file
    with open(f"/var/data/{filename}", 'r') as f:
        return f.read()

if __name__ == "__main__":
    greet("World")