# Project UAE — Innovation, Challenges & Agentic AI Workspace

A portable engineering workspace configured for rapid prototyping and competing in high-stakes UAE & global technology challenges.

---

## 📚 Core Intelligence & Action Files

* 🎯 **[ACTIVE_CHALLENGES_BLUEPRINT.md](./ACTIVE_CHALLENGES_BLUEPRINT.md)**: Detailed technical specs, architectures, problem statements, and winning project ideas for our immediate priority challenges (ITU AI for Good, Future Health, Voice of the Oasis, Nestlé NextGen, Nabat TerraPod, and Create AI Agents).
* 📊 **[uae_opportunities_database.md](./uae_opportunities_database.md)**: The comprehensive master intelligence database covering open competitions, grant funds, developer challenges, and monitoring archives.

---

## 🚀 Moving Between Computers Workflow

To switch between your laptop, desktop, or work computers smoothly without losing state:

### 1. When finishing work on Computer A (Before shutting down):
```bash
git status
git add .
git commit -m "Progress update"
git push
```

### 2. When starting work on Computer B:
* **First time on Computer B**:
  ```bash
  git clone https://github.com/shameel0505/project_uae.git
  cd project_uae
  ```
* **Every subsequent time before you start coding**:
  ```bash
  git pull
  ```

---

## 🤖 Resuming with AI on Another Computer

When you open this folder on another machine in Antigravity or your AI assistant, simply say:
> *"I am continuing my session from my other computer for `project_uae`. Check `ACTIVE_CHALLENGES_BLUEPRINT.md` and `uae_opportunities_database.md` to see our current state and priorities."*

---

## 🔒 Handling Secrets & Environments (.env)
* Sensitive keys are strictly untracked by Git via `.gitignore`.
* Use `.env.example` to configure local keys when starting on a new device:
  ```bash
  cp .env.example .env
  ```
