from django.contrib import admin
from .models import Post

# Register your models here.

#admin.site.register(Post) #umas das maneiras de se registrar um model.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'status')#apresenta uma coluna representando o tipo do campo.
	list_filter = ('status', 'created', 'published', 'author')#barra lateral com o filtro.
	date_hierarchy = 'published'#navegador na parte superior da tabela de apresentação para situar onde está.
	raw_id_fields = ("author",)#para utilizar mais de um author.
	search_fields = ('title', 'content')#cria um componente de pesquisa pelos campos passados em parametro.
	prepopulated_fields = {'slug':('title',)}#autocompleta o slug com base no que for digitado no titulo.


