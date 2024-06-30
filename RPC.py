import pypresence
import psutil
import time
client_id = 'CLIENTID'
RPC = pypresence.Presence(client_id)
RPC.connect()
while True: 
    cpu_percent = psutil.cpu_percent()
    mem_info = psutil.virtual_memory()
    mem_percent = mem_info.percent
    mem_used = round(mem_info.used / (1024 ** 3), 2)  
    mem_total = round(mem_info.total / (1024 ** 3), 2)  
    details = f"CPU: cpu_name  (used {cpu_percent}%)"
    state = f"RAM: {mem_total} GB (used {mem_percent}%)"
    buttons = [
        {"label": "link1", "url": "https://pornhub.com"},
        {"label": "link2", "url": "https://github.com"}
    ]

    RPC.update(details=details, state=state, buttons=buttons, large_image="img1", large_text="text1", small_text="text2", small_image="img2")

    time.sleep(1.2)
