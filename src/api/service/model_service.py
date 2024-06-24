import boto3
import joblib 
from io import BytesIO
import os
# Criar uma sessão boto3
session = boto3.Session()
# Criar um cliente S3 a partir da sessão boto3
s3_client = session.client('s3')
