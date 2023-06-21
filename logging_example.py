#!python3

import logging

# Configure logging
logging.basicConfig(filename='example.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

# Log some information
logging.info('This is an informational message.')
logging.warning('This is a warning message.')
logging.error('This is an error message.')

