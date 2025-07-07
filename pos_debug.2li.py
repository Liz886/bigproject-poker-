# 这个文件用来辅助调整截图区域坐标。运行游戏，全屏截图，放上路径，就可以查看截图区域。
# %%
import cv2
import numpy as np

# Modify the region parameters and the image path
capture_pos = [(290, 738, 1280,260),    # 玩家区域（右移距离，下移距离，宽度，高度）
               (430, 350, 400, 180),    # 玩家上家区域
               (1100, 350, 400, 180),   # 玩家下家区域
               (400, 100, 100, 140),    # 地主标志区域(玩家上家)
               (200, 650, 90, 140),    # 地主标志区域(玩家)
               (1420, 160, 110, 140),   # 地主标志区域(玩家下家)
               (770, 55, 370, 160)      # 地主底牌区域
               ]
img_path = r'C:\Users\李玉瑾\Pictures\Screenshots\屏幕截图 2025-07-07 145833.png'


# %%
img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), -1)
for pos in capture_pos:
    img = cv2.rectangle(img, pos[0:2], (pos[0] + pos[2], pos[1] + pos[3]), (0, 0, 255), 3)
cv2.namedWindow("test", 0)
cv2.imshow("test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
