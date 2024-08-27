#!/bin/bash

# Define the base directory
BASE_DIR="./"

# Create subdirectories and files

# app/controllers
mkdir -p $BASE_DIR/app/controllers
touch $BASE_DIR/app/controllers/main_controller.py
touch $BASE_DIR/app/controllers/admin_controller.py

# app/models
mkdir -p $BASE_DIR/app/models
touch $BASE_DIR/app/models/page.py
touch $BASE_DIR/app/models/user.py
touch $BASE_DIR/app/models/plugin.py
touch $BASE_DIR/app/models/telemetry.py
touch $BASE_DIR/app/models/db.py

# app/views/admin
mkdir -p $BASE_DIR/app/views/admin
touch $BASE_DIR/app/views/admin/dashboard.html
touch $BASE_DIR/app/views/admin/create_page.html
touch $BASE_DIR/app/views/admin/manage_plugins.html

# app/views/public
mkdir -p $BASE_DIR/app/views/public
touch $BASE_DIR/app/views/public/home.html

# app/static
mkdir -p $BASE_DIR/app/static

# app/uploads
mkdir -p $BASE_DIR/app/uploads

# app/plugins
mkdir -p $BASE_DIR/app/plugins

# app/temp
mkdir -p $BASE_DIR/app/temp

# app/hooks
mkdir -p $BASE_DIR/app/hooks
touch $BASE_DIR/app/hooks/hooks.py

# app/config
mkdir -p $BASE_DIR/app/config
touch $BASE_DIR/app/config/config.py
touch $BASE_DIR/app/config/routes.py

# app/docs
mkdir -p $BASE_DIR/app/docs
touch $BASE_DIR/app/docs/installation.md
touch $BASE_DIR/app/docs/usage.md
touch $BASE_DIR/app/docs/development.md

# Create the main.py file
touch $BASE_DIR/main.py

# Notify the user
echo "Project structure created successfully!"