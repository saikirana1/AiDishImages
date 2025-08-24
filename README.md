# AI Dish Image Generation Project

## Overview

This project is an end-to-end practical exploration of Generative AI, focused on generating dish images from menu uploads. When a user uploads a dish menu, the system automatically creates realistic images of the listed dishes using OpenAI's DALL-E 3 model. It demonstrates seamless integration of modern AI, semantic search, scalable storage, and a robust user interface.

## Goals

- Learn and implement Generative AI solutions with practical use cases.
- Enable users to visually preview dishes from any uploaded menu.
- Integrate and experiment with modern AI and web technologies.

## Features

- **AI Image Generation:** Uses DALL-E 3 (OpenAI API) to generate dish images based on menu names and descriptions.
- **Semantic Search:** Employs Pinecone Vector Database for efficient semantic dish searching.
- **Image Storage:** Stores generated images in Supabase storage for scalability and easy access.
- **Relational Data:** Utilizes Supabase PostgreSQL for all RDBMS needs (menus, dish metadata, user data).
- **Backend API:** Built with FastAPI, including background task queue management for asynchronous image generation and processing.
- **Frontend UI:** Developed in React, with a modern user interface using Shadcn UI and TanStack Query for efficient state management and data fetching.

## Tech Stack

| Component        | Technology          |
| ---------------- | ------------------- |
| AI Model         | DALL-E 3 (OpenAI)   |
| Semantic Search  | Pinecone Vector DB  |
| Image Storage    | Supabase Storage    |
| RDBMS            | Supabase PostgreSQL |
| Backend API      | FastAPI             |
| Background Tasks | FastAPI + Queue     |
| Frontend         | React               |
| UI Library       | Shadcn UI           |
| Data Fetching    | TanStack Query      |

## How It Works

1. **Upload Menu:** User uploads a dish menu (text or file).
2. **Semantic Extraction:** System parses and semantically searches dish names/descriptions.
3. **Image Generation:** DALL-E 3 generates dish images based on extracted text.
4. **Storage:** Images are saved in Supabase Storage; metadata in PostgreSQL.
5. **Instant Preview:** User views generated dish images alongside each menu item.
6. **Background Processing:** Heavy image generation jobs are queued and processed asynchronously for scalability.

## Getting Started

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   ```
2. **Backend Setup**

   - Install dependencies: `pip install -r requirements.txt`
   - Configure FastAPI, Pinecone, Supabase, and OpenAI API credentials in `.env`

3. **Frontend Setup**

   - Install dependencies: `npm install`
   - Configure Supabase connection and backend API endpoint

4. **Run locally**
   - Start FastAPI backend
   - Start React frontend

## Learning Outcomes

- Hands-on experience with Generative AI image models
- Integration of vector databases for semantic search
- Building async background tasks in Python FastAPI
- Using Supabase as scalable backend and storage solution
- Modern React frontend development with TanStack Query and Shadcn UI

## Contributing

Contributions are welcome! Open issues, feature requests, or submit pull requests to expand the project.

---

This project is for educational and experimental purposes to explore Generative AI systems practically.
