import subprocess

def observe_screen():
    try:
        output = subprocess.check_output(
            "adb shell dumpsys activity activities | findstr ResumedActivity",
            shell=True,
            text=True,
            stderr=subprocess.DEVNULL
        )

        if "com.instagram.android" in output:
            return {"app": "instagram"}
        else:
            return {"app": "other"}

    except Exception:
        return {"app": "error"}
