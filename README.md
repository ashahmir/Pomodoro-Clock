🍅 Focus Sessions - Pomodoro Timer (Tkinter)

A simple and aesthetic Pomodoro timer built with Python's Tkinter module. This app helps you focus by following the Pomodoro technique — alternating between work and break sessions, with a visual countdown and checkmarks to track your progress.

## 🚀 Features

- ⏱️ Customizable session lengths for:
  - Work (30 seconds in test/demo mode)
  - Short Breaks (10 seconds)
  - Long Break (20 seconds after 4 work sessions)
- 🟢 Visual interface with a tomato icon and timer
- ✅ Tracks work sessions using checkmarks
- 🪟 Pops up the window when a session ends to alert you
- 🔁 Automatic cycling through sessions (no manual restarts)

🧠 How It Works
  The timer starts with a Work session.
  
  After each work session, a Break session starts automatically.
  
  After 4 work sessions, a longer break is given.
  
  The app pops to the front to notify you when a session changes.
  
  Each completed work session adds a ✔️ checkmark at the bottom.

  # In start_timer():
seconds = WORK_MIN * 60        # For work sessions
seconds = SHORT_BREAK_MIN * 60 # For short breaks
seconds = LONG_BREAK_MIN * 60  # For long breaks
