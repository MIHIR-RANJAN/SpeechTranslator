# Mental Health Chatbot

## Overview
This project is a **Mental Health Chatbot** designed using **Streamlit**, **Hugging Face Transformers**, and **PyTorch**. The chatbot performs:

- **Mood Classification**: Uses a fine-tuned **BERT-based model** to classify user emotions (e.g., stress, anxiety, depression, etc.).
- **Response Generation**: Utilizes **Facebook's BlenderBot-400M** to generate deep, meaningful responses.
- **User Interaction**: Provides a friendly and interactive interface via **Streamlit**.

## Features
- **Real-time Mood Detection** based on user input.
- **AI-powered Conversations** using an open-source conversational model.
- **Interactive UI** built with **Streamlit**.
- **Session-based Chat History** to maintain context within a conversation.

## Requirements
Ensure you have the following dependencies installed:

```bash
pip install -r requirements.txt
```

### Required Packages
The project depends on the following Python libraries:

- `streamlit`
- `torch`
- `transformers`
- `scikit-learn`
- `pickle5`

## Installation & Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/mental-health-chatbot.git
   cd mental-health-chatbot
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Download Pretrained Models**:
   - Ensure the following models are downloaded and placed correctly:
     - **Mental Health BERT Model** (`mental_health_bert_model`)
     - **BlenderBot Conversational Model** (`facebook/blenderbot-400M-distill`)
   
4. **Run the Application**:
   ```bash
   streamlit run chatbot.py
   ```

## How It Works
1. The chatbot initializes with a default mood: `IDK`.
2. Users enter a text message in the chatbox.
3. The **BERT-based classification model** predicts the user's emotional state.
4. The **BlenderBot model** generates an appropriate response.
5. The chat history is updated, and the user can continue the conversation.

## Example Interaction
```
User: I feel really stressed about my exams.
Bot:
  Mood: Stress
  Response: I understand, exams can be overwhelming. Have you tried a short break or relaxation exercises?
```

## Future Enhancements
- Integrate **more advanced mental health models**.
- Add **voice-based interactions**.
- Implement **crisis intervention routing**.

## Author
- **Mihir Ranjan**
- National Forensic Sciences University
- Contact: [mihir29062001@gmail.com](mailto:mihir29062001@gmail.com)
- GitHub: [MIHIR-RANJAN](https://github.com/MIHIR-RANJAN)

## License
MIT License  

```
MIT License  

Copyright (c) 2025 Mihir Ranjan  

Permission is hereby granted, free of charge, to any person obtaining a copy  
of this software and associated documentation files (the "Software"), to deal  
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in all  
copies or substantial portions of the Software.  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN  
THE SOFTWARE.  
```