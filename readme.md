# Create revision file inside docker
`docker compose exec backend alembic revision -m "your message here"`

# Run migration inside docker
`docker compose exec backend alembic upgrade head`

# Install the git hook script
`pre-commit install`

# Run all hooks on all files
`pre-commit run --all-files`

# Check for updates and automatically upgrade pre-commit configuration file 
`pre-commit autoupdate`


# Adresses
PGADMIN: localhost:5050
API DOCS: localhost:8008/api/docs