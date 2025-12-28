from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from kivy.clock import Clock

class ColabApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        if platform == 'android':
            # On Android, we defer the WebView loading slightly to ensure the window is ready
            Clock.schedule_once(self.create_webview, 0)
            self.label = Label(text="Loading Google Colab...")
        else:
            # Fallback for Windows/Desktop if run locally
            self.label = Label(text="This Kivy app is designed to run on Android.\n\nOn Android, this will launch a native WebView\nloading https://colab.research.google.com/")
            
        self.layout.add_widget(self.label)
        return self.layout

    def create_webview(self, *args):
        from jnius import autoclass
        from android.runnable import run_on_ui_thread

        WebView = autoclass('android.webkit.WebView')
        WebViewClient = autoclass('android.webkit.WebViewClient')
        activity = autoclass('org.kivy.android.PythonActivity').mActivity

        @run_on_ui_thread
        def run_webview():
            webview = WebView(activity)
            webview.getSettings().setJavaScriptEnabled(True)
            webview.setWebViewClient(WebViewClient())
            webview.loadUrl('https://colab.research.google.com/')
            
            # Set the WebView as the content of the activity
            activity.setContentView(webview)
            
        run_webview()

if __name__ == '__main__':
    ColabApp().run()
