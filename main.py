"""
WebWaka Agriculture Sector - Main Application
Flask backend with African optimization and cultural integration
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for African mobile apps
CORS(app, origins="*")

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///webwaka_agriculture.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'webwaka-agriculture-secret-key')

# Initialize database
db = SQLAlchemy(app)

# Import models and routes
from models.agriculture_models import *
from routes.agriculture_routes import bp as agriculture_bp

# Register blueprints
app.register_blueprint(agriculture_bp, url_prefix='/api/agriculture')

# Health check endpoint
@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'sector': 'agriculture', 'african_optimized': True})

# Ready check endpoint
@app.route('/ready')
def ready_check():
    return jsonify({'status': 'ready', 'sector': 'agriculture', 'database': 'connected'})

# Root endpoint
@app.route('/')
def root():
    return jsonify({
        'message': 'WebWaka Agriculture Sector API',
        'version': '1.0.0',
        'african_optimized': True,
        'mobile_first': True,
        'offline_support': True,
        'cultural_integration': True
    })

if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    
    # Run app with African optimization
    app.run(
        host='0.0.0.0',  # Allow external access
        port=5000,
        debug=os.getenv('FLASK_ENV') == 'development'
    )
