from random import sample
from django.shortcuts import render, HttpResponse
from .api import query
from .models import Transformer,ElectricityBill
from django.forms.models import model_to_dict
from .forms import NLQForm

import json
def index(request):
    # question ="How many stars does the transformers repository have?"
    # table = {
    #             "Repository": ["Transformers", "Datasets", "Tokenizers"],
    #             "Stars": ["36542", "4512", "3934"],
    #             "Contributors": ["651", "77", "34"],
    #             "Programming language": [
    #                 "Python",
    #                 "Python",
    #                 "Rust, Python and NodeJS"
    #             ]
    # }

    # model = Transformer
    # field_names = [f.name for f in model._meta.get_fields()]
    # data = [[getattr(ins, name) for name in field_names]
    #         for ins in Transformer.objects.prefetch_related().all()]
    # model_data = list(Transformer.objects.values())
    # table = {k: [str(d[k]) for d in model_data] for k in model_data[0]}

    model = ElectricityBill
    field_names = [f.name for f in model._meta.get_fields()]
    data = [[getattr(ins, name) for name in field_names]
            for ins in ElectricityBill.objects.prefetch_related().all()]
    model_data = list(ElectricityBill.objects.values())
    table = {k: [str(d[k]) for d in model_data] for k in model_data[0]}

    print(data)
    context = {"header":field_names,"table_data":data}

    question=''
    if request.POST.get('NLQ'):
        question = request.POST['NLQ']
        result = query(question, table)
        print(result)
        context["result"]=result["answer"]

    form1 = NLQForm(initial={'NLQ': question})
    context['form1'] = form1

    return render(request, 'index.html',context=context)

# def load_tables(table_id):
#     f = open(r"D:\MSCS\Thesis\Natural Language Interface for Databases\Project\Text2SQL\nlidbui\sqlui\tables_short.jsonl") 
#     tables_list = [json.loads(l.strip()) for l in  f.readlines()]
#     table_data = [l for l in tables_list if l.get("name")==table_id]     
#     return table_data[0]


# def index(request):
#     # req_table_id = request.GET.get('table')
#     # print("req_table_id:",req_table_id)
#     # table_id=""
#     # if not req_table_id:
#     #     sess_table_id = request.session.get("table_id",False)
#     #     table_id= sess_table_id if sess_table_id else "table_191591_5"
#     # else:
#     #     table_id = req_table_id
    
#     # print("table_id: ",table_id)
#     question ="What is terrence ross' nationality?"
#     if request.POST.get('NLQ'):
#         question = request.POST['NLQ']

#     table_data = "</s> <col0> Player : text <col1> No. : text <col2> Nationality : text <col3> Position : text <col4> Years in Toronto : text <col5> School/Club Team : text"
#     result = query(question, table_data)

#     form1 = NLQForm()
#     form2 = TablesForm()
#     # table_data_dic = load_tables(table_id)
#     # cols = table_data_dic['header']
#     # context = {"header":cols,"table_data": table_data_dic['rows']}

#     header=["Player","No.","Nationality","Position","Years in Toronto","School/Club Team"]
#     context = {"header":header,"table_data":["Saif","1","Pakistani","1","2","Blue"]}
#     context['form1'] = form1
#     context['form2'] = form2

#     return render(request, "index.html", context=context)
