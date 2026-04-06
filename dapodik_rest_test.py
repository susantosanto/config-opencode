import requests
import re
import json

BASE_URL = "http://localhost:5774"
EMAIL = "sdnpasirhalang.cikalong@gmail.com"
PASSWORD = "123Unpas!!!"

session = requests.Session()

# Step 1: GET homepage to extract semester_id and CSRF token
print("=== STEP 1: GET HOMEPAGE ===")
r = session.get(f"{BASE_URL}/", timeout=10)
print(f"Status: {r.status_code}")

# Extract semester_id
m = re.search(r'semester_id.*?value=["\'](\d+)["\']', r.text, re.DOTALL)
sem = m.group(1) if m else None
print(f"Semester ID: {sem}")

# Look for CSRF token or hidden fields
hidden_fields = re.findall(
    r'<input[^>]+name=["\']([^"\']+)["\'][^>]+value=["\']([^"\']*)["\']', r.text
)
print(f"Hidden fields found: {len(hidden_fields)}")
for name, val in hidden_fields[:10]:
    print(f"  {name} = {val[:50]}")

# Check if there's a _token or csrf field
csrf_patterns = ["_token", "csrf", "csrf_token", "token"]
for pattern in csrf_patterns:
    for name, val in hidden_fields:
        if pattern.lower() in name.lower():
            print(f"Found CSRF: {name} = {val}")

# Step 2: Try POST with JSON content type
print()
print("=== STEP 2: TRY DIFFERENT LOGIN APPROACHES ===")

# Approach A: POST with JSON
print("\n--- Approach A: JSON POST ---")
try:
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    data = json.dumps({"username": EMAIL, "password": PASSWORD, "semester_id": sem})
    r = session.post(
        f"{BASE_URL}/login",
        data=data,
        headers=headers,
        timeout=10,
        allow_redirects=False,
    )
    print(f"Status: {r.status_code}")
    print(f"Location: {r.headers.get('Location', 'N/A')}")
    print(f"Response: {r.text[:200]}")
except Exception as e:
    print(f"Error: {e}")

# Approach B: POST with form data and Accept header
print("\n--- Approach B: Form POST with Accept ---")
try:
    headers = {"Accept": "application/json, text/html"}
    data = {
        "username": EMAIL,
        "password": PASSWORD,
        "semester_id": sem,
        "rememberme": "on",
    }
    r = session.post(
        f"{BASE_URL}/login",
        data=data,
        headers=headers,
        timeout=10,
        allow_redirects=True,
    )
    print(f"Status: {r.status_code}")
    print(f"URL: {r.url}")
    print(f"Cookies: {dict(session.cookies)}")
except Exception as e:
    print(f"Error: {e}")

# Approach C: Try REST API with XHR header
print("\n--- Approach C: XHR-style POST ---")
try:
    headers = {
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"{BASE_URL}/",
    }
    data = {"username": EMAIL, "password": PASSWORD, "semester_id": sem}
    r = session.post(
        f"{BASE_URL}/login",
        data=data,
        headers=headers,
        timeout=10,
        allow_redirects=False,
    )
    print(f"Status: {r.status_code}")
    print(f"Response: {r.text[:300]}")
except Exception as e:
    print(f"Error: {e}")

# Approach D: Check if there's a different login endpoint
print("\n--- Approach D: Discover login endpoints ---")
login_eps = [
    "/auth/login",
    "/api/login",
    "/rest/login",
    "/login",
    "/signin",
    "/authenticate",
]
for ep in login_eps:
    try:
        r = session.get(f"{BASE_URL}{ep}", timeout=5, allow_redirects=False)
        print(f"  GET {ep:25s} -> {r.status_code}")
    except:
        print(f"  GET {ep:25s} -> ERROR")
