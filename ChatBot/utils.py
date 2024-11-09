# chatbot/utils.py

import random
import numpy as np
import logging

from langdetect import detect, LangDetectException
from deep_translator import GoogleTranslator
from underthesea import word_tokenize  # Sử dụng underthesea để tokenize tiếng Việt
from nltk.stem import WordNetLemmatizer

logger = logging.getLogger('chatbot_logger')

# Khởi tạo Lemmatizer
lemmatizer = WordNetLemmatizer()

def clean_up_sentence(sentence):
    """
    Tokenize và lemmatize câu đầu vào.
    """
    sentence_words = word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, lemmatizer, show_details=True):
    """
    Trả về mảng bag of words cho câu đầu vào.
    """
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    logger.debug(f"Found in bag: {w}")
    return np.array(bag)

def predict_class(sentence, model, words, classes, lemmatizer):
    """
    Dự đoán lớp của câu đầu vào bằng mô hình đã huấn luyện.
    """
    p = bow(sentence, words, lemmatizer, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    """
    Lấy phản hồi ngẫu nhiên từ intent phù hợp.
    """
    if intents_list:
        tag = intents_list[0]['intent']
        list_of_intents = intents_json['intents']
        for intent in list_of_intents:
            if intent['tag'] == tag:
                result = random.choice(intent['responses'])
                return result
    return "Sorry, I don't understand what you're saying."

def detect_language(text):
    """
    Phát hiện ngôn ngữ của văn bản đầu vào.
    """
    try:
        language = detect(text)
        logger.debug(f"Detected language '{language}' for text: {text}")
        return language
    except LangDetectException:
        logger.warning("Language detection failed. Defaulting to 'en'.")
        return 'en'  # Default to English if detection fails

def chatbot_response(msg, config):
    """
    Sinh phản hồi từ chatbot dựa trên tin nhắn đầu vào.
    """
    try:
        detected_language = detect_language(msg)
        logger.info(f"Detected language in chatbot_response: {detected_language}")

        # Chuyển sang tiếng Anh nếu ngôn ngữ khác không phải là tiếng Anh
        if detected_language != "en":
            msg = GoogleTranslator(source=detected_language, target="en").translate(msg)

        # Xử lý và trả lời bằng tiếng Anh
        response = get_response(predict_class(msg, config.model, config.words, config.classes, config.lemmatizer), config.intents)
        logger.info(f"Bot response in English: {response}")
        return response

    except Exception as e:
        logger.error(f"Error in chatbot_response: {e}")
        return "Sorry, an error occurred while processing your request."
