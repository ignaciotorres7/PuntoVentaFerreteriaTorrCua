import pyodbc

server = 'localhost'
database = 'FerreTorCua'
username = 'ignaciotorres7'
password = 'lC6P6W4T1a'

def conectar_sqlserver():
    try:
        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
        conn = pyodbc.connect(conn_str)
        print("Conexión exitosa a SQL Server.")
        return conn
    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        print(f"Error de conexión: {sqlstate}")
        return None
    
def conectar_sqlserver(server, database, user, password):
    try:
        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={user};PWD={password}"
        conn = pyodbc.connect(conn_str)
        print("Conexión exitosa a SQL Server.")
        return conn
    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        print(f"Error de conexión: {sqlstate}")
        return None
    
def insertar_registro(values, table_name, conn, cols_name):
    sqlquery = f"INSERT INTO {table_name} ("
    long_cols = len(cols_name)
    long_vals = len(values)
    aux = -1

    if long_cols>0 and long_vals>0:
        for i in cols_name:
            if i< long_cols -1:
                sqlquery = sqlquery + f"{cols_name[i]}, "
            else:
                sqlquery = sqlquery + f"{cols_name[i]}) VALUES ("

        for j in values:
            if j < long_vals -1:
                sqlquery = sqlquery + f"{values[j]}, "
            else:
                sqlquery = sqlquery + f"{values[j]})"

        cursor = conn.cursor()
        aux = cursor.execute(sqlquery)

        conn.commit
    else:
        print("las columnas y valores estan vacios")

    return aux

def consulta_registro(table_name, condicion, conn, cols_name):
    sel_query = f"SELECT "
    long_cols = len(cols_name)

    select_response = None

    if long_cols > 0:
        for i in cols_name:
            if i<long_cols -1:
                sel_query = sel_query + f"{cols_name[i]}, "
            else:
                sel_query = sel_query + f"{cols_name[i]} FROM {table_name} where 1=1" + f",{condicion}" if condicion != "" else ""

        cursor = conn.cursor()
        select_response = cursor.execute(sel_query)
    else:
        print("las columnas vienen vacias")
    
    return select_response

def eliminar_registro(table_name, condicion, conn):
    delete_query = f"DELETE FROM {table_name} WHERE {condicion}"
    cursor = conn.cursor()
    cursor.execute(delete_query)
    conn.commit()
    if cursor.Errors:
        print("Error al eliminar el registro")
        return False
    else:
        print("Registro eliminado correctamente")
        return True
    

def actualizar_registro(table_name, set_values, condicion, conn):
    update_query = f"UPDATE {table_name} SET {set_values} WHERE {condicion}"
    cursor = conn.cursor()
    cursor.execute(update_query)
    conn.commit()
    if cursor.Errors:
        print("Error al actualizar el registro")
        return False
    else:
        print("Registro actualizado correctamente")
        return True
    
def borrado_logico(table_name, condicion, conn):
    update_query = f"UPDATE {table_name} SET estado = 0 WHERE {condicion}"
    cursor = conn.cursor()
    cursor.execute(update_query)
    conn.commit()
    if cursor.Errors:
        print("Error al eliminar el registro")
        return False
    else:
        print("Registro eliminado correctamente")
        return True
    
def cerrar_conexion(conn):
    if conn:
        conn.close()
        print("Conexión cerrada.")
    else:
        print("No hay conexión para cerrar.")
