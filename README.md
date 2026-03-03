# ✈️ Travel Agent API

An **agentic, autonomous travel planner** built with **CrewAI** and **Flask**. Given a source city, destination, travel dates, and interests, it orchestrates multiple AI agents to produce a comprehensive, personalized travel plan.

---

## 🧠 How It Works

The system uses a CrewAI multi-agent pipeline with two specialized agents:

- **City Selection Expert** — analyzes weather, season, prices, and travel logistics.
- **Local Tour Guide** — crafts a day-by-day itinerary tailored to the user's hobbies.

Both agents use **DuckDuckGo search** as a real-time web tool, powered by an **OpenAI LLM**.

---

## 🗂️ Project Structure

```
travel-agent/
├── app.py                  # Flask API entry point
├── config/
│   └── settings.py         # Pydantic env validation + logging setup
├── src/
│   ├── agents/
│   │   ├── crew_head.py    # Builds and returns the full Crew
│   │   └── sub_agents/
│   │       ├── city_agent.py
│   │       └── local_guide_agent.py
│   ├── tasks/
│   │   ├── city_plan.py
│   │   ├── guide_plan.py
│   │   └── travel_plan.py
│   └── tools/
│       └── search_tool.py  # DuckDuckGo search tool
├── .env.example            # Required env vars template
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone & install

```bash
git clone https://github.com/sagnik0712mukherjee/travel-agent.git
cd travel-agent
pip install -r requirements.txt
```

### 2. Set up environment

```bash
cp .env.example .env
# Fill in your OPENAI_API_KEY in .env
```

### 3. Run the API

```bash
python app.py
```

The server starts on `http://localhost:7777` by default.

---

## 📡 API Reference

### `GET /get_travel_plan`

Generates a full travel plan for the given trip details.

**Request body (JSON):**
(example)
```json
{
  "from_city": "Mumbai",
  "destination_city": "Paris",
  "start_date": "2025-06-01",
  "end_date": "2025-06-10",
  "hobbies": "photography, street food, museums"
}
```

**Response:**

```json
{
  "result": "## Your Personalized Travel Plan\n..."
}
```

---

## ⚙️ Configuration

| Variable | Required | Default | Description |
|---|---|---|---|
| `OPENAI_API_KEY` | ✅ Yes | — | Your OpenAI API key |
| `APP_PORT` | No | `7777` | Port the Flask server runs on |
| `LLM_MODEL` | No | `gpt-4o-mini` | OpenAI model to use |

---

## 🛣️ Roadmap

- [ ] Guardrails & input validation
- [ ] Agent output evaluations
- [ ] Try/catch & structured error responses
- [ ] Dockerize & deploy
- [ ] Add more specialized agents (budget planner, visa advisor)

---

## 👤 Author

**Sagnik Mukherjee**  
[github.com/sagnik0712mukherjee](https://github.com/sagnik0712mukherjee)
