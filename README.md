# Movies Assignment - Report Generator

## Overview

This Python project parses a movies dataset and generates various reports based on year, genre, or top votes. The program allows the user to request **multiple reports simultaneously** via command-line arguments.

The project demonstrates:

- File parsing with CSV
- Using classes and data structures for clean organization
- Environment variable usage for file paths
- Command-line argument validation
- PEP8-compliant Python code

---

## Features

1. **Report by Year**
   - Highest rating and movie
   - Lowest rating and movie
   - Average runtime in minutes

2. **Report by Genre**
   - Number of movies in the genre
   - Average rating

3. **Top Voted Movies**
   - Display top 10 movies by votes for a given year
   - Visual representation of votes using emojis

4. **Multiple Reports**
   - Run multiple reports simultaneously using CLI flags

---

## Dataset

- The dataset used is `movies_dataset.csv`.
- It contains fields: `id, titleType, originalTitle, startYear, runtimeMinutes, genres, rating, numVotes`.
- Ensure this file exists in your project folder.

---

## Environment Setup

1. Create a `.env` file in the project root:
2. **Python Version**: 3.x  
3. **Required Libraries**:  

```bash
pip install python-dotenv
