import streamlit as st # To make UI of the web app
import random # To generate random characters
import time # Provides time related functionalities
import requests # To manage API calls

api_key = "1234567890"

# Initialize session state for money tracking
if "total_earning" not in st.session_state:
    st.session_state["total_earning"] = 0
    st.session_state["money_history"] = []

# Function to Generate Money 
def generate_money():
    return random.randint(1, 1000)

# Function to get side hustle ideas
def fetch_side_hustle():
    try:
        response = requests.get(f"http://127.0.0.1:8000/side_hustles?api_key={api_key}")
        if response.status_code == 200 :
            hustles = response.json()
            if isinstance(hustles, dict) and hustles:
                return hustles.get("side_hustle", "Stock Trading")
            return ("Freelancing")
        else :
            return ("Freelancing - Start offering your skills online")
    except:
        return ("Something went wrong!")
    
# Function to get Money Quotes
def fetch_money_quotes():
    try:
        response = requests.get(f"http://127.0.0.1:8000/money_quotes?api_key={api_key}")
        if response.status_code == 200 :
            quotes = response.json()
            return quotes["money_quote"]
        else:
            return ("The more you learn, the more you earn. – Warren Buffett")
    except:
        return ("Something went wrong!")
    
# Streamli UI
st.title("💰 Wealth Wizard: Side Hustles & Money Mindset")

tab1, tab2 = st.tabs(["💼 Hustle & Wealth", "🧠 Money Mindset Quiz"])

with tab1:
    # Cash Generator
    st.subheader("💸 Earn Instantly, No Wait!")

    if st.button("Generate Money"):
        amount = generate_money() # Generate the amount
        message = st.empty() # Placeholder for displaying message
        message.write("`Counting Money...`")
        time.sleep(1) # Time delay for one second
        message.empty() # Clear the message
        st.success(f"You made ${amount}!") 
    
        st.session_state["total_earning"] += amount # Update total earning
        st.session_state["money_history"].append(st.session_state["total_earning"])
    
        # Total Earning
        st.info(f"**Total Earnings: ${st.session_state['total_earning']}**")
    
        # Money Growth Tracker
        st.subheader("📊 Money Growth Over Time")
        st.line_chart(st.session_state["money_history"]) # show line chart
    
    # Side Hustle Ideas Generator
    st.subheader("💼 Side Hustle Ideas")

    if st.button("Generate Hustle"):
        message = st.empty()
        message.write("`Generating Idea...`")
        idea = fetch_side_hustle()
        time.sleep(1)
        message.empty()
        st.success(idea)
    
    # Money Quotes Generator 
    st.subheader("🚀 Money-Making Motivation")

    if st.button("Generate Quote"):
        message = st.empty()
        message.write("`Generating Quote...`")
        quote = fetch_money_quotes()
        time.sleep(1)
        message.empty()
        st.success(quote)
    
with tab2:
    # Mindset Quiz
    st.subheader("🧠 What's Your Money Mindset?")
    st.write("Answer these questions to discover your financial personality!")
    # Quiz Questions
    q1 = st.radio("1. What do you do when you get extra money?", [
    "Invest it",
    "Start a side hustle",
    "Save it in a bank",
    "Spend it on something nice"
    ])

    q2 = st.radio("2. What's your ideal way to make money?", [
    "Long-term investments",
    "Multiple side businesses",
    "Stable 9-to-5 job with savings",
    "Winning the lottery"
    ])

    q3 = st.radio("3. How do you feel about financial risk?", [
    "I love it! Higher risk, higher reward!",
    "I take calculated risks with side hustles",
    "I prefer low-risk savings options",
    "I avoid risk at all costs"
    ])
    
    # Function to find money personality
    def get_money_personality():
        
        investor = (q1 == "Invest it") + (q2 == "Long-term investments") + (q3 == "I love it! Higher risk, higher reward!")
        hustler = (q1 == "Start a side hustle") + (q2 == "Multiple side businesses") + (q3 == "I take calculated risks with side hustles")
        saver = (q1 == "Save it in a bank") + (q2 == "Stable 9-to-5 job with savings") + (q3 == "I prefer low-risk savings options")
        spender = (q1 == "Spend it on something nice") + (q2 == "Winning the lottery") + (q3 == "I avoid risk at all costs")
     
        max_score = max(investor, hustler, saver, spender)

        if max_score == investor:
            return "**Investor**! 📈", "You're all about making your money work for you! Focus on long-term investments and wealth building."
        elif max_score == hustler:
            return "**Hustler**! 💼", "You love multiple income streams! Try new side hustles and scale them into full-time businesses."
        elif max_score == saver:
            return "**Saver**! 🏦", "You believe in financial security. Focus on growing savings and low-risk investments."
        else:
            return "**Spender**! 🎉", "You enjoy spending! Consider budgeting to balance fun with financial growth."    
    
    # Button to get answer of Quiz
    if st.button("Find Out Your Money Personality"):
        time.sleep(1)
        personality, advice = get_money_personality()
        st.success(f"🔍 Your Money Personality: {personality}")
        st.info(f"💡 Tip: {advice}")
        
        
