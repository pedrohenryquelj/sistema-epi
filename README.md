# Sistema de Solicitação e Controle de EPIs - CBS

Sistema web simples, feito em Python, para organizar a **solicitação, o registro e a contagem de Equipamentos de Proteção Individual (EPIs)** na empresa.

## 🚧 Status do Projeto

Em desenvolvimento. Fase atual: **Etapa 1 - ambiente e primeira página**.

## ❗ Problema

- Pedidos de EPI feitos de forma errada, de última hora e pessoalmente, sem conferência prévia.
- Contagem de estoque bagunçada e com falhas.
- Nenhum histórico confiável de quem retirou o quê e quando.

## 💡 Solução proposta

Uma página web de formulário, fácil de usar pelo celular, onde o funcionário:

1. Escolhe o EPI em uma lista com busca (ou usa a opção "Outro" para digitar).
2. Informa tamanho/número/tipo, nome completo e telefone.
3. Confirma o pedido.

Ao confirmar, o sistema:

- **Registra o pedido em uma planilha** (fonte oficial dos dados e da contagem).
- **Abre o WhatsApp com a mensagem pronta** para a empresa, no formato:
  `"(nome), solicito (EPI) tamanho/tipo (tamanho). Telefone: (telefone)"`

### Fluxo

```
Funcionário → Formulário web → Servidor Python → ┬→ Planilha (registro oficial)
                                                  └→ WhatsApp (aviso à empresa)
```

## 🧠 Decisões de projeto

| Decisão | Motivo |
|---|---|
| Lista com busca + opção "Outro" | Evita nomes diferentes para o mesmo EPI (padronização), o que mantém a contagem correta. |
| Catálogo de EPIs na própria planilha | Adicionar um EPI é só incluir uma linha, sem alterar o código. |
| Link `wa.me` em vez de API do WhatsApp | Custo zero e sem burocracia. A automação total pode ser avaliada no futuro. |
| Planilha como "banco de dados" inicial | Simples, visível para qualquer pessoa da equipe e fácil de auditar. |

## 🛠️ Tecnologias

| Ferramenta | Função |
|---|---|
| **Python 3.13** | Linguagem principal |
| **Flask** | Servidor web (rotas e páginas) |
| **Jinja2** | Templates HTML dinâmicos (já incluso no Flask) |
| **HTML + CSS** | Interface do formulário |
| **gspread** | Integração com o Google Sheets *(etapa 4)* |

## 📁 Estrutura do Projeto

```
sistema-epi/
├── main.py              # Ponto de entrada: cria o app e define as rotas
├── requirements.txt     # Dependências do projeto
├── templates/           # Páginas HTML
│   └── formulario.html
├── static/              # CSS, imagens e scripts (a criar)
├── package/             # Módulos Python do projeto
└── README.md
```

## 🚀 Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/pedrohenryquelj/sistema-epi.git
   cd sistema-epi
   ```

2. **Crie e ative o ambiente virtual:**
   * Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   * Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Rode o servidor:**
   ```bash
   python main.py
   ```

5. **Acesse no navegador:** http://127.0.0.1:5000

## 🗺️ Roadmap

- [X] Estrutura inicial do repositório
- [X] **Etapa 1:** Ambiente com Flask e primeira página no ar
- [ ] **Etapa 2:** Formulário de pedido (lista de EPIs com busca, tamanho, nome e telefone)
- [ ] **Etapa 3:** Geração da mensagem fixa e do link do WhatsApp
- [ ] **Etapa 4:** Registro dos pedidos no Google Sheets
- [ ] **Etapa 5:** Controle de estoque e gestão de validade
- [ ] **Etapa 6:** Publicação online para acesso pelo celular

## 📚 Glossário (para quem está aprendendo)

- **Servidor:** programa que fica esperando pedidos e responde com páginas ou dados.
- **Rota:** endereço do site ligado a uma função Python.
- **Template:** arquivo HTML que o Python preenche com dados.
- **venv:** ambiente isolado com as bibliotecas só deste projeto.
- **requirements.txt:** lista das bibliotecas necessárias para rodar o projeto.

---

**Desenvolvido por [pedrohenryquelj](https://github.com/pedrohenryquelj)**
