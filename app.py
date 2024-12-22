from flask import Flask, render_template, request, send_file
import google.generativeai as genai
import os
import uuid

app = Flask(__name__)

# Configuração da API do Gemini
genai.configure(api_key="AIzaSyDBxkNd77mrygNI7orDEGymfUKl6rk2p1A")
model = genai.GenerativeModel('gemini-2.0-flash-exp') 

def criar_agente(nome, especialidade, responsabilidades, habilidades):
    """
    Cria um agente a partir dos parâmetros fornecidos.

    :param nome: nome do agente
    :param especialidade: especialidade do agente
    :param responsabilidades: responsabilidades do agente
    :param habilidades: habilidades do agente
    :return: um dicionário com as informações do agente
    """
    
    return {
        "nome": nome,
        "especialidade": especialidade,
        "responsabilidades": responsabilidades,
        "habilidades": habilidades,
    }

def executar_tarefa(tarefa, agentes, coordenação):
        """
        Executa uma tarefa passo a passo, pedindo para cada agente executar sua parte e retorna os resultados.

        :param tarefa: tarefa a ser executada
        :param agentes: lista de agentes a serem utilizados
        :param coordenação: como os agentes devem ser coordenados
        :return: um dicionário com os resultados, onde a chave é o nome do agente e o valor é o resultado da execução
        """
        resultados = {}
        prompt_inicial = f"""Você é um superagente. Sua tarefa é: {tarefa}. Você deve coordenar os seguintes agentes de forma {coordenação}. Os agentes são:"""

        for agent in agentes:
           prompt_inicial += f"""
             - **Agente**: {agent['nome']}.
             - **Especialidade**: {agent['especialidade']}.
             - **Responsabilidades**: {agent['responsabilidades']}.
             - **Habilidades**: {agent['habilidades']}.
            """

        prompt_inicial += "Agora, execute a tarefa passo a passo, pedindo para cada agente executar sua parte e me retorne os resultados no seguinte formato: ```nome_agente: resultado_agente```"

        resultados_str = model.generate_content(prompt_inicial).text
        linhas = resultados_str.strip().split("\n")
        for linha in linhas:
           if ":" in linha:
              nome_agente, resultado_agente = linha.split(":",1)
              resultados[nome_agente.strip()] = resultado_agente.strip()
        return resultados

def gerar_relatorio(tarefa, agentes, coordenação, resultados, analise_superagente):
        """
        Gera um relatório final com todos os dados da tarefa, agentes, coordenação, resultados e análise do superagente.

        :param tarefa: tarefa executada
        :param agentes: lista de agentes utilizados
        :param coordenação: como os agentes foram coordenados
        :param resultados: resultados da execução da tarefa por cada agente
        :param analise_superagente: análise do superagente sobre a execução da tarefa
        :return: um texto no formato markdown com o relatório final
        """
        relatorio_texto = f"""
        # Relatório Final #
        ## Tarefa ##
        {tarefa}
        ## Agentes ##
        """
        for agent in agentes:
            relatorio_texto += f"""
            ### {agent['nome']} ###
            - **Especialidade:** {agent['especialidade']}
            - **Responsabilidades:** {agent['responsabilidades']}
            - **Habilidades:** {agent['habilidades']}
            """
        relatorio_texto+= f"""
        ## Coordenação ##
        {coordenação}

        ## Resultados ##
        """
        for nome_agente, resultado_agente in resultados.items():
            relatorio_texto += f"""
            ### {nome_agente} ###
            {resultado_agente}
            """
        relatorio_texto +=f"""
        ## Análise do Superagente ##
        {analise_superagente}
        """
        return relatorio_texto


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Página principal do superagente.

    Se a requisição for um GET, renderiza a página HTML com o formulário de entrada.

    Se a requisição for um POST, executa a tarefa com os agentes e coordenação informados,
    gera um relatório e salva em um arquivo temporário e retorna o arquivo para download.

    Parameters
    ----------
    tarefa : str
        A tarefa a ser executada
    num_agentes : int
        Número de agentes a serem utilizados
    agentes : list
        Lista de agentes a serem utilizados
    coordenação : str
        Como os agentes devem ser coordenados
    resultados : dict
        Dicionário com os resultados da execução da tarefa por cada agente
    analise_superagente : str
        Análise do superagente sobre a execução da tarefa

    Returns
    -------
    str
        O relatório final em formato markdown
    """
    if request.method == "POST":
        tarefa = request.form["tarefa"]
        num_agentes = int(request.form["num_agentes"])
        agentes = []
        for i in range(num_agentes):
            nome = request.form[f"nome_agente_{i}"]
            especialidade = request.form[f"especialidade_agente_{i}"]
            responsabilidades = request.form[f"responsabilidades_agente_{i}"]
            habilidades = request.form[f"habilidades_agente_{i}"]
            agentes.append(criar_agente(nome,especialidade,responsabilidades,habilidades))
        coordenação = request.form["coordenação"]

        resultados = executar_tarefa(tarefa, agentes, coordenação)
        analise = model.generate_content(f"""Analise o relatório abaixo e dê sugestões de melhorias de como o sistema pode ser melhorado. Relatório: {resultados}""" )
        analise_superagente = analise.text
        relatorio = gerar_relatorio(tarefa, agentes, coordenação, resultados, analise_superagente)

        # Gera um nome de arquivo único para o relatório
        relatorio_filename = f"relatorio_{uuid.uuid4()}.md"
        # Salva o relatório em um arquivo temporário
        with open(relatorio_filename, "w", encoding="utf-8") as f:
            f.write(relatorio)
            
        return send_file(relatorio_filename, as_attachment=True, download_name="relatorio.md")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)