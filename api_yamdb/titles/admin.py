from django.contrib import admin

from titles.models import Category, Genre, Title


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'name',
                    'slug',
                    )
    list_editable = ('name', 'slug')
    search_fields = ('name', 'slug')
    empty_value_display = '-пусто-'


class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'name',
                    'slug',
                    )
    list_editable = ('name', 'slug')
    search_fields = ('name', 'slug')
    empty_value_display = '-пусто-'


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'name',
                    'year',
                    'description',
                    'category',
                    'genre',
                    )
    list_editable = ('genre', 'category')
    search_fields = ('name',)
    list_filter = ('year', 'category', 'genre')
    empty_value_display = '-пусто-'

    def genre(self, obj):
        return "\n".join([a.genre for a in obj.genres.all()])


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
