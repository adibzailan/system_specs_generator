import psutil
import platform
import os
from tkinter import filedialog, Tk
import subprocess
import re

def get_gpu_info():
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        return [{'Name': gpu.name, 'Memory': f"{gpu.memoryTotal} MB"} for gpu in gpus]
    except ImportError:
        # If GPUtil is not available, try using subprocess
        try:
            output = subprocess.check_output(["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader,nounits"]).decode('utf-8')
            gpus = [line.split(',') for line in output.strip().split('\n')]
            return [{'Name': gpu[0].strip(), 'Memory': f"{float(gpu[1]):.0f} MB"} for gpu in gpus]
        except:
            return [{'Name': 'Unable to detect GPU', 'Memory': 'N/A'}]

def get_system_specifications():
    specs = {}
    
    # Overview
    specs['Overview'] = {
        'Model': platform.node(),
        'OS': f"{platform.system()} {platform.release()} Build {platform.version()}",
    }
    
    # Processor
    cpu_info = platform.processor().split()
    specs['Processor'] = {
        'Model': ' '.join(cpu_info),
        'Frequency': f"{psutil.cpu_freq().current:.2f} GHz",
        'Cores': psutil.cpu_count(logical=False),
        'Threads': psutil.cpu_count(logical=True),
    }
    
    # Motherboard
    if platform.system() == 'Windows':
        try:
            import wmi
            c = wmi.WMI()
            board = c.Win32_BaseBoard()[0]
            specs['Motherboard'] = {
                'Manufacturer': board.Manufacturer,
                'Model': board.Product,
            }
        except:
            specs['Motherboard'] = {'Manufacturer': 'Unknown', 'Model': 'Unknown'}
    else:
        specs['Motherboard'] = {'Manufacturer': 'Unknown', 'Model': 'Unknown'}
    
    # RAM
    specs['RAM'] = f"{psutil.virtual_memory().total / (1024**3):.2f} GB"
    
    # Storage
    specs['Storage'] = []
    for disk in psutil.disk_partitions():
        if disk.fstype:
            usage = psutil.disk_usage(disk.mountpoint)
            specs['Storage'].append({
                'Device': disk.device,
                'Total': f"{usage.total / (1024**3):.2f} GB",
                'Used': f"{usage.used / (1024**3):.2f} GB",
                'Free': f"{usage.free / (1024**3):.2f} GB",
            })
    
    # Graphics Card
    specs['Graphics Card'] = get_gpu_info()
    
    # Display
    if platform.system() == 'Windows':
        try:
            import wmi
            c = wmi.WMI()
            monitors = c.Win32_VideoController()
            specs['Display'] = [{
                'Name': monitor.Name,
                'Resolution': f"{monitor.CurrentHorizontalResolution}x{monitor.CurrentVerticalResolution}",
            } for monitor in monitors if monitor.CurrentHorizontalResolution]
        except:
            specs['Display'] = [{'Name': 'Unknown', 'Resolution': 'Unknown'}]
    else:
        specs['Display'] = [{'Name': 'Unknown', 'Resolution': 'Unknown'}]
    
    # Audio
    if platform.system() == 'Windows':
        try:
            import wmi
            c = wmi.WMI()
            sound_devices = c.Win32_SoundDevice()
            specs['Audio'] = [device.Name for device in sound_devices]
        except:
            specs['Audio'] = ['Unable to detect audio devices']
    else:
        specs['Audio'] = ['Unable to detect audio devices']
    
    return specs

def generate_markdown(specs, selected_sections=None):
    markdown = "# System Specifications\n\n"
    
    sections = {
        '1': 'Overview',
        '2': 'Processor',
        '3': 'Motherboard',
        '4': 'RAM',
        '5': 'Storage',
        '6': 'Graphics Card',
        '7': 'Display',
        '8': 'Audio'
    }
    
    if not selected_sections:
        selected_sections = sections.keys()
    
    for key in selected_sections:
        section = sections[key]
        if section in specs:
            markdown += f"## {section}\n"
            if isinstance(specs[section], dict):
                for k, v in specs[section].items():
                    markdown += f"- **{k}:** {v}\n"
            elif isinstance(specs[section], list):
                for item in specs[section]:
                    if isinstance(item, dict):
                        for k, v in item.items():
                            markdown += f"- **{k}:** {v}\n"
                    else:
                        markdown += f"- {item}\n"
            else:
                markdown += f"- {specs[section]}\n"
            markdown += "\n"
    
    return markdown

def save_markdown(content):
    root = Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(
        defaultextension=".md",
        filetypes=[("Markdown files", "*.md")],
        initialfile="pc_specifications.md"
    )
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Specifications saved to {file_path}")
    else:
        print("Save operation cancelled.")

def main():
    print("Gathering system specifications...")
    specs = get_system_specifications()
    
    print("\nSelect the sections you want to include (comma-separated numbers):")
    print("1. Overview")
    print("2. Processor")
    print("3. Motherboard")
    print("4. RAM")
    print("5. Storage")
    print("6. Graphics Card")
    print("7. Display")
    print("8. Audio")
    print("Or press Enter for all sections")
    
    selection = input("Your selection: ").strip()
    selected_sections = selection.split(',') if selection else None
    
    markdown_content = generate_markdown(specs, selected_sections)
    save_markdown(markdown_content)

if __name__ == "__main__":
    main()
