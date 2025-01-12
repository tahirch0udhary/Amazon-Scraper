# Amazon Product Scraper and Frontend Viewer

## Overview

This project is designed to scrape product information from Amazon using a Python script and display the scraped data through a user-friendly frontend application built with React. The backend script fetches product details based on a set of predefined search queries and stores the data in JSON format. The frontend application reads these JSON files and presents the data in a tabular format, allowing users to browse through different product categories effectively.

## Project Components

- **Backend Script**: A Python-based scraper that extracts product information from Amazon.
- **Frontend Application**: A React application that displays products in a table format, enabling easy viewing and interaction with the scraped data.

### Backend Features

- Scrape product details such as title, price, rating, number of reviews, and image URLs.
- Store data in JSON format for easy retrieval by the frontend application.
- Handle pagination to scrape multiple pages of search results.

### Frontend Features

- Display product information in a responsive table.
- Allow users to select different categories of products to view.
- Responsive design for optimal viewing on various devices including desktops, tablets, and smartphones.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Node.js 16.x
- npm (Node Package Manager)

### Setup and Installation

#### Backend Setup

1. **Clone the repository**: git clone https://yourrepository.com/project.git
2. **Navigate to the backend directory**: cd script
3. **Set up a Python virtual environment**:
```bash
python -m venv venv
venv/bin/activate # for windows
source venv/bin/activate # for mac/linux
```
4. **Install required packages**: pip install -r requirements.txt
- if you facing error then install manually:
```bash
pip install beautifulsoup4
pip install playwright
playwright install
```
5. **Run the scraper**: python script.py
After this resulting json files will goes to frontend public folder

#### Frontend Setup
1. **Navigate to the frontend directory**: cd frontend/scraper-frontend
2. **Install required packages**: npm install
3. **Start the application**: npm run dev
4. **Open the application in your browser**
