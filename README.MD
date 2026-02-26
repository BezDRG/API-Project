Installation & Run
⃣ Backend
```bash
cd backend
python -m venv .venv
```
Windows:
```bash 

.venv\Scripts\activate
```
Mac/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run server:

```bash
uvicorn main:app --reload
```

Backend will be available at:

```
http://localhost:8000
```

Swagger documentation:

```
http://localhost:8000/docs
```

---
 Frontend

```bash
cd frontend
npm install
npm run serve
```

Frontend will be available at:

```
http://localhost:8080
``` 
