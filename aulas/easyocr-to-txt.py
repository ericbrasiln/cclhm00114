import easyocr

img_path = "assetssample1/ex01.jpg"
txt_path = "resultado_easyocr.txt"

reader = easyocr.Reader(['pt'])
result = reader.readtext(img_path, detail=0, paragraph=True)

with open(txt_path, "w", encoding="utf-8") as f:
    # Escreve todo o texto extraído (um parágrafo)
    f.write("\n".join(result))

print(f"OCR salvo em: {txt_path}")

