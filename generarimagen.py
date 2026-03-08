from PIL import Image, ImageDraw, ImageFont
import random

# ----------------------------
# ASCII Art + Log de consola
# ----------------------------
ascii_art = """
██████╗ █████╗ ██████╗ ██████╗  ██████╗ ███╗   ██╗ █████╗ ████████╗ ██████╗ 
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗████╗  ██║██╔══██╗╚══██╔══╝██╔═══██╗
██║     ███████║██████╔╝██████╔╝██║   ██║██╔██╗ ██║███████║   ██║   ██║   ██║
██║     ██╔══██║██╔══██╗██╔══██╗██║   ██║██║╚██╗██║██╔══██║   ██║   ██║   ██║
╚██████╗██║  ██║██║  ██║██████╔╝╚██████╔╝██║ ╚████║██║  ██║   ██║   ╚██████╔╝
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ 
"""

console_log = """
> USER: cArbonAto
> MODE: ACTIVIST_HACKER
> STATUS: CONNECTED
> ANONIMOUS
> ACCESSING LUNAR_CORE...
"""

# ----------------------------
# Configuración de fuente y tamaño
# ----------------------------
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
font_size = 28
padding_x = 40
padding_y = 30
visible_lines = 10
scroll_speed = 3

font = ImageFont.truetype(font_path, font_size)

# Combinar ASCII + log
lines = ascii_art.splitlines() + console_log.splitlines()

# ----------------------------
# Calcular ancho y alto
# ----------------------------
line_sizes = [font.getbbox(line) for line in lines]
line_widths = [bbox[2] - bbox[0] for bbox in line_sizes]
line_heights = [bbox[3] - bbox[1] for bbox in line_sizes]

max_width = max(line_widths)
line_height = max(line_heights)
frame_width = max_width + padding_x*2
frame_height = line_height * visible_lines + padding_y*2

# ----------------------------
# Generar frames con scroll y parpadeo verde
# ----------------------------
frames = []
num_frames = len(lines) + visible_lines + 10

for shift in range(num_frames):
    img = Image.new("RGB", (frame_width, frame_height), color=(0,0,0))
    draw = ImageDraw.Draw(img)
    
    y = padding_y - shift*scroll_speed
    for i, line in enumerate(lines):
        # efecto parpadeo verde
        green_val = 180 + random.randint(0,75)
        x = (frame_width - line_widths[i]) // 2  # centrar horizontal
        draw.text((x, y), line, font=font, fill=(0, green_val, 0))
        y += line_height
    
    frames.append(img)

# ----------------------------
# Guardar GIF animado
# ----------------------------
frames[0].save(
    "ascii_hacker_full.gif",
    save_all=True,
    append_images=frames[1:],
    duration=100,
    loop=0
)

print("✅ GIF animado con log y ASCII generado: ascii_hacker_full.gif")
