# Project UAE

Project workspace configured for portable development across computers.

---

## 🚀 Moving Between Computers Workflow

To switch between your devices smoothly without losing work or creating conflicts:

### 1. When finishing work on Computer A (Before shutting down):
```bash
git status
git add .
git commit -m "Describe what was updated"
git push
```

### 2. When starting work on Computer B:
- **First time on Computer B**:
  ```bash
  git clone https://github.com/shameel0505/project_uae.git
  cd project_uae
  ```
- **Every subsequent time before you start coding**:
  ```bash
  git pull
  ```

---

## 🔒 Handling Secrets & Environments (.env)
- Never commit `.env` or sensitive keys to Git (already blocked in `.gitignore`).
- Use `.env.example` to document required environment variables.
- On any new machine, copy `.env.example` to `.env` and fill in local values:
  ```bash
  cp .env.example .env
  ```

