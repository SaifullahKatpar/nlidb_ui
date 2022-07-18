from django import forms

class NLQForm(forms.Form):
    NLQ = forms.CharField(widget=forms.Textarea(attrs={'rows':6, 'cols':100,'id':'query','class':'form-control shadow-sm'}))

# TABLE_CHOICES= [
# ("table_1672976_6", "1-1672976-6"),
# ("table_1672976_7", "1-1672976-7"),
# ("table_1672976_5", "1-1672976-5"),
# ("table_1672976_2", "1-1672976-2"),
# ("table_2_15214004_3", "2-15214004-3"),
# ("table_191591_5", "1-191591-5"),
# ("table_2_15196750_1", "2-15196750-1"),
# ("table_23285849_5", "1-23285849-5"),
# ("table_23285849_6", "1-23285849-6"),
# ("table_23285849_7", "1-23285849-7"),
# ("table_2_15851155_1", "2-15851155-1"),
# ("table_23285849_8", "1-23285849-8"),
# ("table_26611679_3", "1-26611679-3"),
# ("table_2_14245_3", "2-14245-3"),
# ("table_2_17692986_2", "2-17692986-2"),
# ("table_2_15039040_1", "2-15039040-1"),
# ("table_2_15039040_6", "2-15039040-6"),
# ("table_14966537_1", "1-14966537-1"),
# ("table_2_16327510_1", "2-16327510-1"),
# ("table_2_17306260_2", "2-17306260-2"),
# ("table_2_17306260_1", "2-17306260-1"),
# ("table_2_16327510_2", "2-16327510-2"),
# ("table_2_12017602_11", "2-12017602-11"),
# ("table_2_16851_6", "2-16851-6"),
# ("table_14902507_2", "1-14902507-2")]

# class TablesForm(forms.Form):
#     table = forms.CharField(label='Choose a table', widget=forms.Select(choices=TABLE_CHOICES))