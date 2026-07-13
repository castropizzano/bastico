# BɅSTICOᴮᵀ

> **Knowledge. Refined.**  
> Especificação Funcional · Processo de Distribuição · Versão 1.0.0

---

## 1. Objetivo do Processo

Este documento especifica como o **BɅSTICOᴮᵀ** é empacotado a partir do código-fonte Python/Flet em executáveis nativos autocontidos para macOS e Windows, permitindo que um usuário final instale e utilize o software sem necessidade de terminal, sem instalar Python separadamente, e sem qualquer conhecimento técnico de desenvolvimento — em conformidade com o princípio de "Soberania de Dados (Local-First)" do MANIFESTO, que pressupõe uso direto na máquina do usuário.

Este é um processo de engenharia de distribuição, não um módulo do ecossistema de conhecimento (`ᴮᵀObserve` / `ᴮᵀSynthesize` / `ᴮᵀQuery`), e por isso não altera o Léxico definido em `ONTOLOGY.md`.

## 2. Restrições de Engenharia (Inegociáveis)

* **Build Nativo por Plataforma:** a geração do executável `.app`/`.dmg` (macOS) só pode ocorrer em ambiente macOS; a geração do `.exe` (Windows) só pode ocorrer em ambiente Windows. Esta é uma restrição técnica da toolchain Flutter subjacente ao Flet, não uma escolha de arquitetura do projeto.
* **Automação via CI, Zero Dependência de Hardware Físico Múltiplo:** para viabilizar builds em ambas as plataformas a partir de um único mantenedor (que não possui fisicamente Mac e Windows simultaneamente), o processo de empacotamento é obrigatoriamente automatizado via GitHub Actions, utilizando runners nativos de cada sistema operacional disponibilizados pela própria plataforma GitHub.
* **Gatilho por Tag de Versão:** a geração de novos executáveis é disparada exclusivamente pela criação de uma tag Git no padrão `vX.Y.Z` (ex: `v1.0.0`) na branch `main`, nunca por push direto de commits comuns. Isso preserva rastreabilidade absoluta entre binário distribuído e código-fonte auditável.
* **Zero-Terminal para o Usuário Final:** o artefato final de cada build (`.dmg`/`.app` para macOS, `.exe` para Windows) deve ser publicado como asset anexado à Release correspondente no GitHub, disponível para download direto via navegador. Nenhuma etapa de linha de comando, compilação local ou instalação manual de dependências pode ser exigida do usuário final.
* **Isolamento de Dados do Usuário no Empacotamento:** o processo de build deve empacotar exclusivamente código-fonte e runtime (Python + Flet). É proibido incluir `Inventory.json`, conteúdo de `_QUARENTENA_BASTICO/` ou qualquer artefato gerado localmente por execuções de teste dentro do executável distribuído.

## 3. Fluxo de Execução Prática

```text
[ Entrada: Tag de versão Git (ex: v1.0.0) na branch main ]
                       │
                       ▼
      1. Disparo automático do Workflow (GitHub Actions)
                       │
                       ▼
   2. Build paralelo em runners nativos (macOS + Windows)
                       │
                       ▼
        3. Empacotamento via toolchain do Flet
           (Python + Flet + código-fonte, sem dados de usuário)
                       │
                       ▼
     4. Publicação dos executáveis como assets da Release
                       │
                       ▼
[ Saída: .dmg/.app e .exe disponíveis para download direto
  na página de Releases do repositório ]
```

## 4. Limitações Conhecidas (Versão 1.0.0)

* **Ausência de Assinatura Digital:** sem um certificado de desenvolvedor pago (Apple Developer Program para macOS, certificado de Autenticode para Windows), os executáveis não são assinados digitalmente. Isso resulta em um aviso de segurança do sistema operacional (Gatekeeper no macOS, SmartScreen no Windows) na primeira execução, exigindo uma confirmação manual explícita do usuário (ex: "Abrir mesmo assim"). Isso não requer terminal, mas não é uma instalação de fricção zero.
* **Fora de Escopo:** distribuição via App Store / Microsoft Store; build para Linux; assinatura de código; atualização automática (auto-update) do executável instalado.

---

```text
BɅSTICOᴮᵀ // DOC_REF: docs/SPEC_DISTRIBUTION.md // VERSION: 1.0.0 // STATUS: STABLE
```
