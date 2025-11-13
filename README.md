## **Overview**

MythWeaver is a multimodal, agentic storytelling system built with Gradio and the Model Context Protocol (MCP). Users interact through text and optional map/sketch uploads. The system interprets drawings, converts them into structured scene graphs, generates cleaned maps, and uses long-context memory for consistent narrative progression. The Auto-Quest Engine dynamically generates optional quests based on the world state, locations, NPCs, and story progression.

---

## **Features**

* Text-based adventures with user-steered or semi-autonomous narration
* Sketch / map upload for geography-driven storytelling
* Vision parsing into structured scene graphs
* High-resolution map generation
* Long-context world memory (regions, NPCs, quests, inventory, timeline)
* Dynamic model selection
* MCP tool integrations for multimodal reasoning
* Auto-Quest Engine generating map-aware objectives and quests
* Gradio 6 interface with mobile support

---

## **Architecture (Text Diagram)**

```
User
 └── Gradio UI
       ├── Text Input
       ├── Image Upload
       ├── Model Selector
       └── Settings Panel
             │
             ▼
      Claude 4.5 Sonnet (Anthropic, Orchestrator)
             ├── World-memory reasoning
             ├── Quest opportunity detection
             ├── Multi-objective quest generation
             └── Tool-driven map-aware planning
             │
             ├── Gemini Vision MCP (Google)
             │       → Image → Scene Graph
             │
             ├── Map Generator MCP (HuggingFace / Flux / Nano Banana)
             │       → Scene Graph → Clean Map
             │
             ├── Fast Text MCP (OpenAI GPT-5.1)
             │       → Summaries, transforms, procedural utilities
             │
             ├── Memory Store MCP
             │       → Persistent world state
             │
             ├── Modal Tasks MCP
             │       → Heavy compute / batch jobs
             │
             ├── Blaxel MCP
             │       → Sanitization, redaction
             │
             ├── ElevenLabs MCP
             │       → Optional audio narration
             │
             └── SambaNova MCP
                     → Low-cost tagging and memory compression
             │
             └── Auto-Quest Engine (internal module)
                     → memory + scene graph → quest proposals
             │
             ▼
      Gradio Output Display
             ├── Story Text
             ├── Generated Maps
             ├── Quest Options
             └── Suggested Actions
```

---

## **Tech Stack**

### **Frontend**

* Gradio 6
* Chat component
* Image upload
* Gallery display
* Quest selection UI elements
* Model selector
* User settings panel

### **Orchestrator Model**

* Claude 4.5 Sonnet

  * Planning
  * Narrative consistency
  * Tool selection
  * Memory updates
  * Quest detection and generation

### **MCP Tools**

* **Google Gemini Vision** — scene graph extraction
* **HuggingFace / Flux / Nano Banana** — high-resolution map generation
* **OpenAI GPT-5.1** — fast procedural text utilities
* **Memory MCP** — persistent world state
* **Modal MCP** — heavy compute tasks
* **Blaxel MCP** — sanitization
* **ElevenLabs MCP** — optional narration
* **SambaNova MCP** — tagging & compression

### **Internal Modules**

* **Auto-Quest Engine**

  * Generates 1–3 map-aware quests using world memory
  * Produces structured objectives, difficulty, path hints, NPC ties

---

## **Agentic Capabilities**

* Multi-step narrative planning
* Autonomous tool routing
* Scene graph reasoning and validation
* World memory management
* Quest opportunity detection
* Map-aware quest generation
* Semi-autonomous storytelling modes

---

## **User Flow**

1. User starts an adventure.
2. User enters text or uploads a sketch/map.
3. Orchestrator determines required tools.
4. If image uploaded:

   * Gemini Vision → scene graph
   * Map Generator → cleaned/stylized map
5. Memory MCP updated with locations, NPCs, quests, inventory, and timeline events.
6. Claude 4.5 Sonnet generates story continuation.
7. Auto-Quest Engine proposes dynamic quest options.
8. Gradio displays story, maps, and optional quests.
9. User selects a quest or continues freely.

---

## **MCP Tools Summary**

| Tool                        | Purpose                     |
| --------------------------- | --------------------------- |
| Gemini Vision               | Sketch → scene graph        |
| Map Generator               | Scene graph → map image     |
| Memory Store                | Persistent world model      |
| GPT-5.1                     | Text utilities & transforms |
| Modal Tasks                 | Heavy/batch operations      |
| Blaxel                      | Sanitization                |
| ElevenLabs                  | Audio narration             |
| SambaNova                   | Tagging & compression       |
| **Quest Engine (internal)** | Structured quest generation |

---

## **Setup (uv)**

### 1. Create virtual environment

```
uv venv
```

### 2. Activate

```
source .venv/bin/activate
```

### 3. Install dependencies

```
uv add gradio anthropic openai google-generativeai huggingface_hub diffusers pydantic fastapi
```

### 4. Run

```
uv run app.py
```

---

## **Suggested Project Structure**

```
/mythweaver
  ├── app.py
  ├── README.md
  ├── uv.lock
  ├── requirements.txt (optional)
  ├── /mcp-tools
  │     ├── gemini_vision/
  │     ├── map_generator/
  │     ├── memory_store/
  │     ├── openai_tools/
  │     ├── modal_tasks/
  │     ├── blaxel_filter/
  │     ├── elevenlabs_audio/
  │     └── sambanova_inference/
  ├── /utils
  │     ├── helpers.py
  │     └── quest_engine.py
  ├── /assets
  │     └── example_maps/
  ├── /prompts
  │     └── orchestrator.md
```

---

## **Submission Requirements**

* Gradio 6 app with MCP integrations
* Autonomous agentic behavior demonstrated
* Auto-Quest Engine active
* Multimodal pipeline (vision + map generation)
* Documentation included
* Demo video (1–5 minutes)
* Social media link included
* Submitted under the MCP-1st-Birthday organization

---

## **Demo Outline**

1. Start new adventure
2. Upload hand-drawn sketch
3. Scene graph extraction
4. Map generation
5. Story continuation
6. Auto-Quest Engine proposes quests
7. User selects quest or continues
8. Updated map + narrative progression
9. Optional: audio narration
