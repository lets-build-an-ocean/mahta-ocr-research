from google.cloud import vision


def extract_by_table_structure(image_path):
    client = vision.ImageAnnotatorClient()
    
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)
    
    # Get all text blocks
    blocks = []
    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            block_text = ""
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    word_text = ''.join([symbol.text for symbol in word.symbols])
                    block_text += word_text + " "
            
            blocks.append({
                'text': block_text.strip(),
                'bounding_box': block.bounding_box,
                'vertices': [(vertex.x, vertex.y) for vertex in block.bounding_box.vertices]
            })
    
    return blocks



if __name__ == "__main__":
    img = "/home/mohsen/Desktop/homelab/mahta/test-data/test-2.jpg"
    blocks = extract_by_table_structure(img)
    breakpoint()