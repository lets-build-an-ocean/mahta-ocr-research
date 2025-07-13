import pytesseract
import cv2


class tesseractOCR:
    def __init__(self, visualize=False):
        pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # Adjust path if needed
        self.config = '--oem 3 --psm 6 -l ara+fas'
        self.visualize = visualize
        self.confidence_threshold = 0.1
    
    def detect_text(self, image_path: str):
        image = cv2.imread(image_path)
        data = pytesseract.image_to_data(image, config=self.config, output_type=pytesseract.Output.DICT)
        
        detected_text = []
        
        for i in range(len(data['text'])):
            text = data['text'][i].strip()
            confidence = float(data['conf'][i]) / 100.0  # Convert to 0-1 scale like EasyOCR
            
            if confidence > self.confidence_threshold and text:
                detected_text.append({
                    'text': text,
                    'confidence': confidence
                })
                
                if self.visualize:
                    x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        if self.visualize:
            cv2.imwrite('tesseract_result.jpg', image)
        
        return detected_text