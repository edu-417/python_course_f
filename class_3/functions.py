def is_valid_email(value: str) -> bool:
    return "@" in value and "." in value.split("@")[-1]
 
def is_valid_phone(value: str) -> bool:
    return value.replace("+", "").replace("-", "").isdigit() and len(value) >= 8
 
def is_valid_age(value: str) -> bool:
    return str(value).isdigit() and 0 < int(value) < 120
 
def is_valid_field(value: str, validator, field_name: str) -> None:
    if validator(value):
        print(f"  ✓ {field_name}: '{value}' — válido")
    else:
        print(f"  ✗ {field_name}: '{value}' — inválido")
 
fields = [
    ("ana@empresa.com",   is_valid_email,    "email"),
    ("no-es-email",       is_valid_email,    "email"),
    ("+51-987654321",     is_valid_phone, "teléfono"),
    ("abcdefgh",          is_valid_phone, "teléfono"),
    (25,                  is_valid_age,     "edad"),
    (200,                 is_valid_age,     "edad"),
]
 
print("Validando formulario de registro:")
for value, validator, field in fields:
    is_valid_field(value, validator, field)