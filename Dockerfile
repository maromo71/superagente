# Use uma imagem Python como base
FROM python:3.10-slim

# Configurar o diretório de trabalho
WORKDIR /app

# Copiar os arquivos necessários
COPY . /app

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta padrão do Flask
EXPOSE 5000

# Comando para iniciar o aplicativo
CMD ["gunicorn", "app:app"]

