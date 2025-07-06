import cv2
import numpy as np
from PIL import Image
import os

def load_image_safe(img_path):
    """安全加载图像（兼容中文路径和损坏文件）"""
    # 检查文件是否存在
    if not os.path.exists(img_path):
        print(f"错误：文件不存在 - {img_path}")
        return None
    
    try:
        # 尝试用PIL+OpenCV方式加载（解决中文路径问题）
        pil_img = Image.open(img_path)
        img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
        if img is not None:
            print(f"成功加载图像，尺寸: {img.shape}")
            return img
    except:
        pass
    
    # 如果上述方法失败，尝试直接使用OpenCV
    try:
        img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_COLOR)
        return img
    except Exception as e:
        print(f"图像加载失败: {str(e)}")
        return None

# 配置参数
img_path = r'C:\Users\李玉瑾\Desktop\斗地主论文+源码\DouZero_For_HappyDouDiZhu-master\test.png'
capture_regions = [
    (414, 804, 1041, 59),    # 玩家区域
    (530, 470, 380, 160),    # 上家区域
    # 添加其他区域...
]

# 主程序
if __name__ == "__main__":
    # 1. 加载图像
    img = load_image_safe(img_path)
    if img is None:
        print("无法加载图像，程序退出")
        exit(1)
    
    # 2. 绘制所有区域
    for i, (x, y, w, h) in enumerate(capture_regions):
        # 检查区域是否有效
        if x < 0 or y < 0 or w <= 0 or h <= 0:
            print(f"跳过无效区域 {i}: ({x}, {y}, {w}, {h})")
            continue
            
        # 绘制矩形和标签
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(img, f'Area {i}', (x, y-10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
    
    # 3. 显示结果
    cv2.namedWindow("Debug", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Debug", 1200, 800)
    cv2.imshow("Debug", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # 4. 保存结果
    output_path = os.path.join(os.path.dirname(img_path), 'debug_output.jpg')
    cv2.imwrite(output_path, img)
    print(f"调试结果已保存到: {output_path}")