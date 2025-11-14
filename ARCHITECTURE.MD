# 🏛️ MythWeaver Architecture

**Version:** 0.1.0
**Updated:** November 2025
**Purpose:** Technical architecture reference for judges, contributors, and MCP integrators.

MythWeaver is a **multimodal, agentic storytelling system** powered by a **custom Narrative Engine MCP server**, Gemini Vision for scene understanding, Modal GPUs for map generation, and Claude Sonnet for orchestration.

This document details the internal components, data flows, and system interactions.

---

# ⚙️ High-Level System Diagram

```
                       ┌──────────────────────────────┐
                       │        User (Gradio UI)       │
                       │  - Text input                 │
                       │  - Image uploads (maps)       │
                       │  - Quest selection            │
                       └───────────────┬───────────────┘
                                       │
                                       ▼
                      ┌────────────────────────────────────┐
                      │          Orchestrator (Claude)     │
                      │  - Multi-step planning              │
                      │  - Tool routing via MCP             │
                      │  - Narrative generation             │
                      └───────────────┬───────────────┘
                                      │
        ┌─────────────────────────────────────────────────────────────────┐
        │                             MCP Layer                           │
        └───────────────┬───────────────────┬────────────────────────────┘
                        │                   │
                        │                   │
                        │                   │
        ┌───────────────▼──────────────┐    │      ┌───────────────────────┐
        │     ⭐ Narrative Engine       │    │      │     Gemini Vision     │
        │         MCP Server           │    │      │   (Google)            │
        │  - generate_objectives()     │    │      │ - Sketch → scene graph │
        │  - analyze_opportunities()   │    │      │ - Entities, layout     │
        └───────────────┬──────────────┘    │      └───────────────▲───────┘
                        │                   │                      │
                        │                   │                      │
                        │                   │                      │
       ┌────────────────▼───────────────────┘                      │
       │         World State & Memory Store                         │
       │  - Locations, NPCs, relationships                          │
       │  - Quest history                                           │
       │  - Scene graph store                                       │
       └────────────────┬───────────────────────────────────────────┘
                        │
                        ▼
      ┌───────────────────────────────────────────────────────────────┐
      │                           Modal GPU                            │
      │          (FLUX.1 / SDXL Map Generator MCP Client)             │
      │    - scene_graph → styled fantasy map (PNG)                   │
      └────────────────────────────────┬──────────────────────────────┘
                                       │
                                       ▼
                       ┌──────────────────────────────────────┐
                       │            Gradio Output              │
                       │ - Story text                         │
                       │ - Generated maps                     │
                       │ - Quest options                      │
                       │ - (Optional) Audio narration         │
                       └──────────────────────────────────────┘
```

---

# 🧩 Component Breakdown

## 1. Gradio UI (`app.py`)

**Role:** User interface + session container
**Key Features:**

* Multimodal textbox (text + images)
* Chat history
* Quest selection buttons
* Map viewer
* Audio playback (optional)
* Mobile-friendly layout
* Integrates `gr.State` for world persistence

---

## 2. Orchestrator (Claude Sonnet)

**Role:** Brain of the system
**Responsibilities:**

* Reads user input + world state
* Decides which tools to call
* Generates story text
* Chains narrative + map generation
* Maintains thematic consistency

---

## 3. **Narrative Engine MCP Server** (⭐ core innovation)

Directory: `mcp_servers/narrative_engine/`

### Tools Provided:

1. **`generate_narrative_objectives(context, style, difficulty, count)`**

   * Produces structured, goal-driven narrative objectives
   * Includes hooks, conflicts, success criteria

2. **`analyze_narrative_opportunities(scene_graph, character_state)`**

   * Extracts dramatic opportunities
   * Classifies as conflict, discovery, mystery, romance, etc.
   * Scores dramatic potential

### Architecture:

* FastMCP server
* Pydantic models for strict typing
* Docstring-level API reference
* JSON schema–validated outputs
* Graceful failure / fallback

---

## 4. Gemini Vision Client (`mcp_clients/gemini_vision.py`)

**Role:** Convert hand-drawn maps → structured scene graphs
**Output Contains:**

* Locations
* Landmarks
* Characters
* Spatial relationships
* Terrain features

**Why judges care:**
Reliable scene understanding is a hard multimodal problem.

---

## 5. Modal GPU Map Generator (`modal_app/map_generator.py`)

**Role:** Generate high-quality fantasy maps
**Stack:**

* GPU: L40S
* Model: FLUX.1 or SDXL variant
* Input: scene graph
* Output: PNG bytes

**Fallback:** Produces “template map” when GPU offline.

---

## 6. World State System (`core/world_state.py`)

Tracks:

* Locations
* Entities
* Relationships
* Quest history
* Last scene graph
* Player metadata

Purpose:

* Ensures continuity
* Supplies MCP tools with context
* Bridges multiple turns of the story

---

## 7. Story Pipeline (`core/pipeline.py`)

Defines the **full orchestration**:

1. Receive user message / image
2. Extract scene graph
3. Update world state
4. Call MCP tools
5. Generate story continuation
6. Generate map (async)
7. Combine outputs → UI

---

## 8. Memory Store MCP Client (`mcp_clients/memory_store.py`)

Simple version (MVP):

* Dictionary-based
* In-memory storage
* Provides structured retrieval for Claude

Later upgrade (optional):

* LlamaIndex for semantic search

---

## 9. Optional ElevenLabs Narration (`services/narration.py`)

Converts story paragraphs → audio clips.
**Judges love this as a finishing touch**, but it’s not core.

---

# 🧱 Data Flow

### **User Input → Scene Graph**

```
image.png 
    → Gemini Vision 
        → scene_graph.json
```

### **Scene Graph → Narrative Engine MCP**

```
scene_graph + world_state 
    → analyze_opportunities() 
    → generate_objectives()
```

### **User Objective Choice → Claude**

```
objective + history + memory 
    → story_continuation
```

### **Scene Graph → Modal Map Generator**

```
scene_graph 
    → map_generator_gpu() 
    → fantasy_map.png
```

### **Final Output**

```
{story_text, quest_options, map_image, audio(optional)}
```

---

# 🛡️ Reliability Architecture (Winning Requirement)

### **Error Handling**

* Gemini failure → fallback to text-only scene interpretation
* Modal GPU failure → pre-cached placeholder map
* MCP server failure → Claude-based objective generation
* Claude error → retry → summarize fallback

### **Timeout Controls**

* All external APIs wrapped with `asyncio.wait_for()`
* Max 30s GPU jobs
* Max 10s MCP inference

### **Structured Logging**

Each step logs:

```
{
  "component": "modal",
  "event": "map_generation",
  "latency_ms": 3200,
  "status": "success"
}
```

---

# 🔗 Integration Map (Sponsors)

| Sponsor                   | Usage                                               |
| ------------------------- | --------------------------------------------------- |
| **Anthropic**             | Story generation, tool orchestration, MCP reasoning |
| **Google**                | Gemini Vision for scene graphs                      |
| **Modal**                 | GPU diffusion for map generation                    |
| **HuggingFace**           | Deployment of Gradio app                            |
| **ElevenLabs** (optional) | Audio narration                                     |
| **Flux/SDXL**             | High-res map models                                 |

---

# 🧪 Testing Strategy

### Unit Tests

* MCP server tool outputs
* Scene graph validation
* WorldState update logic
* Pipeline branching and fallbacks

### Integration Tests

* Full pipeline run:

  1. messy image → scene graph
  2. narrative engine → objectives
  3. map generation
  4. story continuation

### Stress Tests

* Repeated tool calls
* Large context windows
* Multiple quest loops

---

# 📦 Packaging & Deployment

### HF Spaces

* CPU-only fallback mode
* Secrets injected
* Modal used externally
* Local caching for speed

### CLI Demo

* Proven reusable MCP server
* Minimal dependencies
* Works without Gradio

---

# 🏁 Architecture Summary

MythWeaver is designed with:

* **Reusability** (core MCP engine)
* **Reliability** (fallbacks, retries, structured logs)
* **Multimodal AI** (vision → scene → narrative → maps)
* **Agentic orchestration** (Claude selects tools)
* **Judge-focused clarity** (clean diagrams + typed schemas)
