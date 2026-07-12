# BɅSTICOᴮᵀ

> **Knowledge. Refined.**  
> Architectural Decision Record · ADR 0002

---

## Status
Aceito

## Contexto
O ecossistema do projeto exige o processamento de grandes volumes de dados sensíveis e pessoais (como acervos acadêmicos históricos) diretamente no ambiente do usuário. Aplicações baseadas em web (browsers) impõem restrições de segurança severas que impedem a varredura autônoma de diretórios locais, tornando o cálculo de hashes para desduplicação um processo lento e dependente de uploads custosos. O produto final precisa ser acessível, de uso imediato, leve e visualmente didático.

## Decisão
Fica estabelecido que o **BɅSTICOᴮᵀ** será construído como uma **Aplicações Desktop Offline** instalável (Mac/Win), utilizando a seguinte stack:
1. **Motor de Processamento:** Python. Escolhido por sua performance nativa na manipulação do sistema de arquivos (`os`), criptografia (`hashlib`) e facilidade de integração futura com APIs de IAs e Google Drive.
2. **Interface Visual (UI):** Flet. Escolhido por permitir a construção de interfaces gráficas modernas (baseadas em Flutter) utilizando exclusivamente a linguagem Python, eliminando a necessidade de gerenciar stacks híbridas (ex: Electron + Node + React) e mantendo o projeto gratuito e *open-source*.

## Consequências
* **Positivas:** Processamento ultrarrápido utilizando o hardware local; privacidade total (Zero-Cloud Data); dispensa de custos com servidores de hospedagem; ambiente unificado em uma única linguagem (Python).
* **Negativas:** Requer empacotamento específico para gerar executáveis (`.exe` e `.app`) para distribuição.

---

```text
BɅSTICOᴮᵀ // DOC_REF: docs/adr/0002-tech-stack-python-flet.md // VERSION: 1.0.0 // STATUS: STABLE
```
