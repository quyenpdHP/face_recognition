# face_recognition
Dự án sử dụng Yolov6Face + Arcface để nhận diện danh tính của khuôn mặt

# Cài đặt môi trường  
Sử dụng docker:
Bước 1: docker pull quyenpd/quyenpd:v1.1
Bước 2: docker run -dit --ipc=host -v $(pwd):/face_detect_yolov6 --name quyenpd quyenpd/quyenpd:v1.1
Bước 3: docker exec -it quyenpd /bin/bash

# Cách chạy (trong container docker)  
python main.py --source data/images/image1.jpg --weights weights/yolov6s-face.pt