from gramformer import Gramformer
import torch

def set_seed(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

set_seed(1212)

gf = Gramformer(models = 1, use_gpu=False) # 1=corrector, 2=detector

influent_sentences = [
    "He are moving here.",
    "the collection of letters was original used by the ancient Romans",
    "We enjoys horror movies",
    "Anna and Mike is going skiing",
    "I will eat fish for dinner and drank milk",
    "what be the reason for everyone leave the comapny"
]   

for influent_sentence in influent_sentences:
    corrected_sentences = gf.correct(influent_sentence, max_candidates=1)
    print("[Input] ", influent_sentence)
    for corrected_sentence in corrected_sentences:
      print("[Edits] ", gf.get_edits(influent_sentence, corrected_sentence))
    print("-" *100)