# Project Name

## Table of Contents

1. [Overview](#overview)  
2. [Prerequisites](#prerequisites)  
3. [Setup](#setup)  
4. [Usage](#usage)  
   - [With Make](#with-make)  
   - [With Docker](#with-docker)  

---

## Overview

**Melu** is a app where you can see menus and basic info about local bars. This application can be run using `make` or Docker for an efficient development and deployment workflow.

---

## Prerequisites

Ensure you have the following tools installed:

- **Make**: Install via your package manager (e.g., `apt install make`, `brew install make`).  
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/).  
- (Optional) **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/).  
- **Node.js** (if needed): [Install Node.js](https://nodejs.org/).  

---

## Setup

1. Clone the repository:  
    ```bash
    git clone https://github.com/username/repository.git
    cd repository

---

## Usage

### With Make

Use `make` commands to streamline running the project. Common commands include:

- **Build the project**:  
    make build
- **Run the project**:
    make up

### With Docker

Use `docker` commands to run and build the project:

- **Build the project**:
    docker-compose build
- **Run the project**:
    docker-compose up
- **Build and run the project**:
    docker-compose up --build
