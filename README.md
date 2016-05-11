# PDF Waveform Extraction
Extracts multiple waveforms from the PDF outputs of the Omron/Collins VP-1000/2000 device.

# TO-DO:
1. Extract other relevant numbers from the PDFs for each waveform.
  - SYS, MAP, DIA, PP, %MAP
  - hcPWV, cfPWV, hfPWV, faPWV, ABI
  - PEP, ET, ETc, ET/PEP
2. Calibrate the waveforms
  - Carotid and femoral waveforms should be calibrated w/MAP and DIA of brachial

# Usage
Place all the PDFs in the pdftohtml5canvas/PDFs directory and run the Master.py file
```
python Master.py
```