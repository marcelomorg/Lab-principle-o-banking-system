# Lab-principle-o-banking-system

## 🇧🇷 Sobre o Projeto

Este projeto simula um sistema bancário simples usando **Python 3.11** com persistência de dados via **SQLite**.  
Ele permite realizar **depósitos**, **saques** (com regras), e consultar o **extrato bancário**.

### 📌 Funcionalidades

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
├── App/
│   ├── controller/     # Controladores de menu e fluxo de execução
│   ├── domain/         # Entidades: Account, Client, Transaction
│   ├── repository/     # Comunicação com o banco de dados SQLite
│   ├── service/        # Regras de negócio (depósito, saque, extrato)
│   └── view/           # Textos exibidos ao usuário
├── db/                 # Conexão com banco, schema.sql e banco.db
├── main.py             # Ponto de entrada da aplicação
```

---

## 🇺🇸 About the Project

This is a simple banking system simulation developed in **Python 3.11** using **SQLite** for data storage.  
It supports **deposit**, **withdrawal** (with rules), and **bank statement** operations.

### 📌 Features

- **Deposit**
  - Negative values are not allowed.
  - Saved and shown in the bank statement.
- **Withdraw**
  - Up to 3 withdrawals per day.
  - Maximum of R$500 per withdrawal.
  - Must have enough balance.
  - Saved and shown in the bank statement.
- **Bank Statement**
  - Shows all deposits and withdrawals.
  - Values displayed in `R$` format.

### 🗂️ Project Structure

```
Lab-principle-o-banking-system/
├── App/
│   ├── controller/     # Menu and control flow logic
│   ├── domain/         # Entities: Account, Client, Transaction
│   ├── repository/     # Handles SQLite database access
│   ├── service/        # Business rules (deposit, withdraw, statement)
│   └── view/           # Texts shown to the user
├── db/                 # Database connection, schema, and .db file
├── main.py             # Main entry point
```

---

## ▶️ Como Executar

```bash
python3 main.py
```



---

## 📌 Requisitos

- Python 3.11+
- SQLite3 (já incluso no Python via `sqlite3`)

---

## 📄 Licença

Este projeto é livre para uso educacional.
