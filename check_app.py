#!/usr/bin/env python3

try:
    print("Testing Flask app import...")
    from app import app
    print("✓ Flask app imported successfully")
    
    print("Testing app configuration...")
    print(f"Debug mode: {app.debug}")
    print(f"App name: {app.name}")
    
    print("\n✓ Application is ready to run!")
    print("Starting Flask development server...")
    
    # Start the app
    app.run(debug=True, host='0.0.0.0', port=5000)
    
except ImportError as e:
    print(f"✗ Import error: {e}")
    print("This might be due to missing dependencies or circular imports")
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()





