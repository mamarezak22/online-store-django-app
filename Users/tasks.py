from celery import shared_task
from kavenegar import *
from dotenv import load_dotenv
import os

load_dotenv()
kavenegar_api_key = os.getenv("KAVENEGAR_API_KEY")

@shared_task
def send_code(phone_number : str,
             code : int)->None:
    global kavenegar_api_key
    api = KavenegarAPI(kavenegar_api_key)
    params = {'sender' : '2000660110', 'receptor': phone_number, 'message' : f"کد تایید شما : {code}"}
    api.sms_send(params)
    
        