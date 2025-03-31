from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore
from django.shortcuts import render
import pdfplumber # type: ignore

def pdf_view(request):
    print("raz")
    with pdfplumber.open("pdf_test.pdf") as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()
        print(text)
    return render(request, 'pdfcut.html')