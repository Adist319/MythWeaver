# 🏆 MythWeaver — MCP Hackathon Winning Plan

**Deadline:** November 30, 2025
**Track:** *Building MCP*
**Core Innovation:** **Narrative Engine MCP** — reusable, domain-agnostic narrative generation server
**Goal:** Multimodal storytelling engine (maps, vision parsing, world memory, audio narration)

---

# 🚨 PHASE 0 — Anti-Failure Measures (Required for Demo Stability)

* [ ] Add `exceptions.py` with custom errors
* [ ] Create `FallbackManager` with graceful degradation:
  * [ ] Gemini failure → text-only mode
  * [ ] Modal failure → placeholder map
  * [ ] MCP failure → Claude-only objectives
* [ ] Add retry wrapper (exponential backoff) for all APIs
* [ ] Add timeout wrapper for slow calls
* [ ] Add structured logging (`json` logs)
* [ ] Add `validate_env()` (fail fast if keys missing)

---

# 🏗️ PHASE 1 — Foundation (Days 1–3)

## 1.1 Environment & Keys

* [ ] `.env` + `.env.example`
* [ ] Pydantic `Settings` class for typed secrets
* [ ] `validate_env.py` on startup
* [ ] Separate HF Spaces / local envs

## 1.2 Project Structure

```
mythweaver/
  app.py
  config.py
  core/
    pipeline.py
    world_state.py
    scene_graph_store.py
  mcp_servers/
    narrative_engine/
      server.py
      schemas.py
      prompts.py
      README.md
  mcp_clients/
    gemini_vision.py
    map_generator.py
    memory_store.py
  modal_app/
    map_generator.py
  services/
    claude_client.py
    narration.py
  demos/
    cli_demo.py
  tests/
    test_mcp_server.py
    test_clients.py
  assets/
  prompts/
```

## 1.3 Gradio UI

* [ ] Chat UI with multimodal input
* [ ] Image uploads + preview
* [ ] Quest selection buttons
* [ ] Map display panel
* [ ] Mobile CSS
* [ ] Loading indicators
* [ ] “New Adventure” reset button

## 1.4 Claude Integration

* [ ] Streaming output
* [ ] Token budget logging
* [ ] Error handling & retries

## 1.5 World State

* [ ] Typed `WorldState` model
* [ ] Serialization for HF Spaces
* [ ] State reset logic

---

# ⭐ PHASE 2 — Narrative Engine MCP (Days 4–6)

## 2.1 MCP Server Setup

* [ ] Initialize FastMCP server
* [ ] Add version + metadata
* [ ] Add OpenAPI-style docstrings

## 2.2 Schemas (Typed)

* [ ] Enums: narrative style, difficulty, opportunity types
* [ ] Models: NarrativeObjective, NarrativeOpportunity
* [ ] Input schemas with validation
* [ ] Include example payloads

## 2.3 Tool 1 — `generate_narrative_objectives`

* [ ] Tight prompt + JSON schema
* [ ] Deterministic structure
* [ ] Complexity scoring
* [ ] Structured error messages

## 2.4 Tool 2 — `analyze_narrative_opportunities`

* [ ] Scene-graph interpretation
* [ ] Relationship-aware analysis
* [ ] Dramatic potential scoring

## 2.5 Testing (Judge-critical)

* [ ] Normal cases
* [ ] Error cases
* [ ] Missing fields
* [ ] Schema validation
* [ ] Long context
* [ ] Randomized fuzz tests

## 2.6 CLI Demo

* [ ] CLI using MCP server
* [ ] Standalone reusability proof
* [ ] Documented in `demos/README.md`

---

# 🎨 PHASE 3 — Multimodal Pipeline (Days 7–10)

## 3.1 Gemini Vision → Scene Graph

* [ ] Fantasy map extraction prompt
* [ ] Extract: locations, entities, relationships, topology
* [ ] Handle messy hand-drawn maps
* [ ] Cache results

## 3.2 Modal Map Generation (FLUX.1)

* [ ] L40S GPU config
* [ ] Prompt builder from scene graph
* [ ] Diffusion pipeline → PNG bytes
* [ ] Pre-warm GPU before demo
* [ ] Fallback → placeholder map

## 3.3 Full Pipeline Orchestration

* [ ] Async support
* [ ] Parallel map gen + objective gen
* [ ] Unified error handling
* [ ] Structured logs per step

---

# 🧠 PHASE 4 — Memory System (Days 11–13)

## 4.1 Basic Memory (MVP)

* [ ] Dict-based store
* [ ] Store locations, entities, relationships
* [ ] Feed memory into narrative generation

## 4.2 Scene & Quest Tracking

* [ ] Track latest scene graph
* [ ] Track quest history
* [ ] Retrieve relevant context

## 4.3 Relationship Engine

* [ ] Track alliances / hostility
* [ ] Store major events
* [ ] Influence future objectives

> (Optional) LlamaIndex RAG → Mention in README only.

---

# 🔊 PHASE 5 — Polishing & Sponsor Value (Days 14–15)

## 5.1 ElevenLabs Narration

* [ ] Narrate final story chunk
* [ ] Autoplay
* [ ] On/off toggle

## 5.2 UX Polish

* [ ] Clean message formatting
* [ ] Smooth map reveal
* [ ] Error popups
* [ ] Loading animations

## 5.3 Observability

* [ ] JSON logs
* [ ] Tool-call tracing
* [ ] Performance timing

## 5.4 Sponsor Matrix (for submission)

* Anthropic → Orchestrator + MCP reasoning
* Google → Vision → Scene graph
* Modal → GPU diffusion
* ElevenLabs → Narration
* Flux/SDXL → Map

---

# 🚀 PHASE 6 — Deployment & Submission (Days 16–17)

## 6.1 HuggingFace Spaces

* [ ] Generate `requirements.txt` from pyproject
* [ ] Add secrets in HF dashboard
* [ ] Validate CPU-only fallback
* [ ] Confirm modal → HF call works

## 6.2 Demo Video (3–5 min)

1. Upload hand-drawn map
2. Gemini extracts scene
3. Narrative Engine MCP generates objectives
4. User selects quest
5. Claude continues story
6. Modal generates new map
7. ElevenLabs narrates
8. CLI demo to prove reusability

## 6.3 Repo Polish

* [ ] README.md

  * Overview
  * Feature list
  * Installation
  * Usage
  * Architecture diagram
  * Sponsor integrations
* [ ] ARCHITECTURE.md
* [ ] MCP_SERVER.md
* [ ] Demo GIFs

## 6.4 Final Submission

* [ ] HF Space URL
* [ ] GitHub repo
* [ ] Demo video
* [ ] Sponsor summary
* [ ] Highlight innovation:

  > “Narrative Engine MCP — a reusable, domain-agnostic narrative generation server powering multiple clients.”

---

# 🏆 PRIORITY STACK (What Will Win)

### **Tier 1 — Must Ship**

* Narrative Engine MCP
* Gemini Vision
* Modal map generation
* Claude orchestration
* Gradio UI
* CLI demo
* Fallback logic
* HF Spaces + video

### **Tier 2 — Strong Bonus**

* ElevenLabs narration
* Structured logs
* UI polish
* Memory system

### **Tier 3 — Optional**

* RAG
* SambaNova
* Blaxel

