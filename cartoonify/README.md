# 🖼️ Cartoonify Image using OpenCV & K-Means Clustering

This project transforms regular images into cartoon-style artwork using **OpenCV**, **K-Means clustering**, and **image processing techniques** in Python. It’s a fun way to understand how machine learning and computer vision can be applied in creative ways.

---

## 📚 Table of Contents
- [🎯 Objective](#objective)
- [💡 Why This Project?](#why-this-project)
- [🔍 Project Overview](#project-overview)
- [🛠 Technologies Used](#technologies-used)
- [✨ Features](#features)
- [🚀 Room for Improvement](#room-for-improvement)
- [📬 Contact](#contact)

---

## Objective

To take a user-selected image and apply **cartoon-like effects** to it by combining:
- **Color simplification** using K-Means clustering,
- **Edge detection** using adaptive thresholding,
- And **blurring** techniques to smooth the image.

> The final cartoon-style image can be viewed and saved.

---

## 💡 Why This Project?

Inspired by popular photo filter apps like those on Instagram, this project demonstrates how cartoon effects can be created **without heavy tools** – just by using Python and OpenCV.

It also shows how **machine learning (K-Means)** and **image segmentation** can be used together to simplify and stylize images.

---

## 🔍 Project Overview

This is what happens in the project step by step:

1. **Image Loading**  
   The image is loaded using OpenCV and converted from BGR to RGB for proper visualization.

2. **Edge Detection**  
   Adaptive thresholding and median blurring are used to find strong edges and outline the shapes in the image.

3. **Color Quantization using K-Means**  
   Pixel colors are grouped into clusters to reduce the total number of colors. This creates a flat, cartoon-like base.

4. **Image Smoothing**  
   A **bilateral filter** is applied to keep edges sharp while smoothing the color areas.

5. **Combining Effects**  
   The filtered color image is combined with the edges to produce a final cartoonified output.

---

## 🛠 Technologies Used

- **Python** – Programming language
- **OpenCV** – For image processing (reading, converting, blurring, etc.)
- **NumPy** – To manipulate image pixel data as arrays
- **Matplotlib** – To display images during steps
- **Scikit-learn (KMeans)** – For clustering pixel colors into simplified groups

---

## ✨ Features

- 📂 **Load Image** – Load an image of your choice
- 🎨 **Cartoonify** – Apply edge detection,clustering, and smoothing
- 💾 **Save Image** – Option to save the final cartoonified result

---

## 🚀 Room for Improvement

- Currently supports processing one image at a time.  
  Could be extended to handle **multiple images in batch** mode.
- GUI can be added to make the project more user-friendly.

---

## 📬 Contact

😄 Created by – [Umair Khalil](https://www.linkedin.com/in/umair-khalil18/)

📧 Email – umairkhalil18@gmail.com

Feel free to connect or collaborate!
