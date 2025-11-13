# **MythWeaver**

## **Overview**

MythWeaver is a multimodal, agentic storytelling system built with Gradio and the Model Context Protocol (MCP). Users interact through text and optional map/sketch uploads. The system interprets drawings, converts them into structured scene graphs, generates cleaned maps, and uses long-context memory for consistent narrative progression.

---

## **Features**

* Text-based adventures with user-steered or semi-autonomous narration
* Sketch / map upload for geography-driven storytelling
* Vision parsing into structured scene graphs
* High-resolution map generation
* Long-context world memory (regions, NPCs, quests, inventory, timeline)
* Dynamic model selection
* MCP tool integrations for multimodal reasoning
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
             ▼
      Gradio Output Display
             ├── Story Text
             ├── Generated Maps
             └── Suggested Actions
```

---

## **Tech Stack**

### **Frontend**

* Gradio 6
* Chat component
* Image upload
* Gallery display
* Model selector
* User settings panel

### **Orchestrator Model**

* Claude 4.5 Sonnet

  * Controls planning, narrative consistency, tool selection, memory updates, and context management.

### **MCP Tools**

* **Google Gemini Vision**

  * Scene graph extraction from uploaded sketches
* **HuggingFace / Flux / Nano Banana Image Generator**

  * Map generation from structured scene layouts
* **OpenAI GPT-5.1**

  * Fast text utilities and procedural generation
* **Memory MCP**

  * Persistent world state storage
* **Modal MCP**

  * Heavy compute tasks
* **Blaxel MCP**

  * Input sanitization
* **ElevenLabs MCP**

  * Optional narration audio
* **SambaNova MCP**

  * Low-cost tagging and compression

---

## **Agentic Capabilities**

* Multi-step narrative planning
* Autonomous tool routing
* Scene graph reasoning and validation
* World memory system (long-context)
* Map generation pipeline
* Semi-autonomous mode for faster storytelling

---

## **User Flow**

1. User starts an adventure.
2. User enters text or uploads a sketch/map.
3. Orchestrator evaluates intent and tool requirements.
4. If image uploaded:

   * Gemini Vision → scene graph
   * Map Generator → cleaned/stylized map
5. Memory MCP updated with regions, NPCs, quests, inventory, timeline.
6. Claude 4.5 Sonnet generates story continuation.
7. Gradio displays story, maps, and possible actions.

---

## **MCP Tools Summary**

| Tool          | Purpose                 |
| ------------- | ----------------------- |
| Gemini Vision | Sketch → scene graph    |
| Map Generator | Scene graph → map image |
| Memory Store  | Persistent world model  |
| GPT-5.1       | Text utilities          |
| Modal Tasks   | Heavy/batch operations  |
| Blaxel        | Sanitization            |
| ElevenLabs    | Audio narration         |
| SambaNova     | Tagging + compression   |

---

## **Setup (uv)**

### **1. Create virtual environment**

```
uv venv
```

### **2. Activate**

```
source .venv/bin/activate
```

### **3. Install dependencies**

```
uv add gradio anthropic openai google-generativeai huggingface_hub diffusers pydantic fastapi
```

### **4. Run**

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
  ├── /assets
  │     └── example_maps/
  ├── /prompts
  │     └── orchestrator.md
  └── /utils
        └── helpers.py
```

---

## **Running on HuggingFace Spaces**

Add to `README.md` or `Space Description`:

```
space:
  app_file: app.py
  python_version: "3.10"
  sdk: gradio
  sdk_version: 6.x
```

---

## **Submission Requirements**

* Gradio app: complete
* MCP tools: integrated
* Autonomous agent behavior: included
* Multimodal support: included
* Sponsor APIs: included
* Documentation: provided
* Demo-flow supported

---

## **Demo Outline**

1. Start new world
2. Upload hand-drawn sketch
3. Scene graph displayed (optional)
4. Map generated
5. Story continuation
6. User choices
7. Optional audio narration

---
