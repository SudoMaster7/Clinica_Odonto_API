# 🏥 Sistema de Gestão Odontológica

![Django](https://img.shields.io/badge/Django-5.1-green)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)

Um sistema completo para gestão de pacientes em clínicas odontológicas desenvolvido com Django.

## 📌 Índice

- [Funcionalidades](#✨-funcionalidades)
- [Tecnologias](#🛠️-tecnologias)
- [Instalação](#🚀-instalação)
- [Estrutura](#📦-estrutura-do-projeto)
- [Como Contribuir](#🤝-como-contribuir)
- [Licença](#📄-licença)
- [Contato](#✉️-contato)

## ✨ Funcionalidades

### 📋 Cadastro de Pacientes
- **Dados pessoais completos**
- **Histórico médico**
- **Contatos e endereço**

### 🗓️ Gestão de Consultas
- Agendamento automático
- Lembretes por e-mail
- Histórico de atendimentos

### 📊 Painel Administrativo
- Relatórios completos
- Controle de usuários
- Dashboard interativo

## 🛠️ Tecnologias

| Tecnologia       | Descrição                          |
|------------------|------------------------------------|
| Django 5.1       | Framework backend principal        |
| Bootstrap 5      | Estilização e componentes frontend |
| PostgreSQL       | Banco de dados (produção)          |
| SQLite           | Banco de dados (desenvolvimento)   |

## 🚀 Instalação

### Pré-requisitos
- Python 3.12+
- Git
- Pipenv (opcional)

```bash
# Clone o repositório
git clone https://github.com/SudoMaster7/Clinica_Odonto_API.git
cd Clinica_Odonto_API

# Configure ambiente virtual (opções)
python -m venv venv       # Opção 1: venv
pipenv install            # Opção 2: pipenv

# Instale dependências
pip install -r requirements.txt

# Configure o banco de dados
python manage.py migrate

# Crie um superusuário
python manage.py createsuperuser

# Execute o servidor
python manage.py runserver
Acesse no navegador: http://localhost:8000
```

## 📦 Estrutura do Projeto

```
clinica_odonto/
├── pacientes/          # App principal
│   ├── migrations/     # Migrações do banco
│   ├── templates/      # Templates HTML
│   ├── admin.py        # Config admin
│   ├── models.py       # Modelos de dados
│   └── views.py        # Lógica de negócio
├── static/             # Arquivos estáticos
├── templates/          # Templates base
├── manage.py           # Script de administração
└── requirements.txt    # Dependências
```

## 🤝 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b feature/nova-feature
   ```
3. Commit suas mudanças:
   ```bash
   git commit -m 'Adiciona nova funcionalidade'
   ```
4. Push para a branch:
   ```bash
   git push origin feature/nova-feature
   ```
5. Abra um Pull Request

## 📄 Licença
Distribuído sob licença MIT. Veja LICENSE para mais informações.

## ✉️ Contato

🔗 Link do Projeto: [https://github.com/SudoMaster7/Clinica_Odonto_API](https://github.com/SudoMaster7/Clinica_Odonto_API)

---

## 🖼️ Screenshots

![Tela de Login](/docs/screenshots/login.png)
![Dashboard](/docs/screenshots/dashboard.png)

## 🔧 Badges

![GitHub last commit](https://img.shields.io/github/last-commit/SudoMaster7/Clinica_Odonto_API)
![GitHub issues](https://img.shields.io/github/issues/SudoMaster7/Clinica_Odonto_API)

## 🌐 Configuração para Produção

```bash
# Exemplo com Gunicorn + Nginx
gunicorn --bind 0.0.0.0:8000 clinica_odonto.wsgi
```

## 📋 Tabela de Rotas da API

| Endpoint               | Método | Descrição               |
|------------------------|--------|-------------------------|
| `/api/pacientes/`      | GET    | Lista todos pacientes   |
| `/api/pacientes/`      | POST   | Cria novo paciente      |
```

Esse formato está adequado para o GitHub, incluindo todas as seções e informações organizadas de forma clara. Você pode adicionar ou modificar conforme necessário!
