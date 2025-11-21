# Persona Chat AI

A modern, real-time chat application that allows users to interact with distinct AI personas. Built with **React**, **FastAPI**, and **OpenAI GPT-4**, featuring a premium glassmorphism UI and Firebase integration for saving favorites and links.

## 🚀 Features

- **Multiple Personas**: Chat with specialized AI personalities:
  - **Hitesh Choudhary**: A warm, Hinglish-speaking mentor and educator.
  - **Piyush Garg**: A pragmatic, project-focused web development teacher.
- **Real-time Interactions**: Instant responses powered by OpenAI's `gpt-4.1-mini` model.
- **Smart Link Detection**: Automatically detects and saves URLs shared in the chat to Firebase.
- **Favorites System**: Star important messages to save them for later (synced via Firebase).
- **Modern UI**:
  - Dark mode with glassmorphism aesthetics.
  - Smooth animations and transitions.
  - Responsive design for all devices.
  - Auto-scrolling and polished user experience.

## 🛠 Tech Stack

### Frontend
- **Framework**: React 19 (Vite)
- **Styling**: Tailwind CSS v4, Radix UI
- **Icons**: Lucide React
- **State Management**: React Hooks
- **Routing**: React Router DOM
- **BaaS**: Firebase (Firestore) for data persistence

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.x
- **AI Engine**: OpenAI API (`gpt-4.1-mini`)
- **Server**: Uvicorn

## 📂 Project Structure

```
persona-chat-python/
├── backend/                 # FastAPI Backend
│   ├── db/                  # Local database files (legacy)
│   ├── personas/            # Persona definitions and prompts
│   │   ├── persona1.py      # Hitesh Choudhary persona
│   │   └── persona2.py      # Piyush Garg persona
│   ├── main.py              # API Entry point
│   └── requirements.txt     # Python dependencies
├── frontend/                # React Frontend
│   ├── src/
│   │   ├── components/      # UI Components (Chat, Sidebar, etc.)
│   │   ├── context/         # React Context (Persona state)
│   │   ├── firebase/        # Firebase configuration
│   │   └── ...
│   ├── package.json
│   └── ...
└── README.md                # Project Documentation
```

## ⚡ Getting Started

### Prerequisites
- Node.js (v18+)
- Python (v3.8+)
- OpenAI API Key
- Firebase Project Configuration

### 1. Backend Setup

Navigate to the backend directory:
```bash
cd backend
```

Create a virtual environment (optional but recommended):
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Create a `.env` file in the `backend` directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

Run the server:
```bash
uvicorn main:app --reload --port 5000
```
The backend will start at `http://localhost:5000`.

### 2. Frontend Setup

Navigate to the frontend directory:
```bash
cd frontend
```

Install dependencies:
```bash
npm install
```

Configure Firebase:
1. Create a Firebase project.
2. Copy your Firebase configuration.
3. Update `src/firebase/firebaseConfig.ts` with your config keys.

Run the development server:
```bash
npm run dev
```
The app will be available at `http://localhost:5173`.

## 🔌 API Endpoints

### `POST /chat`
Sends a message to the selected persona.

**Request Body:**
```json
{
  "persona": "persona1", // or "persona2"
  "message": "Hello, how are you?",
  "is_favorite": false
}
```

**Response:**
```json
{
  "reply": "AI generated response..."
}
```

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
