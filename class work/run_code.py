import sys

if len(sys.argv) < 2:
    print("Usage: python run_code.py \"<code>\"")
    sys.exit(1)

code_string = sys.argv[1]
print("Received code:", code_string)

# WARNING: Only use exec() with trusted input!
exec(code_string)
