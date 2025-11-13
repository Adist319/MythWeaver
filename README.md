## **Overview**

MythWeaver is a multimodal, agentic storytelling system built with Gradio and the Model Context Protocol (MCP). The core innovation is a **custom Narrative Engine MCP server** that exposes context-aware narrative generation as a reusable tool for ANY application. Users interact through text and optional map/sketch uploads. The system interprets drawings, converts them into structured scene graphs, generates styled maps, and uses the Narrative Engine MCP to dynamically generate objectives, plot hooks, and narrative opportunities.

**Novel Contribution:** The Narrative Engine MCP server provides domain-agnostic narrative generation tools that can be used by games, interactive fiction, writing tools, tabletop RPG assistants, and educational applications.

---

## **Features**

### **Core MCP Innovation**
* **Narrative Engine MCP Server** - Novel, reusable MCP tool for narrative generation
  * Analyzes structured context (world state, entities, relationships, scene graphs)
  * Generates narrative objectives, plot hooks, conflicts, and resolutions
  * Domain-agnostic design works for stories, games, education, writing tools
  * Exposes standardized MCP interface with multiple tools

### **Application Features**
* Text-based adventures with user-steered or semi-autonomous narration
* Sketch / map upload for geography-driven storytelling
* Vision parsing into structured scene graphs (Gemini Vision MCP)
* High-resolution map generation (Flux/SDXL MCP)
* Long-context world memory (Memory Store MCP)
* Gradio 6 interface with mobile support

---

## **Architecture (Text Diagram)**

```
User
 └── Gradio UI
       ├── Text Input
       ├── Image Upload
       └── Quest Selection
             │
             ▼
      Claude 4.5 Sonnet (Anthropic, Orchestrator)
             ├── World-memory reasoning
             ├── Narrative generation
             ├── Tool selection & routing
             └── Multi-step planning
             │
             ├── ⭐ Narrative Engine MCP (CUSTOM - Our Novel Contribution)
             │       → generate_narrative_objectives(context, genre, count)
             │       → analyze_narrative_opportunities(scene_graph, entities)
             │       → Returns structured objectives with narrative hooks
             │
             ├── Gemini Vision MCP (Google)
             │       → parse_scene(image) → Scene Graph
             │
             ├── Map Generator MCP (Flux/SDXL)
             │       → generate_map(scene_graph) → Styled Map Image
             │
             └── Memory Store MCP
                     → update_world(locations, NPCs, events)
                     → query_world() → World State
             │
             ▼
      Gradio Output Display
             ├── Story Text
             ├── Generated Maps
             └── Quest Options
```

**Key:** ⭐ = Novel MCP server built for this hackathon

---

## **Tech Stack**

### **Frontend**

* Gradio 6 - Chat interface with image upload and quest selection

### **Orchestrator Model**

* Claude 4.5 Sonnet - Planning, narrative generation, tool routing

### **MCP Servers (4 Core Tools)**

| MCP Server | Purpose | Status |
|------------|---------|--------|
| **⭐ Narrative Engine MCP** | **Context-aware narrative generation** | **Custom - Our contribution** |
| **Gemini Vision MCP** | Scene graph extraction from sketches | Existing |
| **Map Generator MCP** | High-resolution map generation | Existing/Custom |
| **Memory Store MCP** | Persistent world state | Existing |

### **Narrative Engine MCP Server Details**

**Tools Exposed:**

```python
# Tool 1: generate_narrative_objectives
Input:
  - context: dict         # World state, entities, relationships
  - narrative_style: str  # Genre/tone (fantasy, sci-fi, mystery, etc.)
  - count: int           # Number of objectives (1-5)
  - difficulty: str      # easy, medium, hard

Output:
  - List of objectives with:
    - description: str
    - narrative_hook: str       # Why this matters to the story
    - success_criteria: list
    - conflicts: list           # Potential obstacles/antagonists
    - related_entities: list    # NPCs, locations involved
    - estimated_complexity: str

# Tool 2: analyze_narrative_opportunities
Input:
  - scene_graph: dict    # Structured scene data
  - character_state: dict # Character relationships, goals, conflicts

Output:
  - List of narrative opportunities:
    - opportunity_type: str  # conflict, mystery, romance, discovery, etc.
    - description: str
    - involved_entities: list
    - dramatic_potential: float
```

**Implementation:**
* Python MCP server using `mcp` SDK
* LLM-powered analysis (Claude for reasoning, structured outputs)
* Pydantic schemas for type safety
* Domain-agnostic design - works for any narrative context

---

## **Agentic Capabilities**

* Multi-step narrative planning via Claude orchestration
* Autonomous tool routing based on user input
* Scene graph reasoning and validation
* World memory management and updates
* Context-aware narrative generation via Narrative Engine MCP
* Semi-autonomous storytelling flow

---

## **User Flow**

1. User starts an adventure with text or uploads a sketch/map
2. **If image uploaded:**
   * Gemini Vision MCP → extracts scene graph
   * Map Generator MCP → creates styled map
3. Memory Store MCP → updates world state
4. Claude orchestrator → generates story continuation
5. **Narrative Engine MCP** → analyzes context and generates 1-3 dynamic objectives
6. Gradio displays: story text, map, and quest options
7. User selects a quest or continues exploration
8. Loop repeats with updated memory and context

---

## **MCP Tools Summary**

| Tool | Purpose | Type |
|------|---------|------|
| **⭐ Narrative Engine MCP** | **Context-aware narrative generation** | **Custom** |
| Gemini Vision MCP | Sketch → scene graph | Existing |
| Map Generator MCP | Scene graph → map image | Existing/Custom |
| Memory Store MCP | Persistent world state | Existing |

---

## **Setup (uv)**

### 1. Install dependencies

```
uv sync
```

### 2. Run the app

```bash
uv run python app.py
```

---

## **Suggested Project Structure**

```
/mythweaver
  ├── app.py                          # Main Gradio application
  ├── README.md
  ├── pyproject.toml
  ├── .gitignore
  │
  ├── /mcp_servers
  │     └── narrative_engine/         # ⭐ Custom Narrative Engine MCP Server
  │           ├── server.py           # MCP server implementation
  │           ├── schemas.py          # Pydantic models for narrative objects
  │           ├── generator.py        # LLM-powered narrative logic
  │           └── README.md           # Standalone documentation for reuse
  │
  ├── /mcp_clients                    # Client integrations for existing MCP servers
  │     ├── gemini_vision.py          # Gemini Vision MCP client
  │     ├── map_generator.py          # Map Generator MCP client
  │     └── memory_store.py           # Memory Store MCP client
  │
  ├── /prompts
  │     ├── orchestrator.md           # Claude system prompt
  │     └── narrative_generation.md   # Narrative Engine prompt
  │
  ├── /demos
  │     └── cli_demo.py               # Standalone CLI using Narrative Engine MCP
  │
  └── /assets
        └── example_maps/             # Sample sketches for testing
```

---

## **Hackathon Submission Checklist**

- [ ] **Custom Narrative Engine MCP Server** - Novel, reusable tool with clear API
- [ ] **MythWeaver Gradio app** - Primary demo using Narrative Engine
- [ ] **CLI demo** - Second app proving reusability
- [ ] **Multimodal pipeline** (sketch → scene graph → map → narrative objectives)
- [ ] **Autonomous agent behavior** via Claude orchestration
- [ ] **Standalone MCP documentation** - So others can integrate it
- [ ] **Demo video** (1-5 minutes showing both apps)
- [ ] **Social media post** with #MCPBirthday hashtag
- [ ] **GitHub repo** submitted to MCP-1st-Birthday organization

## **Why This Is Novel**

1. **First Narrative Generation MCP Server** - No existing MCP tool does context-aware story generation
2. **Domain-Agnostic Design** - Works for fantasy, sci-fi, mysteries, education, etc.
3. **Proven Reusability** - Two separate demo apps using the same MCP server
4. **Standardized Interface** - Clean APIs that any MCP client can call
5. **Multi-Agent Orchestration** - Shows MCP servers working together in complex workflow

---

## **Demo Flow**

1. **Start adventure** - Text input or sketch upload
2. **Vision parsing** - Gemini Vision MCP extracts scene graph
3. **Map generation** - Map Generator MCP creates styled map
4. **Story generation** - Claude orchestrator writes narrative
5. **Objective generation** - **Narrative Engine MCP** analyzes context and proposes 1-3 narrative objectives
6. **User interaction** - Select quest or continue exploration
7. **Memory update** - Memory Store MCP persists world changes
8. **Loop** - Repeat with updated context

## **Expected Impact**

The Narrative Engine MCP server can be adopted by:

* **Game developers** - Dynamic quest/objective generation for RPGs and adventure games
* **Interactive fiction platforms** - Branching narrative suggestions (Twine, ChoiceScript, etc.)
* **Writing tools** - Context-aware plot suggestions and story prompts (Scrivener, Obsidian plugins)
* **Tabletop RPG tools** - AI Dungeon Master assistance (Roll20, Foundry VTT)
* **Educational apps** - Generate story-based learning scenarios
* **Creative AI apps** - Any app needing narrative context understanding
