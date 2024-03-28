# Basic Demo Backend Code (without authentication)

## Overview
This repository contains a basic demo backend code built using FastAPI. The code provides various APIs for demonstration purposes, but it lacks authentication mechanisms. It serves as a reference for implementing backend logic and API endpoints.

## Usage

### Docker Command (if you want to run using Docker)
```bash
docker pull admindocker18/test
```

### Running with FastAPI
1. Navigate to the project directory:
```bash
cd Resources/Backend/Project/Project3/fast-api
```
2. Install the required dependencies:
```bash
pip3 install -r requirements.txt
```
3. Launch the FastAPI server:
```bash
uvicorn main:app --port 8000
```

## APIs
The backend code provides the following APIs:

1. `/` - GET
2. `/signup` - GET
3. `/signup` - POST
4. `/login` - GET
5. `/login` - POST
6. `/dashboard` - GET (unauthenticated - accessible without admin role)
7. `/getusers` - GET
8. `/forgot` - POST
9. `/message` - GET
10. `/message` - POST
11. `/getmessage` - GET
12. `/{path}` - OPTIONS

## Note
- This code is not intended for production use.
- Authentication mechanisms are not implemented in this codebase.
- This repository serves as a reference for basic backend logic and API development.
