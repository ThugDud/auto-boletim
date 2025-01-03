# Boletim Automático

Este é um projeto simples que combina uma interface HTML e um script Python para criar boletins escolares automaticamente em formato PDF.

## Estrutura do Projeto

- **`interfacesla.html`**  
  Uma página HTML básica que simula um formulário para entrada de dados, incluindo nome do aluno e suas notas.

- **`main.py`**  
  Um script Python que utiliza a biblioteca `fpdf` para gerar boletins escolares no formato PDF. O boletim inclui:
  - Nome do aluno
  - Turma
  - Notas por matéria
  - Status de aprovação por matéria (baseado na nota mínima de 6.0)

## Pré-requisitos
- Python instalado (versão 3.6+ recomendada)
- Biblioteca `fpdf` instalada:
  ```bash
  pip install fpdf

## Licença
Este projeto não possui uma licença específica e foi criado apenas para fins de aprendizado pessoal.
