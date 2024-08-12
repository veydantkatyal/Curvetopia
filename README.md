# Curvetopia

Curvetopia is an advanced web application designed to seamlessly create, visualize, and manipulate complex curves and shapes with precision and ease.

## Table of Contents

- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setting Up](#setting-up)
- [Usage](#usage)
  - [Google Colab Notebook](#google-colab-notebook)
  - [Streamlit Web App](#streamlit-web-app)
- [Dataset](#dataset)
- [Examples](#examples)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Welcome to Curvetopia! This project is a part of the round 2 of Adobe Gensolve Hackathon. It is a cutting edge web application to identify, regularize and beautify curves in 2D Euclidean space.

## Problem Statement

View the enclosed PDF for understanding the problem statement
[PDF](https://drive.google.com/file/d/1SLqlw6CdDyNZARHDdFShJlumgSMbRN2h/view?usp=sharing)



## Features

- **Model Training & Prediction**: Train machine learning models to predict and manipulate shapes.
- **Interactive Visualization**: Use the Streamlit web app to visualize input and output files side by side.
- **Google Colab Integration**: Seamlessly work with the provided Google Colab notebook for data processing and model training.
- **Responsive Design**: A clean and responsive design for better usability.
- **Integration with Google Drive**: Easily link your Google Drive files for input and output.
- **Zoom and Pan**: Interactive zoom and pan features for detailed inspection of SVG images.

## Installation

### Prerequisites

- **Python 3.7+** 
- **Git** 
- **Google Drive Account** for accessing the dataset.

### Setting Up

1. **Clone the Repository**

   ```bash
   git clone https://github.com/veydantkatyal/curvetopia.git
   cd curvetopia
2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install Depedencies**

   ```bash
   pip install -r requirements.txt
4. **Run the Streamlit App**

   ```bash
   streamlit run app.py
## Usage

### Google Colab Notebook

#### Access the Notebook

Open the [Curvetopia Colab Notebook](https://colab.research.google.com/drive/1Wu4HmXblaEB24dGmTsX60mRvWZUq3PEC?usp=sharing) to get started.

#### Follow the Instructions

The notebook is structured with detailed instructions. Follow each cell sequentially to:

1. Set up the environment.
2. Load and preprocess data.
3. Train the model.
4. Generate predictions.

#### Saving and Accessing Outputs

Outputs, including generated SVGs, are saved to your Google Drive for easy access and integration with the Streamlit app.

## Streamlit Web App

### Access the App

Visit the [Curvetopia Web App](https://curvetopia.onrender.com).

### Provide Input file Link

Enter the Google Drive link of your input file in the provided text box.

### View Results

- The app will display the input and the expected output from our dataset.
- Use the visualization tools to zoom and inspect the details.

### GitHub Repository for Links

For sample input and output SVGs, refer to the **Example Dataset** section in the [GitHub repository](https://github.com/veydantkatyal/Curvetopia).

## Dataset

The dataset comprises pairs of input and output files. Each input file represents an initial shape, and the corresponding output file showcases the expected transformation.

### Sample Dataset

- **Input Files:** [Google Drive Input Folder](https://drive.google.com/drive/folders/1HhsnrRtZZQ7e0KAz_QcvUpWCMAI_gBXU?usp=sharing)
- **Output Files:** [Google Drive Output Folder](https://drive.google.com/drive/folders/1Uyq27oWASkiqtjSkbdl_wGH_zr6uL791?usp=sharing)

### Examples

Here are some example pairs you can use to test the application:

**Example 1**
- **Input:** [Input](https://drive.google.com/file/d/1MLtwF0Hsq9RuVKbzuT649tQKda0frdDz/view?usp=sharin)
- **Output:**[Output](https://drive.google.com/file/d/1kJ3lMqjE74Eg9YAaamyhqet_nP0NdpMX/view?usp=sharing)

**Example 2**
- **Input:** [Input](https://drive.google.com/file/d/1U4hl7m-KPMvqShjwvkqS-9t_85u-_QHd/view?usp=sharing)
- **Output:** [Output](https://drive.google.com/file/d/1L76izM3jr-g_qMYKzk6NtbXL2KbuGoA-/view?usp=sharing)


## Technologies Used

- **Python 3.7+**
- **Streamlit:** 
- **Google Colab:** 
- **CairoSVG:** SVG to PNG conversion
- **Pillow:** Image processing
- **Plotly:** 
- **gdown:** Downloading files from Google Drive
- **GitHub:**

## Contributing

Contributions are welcome! To contribute:

1. **Fork the Repository**
   - Click the 'Fork' button at the top right of the repository page.

2. **Clone Your Fork**
   ```bash
    git clone https://github.com/veydantkatyal/curvetopia.git
3. **Create New Branch**
   - Click the 'Fork' button at the top right of the repository page.

4. **Make your Changes**

4. **Commmit and Push**
   ```bash
   git add .
   git commit -m "Add your commit message here"
   git push origin feature/your-feature-name

5. Submit a Pull Request
Go to the original repository and click on 'Pull Requests' to submit your changes for review.

## License
This project is licensed under the MIT License and Adobe Gensolve Hackathon.

## Contact

**Author:**
- Veydant Katyal
- Vinayak Trivedi

**Team Name:**  
Hackstreet Boys





This README was generated with ❤️.






