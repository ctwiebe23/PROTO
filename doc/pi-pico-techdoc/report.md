---
title: PROTO Technical Documentation
subtitle: Promoting Robotics Opportunity Through Outreach
author: Carston Wiebe
date: March 31, 2025
---

# Introduction

# Hardware Design

: Raspberry Pi Pico pin assignments. \label{picopins}

| Wire       | Pi Pico pin | Micropython pin |
| ---------- | ----------: | --------------: |
| Motor A +  |       `GP0` |               1 |
| Motor A -- |       `GP1` |               2 |
| Motor B +  |       `GP2` |               4 |
| Motor B -- |       `GP3` |               5 |

: Motor driver pin assignments. \label{driverpins}

| Wire       | Driver pin |
| ---------- | ---------: |
| Motor A +  |      `in1` |
| Motor A -- |      `in2` |
| Motor B +  |      `in3` |
| Motor B -- |      `in4` |

# Software Design

# Testing
