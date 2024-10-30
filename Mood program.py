import tkinter as tk
from PIL import Image, ImageTk  # For working with images (requires Pillow library)

# Function to evaluate the user's mood based on the rating
def evaluate_mood():
    try:
        # Get the value from the text input field
        rating = int(entry.get())
        
        if rating >= 1 and rating <= 3:
            display_message("Mood", "Life has its tough moments.\nSometimes, sharing how you feel with someone can make a difference.\nYou don't have to be alone right now.", r"C:\nastena\Downloads\Python-for-everyone\App-for-replying-to-reviews\Image_path\sad_emoji.png", ask_hug)
        elif rating >= 4 and rating <= 6:
            display_message("Mood", "That's good to hear.\n Wishing you even more success and happiness ahead!", r"C:\nastena\Downloads\Python-for-everyone\App-for-replying-to-reviews\image_path\happy_face.png", ask_cafe)
        elif rating >= 7 and rating <= 10:
            display_message("Mood", "I'm thrilled for you!\nHere's to more great moments ahead!", r"C:\nastena\Downloads\Python-for-everyone\App-for-replying-to-reviews\image_path\veryhappy_emoji.png", ask_fireworks)
        else:
            display_message("Warning", "Hmm, that number seems off. Maybe try again?")
    except ValueError:
        display_message("Error", "Please enter a valid number.")

# Custom function to create a new window with a message and large emojis
def display_message(title, message, image_path=None, callback=None):
    window = tk.Toplevel(root)
    window.title(title)

    # If an image path is provided, display the image
    if image_path:
        emoji_image = Image.open(image_path)  # Load the emoji image
        emoji_image = emoji_image.resize((50, 50), Image.LANCZOS)  # Resize if necessary
        emoji_photo = ImageTk.PhotoImage(emoji_image)
        
        # Label for the image
        image_label = tk.Label(window, image=emoji_photo)
        image_label.image = emoji_photo  # Keep a reference to the image
        image_label.pack(pady=(10, 0))  # Pack with padding at the top
    
    # Label for the message text
    label = tk.Label(window, text=message, font=("Comic sans MS", 12), bg="lightyellow")  # Increase font size for emojis
    label.pack(padx=20, pady=20)
    
    # OK button
    button = tk.Button(window, text="OK", font=("Helvetica", 12), bg="pink", fg="black", command=window.destroy)
    button.pack(pady=10)


    # Wait for the window to close before continuing
    window.wait_window()

    # After closing the window, if a callback is provided, call it
    if callback:
        callback()

# Function to ask if the user wants a hug
def ask_hug():
    response = ask_question("Hug", "Do you want a hug?")
    if response == "yes":
        display_emoji(r"C:\nastena\Downloads\Python-for-everyone\App-for-replying-to-reviews\image_path\hug_emoji.png") # Displays the hug emoji
    else:
        display_emoji(r"C:\nastena\Downloads\Python-for-everyone\App-for-replying-to-reviews\image_path\sun_emoji.png") # Displays the sun emoji

# Function to ask about celebrating at a cafe
def ask_cafe():
    response = ask_question("Cafe", "Would you like to celebrate your success at a cafe?")
    if response == "yes":
        display_emoji("coffee_emoji.png")  # Displays the coffee emoji
    else:
        display_emoji("tea_emoji.png")  # Displays the tea emoji

# Function to ask about fireworks
def ask_fireworks():
    response = ask_question("Fireworks", "Do you want a fireworks display in your honor?")
    if response == "yes":
        display_emoji("fireworks_emoji.png")  # Displays the fireworks emoji
    else:
        display_emoji("gift_emoji.png")  # Displays the gift emoji

# Custom function to create a yes/no dialog
def ask_question(title, question):
    window = tk.Toplevel(root)
    window.title(title)

    label = tk.Label(window, text=question, font=("Comic sans MS", 12), bg="lightyellow")
    label.pack(padx=20, pady=20)

    response = tk.StringVar()

    def yes():
        response.set("yes")
        window.destroy()

    def no():
        response.set("no")
        window.destroy()


    # Create a frame to hold the buttons
    button_frame = tk.Frame(window, bg="#f5f5f5")  # Optional: set background to match window
    button_frame.pack(pady=10)  # Add vertical padding for the frame

    # Place the buttons inside the frame with minimal horizontal padding
    yes_button = tk.Button(button_frame, text="Yes", font=("Helvetica", 12), bg="#82b59b", fg="white", command=yes)
    yes_button.pack(side="left", padx=5)  # Small horizontal padding

    no_button = tk.Button(button_frame, text="No", font=("Helvetica", 12), bg="#e3b1bd", fg="white", command=no)
    no_button.pack(side="left", padx=5)  # Small horizontal padding

    window.wait_window()
    return response.get()

# Function to display emoji images
def display_emoji(image_path):  
    window = tk.Toplevel(root)
    window.title("Emoji")

# Load the emoji image
    emoji_image = Image.open(image_path)  # Substitute with the path to your emoji image
    emoji_image = emoji_image.resize((100, 100), Image.LANCZOS)  # Resize the image
    emoji_photo = ImageTk.PhotoImage(emoji_image)

    # Create a label with the emoji image
    label = tk.Label(window, image=emoji_photo)
    label.image = emoji_photo  # Keep a reference to the image to display it
    label.pack(pady=30)

    button = tk.Button(window, text="OK", command=window.destroy)
    button.pack(pady=10)    

# Main window
root = tk.Tk()
root.title("Customized Mood Checker")
root.geometry("350x180")              # Window size
root.configure(bg="lightgrey")        # Window background color

# Label with custom font and background
label = tk.Label(root, text="How are you feeling today?\nRate your mood on a scale of 1 to 10:",
                 font=("Comic sans MS", 12), bg="lightyellow", fg="black")
label.pack(pady=10)

# Entry field for input
entry = tk.Entry(root, font=("Comic sans MS", 12), bd=5)
entry.pack(pady=5)

# Custom Submit button with light orange background
submit_button = tk.Button(root, text="Submit", font=("Comic sans MS", 12), bg="#ffcc7a", fg="black", command=evaluate_mood)
submit_button.pack(pady=20)


root.mainloop()
