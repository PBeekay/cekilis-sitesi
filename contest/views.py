from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ParticipationForm
from .models import Code, Entrant
from django.contrib.auth.decorators import user_passes_test

def contest_view(request):
    if request.method == 'POST':
        form = ParticipationForm(request.POST) ##Kullanıcının girdiği bilgileri forms.py e göre kontrol eder. 
        if form.is_valid():
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            code_value = form.cleaned_data['code'].upper()
            try:
                code_obj = Code.objects.get(code_value=code_value) ### Django tarafından SQL sorgusuna çevrilir ve veritabanından kontrol eder.
                if code_obj.is_used():
                    messages.error(request, 'Bu çekiliş kodu daha önce kullanılmış.')
                else:
                    entrant, created = Entrant.objects.get_or_create( ### Katılımcı var mı yok mu daha nce kontrol eder.
                        email=email,
                        defaults={'first_name': first_name, 'last_name': last_name}
                    )
                    if not created: 
                        entrant.first_name = first_name
                        entrant.last_name = last_name
                        entrant.save()

                    code_obj.entrant = entrant
                    code_obj.save()
                    messages.success(request, f'Tebrikler, {code_obj.code_value} kodunu başarıyla kaydettiniz!')
            except Code.DoesNotExist:
                messages.error(request, 'Geçersiz çekiliş kodu girdiniz.')
            return redirect('contest_page')
    else:
        form = ParticipationForm()
    context = {'form': form}
    return render(request, 'contest/index.html', context)

@user_passes_test(lambda u: u.is_staff) ## Güvenlik dedektörümüz
def pick_winner_view(request): ### kazanan seçmesini istiyoruz
    used_codes = Code.objects.filter(entrant__isnull=False)
    winner, winning_code = None, None
    if used_codes.exists():
        winning_code = used_codes.order_by('?').first() ### alınmış olan kodlardan rasgele 1 tanesini seçmesini istiyoruz.
        winner = winning_code.entrant
    context = {'winner': winner, 'winning_code': winning_code} 
    return render(request, 'contest/winner.html', context) ### Kazanan kodu ve kullanıcıyı seçip yazdırmasını istiyoruz.