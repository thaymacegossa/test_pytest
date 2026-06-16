FROM python:3.11-slim

# # Definir variáveis de ambiente
# ENV PYTHONUNBUFFERED=1 \
#     PYTHONDONTWRITEBYTECODE=1 \
#     PIP_NO_CACHE_DIR=1

WORKDIR /app

# Copiar apenas requirements.txt primeiro (melhor cache)
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código do projeto
COPY . .

# Criar diretório para reports
RUN mkdir -p /app/coverage_reports

# Executar testes por padrão
CMD ["pytest", "-v", "--cov=tests", "--cov-report=html:/app/coverage_reports", "--cov-report=term"]