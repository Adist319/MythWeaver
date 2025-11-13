# **MythWeaver**

**Autonomous MCP-powered storytelling and map-driven adventure engine**
**Track:** mcp-in-action-track-creative, mcp-in-action-track-consumer
**Sponsors integrated:** Anthropic, OpenAI, Google Gemini, HuggingFace, Modal, SambaNova, ElevenLabs, Blaxel

---

## **Overview**

MythWeaver is a multimodal, agentic storytelling system built with Gradio and powered by the Model Context Protocol (MCP). Users write actions, make choices, and upload hand-drawn or digital maps. MythWeaver interprets drawings, converts them into structured scene graphs, generates clean maps, and uses long-context memory to produce consistent adventure narratives.

The goal is to demonstrate autonomous planning, tool use, MCP server integration, and multimodal reasoning in a consumer-friendly, creative application.

---

## **Features**

* Text-based interactive adventures
* User-steered or semi-autonomous narration
* Map/sketch upload
* Vision parsing of drawings into scene structures
* High-resolution map generation
* Long-context world memory (NPCs, regions, timeline, inventory)
* Dynamic LLM model selection
* Full sponsor-integrated MCP tool chain
* Responsive Gradio 6 UI

---

## **Architecture Diagram (Text Version)**

```
User
 └── Gradio UI
       ├── Text Input
       ├── Image Upload (maps)
       ├── Model Selector
       └── Settings Panel
             │
             ▼
      Claude 3.7 Sonnet (Anthropic - Primary Orchestrator)
             │
             ├── Gemini Vision MCP (Google)
             │       → Image → Scene Graph
             │
             ├── Image Generator MCP (HuggingFace / Flux / Nano Banana)
             │       → Scene Graph → Clean Map
             │
             ├── Fast Text Utility MCP (OpenAI GPT-5.1)
             │       → Summaries, transforms, procedural text functions
             │
             ├── Memory Store MCP
             │       → Persistent world state
             │
             ├── Modal Task MCP
             │       → Heavy compute / batch map operations
             │
             ├── Blaxel Filter MCP
             │       → Redaction, sanitization
             │
             ├── ElevenLabs MCP
             │       → Audio narration
             │
             └── SambaNova MCP
                     → Low-cost tagging + memory compression
             │
             ▼
      Gradio Output Layer
             ├── Story Text
             ├── Updated Map
             └── Suggested Actions
```

---

## **Tech Stack**

### **Frontend / UI**

* Gradio 6
* Chat interface
* Image upload
* Gallery viewer
* Settings panel (tone, autonomy, world complexity)
* Dropdown for model selection
* Mobile-responsive layout

### **Primary LLM**

* Claude 4.5 Sonnet (Anthropic)

  * Responsible for planning, narrative consistency, context retention, tool scheduling, and world logic.

### **Secondary LLM Tools (MCP)**

* **Google Gemini Vision**

  * Parses uploaded images into structured scene graphs.

* **HuggingFace / Flux / Nano Banana Image Generator**

  * Produces cleaned, stylized maps.

* **OpenAI GPT-5.1**

  * Fast procedural text generation
  * Code-like utilities
  * Cleanup tasks

### **Sponsor Tool Integrations**

* **Modal:** Heavy compute or batch operations
* **ElevenLabs:** Optional voice narration
* **Blaxel:** Input sanitization + privacy filtering
* **SambaNova:** Low-cost inference for tagging/compression

---

## **Agentic Capabilities**

* Multi-step narrative planning
* Dynamic tool routing and error recovery
* Scene graph reasoning
* World memory system
* Semi-autonomous storytelling mode
* Tool-driven map generation and consistency checking
* Long-context memory for storyline and world state

---

## **User Flow**

1. User starts an adventure.
2. User enters a prompt or uploads a map sketch.
3. Claude determines whether to call MCP tools.
4. If image provided:

   * Gemini Vision: scene graph
   * Map Generator: cleaned map
5. Claude updates world memory (regions, NPCs, quests, inventory).
6. Claude produces story continuation.
7. Gradio displays:

   * Story text
   * Generated/updated map
   * Suggested next actions

---

## **MCP Tools Used**

### **Scene Parser (Gemini Vision)**

**Input:** Image
**Output:** Structured scene graph with objects, terrain, notes, coordinates.

### **Map Generator (HF Image Model / Nano Banana)**

**Input:** Scene graph or text description
**Output:** High-resolution map image

### **Memory MCP**

Persistent world state:

* NPCs
* Regions
* Plot threads
* Inventory
* Timeline events

### **OpenAI MCP (Fast Text Ops)**

* Summaries
* Cleanup
* Procedural utilities

### **Modal MCP**

* Heavy image preprocessing
* Parallel operations

### **Blaxel MCP**

* Sanitization and PII removal

### **ElevenLabs MCP**

* Audio narration

### **SambaNova MCP**

* Cheap classification / memory compression

---

## **Installation**

```
pip install gradio anthropic openai google-generativeai huggingface_hub diffusers pydantic fastapi
```

Additional MCP tools are located in `mcp-tools/`.

---

## **Running Locally**

```
python app.py
```

---

## **Submission Checklist**

* [x] Gradio application
* [x] MCP tool integration
* [x] Autonomous reasoning and planning
* [x] Multimodal input support
* [x] Sponsor tools used
* [x] Documentation included
* [x] Demo-ready structure

---

## **Demo Video Outline**

1. Start a new story
2. Upload a hand-drawn sketch
3. Show scene graph extraction
4. Show the generated map
5. User makes a choice
6. Story progresses with memory updates
7. Optional but nice to have: ElevenLabs narration

---

## **Project Structure (planned)**

```
/mythweaver
  ├── app.py
  ├── README.md
  ├── requirements.txt
  ├── /mcp-tools
  │     ├── gemini_vision/
  │     ├── map_generator/
  │     ├── memory_store/
  │     ├── modal_tasks/
  │     ├── blaxel_filter/
  │     ├── elevenlabs_audio/
  │     └── sambanova_inference/
  ├── /assets
  │     └── example_maps/
  ├── /prompts
  │     └── orchestrator_prompt.md
  └── /utils
        └── helpers.py
```
