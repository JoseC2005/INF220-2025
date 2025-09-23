import sys
import os

# Agregar el directorio controllers al path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from controllers.app import app

# Vercel requiere que la aplicación se llame 'application'
application = app

# Opcional: Handler para Serverless
def handler(request, context):
    return application(request, context)