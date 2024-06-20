import csv

# Variáveis que armazenam usuários e produtos
users = {}
products = []
current_user = None

### Funções para gerenciar usuários ###
# Carrega os usuários do arquivo CSV
def load_users():
    with open('bancos_de_dados/usuarios.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            users[row['username']] = {'password': row['password'], 'cargo': row['cargo']}

# Recebe os dados do usuário cadastrado como parâmetro e salva no arquivo CSV
def save_users():
    with open('usuarios.csv', mode='w', newline='') as file:
        fieldnames = ['username', 'password', 'cargo']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for username, info in users.items():
            writer.writerow({'username': username, 'password': info['password'], 'cargo': info['cargo']})

# Cadastra um novo usuário caso ele não exista
def add_user(username, password, role):
    if username in users:
        print("Usuário já existe.")
    else:
        users[username] = {'password': password, 'cargo': role}
        save_users()
        print("Cadastrado com sucesso!")

# Lista os usuários já cadastrados
def list_users():
    for username, info in users.items():
        print(f"Usuário: {username}, Cargo: {info['cargo']}")

# Atualiza informações de um usuário já cadastrado
def update_user(username, password=None, role=None):
    if username in users:
        if password:
            users[username]['password'] = password
        if role:
            users[username]['cargo'] = role
        save_users()
    else:
        print("Usuário não encontrado.")

# Remove um usuário existente
def remove_user(username):
    if username in users:
        del users[username]
        save_users()
    else:
        print("Usuário não encontrado.")

# Pesquisa um usuário já cadastrado
def find_user(username):
    if username in users:
        info = users[username]
        print(f"Username: {username}, Role: {info['cargo']}")
    else:
        print("Usuário não encontrado.")

### Funções para gerenciar produtos ###
# Carrega os produtos do arquivo CSV
def load_products():
    with open('bancos_de_dados/produtos.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({'nome': row['nome'], 'preco': float(row['preco']), 'quantidade': int(row['quantidade'])})

# Recebe o produto cadastrado como parâmetro e salva no arquivo CSV
def save_products():
    with open('produtos.csv', mode='w', newline='') as file:
        fieldnames = ['nome', 'preco', 'quantidade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for produto in products:
            writer.writerow(produto)

# Cadastra um novo produto
def add_product(name, price, quant):
    products.append({'nome': name, 'preco': price, 'quantidade': quant})
    save_products()

# Lista todos os produtos cadastrados
def list_products():
    for product in products:
        print(f"Nome do produto: {product['nome']}, Preço: R${product['preco']}, Quantidade disponível: {product['quantidade']}")

# Atualiza as informações de um produto já cadastrado
def update_product(name, price=None, quant=None):
    for product in products:
        if product['nome'] == name:
            if price is not None:
                product['preco'] = price
            if quant is not None:
                product['quantidade'] = quant
            save_products()
            return
    print("Produto não encontrado.")

# Remove um produto já cadastrado
def remove_product(name):
    global products
    products = [product for product in products if product['nome'] != name]
    save_products()

# Filtra produto pelo nome
def find_product(name):
    for product in products:
        if product['nome'] == name:
            print(f"Nome do Produto: {product['nome']}, Preço: R${product['preco']}, Quantidade disponível: {product['quantidade']}")
            return
    print("Produto não encontrado.")

# Ordena os produtos por nome e os lista
def sort_products_by_name():
    products.sort(key=lambda x: x['nome'])
    list_products()

# Ordena os produtos por preço e os lista
def sort_products_by_price():
    products.sort(key=lambda x: x['preco'])
    list_products()

# Ordena os produtos por quantidade e os lista
def sort_products_by_quant():
    products.sort(key=lambda x: x['quantidade'])
    list_products()

# Carregar dados
load_users()
load_products()

# Função de login
def login():
    global current_user
    print("\nBem vindo(a) ao EconoSmart Supermercados!\n\nFaça seu login:")
    username = input("Nome de usuário: ")
    password = input("Senha: ")
    if username in users and users[username]['password'] == password:
        current_user = username
        print(f"\nBem-vindo, {username} ({users[username]['cargo']})!")
    else:
        print("\nUsuário ou senha incorretos.")
        login()

# Função do menu
def menu():
    role = users[current_user]['cargo']
    print("\nMenu:")
    if role == 'gerente':
        print("1. Adicionar usuário")
        print("2. Remover usuário")
    if role in ['gerente', 'rh']:
        print("3. Listar usuários")
        print("4. Atualizar usuário")
        print("5. Buscar usuário")
    if role in ['gerente', 'rh', 'estoquista']:
        print("6. Adicionar produto")
        print("8. Atualizar produto")
        print("9. Remover produto")
    if role in ['gerente', 'estoquista', 'cliente']:
        print("7. Listar produtos")
        print("10. Buscar produto")
        print("11. Ordenar produtos por nome")
        print("12. Ordenar produtos por preço")
        print("13. Ordenar produtos por quantidade")
        print("14. Trocar usuário")
        print("15. Sair")

    option = input("Escolha uma opção: ")
    return option

# Chama a função que executará a escolha do usuário
login()
while True:
    option = menu()
    role = users[current_user]['cargo']

    match option:
        case '1':
            if role == 'gerente':
                username = input("\nNome de usuário: ")
                password = input("Senha: ")
                role = input("Cargo: ")
                add_user(username, password, role)
            else:
                print("Acesso negado.")

        case '2':
            if role == 'gerente':
                username = input("\nNome de usuário: ")
                remove_user(username)
            else:
                print("Acesso negado.")

        case '3':
            if role == 'gerente':
                list_users()
            else:
                print("Acesso negado.")

        case '4':
            if role == 'gerente':
                username = input("\nNome de usuário: ")
                password = input("Nova senha (deixe em branco para não alterar): ")
                role = input("Novo cargo (deixe em branco para não alterar): ")
                update_user(username, password if password else None, role if role else None)
            else:
                print("Acesso negado.")

        case '5':
            if role == 'gerente':
                username = input("\nNome de usuário: ")
                find_user(username)
            else:
                print("Acesso negado.")
                
        case '6':
            if role in ['gerente', 'estoquista']:
                nome = input("\nNome do produto: ")
                preco = float(input("Preço do produto: "))
                quantidade = int(input("Quantidade do produto: "))
                add_product(nome, preco, quantidade)
            else:
                print("Acesso negado.")

        case '7':
            list_products()

        case '8':
            if role in ['gerente', 'estoquista']:
                nome = input("\nNome do produto: ")
                preco = input("Novo preço (deixe em branco para não alterar): ")
                quantidade = input("Nova quantidade (deixe em branco para não alterar): ")
                update_product(nome, float(preco) if preco else None, int(quantidade) if quantidade else None)
            else:
                print("Acesso negado.")

        case '9':
            if role in ['gerente', 'estoquista']:
                nome = input("\nNome do produto: ")
                remove_product(nome)
            else:
                print("Acesso negado.")
                
        case '10':
            nome = input("\nNome do produto: ")
            find_product(nome)

        case '11':
            sort_products_by_name()

        case '12':
            sort_products_by_price()

        case '13':
            sort_products_by_quant()

        case '14':
            login()

        case '15':
            print("\nEconoSmart, sua economia de forma inteligente!\n\nAté mais!\n")
            break 
        
        case _:
            print("\nEscolha inválida. Tente novamente.")