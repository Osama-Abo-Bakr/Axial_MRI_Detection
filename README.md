# Axial MRI Detection

## Overview
**Axial MRI Detection** is a cutting-edge AI-driven tool designed to assist in the analysis of axial MRI scans. Utilizing the YOLOv8 model, this project provides accurate and real-time detection of abnormalities within MRI images, classifying findings as either 'negative' or 'positive'. The project is built with an easy-to-use web interface powered by Streamlit, making it accessible for medical professionals and researchers.

## Features
- **Real-Time Detection:** Quickly processes MRI images and identifies areas of concern.
- **Classification:** Differentiates between 'negative' and 'positive' findings, helping to prioritize cases that may require further attention.
- **User-Friendly Interface:** Built with Streamlit, allowing users to upload images and receive immediate feedback through a web application.
- **Confidence Scoring:** Provides confidence levels for each detection, aiding in the decision-making process.

## Technology Stack
- **YOLOv8:** A state-of-the-art object detection framework used to identify abnormalities in MRI scans.
- **Streamlit:** A lightweight web framework that enables the creation of the interactive user interface.
- **Pandas & NumPy:** Essential for data manipulation and numerical computations.
- **OpenCV:** Handles image processing tasks, such as drawing bounding boxes around detected areas.

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Osama-Abo-Bakr/Axial_MRI_Detection.git
   cd Axial_MRI_Detection
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Pre-trained YOLO Model:**
   - Download the `axial_MRI.pt` model and place it in the project directory.

## Usage
1. **Run the Streamlit App:**
   ```bash
   streamlit run axial_mri_detection.py
   ```

2. **Upload MRI Image:**
   - Use the provided file uploader in the web app to upload an axial MRI image in `jpg` or `png` format.

3. **Analyze the Image:**
   - The uploaded image will be processed, and the app will display any detected abnormalities, highlighting them with bounding boxes and labels.

## Customization
- **Model Fine-Tuning:** You can retrain or fine-tune the YOLO model with additional MRI datasets to improve detection accuracy for specific conditions.
- **UI Enhancements:** Customize the Streamlit interface to better suit specific user requirements or integrate additional features, such as batch processing.

## Contributing
We welcome contributions from the community! Please feel free to open issues, suggest enhancements, or submit pull requests to improve the project.

## License
This project is licensed under the MIT License, which allows you to freely use, modify, and distribute the code.
