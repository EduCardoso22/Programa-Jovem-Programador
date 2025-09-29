import requests

filmes_em_cartaz = []

def importar_filmes():

    global filmes_em_cartaz
    api_key = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwODExOGIxM2YwN2NiOWQzYmYwODNiMTFmMjQxYjk1NyIsIm5iZiI6MTc1NzE5NjA5Ny4wNzksInN1YiI6IjY4YmNhZjQxZjIzZDNlMzIwMzk0NzNiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._8jdsXPumfjNOTjnses_QgbQX7syERexuKDQr8kqvHg'
    url = 'https://api.themoviedb.org/3/movie/now_playing?language=pt-BR&region=BR'
    headers = {'Authorization': f'Bearer {api_key}'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        json_filmes = response.json()
        base_filmes = json_filmes.get("results", [])

        filmes_locais = []
        for item in base_filmes:
            filme = {
                "id": item.get("id"),
                "titulo": item.get("title"),
                "descricao": item.get("overview"),
                "estreia": item.get("release_date"),
                "poster": f"https://image.tmdb.org/t/p/w500/{item.get('poster_path')}"
            }
            filmes_locais.append(filme)
        
        filmes_em_cartaz = filmes_locais
        return {"mensagem": "Filmes importados com sucesso!", "total": len(filmes_em_cartaz)}, 200
    except requests.RequestException as e:
        return {"erro": f"Falha ao buscar filmes: {e}"}, 500

def listar_filmes():
    return filmes_em_cartaz

def buscar_filme_por_id(filme_id):

    for filme in filmes_em_cartaz:
        if filme['id'] == filme_id:
            return filme
    return None