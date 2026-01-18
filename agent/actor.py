import subprocess

def take_action():
    print("❌ Closing Instagram...")
    subprocess.call(
        "adb shell am force-stop com.instagram.android",
        shell=True
    )

    print("🔒 Locking phone...")
    subprocess.call(
        "adb shell input keyevent 26",
        shell=True
    )
