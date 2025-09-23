import sys
import os

# Agregar el path para importar desde controllers
sys.path.append(os.path.dirname(__file__))

from controllers.app import app

# Vercel requiere que se llame 'application'
application = app

# Handler para Serverless Functions
def handler(request, context):
    return application(request, context)