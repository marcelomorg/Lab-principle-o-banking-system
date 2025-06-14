
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    age INTEGER NOT NULL
    
);

CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    branch_number TEXT NOT NULL,
    account_number TEXT NOT NULL UNIQUE,
    balance REAL NOT NULL DEFAULT 0,
    client_id INTEGER NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(id)
);

CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT CHECK(type IN ('deposit', 'withdraw', 'bank_statement')) NOT NULL,
    value REAL NOT NULL CHECK(value > 0),
    date_hour TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    account_id INTEGER NOT NULL,
    FOREIGN KEY (account_id) REFERENCES accounts(id)
);

INSERT OR IGNORE INTO clients (name, cpf, age) VALUES ("Clienttest", "000.000.000.00", 90) ;
INSERT OR IGNORE INTO accounts (branch_number, account_number, balance, client_id) VALUES ("0001", "1001", 0, 1);