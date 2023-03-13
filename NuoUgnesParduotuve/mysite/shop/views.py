import datetime

from django.shortcuts import render, redirect
from .models import *
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _



# Create your views here.
def shop(request):

    categories = Category.objects.all()     #navigacija pagal kategorijas
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(category=category_id)
    else:
        products = Product.objects.all()
    context = {'products': products, 'categories': categories}

    if request.method == 'POST':        #produtų pridėjimas į krepšelį
        product = request.POST.get('product')
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            if order.lines.filter(product=product).exists():
                eilute = order.lines.get(product=product)
                eilute.quantity += 1
                eilute.save()
            else:
                nauja_preke = order.lines.create(product_id=product, quantity=1)
                nauja_preke.save()
            messages.info(request, _("%s successfully added to the Cart!") % products[int(product)-1])
        else:
            return redirect('login')


    return render(request, 'shop.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.lines.all()
        order.delivery = False  # jei prieš apmokėjimą persigalvotų dėl pristatymo ir grįžtų į krepšelį
        order.save()

        context = {'items': items,
               'order': order
               }

    else:
        return redirect('login')

    if request.method == "POST":
        quantity = request.POST.get('quantity')
        product = request.POST.get('update')
        product_remove = request.POST.get('remove')
        if product_remove:
            OrderLine.objects.filter(order_id=order, product_id=product_remove).delete()
            messages.info(request, _(f"Successfully removed from the Cart!"))
        else:
            if int(quantity) < 1:
                OrderLine.objects.filter(order_id=order, product_id=product).delete()
                messages.info(request, _(f"Successfully removed from the Cart!"))
            else:
                new_quantity = order.lines.get(product=product)
                new_quantity.quantity = quantity
                new_quantity.save()
                messages.info(request, _(f"Quantity successfully updated!"))


    return render(request, 'cart.html', context)


def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.lines.all()
        context = {'items': items,
                    'order': order
               }
    else:
        return redirect('login')



    return render(request, 'checkout.html', context)

def shipping(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        delivery = order.total() + 5  #pristatymo išlaidos
        items = order.lines.all()
        context = {'items': items,
            'order': order,
            'delivery': delivery
            }

        if request.method == "POST":
            customer = request.user.customer
            address = request.POST['address']
            city = request.POST['city']
            zipcode = request.POST['zipcode']
            country = request.POST['country']
            number = request.POST['number']
            order.delivery = True
            order.save()
            ShippingAddress.objects.create(customer_id=customer.id, order_id=order.id, address=address, city=city, zip_code=zipcode, country=country, telephone=number)
            return redirect('payment')

        return render(request, 'shipping.html', context)

def payment(request):                   #   sb-3cp1e25263800@personal.example.com  sb-tdduk25263796@business.example.com
                                        #   Ytfd4>"-                               ecW8a8/F
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        delivery = order.total() + 5
        items = order.lines.all()
    else:
        items = []
        delivery = 0
        order = {'total': 0, 'total_qty': 0}

    context = {'items': items,
               'order': order,
               'delivery': delivery
               }

    return render(request, 'payment.html', context)


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, _('Username %s already exist!') % username)
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, _('Email %s already exists!') % email)
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    user = User.objects.create_user(username=username, email=email, password=password)
                    Customer.objects.create(user=user, email=email, name=name, surname=surname)
                    messages.info(request, _('User %s successfully registered!') % username)
                    return redirect('login')
        else:
            messages.error(request, _('Passwords do not match!'))
            return redirect('register')
    return render(request, 'registration/register.html')


def search(request):
    query = request.GET.get('query')
    search_results = Product.objects.filter(Q(name__icontains=query))
    return render(request, 'search.html', {'products': search_results, 'query': query})


def productdetail(request, pk):
    context = {}
    context['product'] = Product.objects.get(id=pk)

    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            if order.lines.filter(product_id=pk).exists():
                eilute = order.lines.get(product_id=pk)
                eilute.quantity = eilute.quantity + int(quantity)
                eilute.save()
            else:
                nauja_preke = order.lines.create(product_id=pk, quantity=quantity)
                nauja_preke.save()
        messages.info(request, _(f"Successfully added to the Cart!"))

    return render(request, 'product_detail.html', context=context)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    customer = request.user.customer
    order = Order.objects.get(customer=customer, complete=False)
    order.transaction_id = transaction_id
    order.complete = True
    order.status = 'a'
    order.save()

    context = {
        'order': order
    }

    return render(request, 'processorder.html', context)


class UserOrdersListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'orders.html'

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user.customer, complete=True)

def orderdetail(request, pk):

    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.get(id=pk, customer=customer)
        items = order.lines.all()
    else:
        items = []
        order = {'total': 0, 'total_qty': 0}

    context = {'items': items,
                'order': order,
                   }

    return render(request, 'order_detail.html', context=context)
