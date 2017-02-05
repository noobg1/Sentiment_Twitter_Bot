from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

def sentiment_utility(sentence):
  vs = analyzer.polarity_scores(sentence)
  return vs
