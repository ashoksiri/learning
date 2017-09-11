from fpdf import FPDF
import json
data = {};
with open('./app.json','r') as file:
    data = json.loads(file.read())

print data
import sys


pdf = FPDF()

# for d in data:
#     for k,v in d.items():
#         pdf.add_page()
#         if k == 'header':
#             pdf.set_font('Arial', 'B', 16)
#             pdf.cell(40, 10, v)
#         if k == 'urls':
#             for url in v :
#                 for x,y in url.items():
#                     if x == 'url':
#                         pdf.add_page()
#                         pdf.image(name=y)
# pdf.output('tutoimg.pdf', 'F')
#
# sys.exit(0)
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello World!')
pdf.image('3Dglobe_ir1.jpg', x = None, y = None, w = 100, h = 100, type = '', link = '')
pdf.output('tuto1.pdf', 'F')