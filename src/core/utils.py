import os
from werkzeug.utils import secure_filename

def save_uploaded_file(uploaded_file):
    if uploaded_file is not None:
        # Make the filename safe
        filename = secure_filename(uploaded_file.name)

        # Create the directory if it doesn't exist
        if not os.path.exists('files'):
            os.makedirs('files')

        # Save the file
        with open(os.path.join('files', filename), "wb") as f:
            f.write(uploaded_file.getbuffer())

        return os.path.join('files', filename)
    return None
