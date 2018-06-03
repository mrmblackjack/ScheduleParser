import PyPDF2
import re



dateRe = re.compile("../../..")
locationRe = re.compile("[A-Z][A-Z]")

pdfFileObj= open('sched.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)
stringPdf = pageObj.extractText()

listPdfSplit = stringPdf.split("\n")

#Clean up a bit
listPdf = listPdfSplit[1: - 9]


shiftsRaw = []
shifts = []

currentShiftIndex = -1



for entry in listPdf:

    meetSite = entry.startswith("MeetSite")
    meetTime = entry.startswith("MeetTime")
    startTime = entry.startswith("StartTime")
    supervisor = entry.startswith('Supervisor')
    phoneNum = entry.startswith('07')

    if dateRe.match(entry) or locationRe.match(entry) or meetSite or meetTime or startTime or supervisor or phoneNum:
        shiftsRaw.append(entry)

for entry in shiftsRaw:
    if dateRe.match(entry):
        currentShiftIndex += 1
        shifts.append([])
    shifts[currentShiftIndex].append(entry)

print(shifts)









