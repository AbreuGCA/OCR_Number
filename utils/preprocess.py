import cv2
import numpy as np

def preprocess_image(image_path):
    # Carrega a imagem
    img = cv2.imread(image_path)
    
    # Verifica se a imagem foi carregada
    if img is None:
        raise FileNotFoundError(f"Não foi possível carregar a imagem em {image_path}. Verifique o caminho.")
    
    # Converte para escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Aplicação de threshold para binarizar a imagem
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    
    # Remoção de ruídos com operações morfológicas
    kernel = np.ones((1, 1), np.uint8)
    processed_img = cv2.dilate(thresh, kernel, iterations=1)
    processed_img = cv2.erode(processed_img, kernel, iterations=1)
    
    return processed_img
