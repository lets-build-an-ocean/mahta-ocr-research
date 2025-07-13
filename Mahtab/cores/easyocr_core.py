import easyocr
import cv2
import numpy as np


class easyOCR:
    def __init__(self, visualize = False):
        self.reader = easyocr.Reader(['ar', 'fa'])
        self.visualize = visualize

    def detect_text(self, image_path : str):
        results = self.reader.readtext(image_path)
        
        if self.visualize:
            image = cv2.imread(image_path)

        detected_text = []
        for (bbox, text, confidence) in results:
            if confidence > 0.1:  # Confidence threshold
                confidence = round(float(confidence), 2)
                detected_text.append({'text': text,'confidence': float(confidence)})
                
                if self.visualize:
                    pts = np.array(bbox, dtype=np.int32)
                    cv2.polylines(image, [pts], True, (0, 255, 0), 2)
                
        if self.visualize:
            cv2.imwrite('easyocr_result.jpg', image)
        
        return detected_text