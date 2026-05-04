import logging

logging.basicConfig(
    filename='logs/sistema.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def registrar_error(error):
    logging.error(error)
