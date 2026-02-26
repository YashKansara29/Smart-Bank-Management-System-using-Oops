# 🏦 Simple Bank Management System

A robust, object-oriented Python implementation of a **Bank Management System**.
This project demonstrates core **Object-Oriented Programming (OOP)** principles including **Inheritance, Encapsulation, and Polymorphism** to manage different types of bank accounts.

---

## Key Features

### Savings Account

* Interest rate calculation
* Enforces minimum balance requirement
* Prevents withdrawals below defined threshold

### Current Account

* Integrated overdraft limit
* Allows withdrawals beyond balance within defined limit

### Encapsulation

* Protected balance attribute (`_balance`)
* Controlled access via class methods

### Transaction Logic

* Deposit and withdrawal operations
* Real-time balance updates
* Basic insufficient fund handling

---

## Architecture Overview

The system follows a hierarchical class design:

### `BankAccount` (Base Class)

**Attributes:**

* `account_number`
* `account_holder`
* `_balance`

**Methods:**

* `deposit()`
* `withdraw()`
* `get_balance()`
* `calculate_interest()`

---

### `SavingsAccount` (Child Class)

* Adds `interest_rate`
* Adds `minimum_balance`
* Overrides `withdraw()` to enforce minimum balance rule
* Overrides `calculate_interest()` for custom interest calculation

---

### 🔹 `CurrentAccount` (Child Class)

* Adds `overdraft_limit`
* Overrides `withdraw()` to allow overdraft within limit

---

## How to Run

###  Prerequisites

* Python 3.x installed

---

###  Installation & Execution

Clone the repository:

```bash
git clone https://github.com/your-username/bank-management-system.git
```

Navigate to the project directory:

```bash
cd bank-management-system
```

Run the script:

```bash
python bank_system.py
```

---

## Code Example

```python
# Create a Savings Account
savings = SavingsAccount(0.05, 500, "123", "John Doe", 1000)

savings.deposit(200)    # Balance: 1200
savings.withdraw(300)   # Balance: 900
savings.check_minimum_balance()
```

---

## Project Structure

```
bank-management-system/
│
├── README.md          # Project documentation
└── bank_system.py     # Main Python source code
```

## Future Improvements

* [ ] Integration with database (SQLite / PostgreSQL) for persistent storage
* [ ] Add logging system
* [ ] Implement transaction history tracking
* [ ] Multi-user authentication system
* [ ] REST API integration using FastAPI
* [ ] Graphical User Interface (GUI) using Tkinter
