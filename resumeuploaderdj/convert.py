import convertapi

convertapi.api_secret = 'DBuhCGfisLXtWsTg'
convertapi.convert('pdf', {
    'File': '/home/samarth/reumeparser22-07-22/resumeuploaderdj/media/doc/test_resume.docx'
}, from_format = 'docx').save_files('/home/samarth/reumeparser22-07-22/resumeuploaderdj/media/pdfs')