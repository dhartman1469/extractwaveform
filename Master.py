import os
os.chdir('pdftohtml5canvas')
os.system("python pdftohtml5canvas.py PDFs")
os.system("python FileMover.py")
os.chdir('../')
os.chdir('extract_waveform')
os.system('extract_waveform.py')
os._exit(0)



