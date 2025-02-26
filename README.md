# Python Developer Framework Challenge

## Overview

In this challenge, you will implement a simple CRUD (Create, Read, Update, Delete) API for managing a resource called Item. The Item model represents an entity with the following attributes:
name: (string) The name of the item (max length 100).
description: (string) A short description of the item.
price: (float) The price of the item.

The API should allow clients to:
Create a new Item
Read a list of items or a specific item
Update an existing item
Delete an item

You will implement this API in three frameworks: Django (with Django REST Framework), Flask, and FastAPI. Each framework will be implemented separately, but the resource and functionality will remain the same across all implementations.

## Installing dependencies

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```


## Running on VSCode

There is a launch file for launching all applications via VSCode. Click on the launch menu and it show the 3 different projects as runnable