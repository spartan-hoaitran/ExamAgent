import os
import requests
from app.routers.v1.exam_router import InputCreateExam


class ExamService():
    def __init__(self):
       pass

    def create_exam_handler(self, exam: InputCreateExam):
        self.download_file(exam.exam_id,exam.file_upload)

        
    def download_file(self,exam_id,urls):
        for url in urls:
            # Get the filename from the URL
            filename = os.path.basename(url)
            # Send a GET request to the URL
            response = requests.get(url)
            # Check if the request was successful
            if response.status_code == 200:
                # Open a local file in write-binary mode and save the content
                with open(f"{exam_id}/{filename}", 'wb') as file:
                    file.write(response.content)
                print(f"File downloaded successfully as {filename}")
            else:
                print("Failed to download the file. Status code:", response.status_code)