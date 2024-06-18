from django.contrib import admin
from apps.escola.models import Aluno, Curso, Matricula

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Aluno, AlunoAdmin)

class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cod_curso', 'descricao', 'nivel')
    list_display_links = ('id', 'cod_curso')
    search_fields = ('cod_curso',)
    list_per_page = 20

admin.site.register(Curso, CursoAdmin)

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id',)

admin.site.register(Matricula, MatriculaAdmin)