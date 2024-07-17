# Expresiones regulares REGEXP
import re
# patrones para validar textos comunes como emails, passwords, dni...
email = "armand@gmail.com"
# explicacion patron
# r: raw string: cadena sin interpretar, para evitar problemas con caracteres de escape
# ^: inicio de la cadena
# [a-zA-Z0-9_.+-]: Uno o mas caracteres alfanumericos, punto, guin bajo, simbolo mas o guion
# @: arroba
# [a-zA-Z0-9-]: Lo mismo que el anterior
# \.: punto
# [a-zA-Z0-9-.]: Lo mismo que el anterior
# $: fin de cadena
email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
email_match = re.match(email_pattern, email)
print(bool(email_match))

# dni
dni = "12345678A"
dni_pattern = r"\d{8}[A-Z]$"
# \d{8}: 8 digitos
# [A-Z]: una letra mayuscula