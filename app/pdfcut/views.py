from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore
from django.shortcuts import render
import pdfplumber # type: ignore
import os

def pdf_view(request):
    return render(request, 'pdfcut.html')


class pdfcutAPIView(APIView):
    def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get('pdf')
        if not file_obj:
            return Response({"message": "PDF not sent!"}, status=status.HTTP_400_BAD_REQUEST)

        script_dir = os.path.dirname(os.path.abspath(__file__))
        static_files_dir = os.path.join(script_dir, 'static', 'files')
        filepath = os.path.join(static_files_dir, 'input.pdf')

        os.makedirs(static_files_dir, exist_ok=True)
        self.remove_file("input.pdf")

        try:
            with open(filepath, 'wb+') as destination:
                for chunk in file_obj.chunks():
                    destination.write(chunk)

            results = []
            with pdfplumber.open(filepath) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        results.append(text)

            return Response({"filename": filepath, "extracted_text": results}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": f"Error processing PDF: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def remove_file(self, filename):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'files', filename)
        if os.path.exists(file_path):
            os.remove(file_path)