## Project Title
##### Automatic-Tag-Generator

## Project Overview
The Automatic Tag Generator is an AI-based application that automatically generates relevant tags from textual content using Natural Language Processing (NLP),TF-IDF vectorization,and MAchine Learning techniques.The system analyzes user provided text,performs preproccessing operations such as tokenization and lemitization,extracts important features,and generates meaningful tags.This helps improve content organization ,categorization and searchability while reducing manual effort.

## Problem Statement
In today's didgital environment large amount of textual content such as blogs,articles,documents and reports are generated daily.Assigning tags manually to such content is time-consuming,inconsistent and prone to human error.An automated system is required to analyze text and generate relavant tags accurately.The proposed Automatic Tag Generator aims to solve this problem by using NLP,TF-IDF and machine learning techniques to produce apppropriate tags automatically.

## Technologies Used

### Frontend
- Streamlit

### Backend
- Python

### Database
- PostgreSQL
  
### Natural Language Processing (NLP)
- NLTK
  - Tokenization
  - Stopword Removal
  - Lemmatization
  
### Feature Extraction
- TF-IDF Vectorization (Scikit-learn)

### Machine Learning
- Logistic Regression / Naive Bayes

### Libraries
- NLTK
- Scikit-learn
- Pandas
- NumPy
- Streamlit

### Development Tools
- VS Code
- Git
- GitHub

## Project Objective
This project automatically generates relevant tags from text using Natural Language Processing (NLP) and Machine Learning techniques.


## User & module identification
- Identified system users
- defined project modules
- Documented preprocessing,feature extraction and ML modules
- prepared system architecture structure

 ## use case and diagram preparation
 images/https://github.com/rithika-art/Automatic-Tag-Generator/blob/main/images/ChatGPT%20Image%20Jun%205%2C%202026%2C%2003_33_50%20PM.png

 ## Database requirement analysis
 #### User Input Data
 - input_id(unique identifier)
 - input_text

 #### Generated Tag Data
 - generated_tags

 #### Training Dataset 
 - text content
 - associated tags

   ## ER Diagram creation

### Entity 1: User_Input
- Input_ID (Primary Key)
- Input_Text

### Entity 2: Generated_Tags
- Tag_Text

### Relationship
- One User Input can generate multiple Tags.

 ## ER DIAGRAM
 images https://github.com/rithika-art/Automatic-Tag-Generator/blob/main/images/ChatGPT%20Image%20Jun%208%2C%202026%2C%2008_54_39%20AM.png

 ## Database Schema Creation

### Table: user_input

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| input_id | SERIAL | Unique identifier |
| input_text | TEXT | User entered text |
| generated_tags | TEXT | Generated tags |

### PostgreSQL Schema

```sql
CREATE TABLE user_input (
    input_id SERIAL PRIMARY KEY,
    input_text TEXT NOT NULL,
    generated_tags TEXT
);
```
