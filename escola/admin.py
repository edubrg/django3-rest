from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'cpf')
    list_per_page = 20

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao', 'nivel')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso', 'descricao')
    list_per_page = 20

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id', )
    search_fields = ('aluno', 'curso')
    list_per_page = 20

admin.site.register(Matricula, Matriculas)
