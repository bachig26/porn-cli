from fzf import fzf_prompt

providers = [
    "hentaimama",
    "xxxmax",
    "pornhub",
    "javct",
]

def ask():
    choice = fzf_prompt(providers)
    return choice


