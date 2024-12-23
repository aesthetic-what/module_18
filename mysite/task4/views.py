from django.shortcuts import render

# Create your views here.
def menu(request):
    return render(request, 'fourth_task/menu.html')

def main(request):
    return render(request, 'fourth_task/main.html')

def shop(request):
    games = ['minecraft', 'terraria', 'metro 2033', 'metro last light']
    context = {
        'games': games
    }
    
    return render(request, 'fourth_task/shop.html', context)

def cart(request):
    cont = 'Продолжить покупки'
    done = 'Оформить заказ'
    context = {
        'cont': cont,
        'done': done,

    }
    
    return render(request, 'fourth_task/cart.html', context)