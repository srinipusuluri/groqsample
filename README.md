# Finance AI Advisor

A Streamlit-based financial advisor application that uses local Ollama models to provide AI-powered financial guidance. This application offers two modes of interaction: General (Grok-3) for quick responses and Reasoning (Grok-4) for detailed analysis.

## 🚀 Features

- **Multiple AI Modes:**
  - **General Mode (Grok-3)**: Uses `llama3.2:3b` for quick, concise responses to simple financial questions
  - **Reasoning Mode (Grok-4)**: Uses `llama3:latest` for detailed, analytical responses with step-by-step breakdowns
  - **DeepSeek Mode**: Uses `deepseek-r1:7b` or `deepseek-coder:6.7b` for advanced reasoning and code-aware financial analysis

- **Local AI Processing:** No API keys required - everything runs locally using Ollama
- **Clean Interface:** Simple, intuitive Streamlit UI for easy interaction
- **Financial Guidance:** Get help with investment questions, budgeting, financial concepts, and more

## 📋 Prerequisites

- Python 3.8 or higher
- Ollama installed and running locally
- Required Python packages (see Installation section)

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/srinipusuluri/groqsample.git
   cd groqsample
   ```

2. **Install Python dependencies:**
   ```bash
   pip install streamlit ollama
   ```

3. **Install and setup Ollama:**
   - Download from [https://ollama.ai](https://ollama.ai)
   - Pull required models:
     ```bash
     ollama pull llama3.2:3b
     ollama pull llama3:latest
     ollama pull deepseek-r1:7b  # Optional: For advanced reasoning
     ```

4. **Start Ollama service:**
   ```bash
   ollama serve
   ```

## 🤖 Ollama Basics

### **Essential Commands:**

```bash
# Check Ollama status
ollama --version

# List available models
ollama list

# Pull a new model
ollama pull <model_name>

# Remove a model (free up space)
ollama rm <model_name>

# Start Ollama service
ollama serve

# Stop Ollama service (Ctrl+C or kill the process)
pkill ollama
```

### **Model Management:**

```bash
# Check which models you have
ollama list

# See all available models online
ollama search <model_name>

# Get info about a specific model
ollama show <model_name>

# Free up disk space by removing unused models
ollama rm llama3.2:3b     # Remove general model
ollama rm llama3:latest   # Remove reasoning model
ollama rm deepseek-r1:7b  # Remove DeepSeek model (4.7GB)
```

### **Testing Models:**

```bash
# Test general model (quick responses)
ollama run llama3.2:3b "What is compound interest?"

# Test reasoning model (detailed analysis)
ollama run llama3:latest "Explain investment diversification strategies"

# Test DeepSeek model (advanced reasoning)
ollama run deepseek-r1:7b "Analyze portfolio diversification strategies with step-by-step reasoning"

# Exit the interactive chat
Type /bye or Ctrl+D
```

### **Troubleshooting Ollama:**

```bash
# Check if Ollama is running
ps aux | grep ollama

# Check which port Ollama uses (default: 11434)
lsof -i :11434

# If port is busy, kill conflicting process
kill -9 <process_id>

# Restart Ollama service
ollama serve
```

## 🚀 Usage

1. **Run the application:**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser:**
   Navigate to `http://localhost:8501` (or the URL shown in terminal)

3. **Select your mode:**
   - Choose "General (Grok-3)" for quick answers
   - Choose "Reasoning (Grok-4)" for detailed analysis
   - Choose "DeepSeek" for advanced reasoning with step-by-step analysis

4. **Ask financial questions:**
   - "What is compound interest?"
   - "Should I invest in stocks or bonds?"
   - "How to create a monthly budget?"
   - "What is diversification in portfolio?"

## 📁 Project Structure

```
groqsample/
├── app.py          # Main Streamlit application
└── README.md       # This file
```

## 🔧 Configuration

The application uses these Ollama models:
- **General Mode:** `llama3.2:3b` - Fast, lightweight model for quick responses
- **Reasoning Mode:** `llama3:latest` - More powerful model for detailed analysis
- **DeepSeek Mode:** `deepseek-r1:7b` - Advanced reasoning model (4.7GB)

## 🌟 Example Use Cases

### Quick Questions (General Mode)
- Basic financial concepts
- Simple calculations
- Quick comparisons

### Detailed Analysis (Reasoning Mode)
- Investment strategies
- Portfolio analysis
- Complex financial planning
- Pros/cons analysis

## 🛡️ Security & Privacy

- **No External APIs:** All processing happens locally
- **No Data Collection:** Your financial questions stay private
- **No API Keys Required:** Completely self-contained

## 🐛 Troubleshooting

**Common Issues:**

1. **"Ollama not running" error:**
   - Ensure Ollama is installed: `ollama --version`
   - Start Ollama service: `ollama serve`
   - Pull required models: `ollama pull llama3.2:3b` and `ollama pull llama3:latest`

2. **Import errors:**
   - Install missing packages: `pip install streamlit ollama`

3. **Model not found:**
   - Pull the model: `ollama pull <model_name>`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Ollama](https://ollama.ai/)
- Uses Meta's Llama models

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review existing issues on GitHub
3. Create a new issue with detailed information

---

**Happy Financial Planning!** 💰📊
