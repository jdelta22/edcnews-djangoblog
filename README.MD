# 📰 EDC News - Django Blog

Um portal de notícias desenvolvido com **Django**, permitindo que autores criem, editem e excluam suas próprias notícias através de um painel administrativo personalizado.

---

## 🚀 Funcionalidades

- 🔐 Sistema de autenticação (Login / Logout)
- 📝 CRUD completo de notícias
- 🛡️ Permissão para editar/deletar apenas a própria notícia
- 💬 Sistema de mensagens (feedback ao usuário)
- 🎨 Dashboard personalizado para autores
- 📂 Organização por categorias

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Django
- SQLite (ambiente de desenvolvimento)
- HTML5
- CSS3

---

## 📁 Estrutura do Projeto

```
edcnews-djangoblog/
│
├── authors/
├── news/
├── edcnews/
├── static/
├── media/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Como executar o projeto localmente

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/jdelta22/edcnews-djangoblog.git
cd edcnews-djangoblog
```

### 2️⃣ Crie e ative o ambiente virtual

Linux / Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Execute as migrações

```bash
python manage.py migrate
```

### 5️⃣ Crie um superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 6️⃣ Inicie o servidor

```bash
python manage.py runserver
```

Acesse no navegador:

```
http://127.0.0.1:8000/
```

---

## 👨‍💻 Autor

Desenvolvido por **João Pedro**  
GitHub: https://github.com/jdelta22

---

## 📄 Licença

Este projeto é open-source e pode ser utilizado como base para estudos e projetos pessoais.
