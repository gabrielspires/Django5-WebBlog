from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from django.views.generic import ListView

from .forms import CommentForm, EmailPostForm
from .models import Post


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    # A comment was posted
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # Create a Comment object without saving it to the database
        comment = form.save(commit=False)
        # Assign the post to the comment
        comment.post = post
        # Save the comment to the database
        comment.save()
    return render(
        request,
        "blog/post/comment.html",
        {"post": post, "form": form, "comment": comment},
    )


def post_share(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == "POST":
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} ({cd['email']}) recommends you read {post.title}"
            message = (
                f"Read {post.title} at {post_url}\n\n"
                f"{cd['name']}'s comments: {cd['comments']}"
            )
            send_mail(
                subject=subject,
                message=message,
                from_email=None,
                recipient_list=[cd["to"]],
            )
            sent = True
    else:
        form = EmailPostForm()
    return render(
        request,
        "blog/post/share.html",
        {"post": post, "form": form, "sent": sent},
    )


class PostListView(ListView):
    """View alternativa da lista de posts."""

    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"


def post_list(request: HttpRequest):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)

    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=slug,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    # Form for users to comment
    form = CommentForm()
    return render(
        request,
        "blog/post/detail.html",
        {
            "post": post,
            "comments": comments,
            "form": form,
        },
    )
