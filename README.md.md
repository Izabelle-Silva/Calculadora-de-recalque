# Calculadora de Recalque – Streamlit

Este projeto permite calcular **vazão**, **perda de carga**, **altura manométrica** e **potência útil da motobomba** de uma instalação de recalque hidráulico, usando uma interface web com o Streamlit.

---

##  Requisitos

- Python 3.8 ou superior
- Navegador (Chrome, Edge, etc.)
- Terminal (CMD, PowerShell ou VS Code)
- [Opcional] Visual Studio Code

---

## Instalação

1. **Baixe e extraia o projeto**
   - Arquivo: `recalque_streamlit.zip`
   - Pasta sugerida: `C:\recalque_streamlit`

2. **Instale o Streamlit**
   ```bash
   pip install streamlit
   ```

---

##  Como executar

1. **Abra o terminal**

2. **Navegue até a pasta do projeto**
   ```bash
   cd C:\recalque_streamlit
   ```

3. **Execute o aplicativo**
   ```bash
   streamlit run app_streamlit_recalque.py
   ```

---

##  Acesse o navegador

Depois de rodar o comando, o terminal exibirá:

```
Local URL: http://localhost:8501
```

Clique no link ou cole no navegador para abrir o app.

---

##  Funcionalidades disponíveis

- **Cálculo Completo**: executa todas as etapas (vazão → perdas → altura → potência)
- Cálculos individuais:
  - Vazão
  - Perda de carga
  - Altura manométrica
  - Potência útil e requerida (em W e HP)

---

##  Dicas

- Se `streamlit` não for reconhecido, tente:
  ```bash
  python -m streamlit run app_streamlit_recalque.py
  ```

- Ou adicione este diretório ao PATH:
  ```
  C:\Users\seu_usuário\AppData\Local\Packages\...\Python311\Scripts
  ```

---

##  Autor

Izabelle Slva de Souza