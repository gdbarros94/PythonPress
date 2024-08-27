import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///cms.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configurações de SEO
    SEO_TITLE = "Meu CMS"
    SEO_DESCRIPTION = "Um CMS poderoso e fácil de usar"
    SEO_KEYWORDS = "CMS, Flask, Python"

    # Suporte a múltiplos domínios
    ALLOWED_DOMAINS = ['example.com', 'example.org']

    # Outros parâmetros de configuração
    DEBUG = True
