from google.cloud import vision

class GoogleOCR:
    def __init__(self):
        self.client = vision.ImageAnnotatorClient()
    

    def detect_text(self, image_path : str):
        with open(image_path, 'rb') as image_file:
            content = image_file.read()
    
        image = vision.Image(content=content)
    
        # Detect document text
        response = self.client.document_text_detection(image=image)
    
        if response.error.message:
            raise Exception(f'API Error: {response.error.message}')
    
        if response.full_text_annotation:
            return response.full_text_annotation.text
        else:
            return "No text found"



if __name__ == "__main__":
    gocr = GoogleOCR()
    text = gocr.detect_text("/home/mohsen/Desktop/homelab/mahta/output-03.png")
    print(text)