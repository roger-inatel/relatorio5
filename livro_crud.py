from pymongo import MongoClient
from bson.objectid import ObjectId

class LivroModel:
    def __init__(self, database):
        self.db = database

    def create_livro(self, titulo: str, autor: str, ano: int, preco: float):
        try:
            res = self.db.collection.insert_one({"titulo": titulo, "autor": autor, "ano": ano, "preco": preco})
            print(f"Livro criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o livro: {e}")
            return None

    def read_livro_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Livro encontrado: {res}")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao ler o livro: {e}")
            return None

    def update_livro(self, id: str, titulo: str, autor: str, ano: int, preco: float):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"titulo": titulo, "autor": autor, "ano": ano, "preco": preco}})
            print(f"Livro atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o livro: {e}")
            return None

    def delete_livro(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Livro deletado: {res.deleted_count} documento(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o livro: {e}")
            return None
    

def main():
    # Conectando ao banco de dados
    client = MongoClient('localhost', 27017)
    db = client['mydatabase']
    
    # Inicializando o modelo de livro
    livro_model = LivroModel(db)

    while True:
        print("\nMenu:")
        print("1. Criar Livro")
        print("2. Ler Livro por ID")
        print("3. Atualizar Livro")
        print("4. Deletar Livro")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            ano = int(input("Ano do livro: "))
            preco = float(input("Preço do livro: "))
            livro_model.create_livro(titulo, autor, ano, preco)
        elif choice == "2":
            livro_id = input("ID do livro: ")
            livro_model.read_livro_by_id(livro_id)
        elif choice == "3":
            livro_id = input("ID do livro a ser atualizado: ")
            titulo = input("Novo título do livro: ")
            autor = input("Novo autor do livro: ")
            ano = int(input("Novo ano do livro: "))
            preco = float(input("Novo preço do livro: "))
            livro_model.update_livro(livro_id, titulo, autor, ano, preco)
        elif choice == "4":
            livro_id = input("ID do livro a ser deletado: ")
            livro_model.delete_livro(livro_id)
        elif choice == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
