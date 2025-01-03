# Prediction API

API to predict whether a given input is fake news. Used in flink stream processing pipeline.

Requirements

    Python 3.10.12

Clone the repo - https://github.com/abhimessi16/MI_Fake_News_Prediction

    cd into repo folder
    Create a virtual environment - recommended
    Download and add the model and tokenizer files from - https://drive.google.com/drive/folders/1LSrSNxbLMT5yubg_tghWe1suH8qvGkmE?usp=sharing
    If using own models then update the main, params and utils files accordingly
    Run - pip install -r requirements.txt
    Run - fastapi run app/main.py (or run using uvicorn on different port)
