from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
# 导入数据模型Article
from .models import Article


def article_list(request):
    # 根据GET请求中查询条件
    # 返回不同排序的对象数组
    if request.GET.get('order') == 'total_views':
        article_list = Article.objects.all().order_by('-total_views')
        order = 'total_views'
    else:
        article_list = Article.objects.all().order_by('created')
        order = 'created'

    paginator = Paginator(article_list, 2)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    # 修改此行
    context = { 'articles': articles, 'order': order }

    return render(request, 'article/list.html', context)


# 文章详情
def article_detail(request,id):
    # 取出相应的文章
    article = Article.objects.get(id=id)
    # 需要传递给模板的对象
    context = {'article': article}
    # 载入模板，并返回context对象
    return render(request, 'article/detail.html', context)