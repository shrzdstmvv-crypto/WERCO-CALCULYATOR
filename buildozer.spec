[app]

title = WERCO Calculator

package.name = wercocalculator
package.domain = org.werco

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv

version = 1.0

requirements = python3,kivy==2.3.0

orientation = portrait

fullscreen = 0

# Android
android.api = 33
android.minapi = 21
android.ndk = 25b

# Ilova ikonkasi (keyin qo'shamiz)
# icon.filename = icon.png

[buildozer]

log_level = 2

warn_on_root = 1
