# 💼 Lab-principle-o-banking-system

A simple command-line banking system built with **Python** and **SQLite**.  
Um sistema bancário simples via terminal, desenvolvido em **Python** e **SQLite**.

---

## 🇺🇸 English

### 📌 Project Description

This project simulates a basic banking system allowing deposits, withdrawals, and viewing bank statements. It uses object-oriented design and SQLite for data persistence.

### 🔧 Features

- **Deposit**
  - Rejects negative values
  - Records transactions for statements

- **Withdrawal**
  - Max 3 withdrawals per day
  - Limit of R$ 500.00 per withdrawal
  - Insufficient balance check
  - Transactions recorded for statement

- **Bank Statement**
  - Lists all deposits and withdrawals
  - Amounts displayed in R$ format

---

### 🧱 Project Structure

```
Lab-principle-o-banking-system/
├── Menu.py
├── Client.py          # id, name, cpf, age, account_id[]
├── Account.py         # id, branch_number, account_number
│   └── deposit(), withdraw(), bank_statement()
├── Transaction.py     # id, type, date, hour, account_id
└── database/
    ├── banco.db
    └── (optional) schema.sql
```

### 🗃️ Database Tables

- `client` — client information
- `account` — bank account info
- `transaction` — transaction history

---

### ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/marcelomorg/Lab-principle-o-banking-system.git
   cd Lab-principle-o-banking-system
   ```

2. Run the system:
   ```bash
   python Menu.py
   ```

---

## 🇧🇷 Português

### 📌 Descrição do Projeto

Este projeto simula um sistema bancário básico com suporte a depósitos, saques e extratos. Utiliza princípios de programação orientada a objetos e armazena os dados com SQLite.

### 🔧 Funcionalidades

- **Depósito**
  - Não permite valores negativos
  - Transações são registradas para o extrato

- **Saque**
  - Máximo de 3 saques diários
  - Limite de R$ 500,00 por saque
  - Verificação de saldo insuficiente
  - Saques são registrados para o extrato

- **Extrato**
  - Lista todos os depósitos e saques
  - Valores exibidos em formato R$

---

### 🧱 Estrutura do Projeto

```
Lab-principle-o-banking-system/
├── Menu.py
├── Client.py          # id, nome, cpf, idade, contas[]
├── Account.py         # id, número da agência, número da conta
│   └── deposit(), withdraw(), bank_statement()
├── Transaction.py     # id, tipo, data, hora, conta_id
└── database/
    ├── banco.db
    └── (opcional) schema.sql
```

### 🗃️ Tabelas no Banco de Dados

- `client` — dados dos clientes
- `account` — dados da conta bancária
- `transaction` — histórico de transações

---

### ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/marcelomorg/Lab-principle-o-banking-system.git
   cd Lab-principle-o-banking-system
   ```

2. Execute o sistema:
   ```bash
   python Menu.py
   ```

---

