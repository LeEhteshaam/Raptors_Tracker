# Raptors Tracker 🏀

A simple web app that tracks Toronto Raptors games for the 2025 season.

## Tech Stack
- **Frontend:** HTML + React (via Babel)
- **Backend:** Python FastAPI
- **Deployment:** Vercel
- **API:** [balldontlie.io](https://www.balldontlie.io/)

## Setup

1. Clone the repo
2. Create a `.env` file with your API key:
   ```
   API_KEY=your_balldontlie_api_key
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run locally:
   ```bash
   uvicorn api.main:app --reload
   ```

## Live Demo
[raptors-tracker.vercel.app](https://raptors-tracker.vercel.app)