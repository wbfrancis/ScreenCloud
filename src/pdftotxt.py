import pdfminer.high_level as pm
import re

try:
    text = pm.extract_text('./resource/pdf_scripts/chinatown.pdf')
except:
    print('Error: pdf is password protected')

arr = []
for e in re.split('\n\n|\x0c', text):
    print(repr(e))
    if e !='' and not re.match(r'\d+\.', e):
        result = re.sub('\n', ' ', e)
        if (result != ' '):
            if (not re.match(r'EXT\.|INT\.|\(|\)', result)):
                arr.append(result)

# print(arr)

