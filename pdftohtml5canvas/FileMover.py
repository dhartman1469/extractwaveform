import glob, os, shutil

files = glob.iglob(os.path.join('PDFs', "*.html"))
for file in files:
    if os.path.isfile(file):
        shutil.copy2(file, '../extract_waveform/HTML')
