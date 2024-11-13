from utils.preprocess import preprocess_image
from utils.ocr import extract_text_from_image
from utils.helpers import extract_numbers

def main(image_path):
    # 1. Pré-processamento da imagem
    processed_img = preprocess_image(image_path)
    
    # 2. Extração de texto usando OCR
    text = extract_text_from_image(processed_img)
    print("Texto extraído:", text)
    
    # 3. Extração de números a partir do texto
    numbers = extract_numbers(text)
    print("Números identificados:", numbers)

# Defina o caminho para a imagem
image_path = 'images/sample_image.webp'
main(image_path)
