# 1. Nested dictionaries (like JSON data)
university = {
    "CS": {"students": 120, "head": "Dr. Rao"},
    "Math": {"students": 80, "head": "Dr. Bose"},
}

print("Nested Dictionary",university)
print("head of CS is",university["CS"]["head"])