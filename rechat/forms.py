# -*- coding: utf-8 -*-

from django import forms

class ChatForm(forms.Form):
    message = forms.CharField(
                              max_length=500, 
                              label="", 
                              required=True,
                              )


        



