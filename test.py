from ultralytics import YOLO
import cv2

model = YOLO("runs/detect/train2/weights/best.pt")
results = model.predict( "data/test/images/DSC_0188_JPG.rf.bf57d195d3b907689ee3a4d1a97b3d51.jpg", imgsz=640, conf=0.25)

# 画框并弹窗查看
annotated = results[0].plot()
cv2.imshow("Weed vs Crop", annotated)
cv2.waitKey(0)
cv2.destroyAllWindows()