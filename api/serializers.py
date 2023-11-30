from rest_framework import serializers
from todoapp.models import Tag, TodoList
from django.shortcuts import render,redirect
from rest_framework.response import Response
from django.urls import reverse

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields ='__all__'


class TodoListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    
    class Meta:
        model = TodoList
        fields = ['id','title', 'description', 'due_date', 'tags', 'timestamp','status']
    
    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        todo_list = TodoList.objects.create(**validated_data)
        if tags_data:
            tags = []
            for tag_data in tags_data:
                tag = Tag.objects.create(**tag_data)
                tags.append(tag)

            todo_list.tags.set(tags)
        return todo_list

    def update(self, instance, validated_data):
        # Extract the tags data
        tags_data = validated_data.pop('tags')

        # Update the TodoList instance
        instance.title = validated_data['title']
        instance.description = validated_data['description']
        instance.due_date = validated_data['due_date']
        instance.status = validated_data['status']
    
        instance.save()
           # Update the associated tags
        if tags_data:
            instance.tags.set([])  # Clear existing tags
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            instance.tags.add(tag)
        return instance
      

        def delete(self, instance):
            instance.delete()
            return instance
           