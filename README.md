

# Lab-principle-o-banking-system

## 🇧🇷 Sobre o Projeto


Este projeto simula um sistema bancário simples usando **Python 3.11** sem o uso de frameworks, com persistência de dados via **SQLite** e interface gráfica com **PyQt5**.  
Inclui sistema de **login** para autenticação do usuário, e permite realizar **depósitos**, **saques** (com regras) e consultar o **extrato bancário** com uma interface interativa.

### 📌 Funcionalidades

- **Login**
  - Validação simples de usuário e senha para acesso à aplicação.
- **Depósito**
  - Valor não pode ser negativo.
  - Armazenado para exibição no extrato.
- **Saque**
  - Máximo de 3 saques por dia.
  - Limite de R$500 por saque.
  - Só é permitido se houver saldo suficiente.
  - Armazenado para exibição no extrato.
- **Extrato**
  - Lista todos os depósitos e saques realizados.
  - Exibe valores no formato `R$`.


### 🗂️ Estrutura do Projeto

```
Lab-principle-o-banking-system/
├── app/
│   ├── controllers/     # Menu and control flow
│   ├── models/          # Entities: Account, Client, Transaction
│   ├── services/        # Business logic (deposit, withdraw, statement)
│   └── views/           # GUI with PyQt5
├── db/                  # Database connection and schema
├── libs/                # Locally installed dependencies (e.g., PyQt5)
├── install_libs.py      # Script to install dependencies
├── requirements.txt     # Dependency list
├── main.py              # Main entry point
```
---

## ▶️ Como Executar

1. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\Activate.ps1         # Windows
```

2. Instale as dependências na pasta `libs`:

```bash
python install_libs.py
```

3. Execute o projeto:

```bash
python main.py
```

---

## 📌 Requisitos

- Python 3.11+
- pip
- SQLite3 (já incluso com Python via `sqlite3`)
- Ambiente gráfico (necessário para rodar PyQt5)

---

## 🇺🇸 About the Project

This is a simple banking system simulation developed in **Python 3.11** without the use of frameworks, using **SQLite** for data persistence and **PyQt5** for the graphical interface.  
It includes a login system for user authentication, and supports **deposit**, **withdrawal** (with rules), and **bank statement** viewing via a user-friendly GUI.

### 📌 Features
- **Login**
  - Simple user and password validation for access.
- **Deposit**
  - Negative values are not allowed.
  - Stored and shown in the bank statement.
- **Withdraw**
  - Up to 3 withdrawals per day.
  - Max R$500 per withdrawal.
  - Only allowed with sufficient balance.
  - Stored and shown in the bank statement.
- **Bank Statement**
  - Lists all deposits and withdrawals.
  - Values displayed in `R$` format.

### 🗂️ Project Structure

```
Lab-principle-o-banking-system/
├── app/
│   ├── controllers/     # Menu and control flow
│   ├── models/          # Entities: Account, Client, Transaction
│   ├── services/        # Business logic (deposit, withdraw, statement)
│   └── views/           # GUI with PyQt5
├── db/                  # Database connection and schema
├── libs/                # Locally installed dependencies (e.g., PyQt5)
├── install_libs.py      # Script to install dependencies
├── requirements.txt     # Dependency list
├── main.py              # Main entry point
```

---

## ▶️ How to Run

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\Activate.ps1         # Windows
```

2. Install local dependencies into `libs/`:

```bash
python install_libs.py
```

3. Run the application:

```bash
python main.py
```

---

## 📄 Licença
```
Este projeto é livre para uso educacional.
```
