import os

# 1. Install System Dependencies
print("Updating system and installing dependencies... This may take a few minutes.")
os.system("apt-get update -qq")
os.system("apt-get install -y -qq build-essential git python3-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-ttf-dev libsdl2-mixer-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev")
os.system("apt-get install -y -qq libgstreamer1.0-gstreamer-lite-dev xclip xsel libjpeg-dev")
os.system("apt-get install -y -qq openjdk-17-jdk")
os.system("pip install -q buildozer cython==0.29.33 kivy")

# 2. Create the main.py file
# This code uses pyjnius to call native Android WebView
main_py_content = """
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from jnius import autoclass
from android.runnable import run_on_ui_thread

# Import Android classes
WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
Activity = autoclass('org.kivy.android.PythonActivity').mActivity

class MyWebView(Widget):
    def __init__(self, **kwargs):
        super(MyWebView, self).__init__(**kwargs)
        self.webview = None
        Clock.schedule_once(self.create_webview, 0)

    @run_on_ui_thread
    def create_webview(self, *args):
        self.webview = WebView(Activity)
        self.webview.getSettings().setJavaScriptEnabled(True)
        self.webview.getSettings().setDomStorageEnabled(True)
        self.webview.getSettings().setUserAgentString("Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36")
        self.webview.setWebViewClient(WebViewClient())
        self.webview.loadUrl('https://colab.research.google.com/')
        Activity.setContentView(self.webview)

class WebViewApp(App):
    def build(self):
        return MyWebView()

if __name__ == '__main__':
    WebViewApp().run()
"""

with open('main.py', 'w') as f:
    f.write(main_py_content)

# 3. Initialize and Configure Buildozer
if not os.path.exists('buildozer.spec'):
    os.system("buildozer init")

# Modify buildozer.spec for requirements and permissions
if os.path.exists('buildozer.spec'):
    with open('buildozer.spec', 'r') as f:
        spec = f.read()

    # Update requirements and permissions
    spec = spec.replace('requirements = python3,kivy', 'requirements = python3,kivy,android,pyjnius')
    spec = spec.replace('#android.permissions = INTERNET', 'android.permissions = INTERNET')
    spec = spec.replace('package.name = myapp', 'package.name = colabwebview')
    spec = spec.replace('package.domain = org.test', 'package.domain = com.colab.app')
    spec = spec.replace('title = My Application', 'title = Colab Mobile')

    with open('buildozer.spec', 'w') as f:
        f.write(spec)

# 4. Build the APK
# Note: 'yes |' is used to accept the Android SDK licenses automatically
print("Starting Buildozer... The first build usually takes 15-20 minutes.")
os.system("yes | buildozer -v android debug")

# 5. Locate the APK
print("\nBuild finished! Looking for APK...")
os.system("ls bin/")
