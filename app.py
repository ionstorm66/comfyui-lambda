import os
os.system(f"git lfs install")
os.system(f"git clone https://github.com/comfyanonymous/ComfyUI /home/demo/source/ComfyUI")
os.chdir(f"/home/demo/source/ComfyUI")
os.system(f"pip install -r requirements.txt")
os.system(f"git clone https://github.com/ltdrdata/ComfyUI-Manager /home/demo/source/ComfyUI/custom_nodes/ComfyUI-Manager")
os.system(f"python main.py --dont-print-server --port 8266 --enable-cors-header")
