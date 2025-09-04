# Weed vs Crop – YOLOv8 Demo

1. environment setup: 
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

2. train the model:
```bash
#gpu
yolo detect train data=data/data.yaml model=yolov8n.pt epochs=20 imgsz=640 device=0
# or cpu
yolo detect train data=data/data.yaml model=yolov8n.pt epochs=20 imgsz=640 device=cpu


#my results for example:
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
💡 Learn more at https://docs.ultralytics.com/modes/train
VS Code: view Ultralytics VS Code Extension ⚡ at https://docs.ultralytics.com/integrations/vscode


4. run inference and visualize results:
```bash
python test.py

#my results for example:
Weed vs Crop_inference_results_03.09.2025.png

5. data source:(roboflow)
#The direct link to download your zip file is:
https://universe.roboflow.com/ds/Qf2M6092L9?key=tkLqRm2lhW

#Use this code to download and unzip your dataset via the command line on any *nix machine:
curl -L "https://universe.roboflow.com/ds/Qf2M6092L9?key=tkLqRm2lhW" > roboflow.zip; unzip roboflow.zip; rm roboflow.zip

6.deployment:
You can deploy the model using various platforms such as huggingface, streamlit, flask, etc. For example, to deploy on Hugging Face, you can follow these steps:
## Deployment Steps

### 1. File Structure
Upload these files to your Hugging Face Space:
```
├── app.py
├── requirements.txt  
├── README.md
└── best.pt (your model file)
```
### 2. Deploy on Hugging Face
1. Go to https://huggingface.co/new-space
2. Choose "Gradio" as SDK
3. Upload all files above
4. Your model will be available as a web app

### 43. What You Get
- Web interface for image upload
- Automatic detection display
- Confidence scores
- Shareable public URL

