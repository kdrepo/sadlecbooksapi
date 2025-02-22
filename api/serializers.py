                                                                         
from rest_framework import serializers
from .models import *


class indexWordSerializer(serializers.ModelSerializer): 
    bookname =   serializers.SerializerMethodField()

    def get_bookname(self, obj):
            if "bookname" in self.context:
                return self.context["bookname"]        
            return None
    
    class Meta:
        model = indexword
        fields = [ "id", "word", "alphaTitle", "bookname"]


class indexwordurlSerializer(serializers.ModelSerializer):

    wordname = serializers.SerializerMethodField()

    def get_wordname(self, obj):
            if "wordname" in self.context:
                return self.context["wordname"]        
            return None

    class Meta:
        model = indexUrl
        # fields = "__all__"
        fields = [ "urltext", "url", "wordname"]

        


# seraliezer for displaying booklist

class BooklistSerializer(serializers.ModelSerializer):
    catagory = serializers.StringRelatedField(many=True)
   
    class Meta:
        model = Books
        fields = [ "id", "bookTitle", "bookAuthor", "bookPrice" ,  "catagory", "imagelink" ]


class BookdetailSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Books
        fields = [ "id", "bookTitle", "bookAuthor", "bookPrice", "imagelink" ,"otherinfo", "aurokart"]


#serailizer for displaying toc of a perticular book
class Subhead2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Subhead2
        fields = ["id", "subhead2Titles", "hastext"]

class Subhead1Serializer(serializers.ModelSerializer):
    sub2 = Subhead2Serializer(many=True)
    class Meta:
        model = Subhead1
        fields = ["id", "subhead1Titles","sub2", "hastext"]         


class ChapterSerializer(serializers.ModelSerializer):
    sub1 = Subhead1Serializer(many=True) 
    
    class Meta:
        model = Chapter
        fields = ["id", "chapTitle", "hastext", "sub1"]  


class BookSerializer(serializers.ModelSerializer):
    chap = ChapterSerializer(many=True)   
    

    class Meta:
        model = Books
        fields = [ "id", "bookTitle", "chap"]



#serializer for dipalying chapter content

class ChapterTextSerializer(serializers.ModelSerializer):    
    nextUrl = serializers.SerializerMethodField()
    previousUrl = serializers.SerializerMethodField()
    currentBook = serializers.SerializerMethodField()

    def get_nextUrl(self, obj):
        if "nextUrl" in self.context:
            return self.context["nextUrl"]        
        return None
    
    def get_previousUrl(self, obj):
        if "previousUrl" in self.context:
            return self.context["previousUrl"]        
        return None
    
    def get_currentBook(self, obj):
        if "currentBook" in self.context:
            return self.context["currentBook"]
        return None
    
    class Meta: 
        model = Chapter
        fields = ["id", "currentBook","chapTitle", "chapText", "hastext", "nextUrl", "previousUrl"]  



class Subhead1TextSerializer(serializers.ModelSerializer):
    
    Chapter = serializers.StringRelatedField()        
    currentBook = serializers.SerializerMethodField()
    nextUrl = serializers.SerializerMethodField()
    previousUrl = serializers.SerializerMethodField()

    def get_currentBook(self, obj):
        if "currentBook" in self.context:
            return self.context["currentBook"]
        return None
    
    def get_nextUrl(self, obj):
        if "nextUrl" in self.context:
            return self.context["nextUrl"]        
        return None
    
    def get_previousUrl(self, obj):
        if "previousUrl" in self.context:
            return self.context["previousUrl"]        
        return None

    class Meta:
        model = Subhead1
        fields = ["id", "currentBook", "Chapter", "subhead1Titles","subhead1Text" , "hastext", "nextUrl", "previousUrl"]

    
class Subhead2TextSerializer(serializers.ModelSerializer):
    Subhead1 = serializers.StringRelatedField()    
    currentBook = serializers.SerializerMethodField()
    currentChapter = serializers.SerializerMethodField()
    nextUrl = serializers.SerializerMethodField()
    previousUrl = serializers.SerializerMethodField()

    def get_currentBook(self, obj):
        if "currentBook" in self.context:
            return self.context["currentBook"]
        return None
    
    def get_currentChapter(self, obj):
        if "currentChapter" in self.context:
            return self.context["currentChapter"]        
        return None


    def get_nextUrl(self, obj):
        if "nextUrl" in self.context:
            return self.context["nextUrl"]        
        return None
    
    def get_previousUrl(self, obj):
        if "previousUrl" in self.context:
            return self.context["previousUrl"]        
        return None
    
    
    class Meta:
        model = Subhead2
        fields = ["id", "currentBook", "currentChapter", "Subhead1", "subhead2Titles", "subhead2Text", "hastext", "nextUrl", "previousUrl"]
    
    
