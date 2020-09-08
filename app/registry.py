" API para consulta de registros. "
from flask.views import MethodView
import os
from flask import request

class RegistryAPI (MethodView):
    """
        View para gerir as requisições
    """
    def __init__ (self):
        """
            Inicialização, define chave secreta para view
        """
        self.SECRET = os.environ.get('SECRET_KEY') or 'dev_key'

    def extract_secret_data (self, data):
        """
            Extrair informação de chave da requisição.
        """
        try:
            secret = data.get('secret', str)
        except:
            secret = None
        return secret
    
    def extract_month_data (self, data):
        """
            Extrair informação de nome da requisição.
        """
        try:
            month = data.get('month', str)
        except:
            month = None
        return month

    def get (self, reg_id=None):
        """
            Gerencia requisição GET
        """
        secret = self.extract_secret_data(request.args)
        month = self.extract_month_data(request.args)
        if secret != self.SECRET:
            return 'Chave secreta incorreta!'
        else:
            if reg_id is None:
                # retorna uma lista de registros
                pass
            else:
                # mostra um único registro
                pass
            return f'Listar os registros do mês {month}.'

    def post (self):
        """
            Gerencia requisição POST
        """
        secret = self.extract_secret_data(request.json)
        if secret == self.SECRET:
            return 'Cadastrar novo registro.'
        return 'Chave secreta incorreta'
    
    def delete (self, reg_id=None):
        """
            Gerencia requisição DELETE
        """
        secret = self.extract_secret_data(request.args)
        if secret != self.SECRET:
            return 'Chave secreta incorreta!'
        else:
            if reg_id is None:
                return 'Necessário informar o id do registro.'
            else:
                # mostra um único registro
                pass
            return 'Deletar um único registro.'
    
    def put (self, reg_id=None):
        """
            Gerencia requisição PUT
        """
        secret = self.extract_secret_data(request.args)
        if secret != self.SECRET:
            return 'Chave secreta incorreta!'
        else:
            if reg_id is None:
                return 'Necessário informar o id do registro.'
            else:
                # mostra um único registro
                pass
            return 'Atualizar um único registro.'
