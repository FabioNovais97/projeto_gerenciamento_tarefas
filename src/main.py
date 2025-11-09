from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Gerenciador de Tarefas - TechFlow")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "API de Gerenciamento de Tarefas - TechFlow Solutions"}

@app.post("/tasks/")
def create_task(title: str, description: str, prioridade: str = "Média", db: Session = Depends(get_db)):
    task = models.Task(title=title, description=description, prioridade=prioridade)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@app.get("/tasks/")
def list_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()

@app.put("/tasks/{task_id}")
def update_task(task_id: int, status: str, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    task.status = status
    db.commit()
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    db.delete(task)
    db.commit()
    return {"message": "Tarefa excluída com sucesso"}
