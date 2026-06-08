import os
import sys
import time
import statistics
import secrets
from datetime import datetime

# ==========================================
# YOGI-BEHAVIOR: ZEN EQUILIBRIUM 20-COLOR PALETTE
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;231m', '\033[38;5;212m', '\033[38;5;107m', '\033[38;5;114m', '\033[38;5;223m'
C6, C7, C8, C9, C10  = '\033[38;5;244m', '\033[38;5;111m', '\033[38;5;252m', '\033[38;5;214m', '\033[38;5;137m'
C11, C12, C13, C14, C15 = '\033[38;5;94m', '\033[38;5;235m', '\033[38;5;35m', '\033[38;5;170m', '\033[38;5;248m'
C16, C17, C18, C19, C20 = '\033[38;5;250m', '\033[38;5;61m', '\033[38;5;220m', '\033[38;5;71m', '\033[38;5;52m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE ZEN MEDITATOR
# ==========================================
def yogi_init_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C3}          _          
    {C3}         / \         {C18}Y O G I
    {C3}        /   \        {C5}B E H A V I O R
    {C19}       / / \ \       {C15}v3.8 [INSIDER_MONITOR]
    {C11}      / /   \ \      
    {C13}     /_/     \_\     {C9}* Awareness Active *
    """
    print(logo)
    print(f"{C3}{BLD}   YOGI-BEHAVIOR: BIOMETRIC INTENT ANALYSIS{RST}\n")
    
    # Pulse of awareness
    for i in range(15):
        char = "⦿" if i % 2 == 0 else "·"
        sys.stdout.write(f"\r{C15}[{C7}{char}{C15}] {C8}Mapping User Behavioral DNA...{RST}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\n{C13}[+] Consciousness Calibrated. Monitoring for Subconscious Deviations.{RST}\n")

# ==========================================
# ARCHITECTURE: BEHAVIORAL SIGNATURE ENGINE
# ==========================================
class YogiProfile:
    """Stores the 'Digital DNA' of a specific user."""
    def __init__(self, username):
        self.username = username
        self.typing_speeds = []     # Keystroke dynamics (simulated)
        self.access_sequence = []   # Pattern of files opened
        self.risk_score = 0.0

    def calculate_deviation(self, current_speed, current_sequence):
        """Math: Compares current action against historical DNA."""
        if not self.typing_speeds: return 0.0
        
        # 1. Typing Speed Deviation (Z-Score)
        avg_speed = statistics.mean(self.typing_speeds)
        stdev = statistics.stdev(self.typing_speeds) if len(self.typing_speeds) > 1 else 1.0
        speed_dev = abs(current_speed - avg_speed) / stdev
        
        # 2. Sequence Anomaly (Markov Chain logic)
        # Does the user usually go from login -> email or login -> vault?
        seq_dev = 0.0
        if self.access_sequence and current_sequence != self.access_sequence[-1]:
             # If they jump to a sensitive area directly, it's a deviation
             if "VAULT" in current_sequence: seq_dev = 2.0
             
        return (speed_dev + seq_dev) / 2

# ==========================================
# MONITORING SYSTEM
# ==========================================
class BehaviorSentry:
    def __init__(self):
        self.profiles = {}

    def track_action(self, user, speed, resource):
        if user not in self.profiles:
            self.profiles[user] = YogiProfile(user)
            print(f"{C15}[*] Creating new Behavioral Profile for {C18}{user}{RST}")

        profile = self.profiles[user]
        deviation = profile.calculate_deviation(speed, resource)
        
        # Update Profile DNA
        profile.typing_speeds.append(speed)
        profile.access_sequence.append(resource)
        
        # Verdict Logic
        ts = datetime.now().strftime("%H:%M:%S")
        if deviation > 2.5:
            self._flash_alert(ts, user, deviation, resource)
        else:
            print(f"{C6}[{ts}] {C5}{user:<10} {C16}Acted: {C7}{resource:<12} {C15}Dev: {C19}{deviation:.2f}{RST}")

    def _flash_alert(self, ts, user, dev, resource):
        print(f"\n{C20}{C9}{BLD} !!! BEHAVIORAL MISMATCH DETECTED !!! {RST}")
        print(f"{C20}│ {C1}USER    : {C18}{user}{RST}")
        print(f"{C20}│ {C1}RESOURCE: {C9}{resource}{RST}")
        print(f"{C20}│ {C1}ANOMALY : {C14}{dev:.2f} Sigma Deviation{RST}")
        print(f"{C20}│ {C1}VERDICT : {C2}Account Compromise or Insider Threat Suspected!{RST}")
        print(f"{C20}└{'─'*55}{RST}\n")
        time.sleep(1)

# ==========================================
# SIMULATION ENGINE
# ==========================================
def run_simulation():
    yogi_init_anim()
    sentry = BehaviorSentry()
    
    # Phase 1: Training the Yogi (Normal Behavior)
    print(f"{C17}[Phase 1: Establishing Zen Baseline]{RST}")
    for _ in range(10):
        # Normal Raj: Types at ~50 wpm, stays in EMAIL or DOCS
        sentry.track_action("Raj_Gautam", 50 + secrets.randbelow(10), "EMAIL_CLIENT")
        time.sleep(0.2)
        sentry.track_action("Raj_Gautam", 52 + secrets.randbelow(5), "DOCS_EDITOR")
        time.sleep(0.2)

    print(f"\n{C13}[Phase 2: Monitoring Active Deviations]{RST}")
    # Scenario A: Raj is typing differently (Stress or Hacker) and accessing VAULT
    time.sleep(1)
    sentry.track_action("Raj_Gautam", 120, "CUI_VAULT_ROOT") # Sudden burst + High value target
    
    # Scenario B: Normal Raj behavior returns
    sentry.track_action("Raj_Gautam", 51, "DOCS_EDITOR")

if __name__ == "__main__":
    try:
        run_simulation()
        print(f"{C3}[✔] Yogi-Behavior session concluded. Vigilance remains.{RST}")
    except KeyboardInterrupt:
        print(f"\n{C20}[!] Consciousness disrupted.{RST}")
