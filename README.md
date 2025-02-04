# 📚 **Sistema de Gerenciamento de Livraria**  
Este projeto é um **CRUD completo** para gerenciamento de uma biblioteca pessoal, permitindo o cadastro e organização de **livros físicos e digitais** através de uma **interface gráfica com Tkinter**.

## 🚀 **Funcionalidades**
- ✅ Adicionar livros (físicos e digitais)  
- ✅ Listar todos os livros cadastrados  
- ✅ Listar apenas **livros físicos**  
- ✅ Listar apenas **livros digitais**  
- ✅ Modificar informações de um livro  
- ✅ Deletar ou marcar um livro como vendido  
- ✅ **Adicionar imagens e links para compra** dos livros  
- ✅ Persistência automática dos dados em JSON  

---

## 📌 **Pré-requisitos**
### 🔹 **1. Instalar Python**  
Este projeto requer **Python 3.11.3 ou superior**. Você pode instalar o Python via [Pyenv](https://github.com/pyenv/pyenv) para gerenciar versões.  

```bash
# Instalar pyenv (caso ainda não tenha)
curl https://pyenv.run | bash

# Instalar Python 3.11.3 via pyenv
pyenv install 3.11.3
pyenv global 3.11.3
```

### 🔹 **2. Criar um Ambiente Virtual**
Para manter as dependências organizadas, crie um ambiente virtual antes de rodar o projeto:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 🔹 **3. Instalar Dependências**
Este projeto utiliza um `requirements.txt` para instalar as dependências necessárias:

```bash
pip install -r requirements.txt
```

Se você quiser adicionar novas dependências ao projeto, use:

```bash
pip install <pacote> && pip freeze > requirements.txt
```

---

## 🛠 **Ferramentas Utilizadas**
### 🔹 **Tkinter (Interface Gráfica)**
O **Tkinter** já vem incluído no Python e é usado para criar a interface gráfica do sistema.

### 🔹 **Ruff (Analisador de Código)**
O **Ruff** é um analisador de código estático que detecta erros e formata o código automaticamente.  

- Para rodar a análise:
  ```bash
  ruff check src/
  ```
- Para corrigir automaticamente:
  ```bash
  ruff check src/ --fix
  ```

### 🔹 **Pytest (Testes Automatizados)**
O **Pytest** é usado para validar o funcionamento correto do sistema.

- Para rodar os testes:
  ```bash
  pytest
  ```
- Para ver a cobertura dos testes:
  ```bash
  pytest --cov=src
  ```

---

## 🎮 **Como Executar o Projeto**
1️⃣ **Ativar o ambiente virtual** (caso ainda não esteja ativo)  
```bash
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

2️⃣ **Rodar o programa**  
```bash
python src/main.py
```

3️⃣ **Interagir pela interface gráfica** e gerenciar os livros da sua biblioteca!

---

## 🗂 **Persistência de Dados**
Os livros cadastrados são armazenados automaticamente no arquivo **`livraria.json`** e carregados sempre que o programa é iniciado.

---

## 🚀 **Melhorias Futuras**
- 🎨 Melhorias na interface gráfica (melhor organização dos botões e layout)  
- 📸 Suporte para **upload de imagens locais** (não apenas links)  
- 📚 Integração com APIs externas para buscar dados automaticamente  
- 📝 Documentação com **MkDocs**  

---

## 💻 **Contribuições**
Sinta-se à vontade para contribuir com o projeto! Para isso:  

1. **Faça um fork** do repositório  
2. **Crie uma branch** para suas modificações  
3. **Envie um Pull Request** com suas melhorias  

---

## 📜 **Licença**
Este projeto está sob a licença **MIT**.  

📌 **Desenvolvido por [Daniel Louro Costa]**

