from django.core.mail import send_mail


def contact(request):
    name=request.POST.get('name', '')
    phone=request.POST.get('phone', '')
    data={"name":name,"phone":phone,}
    send_mail('Анкета девочки',str("Имя девочки: "+data['name']+"\n"+"Номер телефона: "+data["phone"]+"\n"+"Это письмо сформировано автоматически. Пожалуйста, не отвечайте на него."), 'llipyc999@gmail.com',['selfiestudionsk@gmail.com'], fail_silently=False)