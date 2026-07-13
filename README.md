# BɅSTICOᴮᵀ

> **Knowledge. Refined.**  
> Um instrumento leve, simples e objetivo para o refinamento computacional do conhecimento.

---

## Visão Geral

O **BɅSTICOᴮᵀ** nasce da convicção de que conhecimento não se reduz a dados armazenados. O conhecimento emerge quando as relações entre artefatos digitais tornam-se perceptíveis, formando estruturas coerentes capazes de serem observadas, interpretadas e continuamente refinadas. Ele atua como um filtro purificador de legados digitais, preparando acervos caóticos para serem consumidos com alta fidelidade por modelos de IA (LLMs).

## Arquitetura e Stack Tecnológica

O sistema é projetado sob uma arquitetura **Local-First** (offline), garantindo privacidade e processamento de alta velocidade direto na máquina do usuário.
* **Motor Lógico:** Python (Manipulação de I/O, criptografia SHA-256 para desduplicação e APIs de Nuvem).
* **Interface Visual:** Flet (Geração de executáveis nativos desktop para Mac/Windows via Flutter).

## Organização Física (Plana)

Para manter o escopo enxuto e de alta visibilidade, o projeto adota uma estrutura de documentação sem aninhamentos complexos:

```text
bastico/
├── README.md           <-- Este portal de entrada
├── LICENSE.md          <-- Termos legais do projeto (MIT)
├── requirements.txt    <-- Dependências Python do projeto
├── .gitignore           <-- Exclusões de versionamento (dados do usuário e ambiente)
├── observe.py           <-- Motor do módulo ᴮᵀObserve
├── app.py               <-- Interface Flet e módulo de Quarentena
└── docs/
    ├── MANIFESTO.md    <-- Filosofia, Identity e Governança unificadas
    ├── ONTOLOGY.md     <-- Modelo conceitual e Léxico de desenvolvimento
    ├── SPEC_OBSERVE.md <-- Especificação Funcional do Módulo Base
    ├── SPEC_QUARANTINE.md <-- Especificação Funcional do Módulo de Quarentena
    └── adr/
        ├── 0001-documentation-precedes-code.md <-- A lei de engenharia do sistema
        └── 0002-tech-stack-python-flet.md      <-- Decisão de Stack e Plataforma
```

## Ecossistema de Módulos

O desenvolvimento do software é incremental e dividido em componentes focados:

* **`ᴮᵀObserve` (Ciclo Atual):** Mapeamento passivo. Abre um *Corpus*, descobre *Artifacts*, calcula hashes (*Fingerprints*), lê metadados e constrói um *Inventory*. Operação estritamente *read-only*, garantindo a base de identificação única que viabiliza etapas posteriores de resolução de duplicatas.
* **Módulo de Quarentena (Ciclo Atual):** Camada de ação sobre o *Inventory* mapeado. Agrupa *Artifacts* por *Fingerprint* idêntica e permite o isolamento físico (*soft delete*) de redundâncias em diretório de quarentena, sem exclusão definitiva. Ver `docs/SPEC_QUARANTINE.md`.
* **`ᴮᵀSynthesize` (Planejado):** Aplicação de ontologias e estruturação semântica sobre o inventário mapeado.
* **`ᴮᵀQuery` (Planejado):** Mecanismo objetivo de busca, consulta e rastreabilidade do conhecimento generativo.

## Regra de Ouro

Este projeto é estritamente orientado ao conhecimento. Nenhuma linha de código de produção é escrita antes que a documentação técnica correspondente esteja consolidada no repositório (Princípio de Engenharia do ADR-0001).

---

```text
BɅSTICOᴮᵀ // DOC_REF: README.md // VERSION: 1.1.0 // STATUS: STABLE
```
