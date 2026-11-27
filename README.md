# ✈️ TravelPlanner – AI-Powered Travel Planning Assistant

TravelPlanner is an AI-powered travel planning application built using **Python and Streamlit**. It helps users create personalized travel plans with the assistance of Large Language Models (LLMs).

The application integrates AI providers to generate travel recommendations and organize trip-planning information through an interactive interface.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Frontend:** Streamlit
- **AI Integration:** LLM Providers / OpenAI API
- **Configuration:** JSON
- **Environment Management:** Python Virtual Environment
- **API Key Management:** Python dotenv

## 📁 Project Structure

```text
Capstone1/
│
├── __pycache__/          # Python cache files
├── myenv/                # Python virtual environment
│
├── .env                  # API keys and environment variables
├── .gitignore            # Git ignored files
│
├── app.py                # Streamlit test application ignore the file
├── config.json           # Application configuration
├── llmproviders.py       # LLM provider integration
├── requirements.txt      # Project dependencies
├── travelplanner.py      # Travel planning functionality
│
└── README.md             # Project documentation
```

## 🚀 Getting Started

Follow these steps to set up and run the application locally.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Capstone1
```

### 2. Create a Virtual Environment

Create an isolated Python environment:

```bash
python -m venv myenv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
myenv\Scripts\activate
```

**macOS / Linux:**

```bash
source myenv/bin/activate
```

### 4. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the root directory of the project.

Add the required API keys:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Replace the placeholder with your actual API key.

If additional LLM providers are configured, add their respective API keys as required by `llmproviders.py` and `config.json`.

**Important:** Never commit your `.env` file or expose API keys in your GitHub repository.

### 6. Run the Application

Launch the Streamlit application:

```bash
streamlit run app.py
```

Open the URL displayed in your terminal:

```text
http://localhost:8501
```

## 📦 Updating Dependencies

Whenever you install additional Python packages, update `requirements.txt`:

```bash
pip freeze > requirements.txt
```

## 🔒 Git Security

Ensure the following files and directories are included in `.gitignore`:

```gitignore
# Virtual Environment
myenv/
venv/

# Environment Variables
.env

# Python Cache
__pycache__/
*.pyc

# IDE Settings
.vscode/
.idea/
```

Never push API keys, credentials, or virtual environment files to GitHub.

## 🔮 Future Enhancements

- AI-powered personalized travel recommendations.
- Day-wise itinerary generation.
- Budget-based travel planning.
- Hotel and accommodation suggestions.
- Flight recommendations.
- Interactive maps and route planning.
- Downloadable travel itineraries.

## 👩‍💻 About the Project

TravelPlanner is a hands-on Generative AI project developed to explore Python-based AI application development, LLM integration, and Streamlit.

The project demonstrates how LLMs can be integrated into practical applications to solve real-world planning problems.

---

⭐ If you find this project interesting, consider giving the repository a star!
