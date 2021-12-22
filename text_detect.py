
import easyocr



def detect_text_from_image(file_name):

    IMAGE_PATH=f'static/uploads/{file_name}'
    reader = easyocr.Reader(['en'],gpu=False)
    result = reader.readtext(IMAGE_PATH)
    final_text=''
    final_confidence =0.00
    for text in result:
        final_text+= f'{text[-2]} '
        final_confidence += (text[-1])
    final_confidence = round(((final_confidence/(len(result))) * 100),2)
    final_drug_info ={
        'detected_text':final_text,
        'confidence':final_confidence
    }
    return final_drug_info