from fastapi import Depends, FastAPI, HTTPException
import os
import uvicorn
from sqlalchemy.orm import Session
from database import database
from database import models

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/todos/")
def get_todos(db: Session = Depends(get_db)):
    try:
        todos = db.query(models.Todos).all()
        return {"todos": todos}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/todos/{todo}")
def add_todo(todo: str, db: Session = Depends(get_db)):
    try:
        db_todo = models.Todos(todo=todo)
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return {"message": f"Todo {todo} added successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/todos/{todo}")
def remove_todo(todo: str, db: Session = Depends(get_db)):
    try:
        db.query(models.Todos).filter(models.Todos.todo == todo).delete()
        db.commit()
        return {"message": f"Todo {todo} removed successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    config = os.environ.get("CONFIG", "dev")
    if config == "dev":
        uvicorn.run(
            "main:app",
            port=int(os.environ.get("PORT", 8000)),
            host=os.environ.get("BACKEND_URL", "localhost"),
            http=os.environ.get("HTTP_TYPE", "auto"),
            reload=bool(os.environ.get("RELOAD_APP", True)),
        )
    elif config == "prod":
        uvicorn.run(
            "main:app",
            port=int(os.environ.get("PORT", 8000)),
            host=os.environ.get("BACKEND_URL", "localhost"),
            http=os.environ.get("HTTP_TYPE", "auto"),
            reload=bool(os.environ.get("RELOAD_APP", False)),
        )
