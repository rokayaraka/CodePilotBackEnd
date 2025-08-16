import subprocess
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.




@api_view(['Post'])
def keyword(request):
    code=request.data.get('code')
    code=' '.join(line.strip() for line in code.splitlines() if line.strip())
    language=request.data.get('language')
    if not code:
        return Response({"error": "No code provided"}, status=status.HTTP_400_BAD_REQUEST)
    if not language:
        return Response({"error": "No language provided"}, status=status.HTTP_400_BAD_REQUEST)
   
    parser_path=''
    if language == 'python':
        parser_path = os.path.join(os.path.dirname(__file__), "parsers",'python_parser')
    elif language == 'c++':
        parser_path = os.path.join(os.path.dirname(__file__), "parsers",'cpp_parser')
    elif language == 'c':
        parser_path = os.path.join(os.path.dirname(__file__), "parsers",'c_parser')
    else:
        return Response({"error": "Unsupported language"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        result = subprocess.run(
            [parser_path],
            input=code + "\n",
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            return Response({"error": "Compilation error", "details": result.stderr}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"output": result.stdout}, status=status.HTTP_200_OK)
    except FileNotFoundError:
        return Response({"error": "Parser not found"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

