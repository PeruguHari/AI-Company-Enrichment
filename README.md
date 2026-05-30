# AI Company Enrichment System

## Overview

AI Company Enrichment System is a web application that extracts business information from company websites and uses Generative AI to generate valuable business insights.

The application scrapes website content, identifies contact information, analyzes business offerings, and generates outreach-ready insights through an easy-to-use dashboard.

---

## Features

* Website scraping and content extraction
* Contact information extraction (emails and phone numbers)
* AI-powered business analysis using Google Gemini
* Company profile generation
* Target customer identification
* Business pain point analysis
* Outreach message generation
* Web dashboard for real-time enrichment
* JSON-based structured output
* Cloud deployment using Render

---

## Tech Stack

### Backend

* Python
* Flask

### Web Scraping

* Requests
* BeautifulSoup

### AI Integration

* Google Gemini API

### Frontend

* HTML
* Bootstrap
* JavaScript

### Deployment

* Render

---

## Project Structure

```text
AI-Company-Enrichment/
│
├── app.py
├── scraper.py
├── ai_processor.py
├── enrichment.py
├── storage.py
├── data.json
├── requirements.txt
├── Procfile
├── .gitignore
│
└── templates/
    └── index.html
```

---

## Workflow

1. User enters a company website URL.
2. The scraper extracts website content.
3. Contact details are collected.
4. Google Gemini analyzes the content.
5. Business insights are generated.
6. Results are displayed on the dashboard.
7. Data is stored in JSON format.

---

## Output Fields

* Website Name
* Company Name
* Address
* Mobile Number
* Email
* Core Service
* Target Customer
* Probable Pain Point
* Outreach Opener

---

## Deployment

Live Application:

https://ai-company-enrichment-dauw.onrender.com

GitHub Repository:

https://github.com/PeruguHari/AI-Company-Enrichment

---

## Author

Perugu Hari

Developed as part of the AI & Automation Developer Hiring Challenge.
