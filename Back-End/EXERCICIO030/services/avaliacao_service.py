avaliacoes = []
proximo_id = 1

def listar_todas_avaliacoes():
    return avaliacoes

def listar_avaliacoes_por_filme(filme_id):
    return [av for av in avaliacoes if av['filme_id'] == filme_id]

def total_avaliacoes():
    return {"total": len(avaliacoes)}

def buscar_avaliacao_por_id(avaliacao_id):
    for avaliacao in avaliacoes:
        if avaliacao['id'] == avaliacao_id:
            return avaliacao
    return None

def criar_avaliacao(dados):
    global proximo_id
    filme_id = dados.get('filme_id')
    comentario = dados.get('comentario')
    nota = dados.get('nota')

    if not all([filme_id, comentario, nota is not None]):
        return None, "Dados incompletos ou inválidos."

    nova_avaliacao = {
        "id": proximo_id,
        "filme_id": int(filme_id),
        "comentario": comentario,
        "nota": int(nota)
    }
    avaliacoes.append(nova_avaliacao)
    proximo_id += 1
    return nova_avaliacao, "Avaliação criada com sucesso."

def atualizar_avaliacao(avaliacao_id, dados):
    avaliacao = buscar_avaliacao_por_id(avaliacao_id)
    if not avaliacao:
        return None, "Avaliação não encontrada."
    
    comentario = dados.get('comentario')
    nota = dados.get('nota')

    if comentario:
        avaliacao['comentario'] = comentario
    if nota is not None:
        avaliacao['nota'] = nota
        
    return avaliacao, "Avaliação atualizada com sucesso."

def excluir_avaliacao(avaliacao_id):
    global avaliacoes
    avaliacao = buscar_avaliacao_por_id(avaliacao_id)
    if not avaliacao:
        return False, "Avaliação não encontrada."
    
    avaliacoes = [av for av in avaliacoes if av['id'] != avaliacao_id]
    return True, "Avaliação excluída com sucesso."