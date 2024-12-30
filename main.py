import tkinter as tk
from tkinter import messagebox, StringVar

# Initialize the dictionary with prevalues (messages in 2024)
members = {
    "mitza": 6987,
    "ahsan": 72867,
    "jdsd": 13231,
    "ras": 6618,
    "hylke": 50190,
    "jussi halla-aho": 1125,
    "lacus": 8504,
    "hogriv": 549
}

SECONDS_PER_MESSAGE = 5
results = {}

# Character card descriptions
character_cards = {
    'A': "Main Character: person who initiates most conversations and is active",
    'B': "Bold Sigma: person with strong opinions, usually challenging the people who think they are main characters",
    'C': "Suspicious Spy: silent, friendly, sometimes active, something malicious must be going on",
    'D': "Wildcard: sometimes annoying, sometimes needed, incredibly questionable"
}

def display_statistics(aw_counter, politics_counter):
    """Display calculated statistics for each member in a new window."""
    stats_window = tk.Toplevel(root)
    stats_window.title("Member Statistics")
    stats_window.geometry("800x600")

    # Set a wider window size
    stats_window.configure(bg="#282c34")  # Dark mode background

    # Create a canvas and scrollbar
    canvas = tk.Canvas(stats_window, bg="#282c34")
    scrollbar = tk.Scrollbar(stats_window, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#282c34")

    # Configure the canvas
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Place the scrollbar on the right side
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # Link scrollbar and canvas
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create frames for each member's statistics
    for index, member in enumerate(members.keys()):
        stats = results[member]  # Get statistics for each member

        # Create a frame for each member
        frame = tk.Frame(scrollable_frame, relief=tk.RAISED, borderwidth=2, bg="#3c3f41")
        frame.grid(row=index // 2, column=index % 2, padx=10, pady=10)

        # Arrange in a grid
        tk.Label(frame, text=f"{member.capitalize()}:", font=("Montserrat", 12), bg="#3c3f41", fg="white").pack(pady=5)
        tk.Label(frame, text=f"Messages Sent: {stats['messages_2025']}", font=("Montserrat", 12), bg="#3c3f41", fg="white").pack(pady=2)
        tk.Label(frame, text=f"More Messages Than Before: {stats['messages_2025'] - members[member]}", font=("Montserrat", 12), bg="#3c3f41", fg="white").pack(pady=2)
        tk.Label(frame, text=f"Increase to Last Year: {stats['percentage_change']:.2f}%", font=("Montserrat", 12), bg="#3c3f41", fg="white").pack(pady=2)
        tk.Label(frame, text="Best Buddy: Ahsan", font=("Montserrat", 12), bg="#3c3f41", fg="white").pack(pady=2)
        tk.Label(frame, text=f"Time Spent: {(stats['messages_2025'] * SECONDS_PER_MESSAGE // 3600)}h {(stats['messages_2025'] * SECONDS_PER_MESSAGE // 60) % 60}m", font=("Montserrat", 12), bg="#3c3f41", fg="white").pack(pady=2)

        # Display selected character card (for reference only)
        selected_card = stats.get('character_card', 'N/A')
        tk.Label(frame, text=f"Character Card: {selected_card}", font=("Montserrat", 12), bg="#3c3f41", fg="white").pack(pady=2)

    # Add counters at the end
    counter_frame = tk.Frame(scrollable_frame, relief=tk.RAISED, borderwidth=2, bg="#3c3f41")
    counter_frame.grid(row=len(members) // 2 + (len(members) % 2), column=0, columnspan=2, padx=10, pady=10)

    tk.Label(counter_frame, text="Counters:", font=("MontserratTitle", 14), bg="#3c3f41", fg="white").pack(pady=5)
    tk.Label(counter_frame, text=f"'Aww' Count: {aw_counter}", font=("Montserrat", 12), bg="#3c3f41", fg="white").pack(pady=2)
    tk.Label(counter_frame, text=f"'Politics' Count: {politics_counter}", font=("Montserrat", 12), bg="#3c3f41", fg="white").pack(pady=2)

def submit_member_stats():
    """Collect and calculate stats for all members."""
    try:
        for member in members.keys():
            subtraction_base = int(subtraction_entries[member]['base'].get().strip())
            if subtraction_base <= members[member]:
                messagebox.showerror("Input Error", f"Subtraction base must be greater than {members[member]} for {member}.")
                return

            count_2024 = members[member]
            count_2025 = subtraction_base - count_2024

            if count_2024 != 0:
                percentage_change = ((count_2025 - count_2024) / count_2024) * 100
            else:
                percentage_change = float('inf') if count_2025 > 0 else 0

            character_card = subtraction_entries[member]['card'].get() or 'N/A'
            results[member] = {
                'messages_2024': count_2024,
                'messages_2025': count_2025,
                'percentage_change': percentage_change,
                'character_card': character_card
            }

        # After collecting all member stats, ask for aw and politics counters
        ask_counters()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers.")

def ask_counters():
    """Ask for aw and politics counters after all members' data is collected."""
    counter_dialog = tk.Toplevel(root)

    counter_dialog.title("Counters Input")

    tk.Label(counter_dialog, text="How many times has Sealver said aww :3?", bg="#282c34", fg="white").pack(pady=5)

    global aw_entry
    aw_entry = tk.Entry(counter_dialog)

    aw_entry.pack(pady=5)

    tk.Label(counter_dialog, text="How many times has Sealver said eww :( ?", bg="#282c34", fg="white").pack(pady=5)

    global politics_entry
    politics_entry = tk.Entry(counter_dialog)

    politics_entry.pack(pady=5)

    submit_button = tk.Button(counter_dialog, text="Submit Counters", command=submit_counters)

    submit_button.pack(pady=20)

def submit_counters():
    """Collect counters and display statistics."""
    try:
        aw_counter = int(aw_entry.get().strip()) 
        politics_counter = int(politics_entry.get().strip()) 

        # Close the counter window and display statistics
        display_statistics(aw_counter ,politics_counter)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers.")

# Create main window
root = tk.Tk()
root.title("Member Statistics Input")
root.geometry("600x600") 
root.configure(bg="#282c34")

# Title Label
title_label = tk.Label(root, text="Member Statistics Input", font=("MontserratTitle.ttf", 16), bg="#282c34", fg="white")
title_label.pack(pady=(10, 20))

# Add character card names (A-D) to the first window
card_names = ["A: Main Character", "B: Bold Sigma", "C: Suspicious Spy", "D: Wildcard"]
for card_name in card_names:
    tk.Label(root, text=card_name, font=("MontserratTitle.ttf", 14), bg="#282c34", fg="white").pack(pady=5)

# Updated Label
tk.Label(root, text="Enter message counts and select character cards for each member:", 
          bg="#282c34", fg="white").pack()

subtraction_entries = {}
for member in members.keys():
   frame = tk.Frame(root)
   frame.pack(pady=5)

   tk.Label(frame, text=f"{member.capitalize()}:", bg="#282c34", fg="white").pack(side=tk.LEFT)

   entry_base = tk.Entry(frame) 
   subtraction_entries[member] = {'base': entry_base}
   entry_base.pack(side=tk.LEFT)

   # Character card selection dropdown (A-D)
   card_var = StringVar(value='A') 
   card_menu = tk.OptionMenu(frame ,card_var,*character_cards.keys()) 
   card_menu.config(bg="#61afef") 
   card_menu.pack(side=tk.LEFT) 
   subtraction_entries[member]['card'] = card_var 

# Submit button to calculate stats
submit_button = tk.Button(root ,text="Calculate Stats",
                          command=submit_member_stats,
                          bg="#61afef",
                          fg="black",
                          width=20,   # Set a wider width for better clickability
                          height=2)   # Set a taller height for better visibility
submit_button.pack(pady=(20), padx=10)  # Add padding around the button

# Run the application
root.mainloop()
