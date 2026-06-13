# Caso de uso real: validar contraseñas
# Sin función — código repetido en cada formulario 😞
password = "abc123"
if len(password) >= 8 and any(c.isdigit() for c in password):
    print("Contraseña válida")
 
# Con función — reutilizable y clara 😊
def is_valid_password(password: str) -> str:
    has_length = len(password) >= 8
    has_number = any(c.isdigit() for c in password)
    has_uppercase = any(c.isupper() for c in password)

    is_valid = has_length and has_number and has_uppercase

    return is_valid
 
print(is_valid_password("abc123"))        # False — sin mayúscula
print(is_valid_password("Secure1"))       # False — solo 7 chars
print(is_valid_password("Secure123"))     # True
 
# Retornar múltiples valores: análisis de texto
def analyze_text(texto):
    words = texto.split()
    characters = len(texto)
    longest_word = max(words, key=len)
    return len(words), characters, longest_word
 
resena = "La inteligencia artificial está cambiando el mundo velozmente"
n_palabras, n_chars, longest_word = analyze_text(resena)
print(f"Palabras: {n_palabras} | Chars: {n_chars} | Más larga: '{longest_word}'")
 
# Sin return → devuelve None (útil para funciones de "acción")
def register_event(evento, usuario):
    print(f"[LOG] {usuario} realizó: {evento}")
    # no hay return → devuelve None implícitamente
 
resultado = register_event("login", "ana@mail.com")
print(f"Retornó: {resultado}")   # None