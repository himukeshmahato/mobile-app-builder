import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile

class MobileColabApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 1. Setup the Window for Mobile View
        self.setWindowTitle("Google Colab Mobile App")
        # Dimensions for iPhone X/11/12 Pro (375x812)
        self.resize(375, 812) 
        
        # 2. Setup the Web Engine
        self.browser = QWebEngineView()
        
        # 3. Configure User-Agent to simulate a mobile device
        # This tells Google Colab we are visiting from an iPhone
        user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
        
        # Get the default profile and set the User-Agent
        profile = QWebEngineProfile.defaultProfile()
        profile.setHttpUserAgent(user_agent)
        
        # 4. Load the URL
        self.browser.setUrl(QUrl("https://colab.research.google.com/"))
        
        # 5. Set the browser as the main widget
        self.setCentralWidget(self.browser)

def main():
    app = QApplication(sys.argv)
    
    # Create and show the window
    window = MobileColabApp()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
