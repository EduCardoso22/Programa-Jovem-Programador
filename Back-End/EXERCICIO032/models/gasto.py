class Gasto:
    def __init__(self, id, descricao, categoria, valor, data):
        self.id = id
        self.descricao = descricao
        self.categoria = categoria
        self.valor = valor
        self.data = data

    @classmethod
    def from_db(cls, row):
        if isinstance(row, dict):
            gasto = cls(row["idgasto"], row["descricao"], row["categoria"], row["valor"], row["dt_gasto"])
        else:
            gasto = cls(row[0], row[1], row[2], row[3], row[4])
        return gasto

    def to_insert_db(self):
        return (self.descricao, self.categoria, self.valor, self.data)

    def to_update_db(self):
        return (self.descricao, self.categoria, self.valor, self.data, self.id)

    def to_dict(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "categoria": self.categoria,
            "valor": float(self.valor), # Garante que o valor seja float no JSON
            "data": self.data.isoformat() if hasattr(self.data, 'isoformat') else self.data
        }