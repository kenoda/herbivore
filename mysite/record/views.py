from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Plant, Post

from .forms import PlantForm, PostForm

app_name = 'record'
class IndexView(generic.TemplateView):
    template_name = "record/index.html"
#
#
# class DetailView(generic.DetailView):
#     model = Plant
#     template_name = 'record/list.html'
#
#
# class ResultsView(generic.ListView):
#     model = Plant
#     template_name = 'record/detail.html'


def plant_list(request):
    """植物のリスト"""
    plants = Plant.objects.all().order_by('id')
    return render(request, 'record/list.html', {'plants':plants})


def plant_edit(request, plant_id=None):
    """植物の編集"""
    if plant_id:   # plant_id が指定されている (修正時)
        plant = get_object_or_404(Plant, pk=plant_id)
    else:         # plant_id が指定されていない (追加時)
        plant = Plant()

    if request.method == 'POST':
        form = PlantForm(request.POST, instance=plant)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            plant = form.save(commit=False)
            plant.save()
            return redirect('record:plant_list')
    else:    # GET の時
        form = PlantForm(instance=plant)  # plant インスタンスからフォームを作成

    return render(request, 'record/plant_edit.html', dict(form=form, plant_id=plant_id))


def plant_del(request, plant_id):
    """植物の削除"""
    plant = get_object_or_404(Plant, pk=plant_id)
    plant.delete()
    return redirect('record:plant_list')


class PostList(generic.list.ListView):
    """植物の記録の一覧"""
    context_object_name='posts'
    template_name='record/post_list.html'
    paginate_by = 10  # １ページは最大2件ずつでページングする

    def get(self, request, *args, **kwargs):
        plant = get_object_or_404(Plant, pk=kwargs['plant_id'])  # 親の書籍を読む
        posts = plant.posts.all().order_by('id')   # 書籍の子供の、感想を読む
        self.object_list = posts

        context = self.get_context_data(object_list=self.object_list, plant=plant)
        return self.render_to_response(context)


def post_edit(request, plant_id, post_id=None):
    """記録の編集"""
    plant = get_object_or_404(Plant, pk=plant_id)  # 親の植物を読む
    if post_id:   # post_id が指定されている (修正時)
        post = get_object_or_404(Post, pk=post_id)
    else:               # post_id が指定されていない (追加時)
        post = Post()

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            post = form.save(commit=False)
            post.plant = plant  # この感想の、親の書籍をセット
            post.save()
            return redirect('record:post_list', plant_id=plant_id)
    else:    # GET の時
        form = PostForm(instance=post)  # post インスタンスからフォームを作成

    return render(request,
                  'record/post_edit.html',
                  dict(form=form, plant_id=plant_id, post_id=post_id))


def post_del(request, plant_id, post_id):
    """記録の削除"""
    post = get_object_or_404(Plant, pk=post_id)
    post.delete()
    return redirect('record:post_list', plant_id=plant_id)


# def post_draft_list(request, plant_id):
#     posts = Post.objects.filter(pub_date__isnull=True).order_by('created_date')
#     return render(request, 'record/post_draft_list.html', {'posts': posts})
#
#
# def post_publish(request, plant_id):
#     post = get_object_or_404(Plant, pk=plant_id)
#     post.publish()
#     return redirect('record/detail', pk=plant_id)


# def post_new(request, plant_id):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('record/detail', pk=plant_id)
#     else:
#         form = PostForm()
#     return render(request, 'record/post_edit.html', {'form': form})
