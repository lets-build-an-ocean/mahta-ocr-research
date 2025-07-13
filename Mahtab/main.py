import os
from cores import easyocr_core, tesseract_core

images_path = "/home/mohsen/Desktop/homelab/mahta/test-data"
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif', '.webp')
image_list = [f for f in os.listdir(images_path) if f.lower().endswith(image_extensions)]

visualize_input = input("Visualize? [y|n]: ").strip().lower()
visualize = visualize_input in ['y', 'yes']

print("#" * 69)

easyocr_model = easyocr_core.easyOCR(visualize)
tesseract_model = tesseract_core.tesseractOCR(visualize)

for i, image in enumerate(image_list, 1):
    print(f"[{i}/{len(image_list)}] {image}")
    
    image_path = os.path.join(images_path, image)
    
    try:
        result_easyocr = easyocr_model.detect_text(image_path)
        result_tesseract = tesseract_model.detect_text(image_path)
        
        print(f"EasyOCR: {result_easyocr}")
        print(f"Tesseract: {result_tesseract}")
        
        if result_easyocr == result_tesseract:
            print("Match")
        else:
            print("Different")
            
    except Exception as e:
        print(f"Error: {e}")
    
    print()

print("Done")