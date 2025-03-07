import unicodedataplus

def scripture_guess(texts):
    #return scripture category for a batch of texts
    labels_guessed = []
    for text in texts:
        sample = text[:20]
        guess = []
        for c in sample:
            guess.append(unicodedataplus.script(c))

        labels_guessed.append(max(set(guess), key=guess.count))
    return labels_guessed