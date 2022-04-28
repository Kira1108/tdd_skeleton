from newspaper import Article

def generate_summary(url: str) -> str:
    article = Article(url)
    article.download()
    article.parse()
    # article.nlp()
    return article.text[:150]


if __name__ == "__main__":
    summary = generate_summary('http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/')
    print(summary)