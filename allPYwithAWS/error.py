import logging 
import boto3
from botocore.exceptions import ClientError



integer = 50 
string = "The number is"

try: 
   
    print (string + integer)
except TypeError as t_err:
    logging.warning("Error - {}. You cannot add a string to an integer, without converting the integer to a string first".format(t_err))
except ValueError as v_err:
    logging.warning("Error - {}. Your message".(v_err))