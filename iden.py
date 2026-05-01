import os
import magic

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"
folder_path = input(YELLOW +"Provide a valid directory address: " +RESET)
file_names = [f for f in os.listdir(folder_path)]

mime_map = {
    ".txt": "text/plain",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".exe": "application/x-dosexec"
}
for filename in file_names:
    #root, ext = os.path.splitext(filename)
    full_path = os.path.join(folder_path, filename)
    if os.path.isfile(full_path):
        r,ext = os.path.splitext(filename)
        ext = ext.lower()
        mime = magic.from_file(full_path, mime=True)
        if ext in mime_map and mime_map[ext] == mime:
            print(GREEN + f"{filename} → ✅ Valid ({mime})" + RESET)
        else:
            print(RED + f"{filename} → ❌ Mismatch (Extension: {ext}, Actual: {mime})" + RESET)
