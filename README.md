# 数字图像处理-画图板

## 主要技术

- PyQt5
- QtDesigner
- OpenCV

## 主要功能

- 文件管理
  - 新建
  - 打开
  - 保存
- 画图
  - 画笔
  - 油漆桶
  - 直线
  - 举行
  - 椭圆
  - 橡皮擦
- 图像处理
  - 旋转
  - 翻转
  - 调节
    - 亮度
    - 饱和度
    - 对比度
    - 色调
  - 灰度化
  - 二值化
  - 反相
  - 浮雕
  - 边缘检测
  - 模糊
  - 锐化

## 参考代码

https://github.com/BENULL/Paint

## 贡献

1. 将图像调节和图像反相的逐像素点计算改为了矩阵计算；
2. 为图像旋转和翻转增加了独立的对话框；
3. 修复了无法打开已有图像的问题；
4. 修复了新建图像后仍能恢复到之前图像的问题；
5. 修复了无法将`QImage`转化为`numpy.ndarray`的问题。

