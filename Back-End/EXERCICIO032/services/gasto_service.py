from models.gasto import Gasto
from conn import conectar

def gastos_listar_todos():
    resultado = []
    try:    
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT IDGASTO, DESCRICAO, CATEGORIA, VALOR, DT_GASTO FROM GASTO")
        dados = cursor.fetchall()
        resultado = [Gasto.from_db(item).to_dict() for item in dados]
        cursor.close()
        conexao.close()  
    except Exception as e:
        print(f"Erro ao listar os gastos: {e}")
    return resultado

def gastos_lista_selecionado(id):
    try:    
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT IDGASTO, DESCRICAO, CATEGORIA, VALOR, DT_GASTO FROM GASTO WHERE IDGASTO = %s", (id,))
        dados = cursor.fetchone()
        if dados:
            gasto = Gasto.from_db(dados).to_dict()
            cursor.close()
            conexao.close()
            return gasto
        return None
    except Exception as e:
        print(f"Erro ao localizar o gasto: {e}")
        return None

def gastos_lista_categoria(categoria):
    resultado = []
    try:    
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT IDGASTO, DESCRICAO, CATEGORIA, VALOR, DT_GASTO FROM GASTO WHERE CATEGORIA = %s", (categoria,))
        dados = cursor.fetchall()
        resultado = [Gasto.from_db(item).to_dict() for item in dados]
        cursor.close()
        conexao.close()  
    except Exception as e:
        print(f"Erro ao listar gastos por categoria: {e}")
    return resultado
    
def gastos_valor_categoria(categoria):
    try:    
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT SUM(VALOR) AS VALOR FROM GASTO WHERE CATEGORIA = %s", (categoria,))
        dados = cursor.fetchone()
        valor = dados[0] if dados and dados[0] is not None else 0
        cursor.close()
        conexao.close()
        return valor
    except Exception as e:
        print(f"Erro ao calcular valor por categoria: {e}")
        return None
    
def gastos_salvar_novo_gasto(gasto):
    if not isinstance(gasto, Gasto):
        print("Erro: O objeto fornecido não é um Gasto válido.")
        return False
    try:    
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO GASTO (DESCRICAO, CATEGORIA, VALOR, DT_GASTO) VALUES (%s, %s, %s, %s)", gasto.to_insert_db())
        conexao.commit()
        cursor.close()
        conexao.close()
        return True
    except Exception as e:
        print(f"Erro ao salvar novo gasto: {e}")
        return False

def gastos_salvar_gasto_existente(gasto):
    if not isinstance(gasto, Gasto):
        print("Erro: O objeto fornecido não é um Gasto válido.")
        return False
    try:    
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("UPDATE GASTO SET DESCRICAO = %s, CATEGORIA = %s, VALOR = %s, DT_GASTO = %s WHERE IDGASTO = %s", gasto.to_update_db())
        conexao.commit()
        cursor.close()
        conexao.close()
        return True
    except Exception as e:
        print(f"Erro ao alterar gasto: {e}")
        return False

def gastos_excluir_gasto_existente(id):
    try:    
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM GASTO WHERE IDGASTO = %s", (id,))
        conexao.commit()
        cursor.close()
        conexao.close()
        return True
    except Exception as e:
        print(f"Erro ao excluir o gasto: {e}")
        return False