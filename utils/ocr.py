import pytesseract

def extract_text_from_image(processed_img):
    # Configura o Tesseract para focar na extração de números
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    
    # Realiza o OCR e extrai texto
    text = pytesseract.image_to_string(processed_img, config=custom_config)
    
    return text
