# Sistema de Gerenciamento de Tarefas - TechFlow Solutions

## 🎯 Objetivo
Este projeto foi desenvolvido como parte da disciplina de Engenharia de Software.  
O objetivo é aplicar metodologias ágeis para criar um sistema simples de gerenciamento de tarefas com CRUD e controle de qualidade automatizado.

## 🧩 Escopo
O sistema permite:
- Criar, listar, atualizar e excluir tarefas.
- Visualizar status (A Fazer, Em Progresso, Concluído).

## 🚀 Tecnologias
- **Python 3.10+**
- **FastAPI**
- **SQLite**
- **Pytest**
- **GitHub Actions (CI/CD)**

## 🔄 Metodologia Ágil
Foi adotado o **Kanban**, utilizando a aba *Projects* do GitHub:
- **To Do**: tarefas pendentes  
- **In Progress**: tarefas em andamento  
- **Done**: tarefas concluídas

## ⚙️ Execução local
```bash
# Clonar repositório
git clone https://github.com/seuusuario/projeto_gerenciamento_tarefas.git
cd projeto_gerenciamento_tarefas

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
uvicorn src.main:app --reload
```

Acesse: [http://localhost:8000/docs](http://localhost:8000/docs)

## 🧪 Testes automatizados
Os testes são executados via **Pytest**:
```bash
pytest
```

## 🔁 Integração Contínua
O repositório possui pipeline no GitHub Actions para rodar os testes automaticamente a cada *push*.

## 🔄 Mudança de Escopo
**Original:** CRUD básico de tarefas.  
**Mudança:** Adição do campo `prioridade` (baixa, média, alta) e filtro por prioridade.  
Justificativa: melhoria para priorização ágil de tarefas críticas.
