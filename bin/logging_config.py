# https://github.com/WhyAskWhy/mysql2sqlite

"""Logging configuration for mysql2sqlite project"""

import logging
import logging.handlers
import sys

# TODO: Import __main__ and reference the value from there?
# import __main__
# app_name = __main__.app_name
app_name = 'mysql2sqlite'


# TODO: Configure formatter to log function/class info
file_formatter = logging.Formatter('%(asctime)s - %(name)s - L%(lineno)d - %(funcName)s - %(levelname)s - %(message)s')
stdout_formatter = logging.Formatter('%(levelname)s - L%(lineno)d - %(funcName)s - %(message)s')

# Grab root logger and set initial logging level
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler(stream=sys.stdout)
console_handler.setFormatter(stdout_formatter)
# Apply lax logging level since we will use a filter to examine message levels
# and compare against allowed levels set within the main config file.
console_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler(app_name + '.log', mode='a')
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.DEBUG)

# Create logger object that inherits from root and will be inherited by
# all modules used by this project
app_logger = logging.getLogger(app_name)
app_logger.addHandler(file_handler)
app_logger.addHandler(console_handler)
app_logger.setLevel(logging.DEBUG)
