# Carbon Footprint Calculator

![VSCode](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)
![Hugging Face](https://img.shields.io/badge/-HuggingFace-FDEE21?style=for-the-badge&logo=HuggingFace&logoColor=black)
![Netlify](https://img.shields.io/badge/Netlify-00C7B7?style=for-the-badge&logo=netlify&logoColor=white)

![Gif](CarbonFT.gif)

## Table of Contents

- [About the Project](#about-the-project)
- [Running Locally with Docker](#running-locally-with-docker)
- [Contributing](#contributing)

## About the Project

This project is a Carbon Footprint Calculator that helps users estimate their carbon footprint based on their monthly energy consumption and travel habits. It uses Google's Gemini API to provide personalized recommendations for reducing carbon emissions.

## Running Locally with Docker

To run this application locally using Docker, follow these steps:

1. **Build the Docker image:**

   ```bash
   docker build -t carbon-footprint-calculator .
   ```

2. **Run the Docker container:**

   ```bash
   docker run -p 7860:7860 carbon-footprint-calculator
   ```

3. **Access the application:**

   Open your web browser and navigate to `http://localhost:7860`.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. **Fork the repository.**
2. **Create a new branch for your feature or bug fix.**
3. **Make your changes and commit them with descriptive messages.**
4. **Push your changes to your fork.**
5. **Create a pull request to the main repository.**

Please make sure to update the documentation as well if you make any changes to the application.
