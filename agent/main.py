import time
from observer import observe_screen
from actor import take_action

REEL_TIME_LIMIT = 300  

print("🛡️ LoopBreak Agent Started")

reel_start_time = None

while True:
    obs = observe_screen()
    app = obs["app"]

    if app == "instagram":
        if reel_start_time is None:
            reel_start_time = time.time()
            print("▶️ Instagram detected")

        elapsed = int(time.time() - reel_start_time)
        print(f"⏱️ Reels time: {elapsed}s")

        if elapsed >= REEL_TIME_LIMIT:
            print("⚠️ Reel time limit reached!")
            take_action()
            reel_start_time = None
            time.sleep(5)

    else:
        reel_start_time = None

    time.sleep(1)
