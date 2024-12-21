from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'third_task/main.html')

def shop(request):
    return render(request, 'third_task/shop.html')

def cart(request):
    return render(request, 'third_task/cart.html')