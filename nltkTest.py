import nltk
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
nltk.download("maxent_ne_chunker")