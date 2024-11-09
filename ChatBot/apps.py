import os
import json
import pickle
import logging
import numpy as np
from django.apps import AppConfig

from keras.models import load_model
from nltk.stem import WordNetLemmatizer
from nltk import download as nltk_download
from langdetect import detect, LangDetectException
from deep_translator import GoogleTranslator
from underthesea import word_tokenize

from .logging_config import logger

class ChatbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ChatBot'

    model = None
    intents = None
    words = None
    classes = None
    lemmatizer = WordNetLemmatizer()

    def ready(self):
        # Tải dữ liệu NLTK nếu chưa có
        nltk_download('popular')

        # Đường dẫn cố định đến các tệp
        MODEL_PATH = r'D:\Project\DjChatBox\EduCare\EduCare\File\model.h5'
        INTENTS_PATH = r'D:\Project\DjChatBox\EduCare\EduCare\File\intents.json'
        WORDS_PATH = r'D:\Project\DjChatBox\EduCare\EduCare\File\texts.pkl'
        CLASSES_PATH = r'D:\Project\DjChatBox\EduCare\EduCare\File\labels.pkl'

        # Tải mô hình nếu chưa tải
        if ChatbotConfig.model is None:
            try:
                ChatbotConfig.model = load_model(MODEL_PATH)
                logger.info(f"Model loaded successfully from {MODEL_PATH}")
            except Exception as e:
                logger.error(f"Failed to load model from {MODEL_PATH}: {e}")
                raise

        # Tải các file dữ liệu intents, words, classes nếu chưa tải
        if ChatbotConfig.intents is None:
            try:
                with open(INTENTS_PATH, 'r', encoding='utf-8') as file:
                    ChatbotConfig.intents = json.load(file)
                logger.info(f"Intents loaded successfully from {INTENTS_PATH}")
            except Exception as e:
                logger.error(f"Failed to load intents from {INTENTS_PATH}: {e}")
                raise

        if ChatbotConfig.words is None:
            try:
                with open(WORDS_PATH, 'rb') as file:
                    ChatbotConfig.words = pickle.load(file)
                logger.info(f"Words loaded successfully from {WORDS_PATH}")
            except Exception as e:
                logger.error(f"Failed to load words from {WORDS_PATH}: {e}")
                raise

        if ChatbotConfig.classes is None:
            try:
                with open(CLASSES_PATH, 'rb') as file:
                    ChatbotConfig.classes = pickle.load(file)
                logger.info(f"Classes loaded successfully from {CLASSES_PATH}")
            except Exception as e:
                logger.error(f"Failed to load classes from {CLASSES_PATH}: {e}")
                raise
