# 🏠 SIGA 1.0 — Sistema Integrado de Gestão para Acolhimento

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white) ![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white) ![Status](https://img.shields.io/badge/Status-Prot%C3%B3tipo-yellow?style=for-the-badge)

## 📌 Motivação

O **SIGA** é um projeto autoral que une experiência em gestão de serviços de acolhimento com estudos em **Python, SQLite e SQL**. A proposta é explorar como informações administrativas e de ocupação podem ser organizadas em um sistema de apoio à gestão.

**SIGA 1.0 é um protótipo educacional**, não uma ferramenta pronta para uso operacional ou armazenamento de dados pessoais reais.

## ✅ O que já exploramos no Google Colab

O registro da primeira etapa apresenta funcionalidades experimentais de:

- Criação de tabela e consultas em banco **SQLite**;
- Cadastro e consulta de acolhidos;
- Busca de registros;
- Exibição da situação e disponibilidade dos leitos;
- Liberação de leitos;
- Navegação por menu no console e validação de opções.

### Código publicado

- [`src/siga_demo.py`](src/siga_demo.py) — **reimplementação demonstrativa**, usando dados fictícios;
- [`.gitignore`](.gitignore) — evita versionar arquivos locais do banco;
- [Origem das evidências](docs/ORIGEM_DAS_EVIDENCIAS.md).

> **Transparência técnica:** o notebook Python original do Colab ainda não foi recuperado como arquivo editável. O arquivo `siga_demo.py` é uma demonstração baseada nas funcionalidades registradas em capturas, **não uma cópia literal do código original**.

## ▶️ Como executar

Requer Python 3 (a biblioteca `sqlite3` já vem com Python):

```bash
python src/siga_demo.py
```

Será criado um arquivo `src/siga_demo.db` local, ignorado pelo Git. Insira **somente dados fictícios** para testar.

## 📸 Evidências da primeira versão

As evidências foram registradas no Google Colab e serão adicionadas na pasta `imagens/` em uma próxima atualização. Elas incluem:

1. Código Python, tabelas e consultas SQL;
2. Cadastro, consulta, busca e situação dos leitos;
3. Execução do menu e teste de opção inválida.

**Quando os prints forem publicados**, esta seção receberá as imagens com suas descrições. [Pasta de imagens (a ser preenchida)](imagens/).

## 🗺️ Próximas etapas

- Recuperar e preservar o código original do notebook;
- Aprimorar a organização em módulos e validações;
- Explorar recursos de estoque, manutenção e relatórios;
- Estudar indicadores e integração com Power BI;
- Planejar segurança, autenticação e trilhas de auditoria.

Esses itens estão no **planejamento**, não são recursos concluídos do SIGA 1.0.

## 🔐 Privacidade

O repositório **não contém** cadastros de pessoas reais, dados de saúde ou o banco `siga.db` original guardado no Drive. Antes de qualquer aplicação em serviço real, seriam necessários controles de acesso, governança de dados e adequação à LGPD.

---

**Desenvolvimento contínuo:** experiência em gestão + aprendizagem prática em Tecnologia e Dados.
