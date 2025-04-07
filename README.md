
# 🏥 Sistema de Gestão Odontológica

![Django](https://img.shields.io/badge/Django-5.1-green)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)

Um sistema completo para gestão de pacientes em clínicas odontológicas desenvolvido com Django.

---

## 📌 Índice

- [Funcionalidades](#✨-funcionalidades)
- [Tecnologias](#🛠️-tecnologias)
- [Instalação](#🚀-instalação)
- [Execução em outro PC](#💻-execução-em-outro-pc)
- [Estrutura](#📦-estrutura-do-projeto)
- [Como Contribuir](#🤝-como-contribuir)
- [Licença](#📄-licença)
- [Contato](#✉️-contato)

---

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

---

## 🛠️ Tecnologias

| Tecnologia       | Descrição                          |
|------------------|------------------------------------|
| Django 5.1       | Framework backend principal        |
| Bootstrap 5      | Estilização e componentes frontend |
| PostgreSQL       | Banco de dados (produção)          |
| SQLite           | Banco de dados (desenvolvimento)   |

---

## 🚀 Instalação

### ✅ Pré-requisitos

- Python 3.12+
- Git
- Pip (ou Pipenv)

### ✅ Passos

```bash
# Clone o repositório
git clone https://github.com/SudoMaster7/Clinica_Odonto_API.git
cd Clinica_Odonto_API

# Crie o ambiente virtual
python -m venv .venv

# Ative o ambiente virtual
# No Windows:
.venv\Scripts\activate
# No Linux/Mac:
source .venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Aplique as migrações do banco de dados
python manage.py migrate

# Crie um superusuário
python manage.py createsuperuser

# Rode o servidor
python manage.py runserver

# Acesse no navegador:
http://localhost:8000
```

---

## 💻 Execução em outro PC

Se quiser rodar o projeto em outro computador:

1. Copie os arquivos do projeto (sem a pasta `.venv`).
2. Instale o Python (recomenda-se mesma versão).
3. Crie um novo ambiente virtual:
   ```bash
   python -m venv .venv
   ```
4. Ative o ambiente:
   ```bash
   # Windows:
   .venv\Scripts\activate
   # Linux/Mac:
   source .venv/bin/activate
   ```
5. Instale os pacotes:
   ```bash
   pip install -r requirements.txt
   ```
6. Siga os comandos de migração e execução como acima.

---

## 📦 Estrutura do Projeto

```
clinica_odonto/
├── core/               # App principal
│   ├── templates/      # Templates HTML
│   ├── admin.py        # Administração Django
│   ├── models.py       # Modelos de dados
│   └── views.py        # Lógica de visualização
├── static/             # Arquivos estáticos
├── templates/          # Templates base
├── manage.py           # Utilitário Django
└── requirements.txt    # Dependências
```

---

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

---

## 📄 Licença

Distribuído sob licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## ✉️ Contato

🔗 Link do Projeto: [https://github.com/SudoMaster7/Clinica_Odonto_API](https://github.com/SudoMaster7/Clinica_Odonto_API)

---

## 🖼️ Screenshots

![Tela de Login](/docs/screenshots/login.png)
![Dashboard](/docs/screenshots/dashboard.png)

---

## 🔧 Badges

![GitHub last commit](https://img.shields.io/github/last-commit/SudoMaster7/Clinica_Odonto_API)
![GitHub issues](https://img.shields.io/github/issues/SudoMaster7/Clinica_Odonto_API)

---

## 🌐 Configuração para Produção

```bash
# Exemplo com Gunicorn + Nginx
gunicorn --bind 0.0.0.0:8000 clinica_odonto.wsgi
```

---

## 📋 Tabela de Rotas da API

| Endpoint                        | Método | Descrição                          |
|---------------------------------|--------|------------------------------------|
| `/api/pacientes/`               | GET    | Lista todos os pacientes           |
| `/api/pacientes/`               | POST   | Cria um novo paciente              |
| `/api/pacientes/<id>/`          | GET    | Detalha um paciente específico     |
| `/api/pacientes/<id>/`          | PUT    | Atualiza dados de um paciente      |
| `/api/pacientes/<id>/`          | DELETE | Remove um paciente                 |
| `/consultas/`                   | GET    | Lista todas as consultas           |
| `/consultas/<id>/`              | GET    | Detalhes de uma consulta           |
| `/consultas/criar/`             | POST   | Cria uma nova consulta             |
| `/consultas/editar/<id>/`       | PUT    | Edita uma consulta existente       |
| `/consultas/excluir/<id>/`      | DELETE | Exclui uma consulta                |
| `/fluxo_caixa/`                 | GET    | Lista os lançamentos do caixa      |
| `/fluxo_caixa/novo/`            | POST   | Cadastra novo lançamento           |
| `/fluxo_caixa/editar/<id>/`     | PUT    | Edita lançamento do caixa          |
| `/fluxo_caixa/excluir/<id>/`    | DELETE | Remove lançamento do caixa         |
| `/dentistas/`                   | GET    | Lista todos os dentistas           |
| `/dentistas/novo/`              | POST   | Adiciona novo dentista             |
| `/dentistas/editar/<id>/`       | PUT    | Atualiza dados do dentista         |
| `/dentistas/excluir/<id>/`      | DELETE | Remove um dentista                 |
| `/orcamentos/`                  | GET    | Lista todos os orçamentos          |
| `/orcamentos/novo/`             | POST   | Cria um novo orçamento             |
| `/pagamentos/`                  | GET    | Lista todos os pagamentos          |
| `/pagamentos/novo/`             | POST   | Registra novo pagamento            |

## 🛠️ Considerações Adicionais

- Este projeto utiliza o Django Admin para o gerenciamento avançado de dados.
- Há páginas HTML com Bootstrap 5 integradas para melhorar a experiência visual e responsiva.
- Os templates estão organizados por aplicação para facilitar a manutenção e expansão do sistema.

## 💡 Dicas para Produção

- Configure o `.env` com variáveis sensíveis como `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`.
- Use PostgreSQL no ambiente de produção.
- Faça deploy com Gunicorn + Nginx ou serviços como Heroku, Railway, Render, etc.
- Use serviços de e-mail para envio real de notificações.

## ✅ Status do Projeto

🚧 Em desenvolvimento — novas features e melhorias são bem-vindas!
