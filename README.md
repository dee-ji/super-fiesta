# super-fiesta
A react-fastapi-postgres app for my personal testing

## Goals
- [ ] Create a frontend framework and landing page using React.js
- [ ] Connect the frontend with the backend using Axios
- [ ] Create a backend framework using FastAPI (Python)
- [ ] Build a PostgresDB and MongoDB and build APIs that only FastAPI is authorized to access
- [ ] Build Dockerfiles and docker-compose.yml files for development and production
- [ ] Build tests for both frontend and backend
- [ ] Bonus: Build a Hashicorp Vault to store environment variables

## Steps needed to build from scratch
1. First build the frontend using `cd frontend && npm create vite@latest vite-react-app -- --template react-ts && cd vite-react-app && npm install`
2. Create a virtual environment and install fastapi and uvicorn `cd backend && python3.11 -m venv venv && source venv/bin/activate/ && pip install fastapi uvicorn && pip freeze > requirements.txt`
3. You can currently run the `docker-compose.dev.yml` file, given you have the `.env` file ;) `docker-compose -f docker-compose.dev.yml up -d --build` to build and `docker-compose -f docker-compose.dev.yml down -v` to bring it all down