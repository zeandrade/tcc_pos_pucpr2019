connection = ""


def validar_admin(connection, usuario: str) -> bool:
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT admin FROM usuarios WHERE usuario = '%s'" % usuario)
        result = cursor.fetchone()
    admin, = result
    return admin


validar_admin(connection, "'; select true; --")
# True

# como o código fica
"SELECT admin FROM usuarios WHERE usuario = '%s'" % "'; select true; --"

# como o a instrução SQL será executada
"SELECT admin FROM usuarios WHERE usuario = ''; select true; --'"