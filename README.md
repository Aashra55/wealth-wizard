# 💰 Wealth Wizard: Side Hustles & Money Mindset

Wealth Wizard is a fun and interactive Streamlit web app designed to help users generate side hustle ideas, track earnings, get motivated with money-related quotes, and discover their financial personality through a money mindset quiz.

## 🚀 Features
- **💸 Money Generator**: Instantly generate a random amount of money.
- **💼 Side Hustle Ideas**: Get inspiration for new ways to earn money.
- **🚀 Money Quotes**: Stay motivated with financial wisdom.
- **🧠 Money Mindset Quiz**: Find out your financial personality.
- **📊 Money Growth Tracker**: Track your total earnings over time.

## 🛠️ Installation

1. Install UV:
```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. Initialize the Project:
```sh
uv init wealth-wizard
cd wealth-wizard
```

3. Install Streamlit:
Without dependencies:
```sh
uv pip install streamlit
```
With dependencies:
```sh
uv add streamlit
```

4. Activate Virtual Environment:
For windows:
```sh
.venv\Scripts\activate
```
For MacOs/Linux:
```sh
source env/bin/activate
```

## 🚀 Running the Web App
```sh
streamlit run app.py
```

## API Requirements
```sh
api_key = "1234567890"
SIDE_HUSTLE_API = "http://127.0.0.1:8000/side_hustles?api_key={api_key}"
MONEY_QUOTES_API = "http://127.0.0.1:8000/money_quotes?api_key={api_key}"
```

