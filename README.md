```markdown
# Weed vs Crop – YOLOv8 Demo

## 1. Environment Setup
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Train the Model
```bash
# GPU
yolo detect train data=data/data.yaml model=yolov8n.pt epochs=20 imgsz=640 device=0

# CPU
yolo detect train data=data/data.yaml model=yolov8n.pt epochs=20 imgsz=640 device=cpu
```

### Example Results
```
20 epochs completed in 0.022 hours.
Optimizer stripped from runs/detect/train2/weights/last.pt, 6.2MB
Optimizer stripped from runs/detect/train2/weights/best.pt, 6.2MB

Validating runs/detect/train2/weights/best.pt...
Ultralytics 8.3.191 🚀 Python-3.12.2 torch-2.5.1+cu121 CUDA:0 (NVIDIA GeForce RTX 4060 Laptop GPU, 7940MiB)
Model summary (fused): 72 layers, 3,006,038 parameters, 0 gradients, 8.1 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 2/2 11
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 2/2 11.4it/s 0.2s
                   all         60         60      0.801      0.778      0.854      0.403
                  weed         24         24      0.824      0.779      0.861       0.42
                  crop         36         36      0.779      0.778      0.848      0.386
Speed: 0.2ms preprocess, 1.7ms inference, 0.0ms loss, 0.2ms postprocess per image
Results saved to runs/detect/train2
```

## 3. Run Inference & Visualize
```bash
python test.py
```

### Example Output
Weed vs Crop_inference_results_03.09.2025.png

## 4. Data Source (Roboflow)
- Direct download:  
  https://universe.roboflow.com/ds/Qf2M6092L9?key=tkLqRm2lhW

- CLI download:
```bash
curl -L "https://universe.roboflow.com/ds/Qf2M6092L9?key=tkLqRm2lhW" > roboflow.zip \
&& unzip roboflow.zip \
&& rm roboflow.zip
```

## 5. Deployment
Deploy via Hugging Face, Streamlit, Flask, etc.

### Hugging Face (Gradio) Quick Start
1. **File Structure**
   ```
   ├── app.py
   ├── requirements.txt
   ├── README.md
   └── best.pt
   ```
2. **Create Space**  
   Go to https://huggingface.co/new-space → choose **Gradio** → upload files.

3. **What You Get**
   - Web UI for image upload  
   - Real-time detection & confidence scores  
   - Shareable public URL  

   Example: https://huggingface.co/spaces/XXuSea/YOLO_Weed_Detection
```
