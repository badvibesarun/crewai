# Flight Finder & Trip Planner CrewAI

## 🚀 Project Overview
This project is a **Flight Finder & Trip Planner** built using **CrewAI**, integrating AI-powered flight search functionalities. The backend is developed using **Next.js & Python**, and it utilizes **OpenAI's API & SerpAPI** for data retrieval.

---

## 📌 Steps Followed

### 1️⃣ **Set Up Virtual Environment**
```sh
python -m venv .venv
```
Activate it:
```sh
# Windows (PowerShell)
.venv\Scripts\Activate

# Mac/Linux
source .venv/bin/activate
```

### 2️⃣ **Installed Dependencies**
```sh
pip install -r requirements.txt
```

### 3️⃣ **Configured API Keys**
- OpenAI API Key (for AI responses)
- SerpAPI Key (for flight search)

Added them to `.env`:
```sh
OPENAI_API_KEY=your-api-key
SERPAPI_API_KEY=your-api-key
```

### 4️⃣ **Ran the Streamlit App**
```sh
streamlit run main_streamlit.py
```

### 5️⃣ **Started Next.js Backend**
```sh
npm install
npm run dev
```

### 6️⃣ **Tested API**
Checked if the API is running:
```sh
http://localhost:3000/api/flight
```

---

## ❌ Errors Faced & Fixes

### ⚠️ **SerpAPI Import Error**
**Error:**
```sh
ImportError: cannot import name 'GoogleSearch' from 'serpapi'
```
✅ **Fix:** Installed correct package
```sh
pip install serpapi
```

### ⚠️ **OpenAI Rate Limit Error (429)**
**Error:**
```sh
RateLimitError: OpenAIException - Error code: 429 - 'You exceeded your current quota'
```
✅ **Fix:**
1. Checked **OpenAI billing**: https://platform.openai.com/account/billing
2. Used a **new API key** or upgraded plan

### ⚠️ **Backend Not Responding, Serving HTML Instead of JSON**
**Error:** When visiting `http://localhost:3000/api/flight`, an HTML page loaded instead of JSON response.
✅ **Fix:** Checked API route and ensured it was properly set up in `Next.js` backend.

---

## 🛠️ How to Run the Project

1️⃣ **Clone the Repository**
```sh
git clone https://github.com/YOUR_USERNAME/flight_finder_and_trip_planner_crewai.git
cd flight_finder_and_trip_planner_crewai
```

2️⃣ **Set Up Virtual Environment & Install Dependencies**
```sh
python -m venv .venv
.venv\Scripts\Activate
pip install -r requirements.txt
```

3️⃣ **Run Backend (Next.js)**
```sh
npm install
npm run dev
```

4️⃣ **Run Streamlit App**
```sh
streamlit run main_streamlit.py
```

---

## 📌 Author
**Arunkumar**

GitHub: [badvibesarun](https://github.com/badvibesarun)

---

