# CPF Generator

Pacote Python leve para **geração** e **validação** de números de CPF brasileiros por meio de uma interface de linha de comando (CLI).

## Funcionalidades

* **Gerar CPF**: Produz CPFs válidos, nos formatos:

  * Formatado: `000.000.000-00`
  * Sem formatação: `00000000000`
* **Validar CPF**: Verifica a validade de CPFs, tanto formatados quanto sem formatação.
* **CLI Amigável**: Comandos simples construídos com `argparse`.
* **Teste Automatizado**: Cobertura completa de testes com `pytest`.

## Instalação

1. **Clone o repositório:**

```bash
git clone https://github.com/pycodebr/cpf_generator_test.git
cd cpf_generator
```

2. **Instale em modo editável:**

```bash
pip install -e .
```

   Isso registra o pacote no seu ambiente e permite:

   * Importações absolutas (`import cpf.generator`).
   * Execução da CLI via `python -m cli`.

## Uso

Execute a CLI a partir da raiz do projeto:

```bash
# Gerar CPF formatado (padrão)
python -m cli generate

# Gerar CPF sem formatação
python -m cli generate --raw

# Validar CPF formatado
python -m cli validate 529.982.247-25

# Validar CPF sem formatação
python -m cli validate 52998224725
```

> **Dica:** Se ocorrer erro de importação, verifique:
>
> 1. Você está na raiz do projeto.
> 2. O ambiente virtual ativo é o mesmo em que o pacote foi instalado.

## Estrutura do Projeto

```
cpf_generator/
├── src/
│   ├── cpf/
│   │   ├── generator.py      # Lógica de geração de CPF
│   │   └── validator.py      # Lógica de validação de CPF
│   └── cli.py               # Ponto de entrada da CLI
├── tests/
│   ├── test_generator.py    # Testes do gerador de CPF
│   └── test_validator.py    # Testes do validador de CPF
└── setup.py                 # Configuração do pacote
```

## Executar Testes

1. Instale o `pytest`, se ainda não tiver:

```bash
pip install pytest
```

2. Rode todos os testes:

```bash
pytest -v
```

## Contribuindo

1. Fork este repositório.
2. Crie uma branch de feature:

```bash
git checkout -b feature/NomeDaFuncionalidade
```
3. Faça seus commits:

```bash
git commit -m "Descrição da mudança"
```
4. Envie para sua branch:

```bash
git push origin feature/NomeDaFuncionalidade
```
5. Abra um Pull Request.

> Siga o guia de estilo PEP 8 e inclua testes para novas funcionalidades.

## Licença

Este projeto está sob a [Licença MIT](LICENSE).
