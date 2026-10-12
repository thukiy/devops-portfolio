# devops-portfolio

A small Java command-line program, built as the final project for the
CDS212 DevOps module at FH Graubünden. The project grows every week with
DevOps topics such as testing, CI/CD and containers.

## Prerequisites

- Java 21 (JDK)
- Git

## Installation / Setup

```bash
git clone https://github.com/thukiy/devops-portfolio.git
cd devops-portfolio
javac -d target/classes src/main/java/ch/fhgr/devops/App.java
```

## Usage

```bash
java -cp target/classes ch.fhgr.devops.App
# Hello, World!

java -cp target/classes ch.fhgr.devops.App Thuki
# Hello, Thuki!
```
