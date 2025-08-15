# 🦸 Superhero & Villain Class Project

## Overview
This Python project demonstrates **Object-Oriented Programming (OOP)** concepts such as:
- **Class creation**
- **Attributes and methods**
- **Constructors (`__init__`)**
- **Inheritance**
- **Encapsulation**
- **Polymorphism**

The project features a **Superhero** defending their city and a **Villain** plotting evil plans, along with a separate **Polymorphism Challenge** using vehicles.

---

## 📂 Files
- `superheroes.py` — Contains the `Hero`, `Superhero`, and `Villain` classes, and an example usage.
- `vehicles.py` — Demonstrates polymorphism with different types of vehicles.

---

## 🏗️ Assignment 1: Superhero Classes
### Features
- **`Hero` Class**
  - Attributes: `name`, `power`, `city`
  - Methods: 
    - `introduce()` → Introduces the hero
    - `use_power()` → Displays their power in action

- **`Superhero` Class (inherits from `Hero`)**
  - Adds `special_move` attribute
  - Method: `use_special()` → Displays their ultimate move

- **`Villain` Class (inherits from `Hero`)**
  - Private attribute: `__evil_plan`
  - Method: `reveal_plan()` → Reveals the villain's secret plan

### Example Usage
```python
hero1 = Superhero("Night Falcon", "super speed", "Metropolis", "Lightning Strike")
villain1 = Villain("Shadow Fang", "dark magic", "Metropolis", "Steal the city’s power grid")

hero1.introduce()
hero1.use_special()

villain1.introduce()
villain1.reveal_plan()
