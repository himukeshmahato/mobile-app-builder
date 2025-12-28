[app]

# (str) Title of your application
title = Colab Mobile

# (str) Package name
package.name = colabmobile

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (str) Source filename (default: main.py)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,android,pyjnius,hostpython3

# (list) Permissions
android.permissions = INTERNET

# (list) architectures to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = armeabi-v7a

# (int) Target Android API, should be as high as possible (mostly)
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (list) Service to add to the manifest
# android.services =

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (list) List of Java classes to add to the compilation
# android.add_jars = foo.jar,bar.jar,common/libs/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
# android.add_src =

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 1

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
