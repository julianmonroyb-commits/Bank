# 🏦 Bank Management System

A modular banking system developed in **Python**, applying **Object-Oriented Programming (OOP)** principles and a layered architecture.

The project simulates basic banking operations such as creating accounts, making deposits, withdrawals, transfers, and managing customer information while keeping the code organized, scalable, and maintainable.

---

## 📌 Features

- Create bank accounts
- Deposit money
- Withdraw funds
- Transfer money between accounts
- Manage different account types
- Data persistence
- Audit logging
- Custom exception handling
- Modular architecture

---

## 📂 Project Structure

```
Bank/
│
├── Entities/
│   ├── bank_account.py
│   ├── checking_account.py
│   ├── savings_account.py
│   ├── premium_account.py
│
├── Logic/
│   └── bank.py
│
├── Persistence/
│   └── repository.py
│
├── Security/
│   └── audit.py
│
├── Exceptions/
│   └── errors.py
│
├── main.py
└── README.md
```

---

## 🏛 Architecture

The project follows a layered architecture where each module has a single responsibility.

### Entities

Contains the business models.

- BankAccount
- SavingsAccount
- CheckingAccount
- PremiumAccount

Each account type inherits from the base `BankAccount` class.

---

### Logic

Contains the business rules of the banking system.

Responsibilities include:

- Account creation
- Deposits
- Withdrawals
- Transfers
- Account management
- Validations

---

### Persistence

Responsible for storing and retrieving application data.

This layer can easily be replaced with a database implementation in the future.

---

### Security

Provides audit logging for important operations performed within the system.

---

### Exceptions

Defines custom exceptions to improve error handling and application reliability.

---

## 🚀 Technologies

- Python 3
- Object-Oriented Programming (OOP)
- Modular Design
- Exception Handling
- File Persistence

---

## ▶️ Getting Started

Clone the repository

```bash
git clone https://github.com/your-username/bank-management-system.git
```

Navigate to the project directory

```bash
cd bank-management-system
```

Run the application

```bash
python main.py
```

---

## 💡 Object-Oriented Concepts Used

- Classes
- Objects
- Inheritance
- Encapsulation
- Polymorphism
- Abstraction
- Composition

---

## 📈 Future Improvements
