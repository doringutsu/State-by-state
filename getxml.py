import pdfquery
from lxml import etree

def getxml(filename):
	pdf = pdfquery.PDFQuery(filename + '.pdf')
	pdf.load()

	tree_root = pdf.tree
	with open(filename + '.xml', 'w') as f:
		f.write(etree.tostring(tree_root, pretty_print=True))
