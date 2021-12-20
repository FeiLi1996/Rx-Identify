import cv2
import easyocr
from matplotlib import pyplot as plt
import numpy as np



#https://www.jaided.ai/easyocr/tutorial/

def detect_text_from_image(file_name):
    #3rd parameter result is the confidence percentatge
    #IMAGE_PATH='static/images/test20.png'
    IMAGE_PATH=f'static/uploads/{file_name}'
    reader = easyocr.Reader(['en'],gpu=False)
    # result = reader.readtext(IMAGE_PATH)
    result = reader.readtext(IMAGE_PATH)

    final_text=''
    final_confidence =0.00

    for text in result:
        final_text+= f'{text[-2]} '
        final_confidence += (text[-1])
    final_confidence = round(((final_confidence/3) * 100),2)
    print(final_text)
    print(round(final_confidence,2) ,'confidence')

    print(result)

    final_drug_info ={
        'detected_text':final_text,
        'confidence':final_confidence
    }

    return final_drug_info