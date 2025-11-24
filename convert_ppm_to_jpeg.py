#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import cv2
from pathlib import Path

def convert_ppm_to_jpeg(source_dir="imgs", quality=95):
    """
    Chuyển đổi tất cả file PPM sang JPEG trong thư mục source_dir.
    Args:
        source_dir: Thư mục chứa các file PPM (mặc định là 'imgs').
        quality: Chất lượng JPEG (0-100, mặc định 95).
    """
    source_path = Path(source_dir)
    
    if not source_path.exists():
        print(f"Thư mục '{source_dir}' không tồn tại!")
        return
    
    # Tìm tất cả file .ppm
    ppm_files = list(source_path.rglob("*.ppm"))
    
    if not ppm_files:
        print(f"Không tìm thấy file .ppm trong '{source_dir}'")
        return
    
    print(f"Tìm thấy {len(ppm_files)} file PPM, bắt đầu chuyển đổi...")
    
    for ppm_file in ppm_files:
        try:
            # Đọc ảnh PPM
            img = cv2.imread(str(ppm_file))
            
            if img is None:
                print(f"Lỗi: Không thể đọc {ppm_file.name}")
                continue
            
            # Tạo tên file JPEG
            jpeg_file = ppm_file.with_suffix(".jpg")
            
            # Lưu ảnh dưới dạng JPEG
            cv2.imwrite(str(jpeg_file), img, [cv2.IMWRITE_JPEG_QUALITY, quality])
            
            print(f"✓ Chuyển đổi: {ppm_file.name} -> {jpeg_file.name}")
            os.remove(str(ppm_file))  # Xoá file PPM gốc
            
            
        except Exception as e:
            print(f"✗ Lỗi khi xử lý {ppm_file.name}: {str(e)}")
    
    print("Chuyển đổi hoàn tất!")

if __name__ == "__main__":
    convert_ppm_to_jpeg()
