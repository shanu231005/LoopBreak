# 🛑 LoopBreak – AI Digital Wellbeing Agent

LoopBreak is an AI-powered Android Digital Wellbeing Agent that helps users break addictive scrolling habits.

It monitors Instagram usage in real time and automatically intervenes when excessive usage is detected.

---

## 🎯 Problem
Short-form content like Instagram Reels causes addictive behavior, reducing focus and productivity.

---

## 💡 Solution
LoopBreak monitors app usage using Android Accessibility + ADB.

If Instagram is used continuously for **5 minutes**, LoopBreak:
- Shows a warning
- Force closes Instagram
- Locks the phone temporarily

This creates a **hard break** in addictive behavior.

---

## ⚙️ How It Works
1. Observes current foreground app using ADB
2. Tracks continuous Instagram usage time
3. When limit is exceeded:
   - Closes Instagram
   - Locks the device

---

## 🛠️ Tech Stack
- Python
- Android ADB
- DroidRun
- MobileRun Cloud
- Android Accessibility Service

---

## 🎥 Demo Video
🔗 Unlisted YouTube Demo:  
PASTE YOUR VIDEO LINK HERE

---

## 👥 Team
- Thakur Shanu(GitHub: shanu231005)
- Sharma Neha (GitHub: Neha-23sn)

---

## 🚀 Future Improvements
- Reel-by-reel detection
- Custom usage limits
- App-based dashboards
- Parental control mode
