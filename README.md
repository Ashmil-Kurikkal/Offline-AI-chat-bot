
<br/>
<div align="center">

<h3 align="center">Offline AI Chatbot</h3>
<p align="center">
All Thanks to Ollama API

<br/>
<br/>
<a href="https://ibb.co/4NzBs2Q">View Demo .</a>  


</p>
</div>

## About The Project

[![Discord](https://dcbadge.vercel.app/api/server/ollama?style=flat&compact=true)](https://discord.gg/ollama) ![Python](https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54)

# Chatbot with Ollama API

Welcome to the Chatbot project! This repository contains a Python script that leverages the Ollama API to run various models, including Llama2-Uncensored, Llama3, and DeepSeekCoder. The chatbot is designed to provide a range of interactive features, powered by advanced AI models. The project has speech recognition as well typing as input methods and displays as well as speaks back the responses from the API.

## Overview

The core functionality of this chatbot is implemented in the `main.py` script. It utilizes the following models through the Ollama API:

- **Llama2-Uncensored**: An advanced language model for generating responses without content filters.
- **Llama3**: An enhanced version of Llama2 with improved capabilities.
- **DeepSeekCoder**: A specialized model for code generation and understanding.

## Prerequisites

Before running the chatbot, ensure you have completed the following steps:

1. **Install Ollama CLI**:
   - Follow the installation instructions for the Ollama CLI to interact with the Ollama API. You can find the instructions on the [Ollama official website](https://ollama.com/)

2. **Install Python Libraries**:
   - The script requires several Python libraries. You can install them using pip. The required libraries are:
     - `speech_recognition`
     - `pyttsx3`
     - `requests`
     - `json`
     - `cv2` (OpenCV)
     - `face_recognition`
     - `time`
     - `subprocess`
     - `os`
     - `dotenv`

   To install these libraries, run the following command:

   ```bash
   pip install speech_recognition pyttsx3 requests opencv-python face_recognition python-dotenv

### Built With

As in the beginning, all thanks to Ollama. Ollama is a tool that provides the service of running LLMs completely local without internet connection after installation. Many open source models and their different versions, censored and uncensored are available in the official website.

- [Ollama](https://ollama.com)
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.
### Installation

Setup

1. There're are no API keys as it runs completely locally on your device and not on a remote server. Thus first complete the installation of Ollama from the official website. Then open a terminal and run the following :

```sh
ollama serve
```
```sh
ollama pull <the_name_of_the_model_you_want_to_use>
```
Refer the names of available models in the ollama website. It's recommended to use models with the smaller parameters for devices in 16 gigs of RAM category and all, And I would not recommend doing it on 8 gigs. And definitely not on a 4 gig. 

The python scrip is made to use 3 models, llama2-uncensored, llama3 and deepseek-coder. You can build your own models based off of these available LLMs, I did it and used it, The tutorials to it are pretty common on the internet, now even if you can't find, there're previous team members of Ollama giving detailed tutorials to everybody on every topic.

2. Clone the repo
   ```sh
   git clone https://github.com/Ashmil-Kurikkal/Offline-AI-chat-bot/
   ```
4. Create a file named .env in the same directory, add your personal details and edit the code to self introduce yourself to the LLM so that the LLM can explain it to the audience. The self introduction can either be given inside a .env file or it can be given in the line 180, as a string assigned to the variable 'text'.

5. Copy an image of your face to the directory in which you have cloned the repo into, for facerecognition. Rename the photo as known_face.jpg.
## Usage

Usage is pretty simple, just make sure you have python updated and you can either double click and run it or run it from the terminal.
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
## License

Distributed under the MIT License. See [MIT License](https://opensource.org/licenses/MIT) for more information.
## Contact
ashmilkurikkal - [@X account](https://x.com/ashmilkurikkal) - ashmilkurikkal12@gmail.com

Project Link: [Offline Chat Bot](https://github.com/Ashmil-Kurikkal/Offline-AI-chat-bot/)
