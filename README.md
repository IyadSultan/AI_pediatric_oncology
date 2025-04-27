# Medical AI Educational Resources

A comprehensive collection of Python notebooks and tutorials focused on healthcare AI applications, with an emphasis on pediatric oncology and clinical text analysis. Prepared by Dr. Iyad Sultan from the AI office at KHCC.

## 📋 Overview

This repository contains educational materials designed to bridge the gap between healthcare professionals and AI technology. The tutorials progress from fundamental Python concepts to advanced natural language processing and machine learning techniques specifically tailored for clinical data and applications.

## 🎓 Learning Path

The materials follow a structured learning progression:

### 1. [Python for Pediatric Oncology](01_Python_for_Pediatric_Oncology.ipynb)
**Introductory Coding Workshop**

A beginner-friendly Python course designed specifically for healthcare professionals with minimal coding experience:

- ✅ Python fundamentals (variables, data types, lists)
- ✅ Control structures (loops and conditionals)
- ✅ Functions and code organization
- ✅ Working with libraries and modules
- ✅ Data analysis with pandas
- ✅ Data visualization techniques
- ✅ Interactive application development
- ✅ Introduction to OpenAI API for healthcare applications

### 2. [Hugging Face Transformers for Medical NER](02_Hugging_Face_Transformers.ipynb)
**Applied Medical Text Analysis**

An introduction to using pre-trained transformer models for Named Entity Recognition in medical text:

- ✅ Setting up Hugging Face Transformers
- ✅ Loading and using pre-trained medical NER models
- ✅ Tokenization and analysis of clinical text
- ✅ Creating an interactive UI for medical text analysis
- ✅ Practical applications in clinical settings

### 3. [Training a Custom Medical NER Model](03_training_a_transformer_NER.ipynb)
**Advanced Model Development**

A comprehensive guide to fine-tuning transformer models for specialized medical NER tasks:

- ✅ GPU-accelerated environment configuration
- ✅ Medical dataset preparation and preprocessing 
- ✅ Entity label alignment with tokenization
- ✅ Domain-specific model selection (BioClinicalBERT)
- ✅ Fine-tuning with the Hugging Face Trainer API
- ✅ Performance evaluation and metrics
- ✅ Practical testing on clinical examples

### 4. [Training BERT for Adverse Drug Reaction Detection](04_train_BERT_on_ADR.ipynb)
**Specialized Clinical Text Analysis**

An in-depth tutorial on training models for adverse drug reaction (ADR) detection:

- ✅ Multi-task approach: Classification and NER
- ✅ Working with specialized medical datasets
- ✅ Fine-tuning biomedical language models
- ✅ Performance comparison before and after training
- ✅ Real-world application testing

## 🚀 Getting Started

1. These tutorials are designed to run in Google Colab. Click the "Open in Colab" badge at the top of each notebook.

2. For training notebooks (03 and 04), select a GPU runtime in Colab:
   - Go to **Runtime** > **Change runtime type** > **Hardware accelerator** > **GPU**

3. Follow the installation instructions in each notebook to set up the required libraries.

## 📦 Requirements

- Python 3.7+
- Key libraries (installed within notebooks):
  - **Data analysis**: pandas, matplotlib, numpy
  - **NLP/ML**: transformers, datasets, evaluate, seqeval
  - **Interactive UI**: streamlit
  - **Deep learning**: torch

## 🔍 Use Cases

These materials can support:
- Clinical text extraction and analysis
- Medical entity recognition
- Patient data analysis and visualization
- Adverse drug reaction monitoring
- Research data mining and processing

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Dr. Iyad Sultan - AI office @ KHCC

## 📝 Notes

- All examples use synthetic clinical data to ensure privacy and ethical compliance
- The notebooks demonstrate practical AI applications in pediatric oncology and clinical text analysis
- These materials are regularly updated with advances in healthcare AI technology
