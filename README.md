# Controlar Brilho da Tela

Este projeto é um script em **Python** que limita automaticamente o brilho da tela para um valor máximo definido em um arquivo de configuração.
Ele é útil para evitar que o brilho ultrapasse um limite desejado, ajudando no **conforto visual** e na **economia de energia**.

---

## ✨ Funcionalidades

- Monitora continuamente o brilho da tela.
- Reduz o brilho automaticamente caso ultrapasse o limite definido.
- Permite configurar:

  - `max_brightness` → brilho máximo permitido (em %).
  - `recheck_time_seconds` → intervalo de tempo (em segundos) para verificar o brilho.

---

## 📦 Requisitos

- Python 3.7+
- Bibliotecas:

  ```bash
  pip install screen-brightness-control
  ```

---

## ⚙️ Configuração

Crie um arquivo chamado **`controlar_brilho_settings.ini`** no mesmo diretório do script com o seguinte conteúdo:

```ini
[controlar_brilho_settings]
max_brightness = 70
recheck_time_seconds = 60
```

---

## ▶️ Como executar

1. Clone ou baixe este repositório.
2. Instale as dependências:

   ```bash
   pip install screen-brightness-control
   ```

3. Execute o script:

   ```bash
   python controlar_brilho.py
   ```

O programa ficará em loop, monitorando e ajustando o brilho automaticamente.

---

## 📂 Estrutura de Arquivos

```
.
├── controlar_brilho.py              # Script principal
├── controlar_brilho_settings.ini    # Arquivo de configuração (criado pelo usuário)
└── README.md                        # Documentação do projeto
```

---

## 📝 Notas

- Por padrão, o brilho máximo inicial é **70%** e o intervalo de checagem é de **10 segundos**.
- Caso o arquivo `controlar_brilho_settings.ini` não exista ou esteja incorreto, o script continuará usando os valores padrão.
- Testado apenas em **Windows** (pode variar em Linux/Mac).
