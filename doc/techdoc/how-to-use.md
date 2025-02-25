---
title: Using MAKE
author: Carston Wiebe
date: 24.2.2025

documentclass: scrartcl

toc: true
numbersections: true
indent: false
colorlinks: false

fontfamily: palatino
fontsize: 12pt
linestretch: 1.3
---

# Introduction

MAKE is the Python embedded-programming library used by
PROTO.  It is built on top of
[CircuitPython](https://circuitpython.org/), and is designed to be hardware
independent using a schema system to "swap out" different electrical
components.

# Writing Programs

Each program consists of two parts:  First you name the components
that you will use in the program, and then you take actions using those
named components.  In programming terms, you first define your variables and
instantiate your objects, and then you call your functions.

*(Note that you need to start every program with the same line:  `import make`.
This tells the robot that you want to use the MAKE library, so
that it knows where to look to find our code.)*

```python
import make

# name components
leftmotor = make.largemotor(port=6)
rightmotor = make.largemotor(port=7)

# take actions
leftmotor.spin(power=100)
rightmotor.spin(power=-100)

make.wait(seconds=2)

leftmotor.stop()
rightmotor.stop()
```

## Naming Components

## Taking Actions

# Advanced Topics

## Glossary Of Classes And Functions

## Creating Schema For New Components