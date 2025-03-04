#!/bin/bash

# Variables
DB_NAME="fincenter_db"
DB_USER="your_db_user"
DB_PASSWORD="your_db_password"

# Step 1: Install PostgreSQL
echo "Installing PostgreSQL..."
brew install postgresql

# Step 2: Start PostgreSQL Service
echo "Starting PostgreSQL service..."
brew services start postgresql

# Wait for PostgreSQL to start
sleep 5

# Step 3: Create Database and User
echo "Creating database and user..."
psql postgres -c "CREATE DATABASE $DB_NAME;"
psql postgres -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"
psql postgres -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"

# Step 4: Verify Database and User
echo "Verifying database and user..."
psql postgres -c "\l"  # List all databases
psql postgres -c "\du" # List all users

echo "PostgreSQL setup complete!"
