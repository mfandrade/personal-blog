# Personal Blog

**Personal Blog** é uma simples aplicação de exemplo implementando uma
intuitiva lógica de negócio de um blog em [Django Framework](https://www.djangoproject.com/).

Seu objetivo é ser uma aplicação funcional para fins de demonstração de
implantação e boas práticas em DevOps, além, é claro, de poder ser utilizada
como referência também para estudo de Python e Django.

![Tela inicial](screenshot.png)

# TOC

<!--toc:start-->

- [Pré-requisitos](#pré-requisitos)
- [Executando](#executando)
<!--toc:end-->

## Pré-requisitos

- Python
- Django
- Docker
- Make

## Executando

1. Clone este repositório

```bash
git clone https://github.com/mfandrade/personal-blog
```

2. Execute-o localmente

```bash
cd personal-blog
make
```

3. Acesse a aplicação no endereço <http://localhost:8080>

## Configuração de DB

Localmente, a aplicação utiliza SQLite como banco de dados.

Em desenvolvimento, edite as configurações de banco de dados diretamente no
arquivo `.env.local`. Este arquivo, quando existir, será preferencialmente
usado para conter as configurações de acesso a banco de dados local.

Já em produção, remova-o ou renomeie-o para `.env` defina as configurações
de acordo.

**ATENÇÃO!** Este arquivo `.env`, por conter credenciais de acesso a dados
de produção é ignorado pelo git e não deve ser incluído no controle de versão.
