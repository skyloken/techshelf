import json

from django.shortcuts import get_object_or_404
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Review, Book


class LikeReview(APIView):
    authentication_classes = (authentication.SessionAuthentication,)  # ユーザーが認証されているか確認
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, review_id):

        review = get_object_or_404(Review, pk=review_id)
        status = json.loads(request.query_params.get('status'))
        user = self.request.user

        if user in review.likes.all():
            if not status:
                liked = True
            else:
                review.likes.remove(user)
                liked = False
        else:
            if not status:
                liked = False
            else:
                review.likes.add(user)
                liked = True
        data = {
            "liked": liked,
            "likeCount": review.likes.count()
        }
        return Response(data)


class MarkBook(APIView):
    authentication_classes = (authentication.SessionAuthentication,)  # ユーザーが認証されているか確認
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, book_id):

        book = get_object_or_404(Book, pk=book_id)
        status = json.loads(request.query_params.get('status'))
        user = self.request.user

        if user in book.marks.all():
            if not status:
                marked = True
            else:
                book.marks.remove(user)
                marked = False
        else:
            if not status:
                marked = False
            else:
                book.marks.add(user)
                marked = True
        data = {
            "marked": marked,
            "markCount": book.marks.count()
        }
        return Response(data)
