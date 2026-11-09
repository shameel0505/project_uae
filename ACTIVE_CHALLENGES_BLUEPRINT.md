# Active Challenges Blueprint & Action Plan

*This document contains the complete technical briefing, project blueprints, architecture specs, and continuation plan from our session. Pull this repository on any computer to pick up development immediately.*

---

## 📌 Executive Status (Updated 9 November 2026)

* **Repository:** `https://github.com/shameel0505/project_uae`
* **Lead Engineer:** Mohamed Shameel (`shameel0505@gmail.com`)
* **Primary Focus:** High-yield innovation competitions with **zero company requirement**, **cash/grant prizes**, and **deep AI / autonomous engineering**.
* **Immediate Priority Track (Next 10 Days):**
  1. 🌾 **Nabat TerraPod Challenge** ($50,000 USD / AED 183.6k) — Phase 1 Proposal Closes **19 November 2026**.
     * **Full Execution Dossier:** See [`NABAT_TERRAPOD_EXECUTION_DOSSIER.md`](file:///c:/Users/m.shameel/Downloads/project_uae/NABAT_TERRAPOD_EXECUTION_DOSSIER.md).
  2. 🤖 **Google Gemma 4 Developer Agent (Code Track)** ($75,000 USD) — Entry/Merge **25 November 2026** / Final Code **2 December 2026**.
  3. 💳 **CBUAE Financial Health Innovation** (AED 120,000) — Closes **30 November 2026**.
  4. 🏜️ **Tatweer Hackathon (Ed. 2)** (AED 100,000) — Closes **30 November 2026**.
* **Major Medium-Term Flagships:**
  * 👑 **Create AI Agents Championship** ($750,000 USD) — Closes **December 2026** (Finals: May 2027).
  * 🏛️ **Global Best M-Gov Award & WGS 2027 GovTech Prize** (AED 1,750,000) — Closes **Dec 2026 / Jan 2027**.

---

## 🚀 Deep-Dive Technical Blueprints (Active Opportunities)

---

### 1. 🌾 Nabat TerraPod Challenge (Hardware & Materials Science)
* **Deadline:** **19 November 2026** *(Phase 1 Written Proposal Deck, 8–10 Slides PDF)*
* **Prize:** **$50,000 USD** (AED 183,600) + UAV field validation across Abu Dhabi desert + commercial partnership with Nabat.
* **Host:** ASPIRE / Advanced Technology Research Council (ATRC) Abu Dhabi + Nabat (VentureOne).
* **Eligibility:** Individuals 18+, researchers, innovators, teams. No registered company required.
* **Portal:** [ChallengeON NTPC Portal](https://challengeon.atrc.ae/en/challenges/ntpc)
* **Phase Structure ($0 Upfront Cost):**
  * **Phase 1 (Due 19 Nov 2026):** Purely a **written technical proposal** (8–10 slides PDF, $0 cost).
  * **Phase 2 (December 2026):** **Video pitch** to the ATRC expert jury ($0 cost).
  * **Phase 3 (Materials Jan 2027; Drone Trials Jan–Feb 2027):** Physical biodegradable seed pods required **only if** selected as a finalist.
* **Our Project Blueprint:** **Nabat-BioDrop™ Ovoid TerraPod**
  * Complete 10-slide word-for-word copy, aerodynamic CAD specs, UAE supplier map, and peer-reviewed citations are fully detailed in [`NABAT_TERRAPOD_EXECUTION_DOSSIER.md`](file:///c:/Users/m.shameel/Downloads/project_uae/NABAT_TERRAPOD_EXECUTION_DOSSIER.md).
  * **Key Innovations:**
    1. *Prolate Ovoid Geometry ($C_d = 0.29$):* Reduces wind drift by 62% vs spheres and self-anchors into sand at 16.2 m/s impact.
    2. *Translucent PAR Optical Window:* Transmits 82% photosynthetically active radiation, solving the photoblastic requirement of native seeds (*Cyperus*, *Eremobium*).
    3. *15µm Carnauba Weathering Barrier:* Suppresses false germination from fleeting morning dew (<3mm).
    4. *UAE Date Palm Waste Valorization:* 68% circular local biomass, slashing factory-gate cost to **AED 0.342 per pod** ($\le$ AED 0.40 ceiling).

---

### 2. 🤖 Google Gemma 4 Developer Agent (Code Track)
* **Entry / Team Merge Deadline:** **25 November 2026**
* **Final Code Submission:** **2 December 2026**
* **Platform:** Kaggle (100% Online, Free Entry)
* **Prize Pool:** **$75,000 USD** (Direct Cash)
* **Tech Scope:** Fine-tuning lightweight Gemma 4 open-weights models into fully offline autonomous software engineering agents solving multi-turn SWE-bench GitHub issues.

#### What to Build:
* **Architecture:**
  ```text
  [Issue Description + Repo Index]
                │
                ▼
  [Gemma 4 Orchestrator Agent] ──> [File Tree & Grep Search Tool]
                │                               │
                ▼ (Hypothesis Generation)       ▼ (Relevant Source Files)
  [Synthesizer Agent] ───────────────> [Patch Generator Tool]
                │
                ▼ (Unified Diff)
  [Local Sandbox Test Runner] ───────> PASS: Emit Submission / FAIL: Self-Correction Loop
  ```
* **Winning Edge:** Fine-tuned tool-calling syntax, constrained multi-file context windows, and test-driven self-correction loops running completely offline without external internet.

---

### 3. 👑 Create AI Agents Championship (Flagship Anchor)
* **Deadline:** **December 2026** (Grand Final: May 2027)
* **Entry Fee:** **Free**
* **Prize Pool:** **$750,000 USD total** (4x AED 550,000 category winners + AED 1,000,000 overall title grant).
* **Eligibility:** Individuals & teams up to 6. Worldwide. No company needed to enter (Dubai trade license required only post-win to claim grant funds).
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
Everything is documented in `README.md`, `ACTIVE_CHALLENGES_BLUEPRINT.md`, `NABAT_TERRAPOD_EXECUTION_DOSSIER.md`, and `uae_opportunities_database.md`. 
Check our immediate priority (Nabat TerraPod Challenge due 19 Nov 2026) and let's finalize the proposal slides and materials.
```

Your AI assistant will immediately read the files in the workspace and continue without missing any context.
