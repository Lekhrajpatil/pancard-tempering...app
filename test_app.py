#!/usr/bin/env python3

try:
    print("Testing imports...")
    from flask import Flask
    print("✓ Flask imported successfully")
    
    import cv2
    print("✓ OpenCV imported successfully")
    
    from PIL import Image
    print("✓ PIL imported successfully")
    
    from skimage.metrics import structural_similarity
    print("✓ scikit-image imported successfully")
    
    import imutils
    print("✓ imutils imported successfully")
    
    print("\nAll imports successful! Starting application...")
    
    # Test the app
    from app import app
    print("✓ Flask app created successfully")
    
    print("\nApplication is ready to run!")
    print("Run: python app.py")
    
except ImportError as e:
    print(f"✗ Import error: {e}")
    print("Please install missing dependencies:")
    print("pip install Flask opencv-python Pillow scikit-image imutils")
except Exception as e:
    print(f"✗ Error: {e}")





