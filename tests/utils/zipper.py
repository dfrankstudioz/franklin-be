import zipfile, os
from datetime import datetime

def zip_project(base_dir='.', output_dir='logs'):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    zip_filename = f"{output_dir}/project_backup_{timestamp}.zip"
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for foldername, _, filenames in os.walk(base_dir):
            if 'logs' in foldername:
                continue
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                arcname = os.path.relpath(filepath, base_dir)
                zipf.write(filepath, arcname)
    print(f"✅ Project zipped to {zip_filename}")

if __name__ == "__main__":
    zip_project()
