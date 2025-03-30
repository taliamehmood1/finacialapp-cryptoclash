import streamlit as st
import random
import time
import pandas as pd

st.markdown(
    "<h1 style='text-align: center; color: #FF5733;'>🚀 Crypto Clash – The Ultimate Finance Battle! ⚔️</h1>", 
    unsafe_allow_html=True
)

# 🎈 Balloons Effect only on Home Page
def show_balloons():
    st.session_state.show_balloons = True

if "show_balloons" not in st.session_state:
    show_balloons()

st.write("Dive into the world of finance like never before! This interactive finance app lets you explore, play, and learn through exciting financial activities! 💰Sharpen your skills, make smart financial decisions, and have a blast along the way! 🎯🔥")

# 🎭 Activity Selection
activity = st.selectbox("🎮 Choose Your Activity:", 
                        ["Select an Activity", "1v1 Finance Quiz Battle", "Crypto Market Prediction Game", 
                         "Risky Investment Challenge", "AI Financial Advisor", 
                         "Financial Personality Quiz", "Virtual Crypto Trading Game", "Crypto Puzzle Game"])

# 🎈 Show balloons only when home page is opened
if st.session_state.show_balloons:
    st.balloons()
    st.session_state.show_balloons = False  

# 🎯 1v1 Finance Quiz Battle
if activity == "1v1 Finance Quiz Battle":
    st.header("🧠 1v1 Finance Quiz Battle!")

    questions = [
        {"question": "What does ROI stand for?", "options": ["Return on Investment", "Rate of Interest", "Revenue of Industry"], "answer": "Return on Investment"},
        {"question": "Which asset is the most liquid?", "options": ["Real Estate", "Stocks", "Cash"], "answer": "Cash"},
        {"question": "What does ETF stand for?", "options": ["Electronic Transfer Fund", "Exchange-Traded Fund", "Equity Trade Finance"], "answer": "Exchange-Traded Fund"},
    ]

    score = 0
    for q in questions:
        answer = st.radio(f"❓ {q['question']}", q["options"], index=None)
        if answer and answer == q["answer"]:
            score += 1

    if st.button("Submit Answers"):
        if score == len(questions):
            st.success("🎉 Perfect Score! You're a finance genius!")
            st.snow()  
        else:
            st.warning(f"You scored {score}/{len(questions)}. Keep Learning! 🔥")

# 📈 Crypto Market Prediction Game
elif activity == "Crypto Market Prediction Game":
    st.header("📊 Predict the Crypto Market!")
    price_trend = [random.randint(90, 110) for _ in range(10)]
    st.line_chart(price_trend)

    user_choice = st.radio("📉 Will the price go UP or DOWN?", ["UP", "DOWN"], index=None)
    
    if st.button("Submit Prediction"):
        actual_movement = "UP" if price_trend[-1] > price_trend[0] else "DOWN"
        if user_choice == actual_movement:
            st.success("✅ Correct Prediction! 🚀")  
        else:
            st.warning("❌ Incorrect! Try Again.")

# 🎰 Risky Investment Challenge
elif activity == "Risky Investment Challenge":
    st.header("🎰 Risky Investment Challenge! 💸")

    if "investment_balance" not in st.session_state:
        st.session_state.investment_balance = 10000  

    assets = ["Bitcoin", "Ethereum", "NFTs", "Tech Stocks", "Penny Stocks"]
    chosen_asset = st.selectbox("📈 Choose an Asset to Invest In:", assets)
    investment_amount = st.slider("💰 How much do you want to invest?", min_value=100, max_value=st.session_state.investment_balance, step=100)

    if st.button("📊 Invest Now!"):
        st.write(f"⏳ Investing in {chosen_asset}...")
        with st.spinner("Market Fluctuating... 📉📈"):
            time.sleep(3)  

        if random.choice([True, False]):
            st.session_state.investment_balance += investment_amount  
            st.success(f"🚀 Wow! Your {chosen_asset} investment doubled! New Balance: ${st.session_state.investment_balance}")
        else:
            st.session_state.investment_balance -= investment_amount // 2  
            st.error(f"📉 Oops! Your {chosen_asset} investment crashed. New Balance: ${st.session_state.investment_balance}")

    st.write(f"🏦 Current Balance: *${st.session_state.investment_balance}*")

# 🤖 AI Financial Advisor
elif activity == "AI Financial Advisor":
    st.header("🤖 AI Financial Advisor")
    uploaded_file = st.file_uploader("📂 Upload your financial data (CSV)", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("📊 Your uploaded data:")
        st.dataframe(df)

        df.columns = df.columns.str.lower()  
        if "income" in df.columns and ("expense" in df.columns or "expenses" in df.columns):
            total_income = df["income"].sum()
            total_expense = df["expense"].sum() if "expense" in df.columns else df["expenses"].sum()
            savings = total_income - total_expense

            st.write(f"💰 Total Income: ${total_income}")
            st.write(f"💸 Total Expenses: ${total_expense}")
            st.write(f"💾 Savings: ${savings}")

            if savings > 0:
                st.success("✅ You're saving money! Keep up the good financial habits! 🚀")
            else:
                st.warning("⚠️ You're spending more than you earn! Try to reduce unnecessary expenses. 📉")

# 🧠 Financial Personality Quiz (Fixed)
elif activity == "Financial Personality Quiz":
    st.header("🔍 Financial Personality Quiz! 💡")

    questions = [
        {"question": "How do you handle unexpected expenses?", 
         "options": ["Use emergency savings", "Put it on a credit card", "Ignore it & hope for the best"]},
        
        {"question": "What’s your investment strategy?", 
         "options": ["Long-term & diversified", "High-risk, high-reward", "I don’t invest"]},

        {"question": "How often do you track your spending?", 
         "options": ["Daily", "Once in a while", "Never"]},

        {"question": "What do you do with extra money?", 
         "options": ["Save or invest it", "Spend on wants", "Give it away"]},

        {"question": "Your ideal retirement plan is?", 
         "options": ["Financial freedom by 50", "Work as long as possible", "No plan yet"]},
    ]

    answers = []
    for q in questions:
        answer = st.radio(f"❓ {q['question']}", q["options"], index=None)
        if answer:
            answers.append(answer)

    if st.button("🔎 Get My Financial Personality"):
        if len(answers) == len(questions):
            st.success("✅ Analysis Complete! Here’s your financial personality:")
            
            risk_takers = ["High-risk, high-reward", "Put it on a credit card", "Spend on wants"]
            savers = ["Long-term & diversified", "Use emergency savings", "Save or invest it", "Daily"]

            risk_score = sum(1 for ans in answers if ans in risk_takers)
            saver_score = sum(1 for ans in answers if ans in savers)

            if risk_score > saver_score:
                st.subheader("🔥 Risk-Taker! 🎢")
                st.write("You love high-reward investments, but be cautious of potential losses.")
            elif saver_score > risk_score:
                st.subheader("💰 Smart Saver! 🏦")
                st.write("You're a responsible money manager. Keep building your financial future!")
            else:
                st.subheader("⚖️ Balanced Planner! 🎯")
                st.write("You mix risk with careful planning. A solid strategy for financial success!")
        else:
            st.warning("⚠️ Please answer all questions to get your result!")

# 💰 Virtual Crypto Trading Game
elif activity == "Virtual Crypto Trading Game":
    st.header("💰 Virtual Crypto Trading Game 🎮")

    if "crypto_balance" not in st.session_state:
        st.session_state.crypto_balance = 5000  
        st.session_state.portfolio = {}

    st.write(f"🏦 *Your Crypto Balance:* ${st.session_state.crypto_balance}")

    cryptos = ["Bitcoin", "Ethereum", "Solana", "Dogecoin", "Ripple"]
    chosen_crypto = st.selectbox("📈 Choose a Cryptocurrency to Trade:", cryptos)
    
    trade_type = st.radio("📊 Do you want to *BUY or SELL*?", ["Buy", "Sell"], index=None)

    trade_amount = st.slider("💰 Choose Amount to Trade:", min_value=100, max_value=st.session_state.crypto_balance, step=100)

    if st.button("🚀 Execute Trade!"):
        price_change = random.choice([-10, 5, 10, 20, -5, -20])  

        if trade_type == "Buy":
            st.session_state.crypto_balance -= trade_amount  
            st.session_state.portfolio[chosen_crypto] = st.session_state.portfolio.get(chosen_crypto, 0) + trade_amount
            st.success(f"✅ *Purchased ${trade_amount} of {chosen_crypto}!* 🚀 New Balance: ${st.session_state.crypto_balance}")
        elif trade_type == "Sell" and st.session_state.portfolio.get(chosen_crypto, 0) >= trade_amount:
            st.session_state.crypto_balance += trade_amount + (trade_amount * price_change / 100)
            st.session_state.portfolio[chosen_crypto] -= trade_amount
            st.success(f"✅ *Sold ${trade_amount} of {chosen_crypto}!* New Balance: ${st.session_state.crypto_balance}")
        else:
            st.error(f"❌ You don't have enough {chosen_crypto} to sell!")

    st.subheader("📜 Your Crypto Portfolio:")
    for crypto, amount in st.session_state.portfolio.items():
        st.write(f"🔹 *{crypto}:* ${amount}")

    st.write("🎉 Keep trading and grow your portfolio! 🚀")

# 🧩 Crypto Puzzle Game
elif activity == "Crypto Puzzle Game":
    st.title("🧩 Puzzle Game - Arrange the Numbers!")

    uploaded_file = st.file_uploader("📂 Upload an image to start the puzzle:", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        st.image(uploaded_file, caption="Your Puzzle Image", use_container_width=True)

        numbers = list(range(1, 9))
        random.shuffle(numbers)
        st.write("🔀 *Shuffled Sequence:*", numbers)

        user_input = st.text_input("✍️ Enter the correct sequence (comma-separated numbers):")

        if st.button("✅ Submit"):
            if user_input.replace(" ", "") == "1,2,3,4,5,6,7,8":
                st.success("🎉 Congratulations! You solved the puzzle! 🎊")
                st.balloons()
            else:
                st.error("❌ Incorrect! Try again.")
