[app]

# (str) Title of your application
title = R Video App

# (str) Package name
package.name = rvideoapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.rvideo

# (list) Source files to include (let empty to include all files)
source.dir = .

# (list) Source files to include (allowitted extensions)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests,bin,venv

# (str) Application version (method 1)
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,kivymd,pillow

# (list) Supported orientations
orientation = portrait

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

#
# Full screen
#
fullscreen = 0

#
# Android specific
#
# (string) Presplash background color (hex format #RRGGBB or named color)
#android.presplash_color = #FFFFFF

# (string) Background color of the window (hex format #RRGGBB or named color)
#android.background_color = #FFFFFF
