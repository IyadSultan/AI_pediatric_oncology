# Medical AI Educational Resources

A collection of Python notebooks and tutorials focused on healthcare AI applications, particularly for pediatric oncology and clinical text analysis.  These files were prepared by Dr. Iyad Sultan / AI office @ KHCC

## Overview

This repository contains educational materials designed to help healthcare professionals learn Python programming and AI applications specific to medical contexts. The tutorials progress from basic Python concepts to more advanced natural language processing and machine learning techniques for clinical data.

## Tutorials

### 1. Python for Pediatric Oncology: Introductory Coding Workshop
**(`01_Python_for_Pediatric_Oncology.ipynb`)**

An introductory Python course designed specifically for pediatric oncologists and healthcare professionals with minimal coding experience. It covers:

- Basic Python concepts (variables, data types, lists)
- Loops and conditional logic
- Functions and reusable code
- Using libraries and importing modules
- Data analysis with pandas
- Data visualization
- Building simple interactive applications
- Using the OpenAI API for healthcare applications

### 2. Hugging Face Transformers for Medical NER
**(`02_Hugging_Face_Transformers.ipynb`)**

A tutorial on using pre-trained transformer models for Named Entity Recognition in medical text. Topics include:

- Setting up the Hugging Face Transformers library
- Loading pre-trained medical NER models
- Tokenizing and analyzing medical text
- Building a simple interactive UI for medical text analysis
- Real-world applications of NLP in clinical settings

### 3. Training a Custom Medical NER Model
**(`03_training_a_transformer_NER.ipynb`)**

An advanced tutorial on fine-tuning transformer models for medical Named Entity Recognition. This notebook covers:

- Setting up a GPU-enabled environment
- Loading and preprocessing medical NER datasets
- Aligning entity labels with subword tokens
- Selecting appropriate pre-trained models (BioClinicalBERT)
- Fine-tuning models for NER using Hugging Face Trainer API
- Evaluating model performance
- Testing on clinical text examples

## Getting Started

1. These tutorials are designed to run in Google Colab. Click the "Open in Colab" badge at the top of each notebook to open it in Colab.
2. For the third notebook (`03_training_a_transformer_NER.ipynb`), make sure to select a GPU runtime in Colab for faster training.
3. Follow the installation instructions in each notebook to set up the required libraries.

## Requirements

- Python 3.7+
- For specific library requirements, see the installation cells in each notebook:
  - pandas, matplotlib, numpy for data analysis
  - transformers, datasets, evaluate, seqeval for NLP models
  - streamlit for interactive applications
  - torch for deep learning

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Iyad Sultan

## Acknowledgments

- These materials are designed for educational purposes in healthcare AI
- The examples use synthetic clinical data to ensure privacy
- The notebooks demonstrate practical applications of AI in pediatric oncology and clinical text analysis
