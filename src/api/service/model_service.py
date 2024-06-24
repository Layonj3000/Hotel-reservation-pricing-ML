import boto3
import joblib 
from io import BytesIO
import os
# Criar uma sessão boto3
session = boto3.Session()
# Criar um cliente S3 a partir da sessão boto3
s3_client = session.client('s3')

def get_model(): 
    # Nome do bucket S3 onde o modelo está armazenado
    bucket_name = os.getenv("BUCKET_NAME")
    # Chave (caminho) do arquivo do modelo no bucket S3
    key = 'caminho para o seu modelo.joblib no S3'
    try:
        # Obter o objeto do S3
        response = s3_client.get_object(Bucket=bucket_name, Key=key)
        # Ler os bytes do corpo da resposta
        model_bytes = response['Body'].read()
        # Carregar o modelo a partir dos bytes usando joblib
        return joblib.load(BytesIO(model_bytes))
    
    except Exception as e:
        # Lançar uma exceção em caso de erro ao carregar o modelo do S3
        raise Exception("Erro ao carregar modelo do S3") from e