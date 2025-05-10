# Image Description AI

A web application that generates creative stories from uploaded images using Llama 3.2 Vision model.

![Image Description AI](https://img.shields.io/badge/AI-Image%20Description-gold)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)

## 📋 Overview

Image Description AI is a web application that allows users to upload images and receive AI-generated stories based on the image content. The application uses Meta's Llama 3.2 Vision model through Together.ai's API to analyze images and create descriptive narratives.

## ✨ Features

- Simple, intuitive user interface
- Real-time image preview
- AI-powered story generation from images
- Responsive design
- Fast processing via API integration

## 🔧 Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML, CSS, JavaScript
- **AI Model**: Meta Llama 3.2 11B Vision Instruct
- **API Integration**: Together.ai via Hugging Face Hub

## 🚀 Installation & Setup

### Prerequisites

- Python 3.7+
- pip (Python package manager)
- Together.ai API key

### Setup Steps

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/image-description-ai.git
cd image-description-ai
```

2. **Install dependencies**

```bash
pip install fastapi uvicorn python-multipart pillow python-dotenv huggingface-hub requests
```

3. **Create a `.env` file in the project root and add your API key**

```
KEY=your_together_ai_api_key_here
```

4. **Run the backend server**

```bash
uvicorn app:app --reload
```

5. **Access the application**

Open `index.html` in your browser or serve it with a simple HTTP server:

```bash
# Python 3
python -m http.server
```

Then navigate to `http://localhost:8000` in your web browser.

## 🖼️ How to Use

1. Click the file input button to select an image from your device
2. Preview the selected image
3. Click "Generate Description" button
4. Wait a few seconds for the AI to process the image
5. Read the generated story in the result section

## ⚙️ API Endpoints

- `POST /upload` - Upload an image and receive an AI-generated description

## 🔒 Security Notes

- The current CORS settings allow requests from any origin (`*`). For production, restrict this to your specific frontend domain.
- API keys should be kept secure. The current implementation uses environment variables to keep the key out of the codebase.

## 🔮 Future Enhancements

- User accounts to save favorite images and descriptions
- Additional AI models for different types of descriptions
- Ability to customize the prompt for different narrative styles
- Image editing capabilities before processing
- Social sharing options



## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

Created with ❤️ using FastAPI and Llama 3.2
