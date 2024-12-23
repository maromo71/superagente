# CogniLens: Insights Orquestrados

![CogniLens Logo](link_para_a_sua_logo_aqui)

**Um Superagente para Análise e Coordenação de Tarefas**

## Autor

*   **Nome:** [Seu Nome Aqui]
*   **Email:** [Seu Email Aqui]
*   **GitHub:** [Seu Usuário no GitHub Aqui]
*   **LinkedIn:** [Seu Perfil no LinkedIn Aqui]

## Finalidade

CogniLens é um superagente projetado para automatizar a execução de tarefas complexas que envolvem análise de dados e coordenação de diferentes agentes. O sistema permite que usuários definam uma tarefa principal, especifiquem agentes com diferentes especialidades e habilidades, e configurem como esses agentes devem trabalhar em conjunto. O objetivo principal é simplificar a resolução de problemas complexos, fornecendo uma análise detalhada e um relatório final com insights valiosos.

## Objetivos

### Objetivos Gerais

*   Desenvolver um sistema flexível que possa ser adaptado a diferentes tipos de tarefas.
*   Criar um superagente capaz de orquestrar múltiplos agentes de forma eficiente.
*   Automatizar processos que normalmente requerem intervenção humana.
*   Gerar relatórios analíticos que auxiliem na tomada de decisões.
*   Simplificar a resolução de problemas complexos.

### Objetivos Específicos

*   Permitir que usuários definam tarefas e agentes através de uma interface web.
*   Permitir que os usuários definam a forma como os agentes trabalham (sequencial ou paralela).
*   Utilizar o modelo Gemini para análise de dados e geração de resultados.
*   Gerar relatórios finais em formato Markdown (.md).
*   Fornecer um relatório com análise do superagente de como o sistema pode ser melhorado.
*  Realizar a limpeza dos arquivos temporários corretamente.
*  Facilitar o deploy do sistema em plataformas como Render.
*  Usar variáveis de ambiente para as credenciais de API.

## Como Funciona

O CogniLens opera através dos seguintes passos:

1.  **Entrada do Usuário:** O usuário acessa a interface web e:
    *   Descreve a tarefa principal em linguagem natural.
    *   Define os agentes, especificando seus nomes, especialidades, responsabilidades e habilidades.
    *   Escolhe como os agentes devem trabalhar (sequencial ou paralelamente).
2.  **Orquestração da Tarefa:**
    *   O sistema recebe a descrição da tarefa, os dados dos agentes e a forma de coordenação.
    *   O superagente delega tarefas para cada agente, um de cada vez (na versão atual, sequencialmente) de acordo com suas responsabilidades, através de prompts para o Gemini.
    *   O Gemini age como o superagente que coordena os agentes e seus respectivos resultados.
3.  **Execução das Tarefas:** Cada agente executa sua parte da tarefa e retorna um resultado. O superagente armazena os resultados.
4.  **Análise e Geração do Relatório:** O superagente analisa o resultado e gera um relatório com:
    *   Descrição da tarefa principal.
    *   Dados de cada agente utilizado.
    *   Forma de coordenação dos agentes.
    *   Resultados gerados por cada agente.
    *  Uma analise do superagente.
    *   O relatório é gerado em formato Markdown (.md) e disponibilizado para download.
5.  **Download do relatório:** O usuário poderá baixar o relatório final, já em Markdown.

## Ferramentas e Tecnologias Usadas

*   **Python:** Linguagem de programação principal.
*   **Flask:** Framework web para criar a interface do usuário.
*   **Google Gemini:** Modelo de linguagem para análise de texto e geração de resultados.
*   **python-dotenv:** Para carregar variáveis de ambiente de arquivos `.env`.
*  **Gunicorn:** Para rodar o app Flask em produção.
*   **HTML, CSS, JavaScript:** Para criar a interface web.
*   **Bootstrap:** Framework CSS para estilização e responsividade.
*   **Render:** Plataforma de deploy.
*   **Git e GitHub:** Para versionamento e gestão de código (com repositório privado).
* **Docker:** Para o empacotamento da aplicação.

## Como Utilizar

1.  **Clone o repositório:**

    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd <NOME_DO_REPOSITORIO>
    ```
2.  **Crie um ambiente virtual (recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate   # No Linux ou macOS
    .\venv\Scripts\activate  # No Windows
    ```
3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```
4.  **Crie um arquivo `.env` na raiz do seu projeto e defina a variável de ambiente `GOOGLE_API_KEY` com sua chave API do Gemini.**
5.  **Execute a aplicação:**

    ```bash
    python app.py
    ```
6.  **Acesse a interface web:** Abra seu navegador e acesse o endereço que aparecer no terminal (geralmente [http://127.0.0.1:5000/](http://127.0.0.1:5000/)).
7.  **Preencha o formulário:** Insira a descrição da tarefa, defina os agentes e a forma de coordenação.
8.  **Execute a tarefa:** Clique no botão "Executar".
9.  **Baixe o relatório:** O relatório final será disponibilizado para download em formato Markdown.

## Próximos Passos

*   Implementar a execução paralela dos agentes.
*   Adicionar mais opções de configuração para os agentes.
*   Criar uma interface web mais intuitiva e com mais funcionalidades.
*   Adicionar mais ferramentas de análise e geração de resultados.
*  Aumentar o tratamento de erros e exceções.
*  Explorar outros modelos de linguagem.
*  Aprimorar a análise feita pelo superagente e suas sugestões.

## Licença

Este projeto é distribuído sob a licença MIT (adicione a sua licença, se preferir).

## Contribuições

Contribuições são bem-vindas! Se você tiver alguma ideia ou sugestão, por favor, abra um issue ou envie um pull request.