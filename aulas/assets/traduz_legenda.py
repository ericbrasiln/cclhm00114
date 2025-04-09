from googletrans import Translator
import re

# Nome do arquivo original e de saída
input_file = "blade_runner.srt"
output_file = "blade_runner.pt.srt"

translator = Translator()
translated_lines = []

with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

buffer = []
for line in lines:
    if re.match(r"^\d+$", line.strip()) or "-->" in line or line.strip() == "":
        # Número da linha, marcação de tempo ou linha em branco: manter
        if buffer:
            # Traduzir bloco anterior
            text = " ".join(buffer).strip()
            translated = translator.translate(text, src='en', dest='pt').text
            translated_lines.append(translated + "\n")
            buffer = []
        translated_lines.append(line)
    else:
        buffer.append(line.strip())

# Último bloco
if buffer:
    text = " ".join(buffer).strip()
    translated = translator.translate(text, src='en', dest='pt').text
    translated_lines.append(translated + "\n")

# Salva novo arquivo
with open(output_file, 'w', encoding='utf-8') as file:
    file.writelines(translated_lines)

print("✅ Legenda traduzida salva como:", output_file)

