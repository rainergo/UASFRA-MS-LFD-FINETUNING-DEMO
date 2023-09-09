from transformers import AutoTokenizer
from sklearn.metrics import accuracy_score, f1_score, ConfusionMatrixDisplay, confusion_matrix
import matplotlib.pyplot as plt


def tokenize(batch, model_name):
    tokenizer = get_tokenizer(model_name=model_name)
    return tokenizer(batch['text'], padding=True, truncation=True)


def get_tokenizer(model_name):
    return AutoTokenizer.from_pretrained(pretrained_model_name_or_path=model_name)


def get_metrics(pred):
    pred_labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    f1 = f1_score(pred_labels, preds, average="weighted")
    acc = accuracy_score(pred_labels, preds)
    return {"accuracy": acc, "f1": f1}


def plot_confusion_matrix(y_preds, y_true, labels):
    cm = confusion_matrix(y_true, y_preds, normalize="true")
    fig, ax = plt.subplots(figsize=(6, 6))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    disp.plot(cmap="Blues", values_format=".2f", ax=ax, colorbar=False)
    plt.title("Normalized confusion matrix")
    plt.show()
