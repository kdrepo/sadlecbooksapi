

# from .models import *

from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework.decorators import api_view
from .models import Books, Chapter, Subhead1, Subhead2

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def Subhead1Text(request, bookid, chapid, sub1id):
    try:
        # Get the book title
        bookname = Books.objects.get(id=bookid).bookTitle

        # Get the current Subhead1
        mysub1 = Subhead1.objects.get(id=sub1id)

        # Get all Subhead1 ids for the current chapter
        subhead1_ids = list(Subhead1.objects.filter(Chapter__id=chapid).values_list("id", flat=True))
        pos_of_current_sub1 = subhead1_ids.index(sub1id)

        # Get all chapter ids for the current book
        chapter_ids = list(Chapter.objects.filter(Books__id=bookid).values_list("id", flat=True))
        pos_of_current_chap = chapter_ids.index(chapid)

        # Determine next URL
        try:
            next_sub2 = Subhead2.objects.filter(Subhead1__id=sub1id)
            if next_sub2.exists():
                nextid = next_sub2.values('id').first()
                next_url = f"{bookid}/{chapid}/{sub1id}/{nextid}"
            else:
                if pos_of_current_sub1 < len(subhead1_ids) - 1:
                    next_sub1_id = subhead1_ids[pos_of_current_sub1 + 1]
                    next_url = f"{bookid}/{chapid}/{next_sub1_id}"
                elif pos_of_current_chap < len(chapter_ids) - 1:
                    next_chap_id = chapter_ids[pos_of_current_chap + 1]
                    next_url = f"{bookid}/{next_chap_id}"
                else:
                    next_url = None
        except:
            next_url = None

        # Determine previous URL
        try:
            if pos_of_current_sub1 > 0:
                prev_sub1_id = subhead1_ids[pos_of_current_sub1 - 1]
                prev_url = f"{bookid}/{chapid}/{prev_sub1_id}"
            else:
                prev_url = f"{bookid}/{chapid}" if pos_of_current_sub1 == 0 else None
        except:
            prev_url = None

        # Return JSON response with URLs
        return JsonResponse({
            'book_title': bookname,
            'current_subhead_id': sub1id,
            'next_url': next_url,
            'previous_url': prev_url
        })

    except Books.DoesNotExist:
        return HttpResponseBadRequest("Book not found")
    except Subhead1.DoesNotExist:
        return HttpResponseBadRequest("Subhead1 not found")
    except Chapter.DoesNotExist:
        return HttpResponseBadRequest("Chapter not found")
    except Exception as e:
        return HttpResponseBadRequest(f"Something went wrong: {e}")

















# def Subhead2Text(request, bookid, chapid, sub1id, sub2id):
#     bookname = Books.objects.get(id=bookid).bookTitle
#     mychapter = Chapter.objects.get(id=chapid).chapTitle
#     # mysub1 = Subhead1.objects.get(id=sub1id)
#     mysub2 = Subhead2.objects.get(id=sub2id)






#     p = Subhead2.objects.filter(Subhead1__id=sub1id).values("id")
#     no_of_ids = p.filter().values("id")
#     mylist = []
#     for x in no_of_ids:
#         mylist.append(x.get('id'))
#     pos_of_current_sub2 = mylist.index(sub2id)
#     pos_last_id_in_list = mylist.index(mylist[-1])
#     difference1 = pos_last_id_in_list-pos_of_current_sub2


#     s1 = Subhead1.objects.filter(Chapter__id=chapid).values("id")
#     mylist2 = []
#     for x in s1:
#         mylist2.append(x.get('id'))
#     pos_of_current_sub1 = mylist2.index(sub1id)
#     pos_last_id_in_sub1_list = mylist2.index(mylist2[-1])
#     difference2 = pos_last_id_in_sub1_list - pos_of_current_sub1


#     ch = Chapter.objects.filter(Books__id=bookid).values("id")
#     mylist3 = []
#     for x in ch:
#         mylist3.append(x.get('id'))
#     pos_of_current_chap = mylist3.index(chapid)
#     pos_last_id_in_chap_list = mylist3.index(mylist3[-1])
#     difference3 = pos_last_id_in_chap_list - pos_of_current_chap



    

#     if difference1 != 0:
#         valueofnextid = mylist[pos_of_current_sub2+1]
#         url = str(bookid) + "/" + str(chapid) + "/" + str(sub1id) + "/" + str(valueofnextid)

#     elif difference1 == 0:    
#         if difference2 != 0:
#             valueofnexts1id = mylist2[pos_of_current_sub1+1]
#             url = str(bookid) + "/" + str(chapid) + "/" + str(valueofnexts1id)
#         else:
#             if difference3 != 0:
#                 valueofnextchapid = mylist3[pos_of_current_chap+1]
#                 url = str(bookid) + "/" + str(valueofnextchapid)
#             else:
#                 url = "end of book"