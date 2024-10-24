from rouge_score import rouge_scorer
import numpy as np

def gist_eval(response, ground_truth):
    scorer = rouge_scorer.RougeScorer(['rouge1','rougeL'], use_stemmer=True)
    scores = scorer.score(response, ground_truth)
    return scores