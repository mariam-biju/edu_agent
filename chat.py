import wikipedia

def answer_query(query):
    try:
        return wikipedia.summary(query, sentences=3)
    except:
        return "Sorry, I couldn't find an answer. Try rephrasing?"