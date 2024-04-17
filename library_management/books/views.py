from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer

from rest_framework import generics, status


# Create your views here.
# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListApiView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "status": "success",
            "code": 200,
            "message": f"Returned {len(books)} books",
            "books": serializer_data,
        }
        return Response(data)


# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailApiView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data

            data = {
                "status": "success",
                "code": 200,
                "message": "Book returned successfully",
                "book": serializer_data,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data = {
                "status": "error",
                "code": 404,
                "message": "Book not found",
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)


# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            data = {
                "status": "success",
                "code": 204,
                "message": "Book deleted successfully",
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            data = {
                "status": "error",
                "code": 404,
                "message": "Book not found",
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)


# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
            data = {
                "status": "success",
                "code": 200,
                "message": f"Book '{book_saved.title}' updated successfully",
                "book": serializer.data,
            }
            return Response(data)


# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookCreateApiView(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = BookSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                data = {
                    "status": "success",
                    "code": 201,
                    "message": "Book created successfully",
                    "book": serializer.data,
                }
                return Response(data)
            else:
                data = {
                    "status": "error",
                    "code": 400,
                    "message": serializer.errors,
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            data = {
                "status": "error",
                "code": 400,
                "message": str(e),
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(["GET"])
def book_list_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
