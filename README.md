# BidBrief

BidBrief is a platform designed to streamline the tendering process for UK small and medium‑sized enterprises (SMEs) and bid writers.  The system guides users from uploading a tender pack through compliance checks (PassGate™) all the way to generating a polished Word document ready for submission.  Key features include compliance checklist generation, per‑question answer planning, first‑draft generation, and export to `.docx`.  A high‑level overview of the project goals and technologies is provided below.

## Features

* **Upload & Process Packs** – Users can upload tender packs (ZIP/PDF).  The backend unpacks, performs OCR if necessary, indexes the content into a database/vector store and prepares it for extraction.
* **PassGate™ (Compliance Checklist)** – An extraction pipeline identifies mandatory documents, pass/fail criteria, key dates and evaluation criteria from the tender documents.  Results are surfaced through the API and rendered in the web app.
* **AnswerPlan™ (Per‑Question Planning)** – For each detected question the system generates an outline, evidence prompts and aligns to word limits and weights.  Users can view, edit and mark items as ready.
* **DraftDeck™ (Draft Sections)** – Long‑running jobs produce first‑draft sections (e.g. Methodology, Mobilisation and Social Value) using large language models.  Drafts embed provenance markers so users can trace content back to source documents.
* **WordSync™ Export** – Completed drafts can be exported to Microsoft Word using predefined templates.  Exports include table of contents, correct heading levels and styling.
* **Watchlists** – Basic watchlists allow users to monitor procurement portals such as FTS and Contracts Finder.
* **Authentication & RBAC** – Email magic link login with JWT cookies.  Organisations isolate data, and roles determine access (Owner, Writer, Viewer).
* **Billing** – Stripe Checkout integration for seat‑based plans with usage limits enforced by the API.

This monorepo uses **Turborepo** to coordinate multiple applications and packages, and **Docker Compose** to bootstrap local development.  The frontend is built with Next.js 14 and TypeScript, while the backend and worker services use Python (FastAPI and Celery).  Shared schemas are defined once and reused across TypeScript (Zod) and Python (Pydantic) packages.

## Getting Started

The repository is designed to run locally via Docker Compose.  To get started:

1. Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/).
2. Copy the provided environment examples and fill in secrets:

   ```bash
   cp .env.example .env
   cp apps/web/.env.example apps/web/.env
   cp services/api/.env.example services/api/.env
   cp services/worker/.env.example services/worker/.env
   ```
3. Build and start the stack:

   ```bash
   docker compose -f infra/docker-compose.yml up --build
   ```

4. Seed the database with sample data (e.g. create an organisation and user) using the scripts in `infra/db`.

For development without Docker, each service may be started individually (see the respective `README.md` files in `apps/web` and `services/api`).  You’ll need to install Node.js (for the web app) and Python 3.11 (for the backend).

## Repository Layout

```
/
  README.md          – high level overview and instructions
  turbo.json         – Turborepo pipeline configuration
  package.json       – workspace configuration and common scripts
  .editorconfig      – consistent editor settings
  .gitattributes     – Git attributes (e.g. end of line settings)
  .gitignore         – untracked files and folders
  .prettierrc        – Prettier formatting rules
  .eslintrc.json     – ESLint configuration for TypeScript
  .env.example       – root environment variables template
  /apps
    /web             – Next.js 14 frontend (App Router, TS, Tailwind)
  /services
    /api             – FastAPI backend with SQLAlchemy models and REST endpoints
    /worker          – Celery workers for long running tasks (OCR, extraction, planning, drafting, export)
  /packages
    /ui              – shared React UI components (placeholder)
    /schemas         – shared JSON/Zod (TS) and Pydantic (Python) schemas
    /promptkit       – prompt templates and evaluation fixtures
  /infra
    docker-compose.yml – local development composition
    /db               – database initialisation scripts and migrations
    /docs             – architectural diagrams and documentation (PlantUML/Mermaid)
    /ci               – GitHub Actions workflows
```

### Contributing

This repository uses conventional commits and semantic release to automate changelog generation.  Pull requests should be raised against the `main` branch.  Automated tests and linters run via GitHub Actions on each PR.
