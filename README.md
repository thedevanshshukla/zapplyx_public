# ZapplyX - YC Founder Directory & Personalized Outreach Platform

This repository contains public interface definitions, data schemas, and high-level architectural skeletons for ZapplyX. 

## 🔒 Proprietary Software & License Notice

**Copyright (c) 2026. All Rights Reserved.**

This software is strictly proprietary and confidential. No part of this repository, including the architecture, interface design, data schemas, or code layout, may be copied, reproduced, distributed, replicated, or reverse-engineered in any form or by any means without the prior written permission of the author.

---

## 🛠️ Architectural Blueprint Overview

The project is structured as a distributed FastAPI web application backed by task queues and NoSQL database stores to handle asynchronous crawling, contact verification, and personalized documentation generation.

- **FastAPI Core**: Defines RESTful endpoints, CORS middleware, and dependency injection schemes.
- **Asynchronous Task Workers**: Celery queue definitions for distributed background processing.
- **Agent Framework**: High-level abstract interfaces for data crawling, API-based contact verification, LLM-based text generation, and LaTeX compilation.
- **Data Models**: Pydantic schemas validating user states and founder data shapes.

---

## 📂 Repository Blueprint Structure

This public blueprint showcases the modular software architecture, API design patterns, and database layouts used in the private production repository:

```
public_repo/
├── app/
│   ├── main.py              # Application entrypoint & HTTP server routing
│   ├── config.py            # Pydantic Settings configuration interface
│   ├── database.py          # Asynchronous database connection interface
│   ├── features.py          # Feature gating capability interface
│   ├── models/
│   │   ├── user.py          # Pydantic models for Candidate & Profile Schemas
│   │   └── founder.py       # Pydantic models for Founder & State Schemas
│   ├── routers/
│   │   ├── auth.py          # Authentication and token validation router
│   │   ├── pipeline.py      # Core endpoints orchestrating background jobs
│   │   └── admin.py         # Administrative task monitoring interface
│   ├── agents/
│   │   ├── base.py          # Base LLM Agent design pattern
│   │   ├── scraper.py       # Browser crawler automation interface
│   │   ├── enrichment.py    # Contact verification and enrichment orchestrator
│   │   ├── intelligence.py  # Personalization summary extractor interface
│   │   ├── outreach.py      # Email & LinkedIn pitch generator interface
│   │   └── resume_tailor.py # Document compilation agent interface
│   └── workers/
│       ├── queue.py         # Celery task queue configuration interface
│       └── tasks.py         # Registered background worker tasks
├── LICENSE                  # Strict Proprietary License Notice
└── README.md                # System architectural blueprint overview
```
