# Finetune a pretrained Language Model

## Background
This program accompanied a presentation given as part of the requirements for the Master program (2023) in Computer Science at the [Frankfurt University of Applied Sciences](https://www.frankfurt-university.de/en/about-us/faculty-2-computer-science-and-engineering/welcome-to-faculty-2/) in Frankfurt. It only serves demonstration purposes.

## General Info
The program shows how to download a pretrained language model from [huggingface](https://huggingface.co/) and finetune it according to your topic domain and needs.  
Here, I use a pretrained Google [BERT (bert-base-uncased)](https://huggingface.co/bert-base-uncased) model and finetune it with the [emotion](https://huggingface.co/datasets/SetFit/emotion) (train) dataset that contains Twitter text messages labelled with one of six sentiment classes (sadness, joy, fear, anger, love, surprise).
The emotion (validation) dataset is then used to validate the freshly finetuned model and the emotion (test) datset is used to make predictions on unseen data.

## Setup
Follow the steps below and you can do exactly that yourself.

1. Go to **settings.py** and insert the names of your desired pretrained "*model_name*" (default: [bert-base-uncased](https://huggingface.co/bert-base-uncased)) and "*dataset_name*" (default: [emotion](https://huggingface.co/datasets/SetFit/emotion)). Choose any other from [here](https://huggingface.co/models?pipeline_tag=text-classification&sort=trending) and [here](https://huggingface.co/datasets?task_categories=task_categories:text-classification&sort=trending).
1. To finetune the pretrained model, go to the Jupyter Notebook "*1_finetune_pretrained_model.ipynb*" and run it. -> CAUTION: Pretraining can take some time depending on your setup. The freshly finetuned model will eventually be saved into the "*finetuned_models_folder*" defined in "*settings.py*".
1. To make predictions with your just finetuned model, go to the Jupyter Notebook "*2_make_predictions_with_finetuned_model.ipynb*" and run it. Predictions will be made for the *test subset* of your *dataset*. Results will be shown for 100 random samples of your test data subset in a pandas DataFrame.
