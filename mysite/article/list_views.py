from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import ArticlePost, ArticleColumn
def article_titles(request):
    article_title = ArticlePost.objects.all()  # 获取所有文章
    paginator = Paginator(article_title,5)   # 每页5条数据
    page = request.GET.get('page')           # 获取前端传过来到page=？
    try:
        current_page = paginator.page(page)     # 根据page跳转到"page"页
        articles = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)         # 如果page为空跳转到第1页
        articles = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list
    return render(request, "article/list/article_titles.html",{
        "articles":articles, "page":current_page})

def article_detial(request,id,slug):
    article = get_object_or_404(ArticlePost, id=id, slug=slug)
    return render(request,"article/list/article_content.html",
                  {"article": article})