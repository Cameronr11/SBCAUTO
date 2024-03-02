import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///your_default.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Add other general configuration settings here

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_ECHO = True
    # Add any development-specific configurations here

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///your_test.db'
    # Add any test-specific configurations here

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    # Add any production-specific configurations here

# You can add more configurations if needed
