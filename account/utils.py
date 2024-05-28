import random

def code_generate():
    return ''.join([random.randint(1000, 100000) % 10 for i in range(6)])

def send_email():
    pass