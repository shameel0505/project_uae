# Active Challenges Blueprint & Action Plan

*This document contains the complete technical briefing, project blueprints, architecture specs, and continuation plan from our session. Pull this repository on any computer to pick up development immediately.*

---

## 📌 Executive Status (4 November 2026)

* **Repository:** `https://github.com/shameel0505/project_uae`
* **Primary Focus:** High-yield innovation competitions with **zero company requirement**, **cash/grant prizes**, and **deep AI/autonomous agent development**.
* **Immediate Priority Track (Next 7 Days):**
  1. **ITU AI for Good Lab Hackathon** — Closes **5 November 2026 (Tomorrow)**
  2. **Future Health Digital Innovation** — Safe Deadline **10 November 2026**
  3. **Voice of the Oasis (ElevenLabs)** — Closes **10 November 2026**
  4. **Nestlé NextGen Founders** — Closes **11 November 2026**
* **Major Medium-Term Flagships:**
  * **Nabat TerraPod Challenge** ($50,000 USD) — Closes **19 November 2026**
  * **Create AI Agents Championship** ($750,000 USD) — Closes **January 2027**

---

## 🚀 Deep-Dive Technical Blueprints (Active Opportunities)

---

### 1. 🏛️ ITU AI for Good Lab Hackathon (UAE)
* **Deadline:** **5 November 2026 (Tomorrow)**
* **Event:** 8 December 2026 at Dubai Exhibition Centre (Expo City Dubai)
* **Prize:** CHF 4,700 total (1st: CHF 1,500; 2nd: CHF 1,000; 3rd: CHF 600) + UN stage presentation.
* **Team:** Solo or teams up to 4. No company required.
* **Portal:** [ITU AI for Good Hackathon](https://aiforgood.itu.int/event/ai-for-good-sandbox-hackathon-united-arab-emirates/?topic=485)

#### What to Build:
An **Agentic Compliance & Knowledge Interceptor ("GovShield-Agent")**:
* **Problem:** Autonomous AI agents make decisions that risk violating local policies, data residency laws, or domain-specific guidelines (e.g., patient data privacy, UAE AI ethics).
* **Architecture:**
  ```text
  [User Request] ──> [Autonomous Agent (LangChain / CrewAI)]
                             │ (Proposed Function Call / Tool Action)
                             ▼
                 [GovShield Interceptor Middleware]
                   ├── Vector Search on UAE Legal & Policy Knowledge Base
                   ├── Semantic Triple Graph Validation
                   └── Output: APPROVED (Sign Action) OR REJECTED (Feedback loop)
                             │
                             ▼
                 [Executed Real-World Tool API]
  ```
* **Key Features:**
  * Ingest UAE Personal Data Protection Law and healthcare data regulations into a lightweight vector database (Chroma/Qdrant) or SQLite knowledge graph.
  * Intercept proposed function calls before execution.
  * Provide real-time audit logs of compliant agent actions.

---

### 2. 🏥 Future Health Digital Innovation Challenge
* **Registration Deadline:** **10 November 2026 (Safe)** / 15 November
* **Working Prototype Due:** **20 November 2026**
* **Prize Pool:** **$105,000 USD** (1st: $50k; 2nd: $35k; 3rd: $20k) + clinical mentorship.
* **Team:** Individuals or teams up to 5. No company required.
* **Portal:** [Hack2skill Challenge Portal](https://hack2skill.com/event/futurehealthchallenge/)

#### What to Build:
Choose one of two high-scoring paths:

#### Option A: Population Health Predictive Engine
* **Focus:** Early detection of chronic cardiovascular or metabolic diseases across patient populations.
* **Stack:** Python (FastAPI), scikit-learn / LightGBM, Streamlit / Next.js frontend, SHAP for model explainability.
* **Deliverable:** Interactive clinician dashboard where patient vitals/biomarkers are input, returning a calculated risk trajectory and the top 3 contributing factors.

#### Option B: Wearable Metabolic AI Companion
* **Focus:** Continuous glucose/vitals telemetry agent for proactive wellbeing.
* **Stack:** Time-series feature extraction, local LLM agent providing proactive lifestyle adjustments before glucose spikes.

---

### 3. 🎙️ Voice of the Oasis (ElevenLabs Voice AI Hackathon)
* **Registration Deadline:** **10 November 2026**
* **Hackathon:** 24–25 November 2026 (24h overnight sprint) at Dtec, Dubai Silicon Oasis
* **Perks:** ElevenLabs API credits, Doers Summit VIP passes, live main-stage demonstration.
* **Team:** Solo or teams up to 5. Free entry.
* **Portal:** [Luma Application Page](https://luma.com/voice-of-the-oasis)

#### What to Build:
**"OasisSetup-Voice" — Multilingual Interactive Concierge**:
* **Challenges to pick from:**
  1. *Visitor Wayfinding Guide*
  2. *Business-Setup Assistant (90+ languages)*
  3. *Service Concierge*
* **Architecture:**
  ```text
  [Microphone Audio] ──(WebSocket)──> [ElevenLabs Conversational AI SDK]
                                               │
                                       (Function Calling)
                                               ▼
                              [FastAPI Backend / External APIs]
                               ├── search_dso_license_tiers()
                               ├── calculate_visa_costs()
                               └── book_consultation_slot()
  ```
* **Winning Edge:** Sub-second response latency + functional tool calling that renders live UI cards on-screen while speaking.

---

### 4. 🌿 Nestlé NextGen Founders
* **Application Deadline:** **11 November 2026**
* **Prize Grants:** **AED 150,000** total pool + incubation + zero equity.
* **Eligibility:** Ages 18–30 UAE residents (students, graduates, early founders). Solo or teams.
* **Portal:** [Sheraa Application Portal](https://sheraa.ae/nestle-nextgen)

#### What to Build:
**"ShelfVision AI" — Edge Spoilage & Cold-Chain Optimization**:
* **Problem:** Supermarkets and distributors lose millions in perishable goods waste.
* **Solution:** Computer vision model (YOLOv8) monitoring produce freshness on shelves or in transit, predicting shelf-life decay and automatically recommending dynamic pricing to clear inventory before expiration.

---

### 5. 🌾 Nabat TerraPod Challenge (Hardware & Robotics)
* **Deadline:** **19 November 2026**
* **Prize:** **$50,000 USD** (AED 183,600) + real-world UAV field deployment.
* **Eligibility:** Individuals 18+, researchers, startups. No company needed.
* **Portal:** [ChallengeON Portal](https://challengeon.atrc.ae/en/challenges/ntpc)
* **What to Build:** Biodegradable seed pods optimized for drone payload drops, soil moisture retention materials, and desert germination enhancement.

---

### 6. 👑 Create AI Agents Championship (Flagship Anchor)
* **Deadline:** **January 2027**
* **Prize Pool:** **$750,000 USD total** ($150,000 per category winner + overall title grant).
* **Eligibility:** Individuals & teams up to 6. Worldwide. No company needed.
* **Portal:** [Create AI Agents Official Page](https://myhub.dubaichamber.com/en/web/dubai-chamber-of-digital-economy/create-ai-agents)
* **What to Build:** An original, autonomous multi-step agent in Business Automation, Personal Productivity, Societal Good, or Youth (<21).

---

## 💻 How to Seamlessly Continue on Computer B

When you switch to your laptop or other workstation:

### Step 1: Open Terminal & Pull the Code
* **If it's the first time on that computer:**
  ```bash
  git clone https://github.com/shameel0505/project_uae.git
  cd project_uae
  ```
* **If the repo is already on that computer:**
  ```bash
  cd project_uae
  git pull
  ```

### Step 2: Resume Pair Programming with your AI Assistant
Open the project directory in your IDE/editor, and start the conversation by pasting this exact prompt:

```markdown
I am continuing my session from my other computer for `project_uae`. 
Everything is documented in `README.md`, `ACTIVE_CHALLENGES_BLUEPRINT.md`, and `uae_opportunities_database.md`. 
Check our immediate priorities (ITU AI for Good, Future Health, Voice of the Oasis) and let's start implementing the code for our selected project.
```

Your AI assistant will immediately read the files in the workspace and continue without missing any context.
