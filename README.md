# Giphy Search App

This is a full-stack web application that allows users to search for GIFs using the Giphy API and display trending GIFs. The application consists of a **React frontend** and a **Python backend** that fetches GIFs from the Giphy API.

## 🚀 Features
- **Search for GIFs**: Users can type a query to search for specific GIFs.
- **Trending GIFs**: When no search term is entered, trending GIFs are displayed.
- **Live Search**: The results update dynamically as the user types.
- **Pagination Support**: The API fetches only a limited number of GIFs per request.
- **Backend API**: Built with FastAPI to fetch GIFs from the Giphy API.
- **Cross-Origin Support**: CORS enabled for frontend-backend communication.

---

## 🛠 Tech Stack
### Frontend (React)
- **React.js** - JavaScript library for building UI.
- **Axios** - HTTP client to call backend API.
- **Tailwind CSS** - Styling framework.

### Backend (Python)
- **FastAPI** - Python framework for building APIs.
- **Requests** - HTTP client to fetch GIFs.
- **Uvicorn** - ASGI server to run FastAPI.
- **Python-dotenv** - Load environment variables.
- **CORS Middleware** - Enables cross-origin requests.

### External Libraries
- **Giphy API** - Fetches GIFs from the Giphy service.

---

## 📂 Project Structure
```
giphy-app/
│── backend/               # Backend code (Python)
│   ├── main.py            # Python backend (FastAPI)
│   ├── requirements.txt   # Python dependencies
│── frontend/              # React frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── GifList.js # Component to display GIFs
│   │   ├── App.js         # Main React app
│   │   ├── index.js       # Entry point
│   ├── public/
│   │   ├── index.html     # HTML file
│   ├── package.json       # React dependencies
│   ├── tailwind.config.js # Tailwind CSS configuration
│── .env                   # Environment variables (GIPHY API Key)
│── README.md              # Instructions
```

---

## 🏗 How to Run the App

### 1️⃣ Setup Backend (Python)
1. Navigate to the `backend/` folder:
   ```sh
   cd backend
   ```
2. Install dependencies:
   ```sh
   pip install fastapi uvicorn requests python-dotenv
   ```
3. Set up **Giphy API Key** in `.env`:
   ```
   GIPHY_API_KEY=your_giphy_api_key
   ```
4. Run the FastAPI server:
   ```sh
   python main.py
   ```
   - The API will be available at: `http://localhost:8080/api/gifs?search=funny`

---

### 2️⃣ Setup Frontend (React)
1. Navigate to the frontend folder:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the React app:
   ```sh
   npm start
   ```
4. Open `http://localhost:3000` in your browser.

---

## 🌐 API Endpoint
- **GET /api/gifs?search=funny**
  - Fetches GIFs based on search term.
  - If no search term is provided, trending GIFs are returned.
  
---

## 🛠 Future Improvements
- Add pagination support.
- Implement infinite scrolling.
- Improve UI/UX.
- Deploy to a cloud platform.

---

## 📌 Conclusion
This project is a simple yet powerful GIF search engine that utilizes React for the frontend and Python (FastAPI) for the backend. It fetches GIFs dynamically from the Giphy API and provides a seamless search experience.

Let me know if you need enhancements! 🚀
