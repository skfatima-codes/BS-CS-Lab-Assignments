#  CS-352 Lab Tasks – Object-Oriented Programming

**Author:** First Year (Second Semester) Student – UBIT Department, University of Karachi  
**Program:** BS Computer Science  
**Course:** CS-352 – Object-Oriented Programming (OOP)  

This repository contains my **lab tasks** for CS-352, showcasing different concepts of **Object-Oriented Programming** in Python, including **inheritance**, **constructor overloading**, **cloning**, and **command pattern**.

---

## 🧸 Lab Task 1 – Cuddly Toy Inheritance Program

###  Overview
This project demonstrates **class inheritance** and **method overriding** in Python.  
We start with a **base class** (`CuddlyToy`) and build more specific toys like **Teddy** and **Bunny**, which are then further specialized into **Engineer**, **Gardener**, **Clown**, and **BankManager**.

###  Features
- **Base Class**: `CuddlyToy` with basic attributes (name, size, color) and methods to set/get values.
- **Intermediate Classes**:
  - `Teddy` – a cuddly teddy bear with sounds and hugs.
  - `Bunny` – a bunny toy with playful actions.
- **Specialized Subclasses**:
  - `Engineer` (Blue Teddy) – can build robots and write code.
  - `Gardener` (Red Teddy) – can plant and water flowers.
  - `Clown` (White Bunny) – can tell jokes and do magic.
  - `BankManager` (Black Bunny) – can open accounts and print balances.
- Demonstrates:
  - **Inheritance**
  - **Encapsulation**
  - **Subclass-specific methods**

---

## 🔺 Lab Task 2 – Triangle Class (Constructor Overloading & Cloning)

###  Overview
This project demonstrates **constructor overloading** in Python by creating a `Triangle` class that can be initialized in multiple ways.  
It also includes:
- **Getter and Setter methods** for each side.
- A **clone method** to create a duplicate of an existing triangle.

### 🛠 Features
- **Multiple Constructors** (simulated via `*args`):
  1. **No arguments** → Default triangle with sides `1.0, 1.0, 1.0`
  2. **One argument** → Equilateral triangle (all sides equal)
  3. **Two arguments** → Isosceles triangle `(x, x, y)`
  4. **Three arguments** → Arbitrary triangle `(x, y, z)`
- **Getter & Setter** methods for encapsulation.
- **Cloning** feature using `clone_triangle()`.

--

## 🐢 Lab Task 3 – Turtle Command Pattern Drawing System

### 
 Overview
This project implements a **Pen-based Command Driven Drawing System** using **OOP** and the **Command Pattern** in Python.

It reads a string of commands (e.g., `F+F+F+F`) and executes them one by one to move a virtual turtle.  
- `F` → Move Forward  
- `+` → Turn Right (90°)  
- `-` → Turn Left (90°)  

The program tracks the turtle’s **coordinates** and path, and can be extended to draw **visual shapes** using Python’s `turtle` graphics module.

