from django.contrib import admin
from posts.models import Post, Product, Category,Review

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#  #   list_display = ('id','title', 'description', ' rate','created_date','modified_date',)

admin.site.register(Post)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)