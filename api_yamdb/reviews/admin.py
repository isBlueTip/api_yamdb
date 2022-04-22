from django.contrib import admin

from reviews.models import Comment, Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'title',
                    'text',
                    'author',
                    'score',
                    'pub_date',
                    )
    list_editable = ('score',)
    search_fields = ('text',)
    list_filter = ('author', 'title', 'pub_date', 'score')
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'text',
                    'review',
                    'author',
                    'pub_date',)
    search_fields = ('text',)
    list_filter = ('author', 'review', 'pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
