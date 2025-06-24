# Python Project: A Simple Streaming Service Plan Management System

A simple Python-based program simulating a subscription plan management system for a fictional streaming platform, **PacFlix**. PacFlix offers three subscription tiers — **Basic**, **Standard**, and **Premium** — each with its own services, pricing, and benefits. This program provides functionality for comparing plans, upgrading subscriptions for existing users, and applying referral-based discounts for new users.

---

## Objectives

### Learning Objectives
- Demonstrate proficiency in using **Object-Oriented Programming (OOP)** to build a Python program.
- Apply **clean code principles** aligned with **PEP8** style guidelines.
- Showcase **logical and structured problem-solving** through Python.

### Program Features

#### User Features
- `User()` → Base class storing the service plan database and allowing all users to view a comparison of plans.
- `ExistingUser()`:
  - `check_plan()` → Displays the current subscription plan details of the user.
  - `upgrade_plan()` → Enables plan upgrades. A **5% discount** is applied if the user has been subscribed for more than 12 months.
- `NewUser()`:
  - `pick_plan()` → Allows new users to register for a plan, with an optional **4% referral discount**.
  - Referral codes are verified securely via a private method to maintain system integrity.

---

## Tools Used

- **Language**: Python 3
- **Built-in Modules**:
  - [`tabulate`](https://pypi.org/project/tabulate/) – For neatly displaying subscription plans in table format

---

## Program Description

### 1. `pacflix.py`
This script defines the core class structure for the PacFlix subscription system. It supports:
- Viewing all available plans and their features
- Upgrading to higher-tier plans with eligibility checks and duration-based discounts
- Registering new users with optional referral validation and pricing logic

### 2. `test_case_pacflix.ipynb`
This Jupyter Notebook contains structured **test cases** that simulate:
- New user sign-ups (with and without referral codes)
- Plan upgrades by existing users
- Validation of invalid or unauthorized actions
- Real-world user interactions for functional verification

---

## How to Run the Program

1. Download both files:
   - `pacflix.py`
   - `test_case_pacflix.ipynb`

2. Place both files in the **same local directory**.

3. Open `test_case_pacflix.ipynb` in **Jupyter Notebook** or **VS Code with Jupyter support**.

4. Run the notebook cells step by step to explore and test all features.
