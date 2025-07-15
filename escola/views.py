from django.http import JsonResponse

def alunos(request):
    if request.method == 'GET':
        aluno = {
            'id': 1,
            'nome': 'João da Silva',
            'idade': 10,
            'email': 'joao@gmail.com'
        }
        return JsonResponse(aluno)
