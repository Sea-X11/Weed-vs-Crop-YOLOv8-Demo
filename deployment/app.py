import gradio as gr
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image

# Load model
model = YOLO("best.pt")

def predict(image):
    if image is None:
        return None, "Please upload an image"
    
    try:
        # Convert PIL to numpy
        image_np = np.array(image)
        
        # Run prediction
        results = model.predict(image_np, imgsz=640, conf=0.25)
        
        # Get annotated image
        annotated = results[0].plot()
        annotated = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
        
        # Get detection info
        boxes = results[0].boxes
        info = f"Detected {len(boxes)} objects\n"
        
        if len(boxes) > 0:
            for i, box in enumerate(boxes):
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])
                class_name = model.names[class_id]
                info += f"{class_name}: {confidence:.2f}\n"
        
        return annotated, info
        
    except Exception as e:
        return None, f"Error: {str(e)}"

# Create interface
with gr.Blocks(title="YOLO Weed Detection") as demo:
    gr.Markdown("# 🌱 Weed vs Crop Detection")
    gr.Markdown("Upload an image to detect weeds and crops")
    
    with gr.Row():
        with gr.Column():
            input_img = gr.Image(type="pil", label="Upload Image")
            
        with gr.Column():
            output_img = gr.Image(label="Detection Result")
            output_text = gr.Textbox(label="Detection Info", lines=5)
    
    # Auto-predict when image is uploaded
    input_img.change(predict, input_img, [output_img, output_text])

if __name__ == "__main__":
    demo.launch()